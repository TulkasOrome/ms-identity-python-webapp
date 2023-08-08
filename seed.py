import pymysql

conn = pymysql.connect(
    user="admin",
    password="Skeptic89a",
    host="hiver-mysql-dev.cd1wuzxpxrbp.us-west-2.rds.amazonaws.com",
    port=3306
  )
with conn.cursor() as cur:
    cur.execute('create database hiver-sql-dev;')