import socket
import json
from socket import socket

from constant import HDRS
from api import func


def run() -> None:
    server: socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("localhost", 2000))
    server.listen()
    print("Working!")

    while True:
        client, address = server.accept()

        with client:
            data: str = client.recv(1024).decode()

            try:
                result: str = json.dumps(func(data))
            except Exception:
                client.send(HDRS.encode("utf-8") + json.dumps({"details": "ban"}).encode("utf-8"))
            else:
                content: bytes = result.encode("utf-8")
                client.send(HDRS.encode("utf-8") + content)
