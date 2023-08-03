import requests

import app_config
import database


def create_account(account_name):
    endpoint = app_config.CHATWOOT_API_ENDPOINT + "platform/api/v1/accounts"
    data = {"name": account_name}
    headers = {"api_access_token": app_config.CHATWOOT_PLATFORM_APP_API_KEY}
    try:
        r = requests.post(endpoint, data=data, headers=headers).json()
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)
    # add response to database
    database.add_account(r)


def create_user(msauth_res):
    endpoint = app_config.CHATWOOT_API_ENDPOINT + "platform/api/v1/users/"
    data = {"name":msauth_res["name"], "email":msauth_res["email"], "password"}


def create_account_user(account_id):
    endpoint = app_config.CHATWOOT_API_ENDPOINT + "platform/api/v1/accounts/" + account_id + "/account/users"
    data = {"role": "Administrator"}
    headers = {"api_access_token": app_config.CHATWOOT_PLATFORM_APP_API_KEY}
    try:
        r = requests.post(endpoint, data=data, headers=headers).json()
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)
    # add response to database
    database.add_account(r)
