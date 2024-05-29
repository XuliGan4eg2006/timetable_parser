import ast
import psycopg2
import redis
from fastapi import FastAPI

r = redis.Redis(host='redis', port=6379, db=0)
print("Initing db.....")

psycopg_connection = psycopg2.connect(dbname='mtusi', user='postgres', password='lmao123',
                                      host='db',
                                      port='5432')
cursor = psycopg_connection.cursor()

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/groups")
def return_groups():
    groups = r.get("groups")
    decoded_groups = groups.decode('utf-8').replace("'", "")

    return {"groups": decoded_groups.split(",")}


@app.get("/insert_token/{couple}")
def insert_token(couple: str):
    fcm_token, group = couple.split("|")

    cursor.execute("SELECT COUNT(*) FROM users WHERE fcm_token = %s", (fcm_token,))
    result = cursor.fetchone()

    if result[0] == 0:
        cursor.execute("INSERT INTO users VALUES (%s, %s)", (fcm_token, group))
        psycopg_connection.commit()
    else:
        cursor.execute("UPDATE users SET group_name = %s WHERE fcm_token = %s", (group, fcm_token))
        psycopg_connection.commit()
    return {"status": "ok"}


@app.get("/timetable/{group}")
def get_lessons(group: str):
    ret = r.get(group)
    return ast.literal_eval(ret.decode('utf-8'))


# def start_server():
#     uvicorn.run(app, host="0.0.0.0", port=8000)

# if __name__ == "__main__":
#     uvicorn.run(app, host="0.0.0.0", port=8000)