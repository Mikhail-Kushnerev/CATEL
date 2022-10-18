import json
import socket

from src.handler import func
from src.service import (
    NoPass,
    NoKeySentence,
    NoRussian,
    WrongType,
    NoTarget,
    logger
)
from constant import HDRS, HOST, PORT


def build_server() -> None:
    server: socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    logger.info("Создание приёмника запросов")
    server.bind((HOST, PORT))
    logger.info("Установка связи прёмника с хостом и портом")
    server.listen()
    logger.info("Сервер ожидает запросов")
    run(server)
    logger.info("Сервер запущен")


def run(server: socket) -> None:
    while True:
        client, address = server.accept()
        logger.info("Получен запрос")

        with client:
            data: str = client.recv(1024).decode()

            try:
                result: str = json.dumps(func(data))
                logger.info("Обработка запроса")
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
                logger.info("Запрос содержит ошибку")
            else:
                content: bytes = result.encode("utf-8")
                client.send(HDRS.encode("utf-8") + content)
                logger.info("Запрос обработан. Клиент получил ответ")
