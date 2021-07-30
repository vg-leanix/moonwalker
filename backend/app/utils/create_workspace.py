import requests
import json


def create_workspace(workspace_name: str, jwt_token: str, host: str, request: str):

    endpoint = f"https://{host}.leanix.net/services/mtm/v1/workspaces"
    auth_header = 'Bearer ' + jwt_token
    header = {'Authorization': auth_header, 'accept': 'application/json'}

    with open(request) as f:
        workspace_json = json.load(f)

    workspace_json['name'] = workspace_name

    print(workspace_json['name'])
    try:
        res = requests.post(url=endpoint, headers=header, json=workspace_json)
        status_code = res.status_code
        response_data = res.json()
        workspace_id = response_data['data']['id']
        error = None

    except Exception as e:
        error = str(e)
        status_code = None

    return status_code, error, workspace_id


def create_tech_user(name: str, workspace_id: str, host: str, jwt_token: str, specs: str):

    param = {'workspaceId': workspace_id}
    endpoint = f"https://{host}.leanix.net/services/mtm/v1/technicalusers"

    auth_header = 'Bearer ' + jwt_token
    header = {'Authorization': auth_header, "Content-Type": "application/json"}

    with open(specs) as f:
        techuser_json = json.load(f)

    techuser_json['userName'] = name

    try:
        res = requests.post(url=endpoint, params=param,
                            headers=header, json=techuser_json)

        response_json = res.json()
        apiToken = response_json['data']['apiTokenData']['token']
        status_code = res.status_code
        error = None

    except Exception as e:
        error = str(e)
        status_code = None

    return status_code, error, apiToken
