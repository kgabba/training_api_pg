from fastapi import FastAPI
import uvicorn
from router import router_test
import psycopg2
from contextlib import asynccontextmanager
import os
import time


DB_URL = os.getenv('DB_URL')

@asynccontextmanager
async def lifespan(api: FastAPI):
    try:
        time.sleep(7)  # Ждем немного, чтобы база данных могла запуститься
        api.state.conn = psycopg2.connect(DB_URL)
        api.state.conn.autocommit = True
        print('подключение БД успешно создано')

        cursor = api.state.conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS otzyvy (
        id SERIAL PRIMARY KEY,
        text TEXT NOT NULL,
        mail TEXT NOT NULL,
        phone BIGINT, 
        mood TEXT NOT NULL
        )''')
        cursor.close()

    except Exception as e:
        print('ошибка подключения к БД:', e)
        raise RuntimeError('Ошибка подключения к БД')
    
    yield
    
    api.state.conn.close()
    print('Подключение к БД остановлено')

api = FastAPI(lifespan=lifespan)


api.include_router(router_test)

if __name__ == '__main__':
    uvicorn.run(app='main:api', port=8000, host="0.0.0.0", reload=True)
