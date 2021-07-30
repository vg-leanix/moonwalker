import json
import requests


def put_processor(host: str, jwt_token: str, processor: str):

    with open(processor) as f:
        processor_json = json.load(f)

    request_url = f'https://{host}.leanix.net/services/integration-api/v1/configurations'

    auth_header = 'Bearer ' + jwt_token
    header = {'Authorization': auth_header, "Content-Type": "application/json"}

    try:
        r = requests.put(request_url, json=processor_json, headers=header)
        status_code = r.status_code
        error = None

    except Exception as e:
        error = str(e)
        status_code = None

    return status_code, error
