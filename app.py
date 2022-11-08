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


def start():
    uvicorn.run(app, host="127.0.0.1", port=5000)


# if __name__ == "__main__":
#     start()
