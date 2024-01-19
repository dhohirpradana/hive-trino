import os
from trino.dbapi import connect
import dotenv

dotenv.load_dotenv()

HOST = os.getenv("HOST")
PORT = os.getenv("PORT")
USER = os.getenv("USER")

conn = connect(
    host="HOST",
    port=PORT,
    user="USER",
    catalog="hive",
    schema="default",
)
cur = conn.cursor()
cur.execute("SHOW TABLES")
rows = cur.fetchall()

print(rows)
