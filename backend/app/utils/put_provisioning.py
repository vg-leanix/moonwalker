import json
from typing import List
import requests
from requests import status_codes
from pydantic import BaseModel

class ProvisionReqBody(BaseModel):
    extensions: List[str]
    api_token: str

def put_provisioning(host: str, jwt_token: str, apply_base_model: bool, extensions: List[str]):
    pass
    request_url = f'https://{host}.leanix.net/services/provisioning/v1/provision'
    auth_header = 'Bearer ' + jwt_token
    header = {'Authorization': auth_header, "Content-Type": "application/json"}
    print("line 16 put ", extensions)
    reqBody: ProvisionReqBody = {
        extensions: extensions
    }

    parameters = {
        'apply_base_model': apply_base_model,
        'skip_charts': False,
        'skip_dashboards': False,
        'skip_meta_model': False,
        'skip_portals': False,
        'skip_saved_reports': False,
        'skip_saved_searches': False,
        'skip_tag_groups': False,
        'skip_settings': False,
        'skip_violations': False
    }

    try:
        r = requests.put(request_url, body=reqBody, params=parameters, headers=header)
        status_code = r.status_code
        error = None

    except Exception as e:
        error = str(e)
        status_code = None

    return status_code, error
