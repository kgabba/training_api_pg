import os
import psycopg2
from fastapi import Request, Depends

DB_URL = os.getenv('DB_URL')

def read_all():
    con = psycopg2.connect(DB_URL)
    cursor = con.cursor()
    cursor.execute('''select * from otzyvy''')
    data = cursor.fetchall()
    con.commit()
    con.close()
    return data

#подключение к БД - используется везде, где надо обратиться к БД
def con_db(req: Request):
    return req.app.state.conn




