import requests

import app_config


def create_account(account_name):
    endpoint = app_config.CHATWOOT_API_ENDPOINT + "platform/api/v1/accounts"
    data = {"name": account_name}
    headers = {"api_access_token": app_config.CHATWOOT_PLATFORM_APP_API_KEY}
    try:
        r = requests.post(endpoint, data=data, headers=headers).json()
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)
    # add response to database

    return r
