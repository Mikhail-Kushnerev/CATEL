import json
import re
from typing import Callable, Any, Match

from constant import PATTERN, PASSWORD, CONTENT
from service.exceptions import (
    NoPass,
    NoKeySentence,
    WrongType,
    NoRussian
)


def check_apli(foo: Callable):
    def wrapper(*args):
        target: str = args[0].lower()

        if CONTENT not in target:
            raise WrongType("Неверный Content-Type")
        elif PASSWORD not in target:
            raise NoPass("Нет ключа")

        return foo(*args)

    return wrapper


def check_key(func: Callable):
    def wrapper(*args):
        target: str = args[0]
        match: Match[str | bytes | Any] | None = PATTERN.search(target)

        if match:
            target: str = match.group("target")
            target: dict[str, str] = json.loads(target)
        else:
            raise NoKeySentence("В данных нет ключа 'sentence'")

        key = target.get("sentence")

        if not key:
            raise NoKeySentence("Пустая фраза")
        elif re.match(r"[a-zA-Z]", "".join(key)):
            raise NoRussian("В тексте присутсвует латиница")
        key = re.findall(r"[а-яА-Я]+", key)
        return func(key)

    return wrapper
