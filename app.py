import os
import sys
import uvicorn
import json

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
