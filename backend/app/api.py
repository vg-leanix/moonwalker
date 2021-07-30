from fastapi import FastAPI
from .modules import auth


tags_metadata = [
    
    {
        "name": "auth",
        "description": "workflow creation workflow endpoint"
    },

]

app = FastAPI(
    title="Moonshoot",
    description="API Hub for smart Workspace provisioning",
    version="1.0.0",
    
    openapi_tags=tags_metadata)

app.include_router(auth.router) 


