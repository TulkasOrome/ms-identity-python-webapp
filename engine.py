from sqlalchemy import create_engine
from models import Base
from sqlalchemy import URL
import pymysql

# DB connection

url_object = URL.create(
    "mysql+pymysql",
    username="root",
    password="arcturus!5",
    host="localhost",
    database="hiver-sql-dev",
)

engine = create_engine(url_object)
Base.metadata.create_all(engine)
