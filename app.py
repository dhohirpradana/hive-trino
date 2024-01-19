from trino.dbapi import connect

conn = connect(
    host="10.1.111.7",
    port=30345,
    user="admin",
    catalog="hive",
    schema="default",
)
cur = conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS test (id int)")
rows = cur.fetchall()

print(rows)
