import sqlite3

def open_basiccrud_db():
    conn = sqlite3.connect('basic_crud.db')
    cur = conn.cursor()
    return conn,cur


def close_database(cur,conn):
    cur.close()
    conn.close()


def print_table_users(sql):
    conn, cur = open_basiccrud_db()
    cur.execute(sql)
    
    data = cur.fetchall()
    for row in data:
        print(row)
    
    cur.close()
    conn.close()
