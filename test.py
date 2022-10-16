import requests
import json
from pprint import pprint as pp


response = requests.post(
    "http://127.0.0.1:2000",
    data=json.dumps({"sentence": "1 думаю"}).encode("utf-8"),
    headers={
        "Content-Type": "application/json",
        "key": "ziax"
    }
)
pp(response.json())
