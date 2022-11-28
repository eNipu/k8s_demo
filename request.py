import requests # pip install requests

#node_ip:node_port
url = "http://192.168.59.105:32000"
url = "http://k8s.dag.com:80"

# get the root
def get_root():
    req = requests.get(url, "/")
    print(req.json())
    print(req.status_code)
    
    # return req.get()

# get the health
def get_health():
    req = requests.get(url, "/health")
    print(req.status_code)
    # return req.get()

# get the id
def get_id():
    req = requests.get(url, "/id = 1")
    print(req.status_code)
    # return req.get()

get_root()