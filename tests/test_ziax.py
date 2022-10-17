import json
import requests

from http import HTTPStatus
from unittest import TestCase


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
        self.assertEqual(response.json(),
                         {
                             "details": "В данных нет ключа 'sentence'"
                         }
                         )
        response = requests.post(
            url=f"http://{self.host}:{self.port}",
            headers={
                "Content-Type": "application/json",
                "key": "ziax"
            },
            data=json.dumps(
                {
                    "sentence": ""
                }
            ).encode("utf-8")
        )
        self.assertEqual(response.json(), {"details": "Пустая фраза"})

    def test_post_result(self):
        response = requests.post(
            url=f"http://{self.host}:{self.port}",
            headers={
                "Content-Type": "application/json",
                "key": "ziax"
            },
            data=json.dumps(
                {
                    "sentence": "1 ! + сильный / * плыву"
                }
            ).encode("utf-8")
        )
        self.assertEqual(
            set(response.json()['first_declined_word']),
            set(
                [
                    'сильный',
                    'сильного',
                    'сильный',
                    'сильным',
                    'сильном',
                    'сильному'
                ]
            )
        )
