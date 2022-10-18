import json
import re
from typing import Callable, Any, Match

from constant import PATTERN, PASSWORD, CONTENT
from src.service import logger
from src.service.exceptions import (
    NoPass,
    NoKeySentence,
    WrongType,
    NoRussian
)


def check_apli(foo: Callable):
    logger.info('Проверка Headers')
    def wrapper(*args):
        target: str = args[0].lower()

        if CONTENT not in target:
            logger.error('В Headers указан неверный Content-Type')
            raise WrongType("Неверный Content-Type")
        elif PASSWORD not in target:
            logger.error('В Headers указан ключ с ошибкой или отсутствует')
            raise NoPass("Нет ключа")

        return foo(*args)

    return wrapper


def check_key(func: Callable):
    def wrapper(*args):
        logger.info("Headers указаны верные")
        target: str = args[0]
        match: Match[str | bytes | Any] | None = PATTERN.search(target)

        if match:
            target: str = match.group("target")
            target: dict[str, str] = json.loads(target)
        else:
            logger.error("В запросе отсутствует параметр 'sentence'")
            raise NoKeySentence("В данных нет ключа 'sentence'")

        key = target.get("sentence")

        if not key:
            logger.error("Параметр 'sentence' содержит пустую строк")
            raise NoKeySentence("Пустая фраза")
        elif re.match(r"[a-zA-Z]", "".join(key)):
            logger.error("Параметр 'sentence' содержит латиницу")
            raise NoRussian("В тексте присутсвует латиница")
        key = re.findall(r"[а-яА-Я]+", key)
        logger.info("Запрос не содержит ошибок")
        return func(key)

    return wrapper
