from sqlalchemy.orm import Session
import engine
from models import Account, User, Account_User


def add_account(res):
    create_response = res
    with Session(engine.engine) as session:
        account = Account(
            id=create_response["id"],
            name=create_response["name"]
        )
    session.add_all([account])
    session.commit()


def add_user(res):
    create_response = res
    with Session(engine.engine) as session:
        user = User(
            id=create_response["id"],
            name=create_response["name"],
            uid=create_response["uid"],
            available_name=create_response["available_name"],
            display_name=create_response["display_name"],
            email=create_response["email"],
            account_id=create_response["account_id"],
            role=create_response["role"],
            confirmed=create_response["confirmed"],
            # custom_attributes=create_response["custom_attributes"],
            accounts=create_response["accounts"],

        )
    session.add_all([user])
    session.commit()


def add_account_user(res):
    create_response = res
    with Session(engine.engine) as session:
        account_user = Account_User(
            account_id=create_response["account_id"],
            user_id=create_response["user_id"],
            role=create_response["role"]
        )
    session.add_all([account_user])
    session.commit()
