from sqlalchemy import create_engine
from models import Base
from sqlalchemy import URL
import pymysql

# DB connection

url_object = URL.create(
    "mysql+pymysql",
    username="admin",
    password="Skeptic89a",
    host="hiver-sql-dev.cd1wuzxpxrbp.us-west-2.rds.amazonaws.com",
    port=3306,
    database="hiver_sql_dev",
)

engine = create_engine(url_object)
Base.metadata.create_all(engine)
