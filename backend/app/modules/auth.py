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
router = APIRouter(
    # psrefix="/v1/auth",
    tags=["auth"],
)


class Config(BaseModel):
    apiToken: str
    edition: str
    instance: str
    workspaceId: str


class Workspace(BaseModel):
    workspaceName: str
    apiToken: str
    instance: str


@router.post("/createws", tags=["auth"])
async def create_workspace(workspace: Workspace):
    bearer_token = lx.authenticate(
        host=workspace.instance, apitoken=workspace.apiToken)

    status_code_ws, error_ws, ws_id = ws.create_workspace(workspace_name=workspace.workspaceName, jwt_token=bearer_token,
                                                          host=workspace.instance, request=WS_REQUEST)

    status_code_techuser, error_techuser, apiToken = ws.create_tech_user(name="ext-integration", host=workspace.instance,
                                                                         jwt_token=bearer_token, specs=TECHUSER)

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
                "error": error_ws
            },
            "techuser": {
                "status": status_code_techuser,
                "error": error_techuser,
                "apiToken":apiToken
            }
        }

    return JSONResponse(output)


@router.post("/workspace", tags=["auth"])
async def prepare_workspace(config: Config):
    bearer_token = lx.authenticate(
        host=config.instance, apitoken=config.apiToken)

    status_code_processor, error_processor = int_api.put_processor(host=config.instance, jwt_token=bearer_token,
                                                                   processor=K8S_PROCESSOR)

    status_code_provisioning, error__provisioning = provision.provision_data_model(
        edition=config.edition, jwt_token=bearer_token)

    statuses = {"status_processor": status_code_processor,
                "status_provisioning": status_code_provisioning}

    errors = {"err_provisioning": error__provisioning,
              "err_processor": error_processor}

    if not 200 in statuses.values():
        output = {
            "data_model": {
                "status": status_code_provisioning,
                "error": error__provisioning
            },
            "processor": {
                "status": status_code_processor,
                "error": error_processor
            }
        }

        raise HTTPException(
            status_code=400,
            detail=json.dumps(output),

        )

    else:
        output = {
            "data_model": {
                "status": status_code_provisioning,
                "error": error__provisioning
            },
            "processor": {
                "status": status_code_processor,
                "error": error_processor
            }
        }

    return JSONResponse(output)
