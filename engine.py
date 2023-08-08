from sqlalchemy import create_engine
from models import Base
from sqlalchemy import URL
import pymysql

# DB connection

url_object = URL.create(
    "mysql+pymysql",
    username="admin",
    password="nC150W&&*zD8",
    host="hiver-mysql.cd1wuzxpxrbp.us-west-2.rds.amazonaws.com:3306",
    database="hiver-mysql",
)

engine = create_engine(url_object)
Base.metadata.create_all(engine)
