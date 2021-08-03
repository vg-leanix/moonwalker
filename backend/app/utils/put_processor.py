import json
import requests


def put_processor(host: str, jwt_token: str, processor: str):

    with open(processor) as f:
        processor_json = json.load(f)

    request_url = f'https://{host}.leanix.net/services/integration-api/v1/configurations'

    auth_header = 'Bearer ' + jwt_token
    header = {'Authorization': auth_header, "Content-Type": "application/json"}

    
    r = requests.put(request_url, json=processor_json, headers=header)
    status_code = r.status_code

    if status_code == 200 or status_code == 204:
        error = None

    else :
        error = r.json()
        status_code = r.status_code


    
    return status_code, error
