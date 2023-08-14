from sqlalchemy import create_engine
from models import Base
from sqlalchemy import URL
import pymysql

# DB connection

url_object = URL.create(
    "mysql+pymysql",
    username="root",
    password="arcturus!5",
    host="127.0.0.1",
    port=3306,
    database="hiver-sql-dev",
)

engine = create_engine(url_object)
Base.metadata.create_all(engine)
