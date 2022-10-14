from b_my_func import open_basiccrud_db
from b_my_func import close_database

conn, cur = open_basiccrud_db()
sql = '''CREATE TABLE IF NOT EXISTS users
(
    name TEXT,
    age INTEGER,
    dateofbirth TEXT,
    sex TEXT, email TEXT
)'''

cur.execute(sql)
conn.commit()

close_database(cur,conn)