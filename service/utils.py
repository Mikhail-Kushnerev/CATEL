import json
import re
from typing import Callable

from service.exceptions import (
    NoPass,
    NoKeySentence,
    WrongType,
    NoRussian
)
from constant import PATTERN, PASSWORD, CONTENT


def check_apli(foo: Callable):
    def wrapper(*args):
        target: str = args[0].lower()

        if CONTENT not in target:
            raise WrongType
        elif PASSWORD not in target:
            raise NoPass

        return foo(*args)

    return wrapper


def check_key(func: Callable):
    def wrapper(*args):
        target: str = args[0]
        match: re.Pattern = PATTERN.search(target)

        if match:
            target: str = match.group("target")
            target: dict[str, str] = json.loads(target)

        key = target.get("sentence")

        if not key:
            raise NoKeySentence
        elif re.match(r"[a-zA-Z]]", "".join(key)):
            raise NoRussian

        return func(key.split())

    return wrapper
