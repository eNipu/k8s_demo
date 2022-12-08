import os
import sys
import uvicorn
import json
import psycopg2

from fastapi import FastAPI

# app = FastAPI(
#     title="k8s-demo",
#     description="k8s Demo using FastAPI",
#     version="0.1.0",
#     contact={"name": "k8s-demo", "url": "localhost:5000"},
#     debug=True,
# )

app = FastAPI(DEBUG=True)


# run the code_format.sh script
def code_format():
    os.system("sh code_format.sh")


@app.get("/")
def read_root():
    return {"Hello": "K8s demo"}


@app.get("/health")
def health():
    # print("health check")
    return {"status": "ok"}


@app.get("/id")
def get_id():
    return {"id": 1}


@app.get("/name/", name="name")
def get_name(name: str):
    tmp = name
    print(tmp)
    return {"name": tmp}


@app.get("/db/")
def get_db():
    file_path = "config/db.json"
    if os.path.isfile(file_path):
        with open(file_path) as json_file:
            data = json.load(json_file)
            return data
    else:
        return {"error": "db.conf not found"}

# connect to the postgres kubernates service using the service name postgres-service, the port is 5432 and the database is postgres
@app.get("/postgres/")
def connect():
    conn = None
    try:
        conn = psycopg2.connect(host="postgres-service", database="postgres", user="postgres" , password="password", port="5432", sslmode="disable")
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS test (id serial PRIMARY KEY, name varchar);")
        cur.execute("INSERT INTO test (name) VALUES ('Amin');")
        cur.execute("SELECT * FROM test")
        row = cur.fetchone()
        while row is not None:
            print(row)
            return {"id": row[0], "name": row[1]}
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    # finally:
    #     return {"error": "error connecting to database"}