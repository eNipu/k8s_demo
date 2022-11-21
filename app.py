import os
import sys
import uvicorn

from fastapi import FastAPI

app = FastAPI(
    title="k8s-demo",
    description="k8s Demo using FastAPI",
    version="0.1.0",
    contact={"name": "k8s-demo", "url": "localhost:5000"},
    debug=True,
)


# run the code_format.sh script
def code_format():
    os.system("sh code_format.sh")


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/id")
def get_id():
    return {"id": 1}

@app.get("/name/", name="name")
def get_name(name: str):
    tmp = name
    print(tmp)
    return {"name": tmp}