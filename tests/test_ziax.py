import json
import requests

from http import HTTPStatus
from unittest import TestCase


TRACEBACKS: tuple[str, ...] = (
    "В тексте присутсвует латиница",
    "В данных нет ключа 'sentence'",
    "Неверный Content-Type"
    "Нет ключа"
)


class TestConnect(TestCase):

    def setUp(self):
        self.host = "127.0.0.1"
        self.port = 2000

    def test_status(self):
        response = requests.get(url=f"http://{self.host}:{self.port}")
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_post(self):
        response = requests.post(url=f"http://{self.host}:{self.port}")
        self.assertEqual(response.json(), {"details": "Неверный Content-Type"})
        response = requests.post(
            url=f"http://{self.host}:{self.port}",
            headers={
                "Content-Type": "application/json"
            }
        )
        self.assertEqual(response.json(), {"details": "Нет ключа"})
        response = requests.post(
            url=f"http://{self.host}:{self.port}",
            headers={
                "Content-Type": "application/json",
                "key": "ziax"
            }
        )
        self.assertEqual(response.json(), {"details": "В данных нет ключа 'sentence'"})
        response = requests.post(
            url=f"http://{self.host}:{self.port}",
            headers={
                "Content-Type": "application/json",
                "key": "ziax"
            },
            data=json.dumps({"sentence": ""}).encode("utf-8")
        )
        self.assertEqual(response.json(), {"details": "В данных нет ключа 'sentence'"})

