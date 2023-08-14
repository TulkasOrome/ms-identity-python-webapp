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
    # todo add specific error handling
    # add response to database
    database.add_account(r)

    return r


def create_user(msauth_res):
    endpoint = app_config.CHATWOOT_API_ENDPOINT + "platform/api/v1/users/"
    data = {"name": msauth_res["name"], "email": msauth_res["email"], "password": msauth_res["password"],
            "custom_attributes": msauth_res["custom_attributes"]}
    headers = {"api_access_token": app_config.CHATWOOT_PLATFORM_APP_API_KEY}
    try:
        r = requests.post(endpoint, data=data, headers=headers).json()
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)
    # todo add specific error handling
    # add response to database
    database.add_user(r)
    return r


def create_account_user(account_id, user_id):
    endpoint = app_config.CHATWOOT_API_ENDPOINT + "platform/api/v1/accounts/" + str(account_id) + "/account_users"
    data = {"user_id": user_id, "role": "administrator"}
    headers = {"api_access_token": app_config.CHATWOOT_PLATFORM_APP_API_KEY}
    try:
        r = requests.post(endpoint, data=data, headers=headers).json()
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)
    # todo add specific error handling
    database.add_account_user(r)
    #todo review database call


def create_sso(user_id):
    endpoint = app_config.CHATWOOT_API_ENDPOINT + "platform/api/v1/users/" + str(user_id) + "/login"
    headers = {"api_access_token": app_config.CHATWOOT_PLATFORM_APP_API_KEY}
    try:
        r = requests.get(endpoint, headers=headers).json()
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)
    return r
