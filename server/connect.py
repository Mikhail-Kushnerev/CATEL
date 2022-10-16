import json
import socket

from handler import func
from service import (
    NoPass,
    NoKeySentence,
    NoRussian,
    WrongType,
    NoTarget
)
from constant import HDRS, HOST, PORT


def build_server() -> None:
    server: socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()
    print("Working!")
    run(server)


def run(server: socket) -> None:
    while True:
        client, address = server.accept()

        with client:
            data: str = client.recv(1024).decode()

            try:
                result: str = json.dumps(func(data))
            except (
                    NoPass,
                    NoKeySentence,
                    NoRussian,
                    WrongType,
                    NoTarget
            ) as e:
                client.send(
                    HDRS.encode("utf-8") + json.dumps(
                        {"details": e.message}
                    ).encode("utf-8")
                )
            else:
                content: bytes = result.encode("utf-8")
                client.send(HDRS.encode("utf-8") + content)
