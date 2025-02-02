import identity.web
import requests
from flask import Flask, redirect, render_template, request, session, url_for
from flask_session import Session

import app_config
import chatwoot_api

# for testing chatwoot apis
test_payload = {
    "name": "Ford",
    "password": "Password!123",
    "id": 1,
    "uid": "12345",
    "custom_attributes": "test",
    "role": "Administrator",
    "available_name": "Some Name",
    "display_name": "Some other Name",
    "email": "email@email.com",
    "account_id": 1,
    "confirmed": "Yes",
    "accounts": "An Account"
}

__version__ = "0.7.0"  # The version of this sample, for troubleshooting purpose

app = Flask(__name__)
app.config.from_object(app_config)
assert app.config["REDIRECT_PATH"] != "/", "REDIRECT_PATH must not be /"
Session(app)

from werkzeug.middleware.proxy_fix import ProxyFix

app.wsgi_app = ProxyFix(app.wsgi_app, x_proto=1, x_host=1)

auth = identity.web.Auth(
    session=session,
    authority=app.config["AUTHORITY"],
    # tenp for testing
    client_id="efbfa13c-1935-471b-a6e6-dec032d43407",
    # tenp for testing
    client_credential="6Pz8Q~ABgeHIv1xj.1D00qU3XNg~FrPGTAQXLbH-",
)


@app.route("/login")
def login():
    return render_template("login.html", version=__version__, **auth.log_in(
        scopes=app_config.SCOPE,  # Have user consent to scopes during log-in
        redirect_uri=url_for("auth_response", _external=True),
        # Optional. If present, this absolute URL must match your app's redirect_uri registered in Azure Portal
    ))


@app.route("/microsoft/auth")
def auth_response():
    result = auth.complete_log_in(request.args)
    if "error" in result:
        return render_template("auth_error.html", result=result)
    return redirect(url_for("index"))


@app.route("/logout")
def logout():
    return redirect(auth.log_out(url_for("index", _external=True)))


@app.route("/")
def index():
    if not (app.config["CLIENT_ID"] and app.config["CLIENT_SECRET"]):
        # This check is not strictly necessary.
        # You can remove this check from your production code.
        return render_template('config_error.html')
    if not auth.get_user():
        return redirect(url_for("login"))
    return render_template('index.html', user=auth.get_user(), version=__version__)


@app.route("/call_downstream_api")
def call_downstream_api():
    token = auth.get_token_for_user(app_config.SCOPE)
    if "error" in token:
        return redirect(url_for("login"))
    # Use access token to call downstream api
    api_result = requests.get(
        app_config.ENDPOINT,
        headers={'Authorization': 'Bearer ' + token['access_token']},
        timeout=30,
    ).json()
    return render_template('display.html', result=api_result)


@app.route("/create")
def create_chatwoot_account():
    a = chatwoot_api.create_account("test account")
    u = chatwoot_api.create_user(test_payload)
    au = chatwoot_api.create_account_user(a["id"], u["id"])
    sso = chatwoot_api.create_sso(u["id"])
    print(sso)

    # todo add async

    # todo add response to account create and user create
    # todo make graph API request for user details


if __name__ == "__main__":
    app.run(port=80)
