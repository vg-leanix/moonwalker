import requests
import json




def create_support_user(host: str, jwt_token: str, request: str,
                        workspace_id: str, workspace_name: str,
                        workspace_url: str):

    endpoint = f"https://{host}.leanix.net/services/mtm/v1/permissions"
    auth_header = 'Bearer ' + jwt_token
    header = {'Authorization': auth_header, 'accept': 'application/json'}

    with open(request) as f:
        support_user_json = json.load(f)

    links = [
        {
            "rel": "contract",
            "href": "/contracts/5b2db257-5618-46fa-a946-1b85b5920177"
        },
        {
            "rel": "instance",
            "href": "/instances/6871b910-c03e-48ea-bebf-d00ffaaa3ebf"
        },
        {
            "rel": "permissions",
            "href": f"/workspaces/{workspace_id}/permissions"
        },
        {
            "rel": "settings",
            "href": f"/workspaces/{workspace_id}/settings"
        },
        {
            "rel": "events",
            "href": f"/workspaces/{workspace_id}/events"
        }
    ]

    support_user_json['workspace']['id'] = workspace_id
    support_user_json['workspace']['name'] = workspace_name
    support_user_json['workspace']['url'] = workspace_url

    support_user_json['workspace']['links'] = links

    r = requests.post(url=endpoint, headers=header, json=support_user_json)

    if r.status_code == 200:
        error = None
        status_code = r.status_code

    else:
        error = r.json()
        status_code = r.status_code

    return status_code, error
