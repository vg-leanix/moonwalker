import requests
import json
from app.utils.create_support_user import create_support_user


def create_workspace(workspace_name: str, jwt_token: str, host: str,
                     request: str, custom_features: str, support_user: str):

    endpoint = f"https://{host}.leanix.net/services/mtm/v1/workspaces"
    endpoint_cf = f"https://{host}.leanix.net/services/mtm/v1/customFeatures"
    auth_header = 'Bearer ' + jwt_token
    header = {'Authorization': auth_header, 'accept': 'application/json'}

    with open(request) as f:
        workspace_json = json.load(f)

    with open(custom_features) as f:
        custom_features_json = json.load(f)

    workspace_json['name'] = workspace_name

    res = requests.post(url=endpoint, headers=header, json=workspace_json)
    status_code = res.status_code

    if status_code == 200:
        print("MTM status: ", status_code)
        response_data = res.json()
        workspace_id = response_data['data']['id']
        workspace_url = response_data['data']['url']
        custom_features_json['workspace']['id'] = workspace_id
        
        res = requests.post(
            url=endpoint_cf, headers=header, json=custom_features_json)

        if res.status_code == 200:
            print("created custom feature flag")

            status_code_support_user, error_support_user = create_support_user(host=host, jwt_token=jwt_token,
                                                                               request=support_user, workspace_id=workspace_id,
                                                                               workspace_url=workspace_url,
                                                                               workspace_name=workspace_name)

            if status_code_support_user == 200:
                print("support user added")
                error = None

            else:
                error = error_support_user
                print(error)

        else:
            error = res.json()
            print(error)
            workspace_id = workspace_id
            workspace_url = workspace_url
            status_code = res.status_code

    else:
        error = res.json()
        print(error)
        status_code = res.status_code
        workspace_id = None
        workspace_url = None

    return status_code, error, workspace_id, workspace_url


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
