import json

from sqlalchemy.orm import Session
import engine
from models import Account


def add_account(res):
    create_response = res
    with Session(engine.engine) as session:
        account = Account(
            id=create_response["id"],
            name=create_response["name"]
        )
    session.add_all([account])
    session.commit()
