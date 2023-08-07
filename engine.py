from sqlalchemy import create_engine
from models import Base
from sqlalchemy import URL
import pymysql

# DB connection

url_object = URL.create(
    "mysql+pymysql",
    username="admin",
    password="jATo75T1N#!7",
    host="hiver-sql-awtest.cd1wuzxpxrbp.us-west-2.rds.amazonaws.com",
    database="hiver-sql-awtest",
)

engine = create_engine(url_object)
Base.metadata.create_all(engine)
