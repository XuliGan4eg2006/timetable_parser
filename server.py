import ast
import uvicorn
import sqlite3
import redis
from config import *
from fastapi import FastAPI

r = redis.Redis(host='localhost', port=6379, db=0)
print("Initing db.....")

sqlite_conn = sqlite3.connect("base.db", check_same_thread=False)
cursor = sqlite_conn.cursor()

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/groups")
def return_groups():
    return {"groups": groups}


@app.get("/insert_token/{couple}")
def insert_token(couple: str):
    fcm_token, group = couple.split("|")

    in_db = cursor.execute("SELECT COUNT(*) FROM users WHERE fcm_token = ?", (fcm_token,)).fetchone()

    if in_db[0] == 0:
        cursor.execute("INSERT INTO users VALUES (?, ?)", (fcm_token, group))
        sqlite_conn.commit()
    else:
        cursor.execute("UPDATE users SET group_name = ? WHERE fcm_token = ?", (group, fcm_token))
        sqlite_conn.commit()
    return {"status": "ok"}


@app.get("/timetable/{group}")
def get_lessons(group: str):
    ret = r.get(group)
    return ast.literal_eval(ret.decode('utf-8'))


def start_server():
    uvicorn.run(app, host="0.0.0.0", port=8000)
