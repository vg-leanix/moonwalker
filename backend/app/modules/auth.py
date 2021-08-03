from requests import api
from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import os
import json
from typing import List, Optional
import app.utils.lx as lx
import app.utils.put_processor as int_api
import app.utils.provision_data_model as provision
import app.utils.create_workspace as ws

K8S_PROCESSOR = "app/modules/k8s.json"
WS_REQUEST = "app/modules/workspace_request.json"
TECHUSER = "app/modules/techuser_request.json"
CUSTOM_FEATURES = "app/modules/customFeature.json"
SUPPORT_USER = "app/modules/support_user.json"


router = APIRouter(
    prefix="/v1",
    tags=["auth"],
)


class Config(BaseModel):
    techuserApiToken: str
    edition: str
    instance: str
    workspaceId: str


class Workspace(BaseModel):
    workspaceName: str
    apiToken: str
    instance: str


@router.post("/createws", tags=["auth"])
async def create_workspace(workspace: Workspace, status_code=200):
    bearer_token, error = lx.authenticate(
        host=workspace.instance, apitoken=workspace.apiToken)

    if error:
        raise HTTPException(
            status_code=400,
            detail=json.dumps({"error": error}),

        )

    status_code_ws, error_ws, ws_id = ws.create_workspace(workspace_name=workspace.workspaceName, jwt_token=bearer_token,
                                                          host=workspace.instance, request=WS_REQUEST, 
                                                          custom_features=CUSTOM_FEATURES, support_user=SUPPORT_USER)

    status_code_techuser, error_techuser, apiToken = ws.create_tech_user(name="ext-integration", host=workspace.instance,
                                                                         jwt_token=bearer_token, specs=TECHUSER, workspace_id=ws_id)

    # status_code_ws, error_ws, ws_id = 200, None, "1234"
    # status_code_techuser, error_techuser, apiToken = 200, None, "1234"

    statuses = {"status_ws": status_code_ws,
                "status_techuser": status_code_techuser}

    errors = {"err_ws": error_ws,
              "err_techuser": error_techuser}

    if not 200 in statuses.values():
        output = {
            "workspace": {
                "status": status_code_ws,
                "error": error_ws
            },
            "techuser": {
                "status": status_code_techuser,
                "error": error_techuser
            }
        }

        raise HTTPException(
            status_code=400,
            detail=json.dumps(output),

        )

    else:
        output = {
            "workspace": {
                "status": status_code_ws,
                "workspaceId": ws_id,
                "error": error_ws
            },
            "techuser": {
                "status": status_code_techuser,
                "error": error_techuser,
                "apiToken": apiToken
            }
        }

    return JSONResponse(content=output, status_code=200)


@router.post("/install", tags=["auth"])
async def install_workspace(config: Config):
    bearer_token, error = lx.authenticate(
        host=config.instance, apitoken=config.techuserApiToken)

    if error:
        raise HTTPException(
            status_code=400,
            detail=json.dumps({"error": error}),

        )

    status_code_provisioning, error_provisioning = provision.provision_data_model(
        edition=config.edition, jwt_token=bearer_token)

    if status_code_provisioning == 200:
        output = {
            "data_model": {
                "status": status_code_provisioning,
                "error": error_provisioning
            }

        }

    else:

        output = {
            "data_model": {
                "status": status_code_provisioning,
                "error": error_provisioning
            }

        }

        raise HTTPException(
            status_code=400,
            detail=json.dumps(output),

        )

    return JSONResponse(content=output, status_code=200)


@router.post("/proccessors", tags=["auth"])
async def put_processors(config: Config):
    bearer_token, error = lx.authenticate(
        host=config.instance, apitoken=config.techuserApiToken)

    if error:
        raise HTTPException(
            status_code=400,
            detail=json.dumps({"error": error}),

        )

    status_code_processor, error_processor = int_api.put_processor(host=config.instance, jwt_token=bearer_token,
                                                                   processor=K8S_PROCESSOR)

    if status_code_processor in [200, 204]:
        output = {
            "processor": {
                "status": status_code_processor,
                "error": error_processor
            }
        }

    else:
        output = {
            "processor": {
                "status": status_code_processor,
                "error": error_processor
            }
        }

        raise HTTPException(
            status_code=400,
            detail=json.dumps(output),

        )

    return JSONResponse(content=output, status_code=200)
