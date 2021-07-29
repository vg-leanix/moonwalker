from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import os
from typing import List, Optional
import app.utils.lx as lx

K8S_PROCESSOR = "app/modules/k8s.json"
router = APIRouter(
    # prefix="/v1/auth",
    tags=["auth"],
)

class Config(BaseModel):
    host: str
    mtmToken: str
    apiToken: str
    ws_edition: str


@router.post("/intapi", tags=["auth"])
async def register_user(config: Config):
    bearer_token = lx.authenticate(host=config.host, apitoken=config.apiToken)
    
    print(bearer_token)
    res = lx.put_processor(host=config.host, jwt_token=bearer_token,
                     processor=K8S_PROCESSOR)

    return JSONResponse(res)
