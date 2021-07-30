from app.utils.put_provisioning import ProvisionReqBody
from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import os
from typing import List, Optional
import app.utils.lx as lx
import app.utils.put_processor as int_api
import app.utils.put_provisioning as provisioning

K8S_PROCESSOR = "app/modules/k8s.json"
router = APIRouter(
    # psrefix="/v1/auth",
    tags=["auth"],
)


class Config(BaseModel):
    apiToken: str
    edition: str
    host: str
    wsName: str

class ProvisioningBody(BaseModel):
    config: Config
    provisionReqBody: ProvisionReqBody
    apply_base_model: bool

@router.post("/createws", tags=["auth"])
async def create_workspace(config: Config):
    bearer_token = lx.authenticate(host=config.host, apitoken=config.apiToken)

    status_code, error = int_api.put_processor(host=config.host, jwt_token=bearer_token,
                                               processor=K8S_PROCESSOR)

    if not error and ((status_code == 200 ) or (status_code == 204)):
        output = {
            "message": "workspace successfully set up",
            "status_code_int_api": status_code
        }
    else:
        raise HTTPException(
            status_code=400,
            detail="Error in Workspace setup workflow",

        )

    return JSONResponse(output)

@router.post("/updateProvisioning", tags=["auth"])
async def update_provisioning(param: ProvisioningBody):
    bearer_token = lx.authenticate(host=param.config.host, apitoken=param.config.apiToken)

    status_code, error = provisioning.put_provisioning(host=param.config.host, jwt_token=bearer_token,apply_base_model=True, extenstions=param.provisionReqBody.extensions)

    if not error and ((status_code == 200 ) or (status_code == 204)):
        output = {
            "message": "workspace successfully provisioned",
            "status_code_int_api": status_code
        }
    else:
        raise HTTPException(
            status_code=400,
            detail="Error in Workspace provision workflow",

        )

    return JSONResponse(output)
