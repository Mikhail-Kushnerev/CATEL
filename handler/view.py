import pymorphy2.analyzer
from pymorphy2 import MorphAnalyzer

from constant import var
from service import check_apli, check_key, logger


@check_apli
@check_key
def func(key) -> dict[str, str | int | list[str]]:
    logger.info("Начало морфологического разбора")
    morph: MorphAnalyzer = MorphAnalyzer(lang="ru")

    result: dict[str, str | int | list[str]] = {
        "status": "ok"
    }
    first_word: pymorphy2.analyzer.Parse = morph.parse(key[0])[0]
    result["first_declined_word"]: list[str] = [key[0]]

    coll: set[str] = set()

    for i in var:
        variant: str = first_word.inflect({i, "sing"}).word
        coll.add(variant)
    coll -= {key[0]}
    result["first_declined_word"].extend(list(coll))
    logger.info("Разобрано первое слово")
    match len(key):
        case 1:
            logger.info("В предложение только одно слово")
        case _:
            last_word: pymorphy2.analyzer.Parse = morph.parse(key[-1])[0]
            variant: str = last_word.normal_form
            result["last_norm_form"]: list[str] = [variant]
            logger.info("Разобрано последнее слово")

    result["num_words"]: int = len(key)
    logger.info("Ответ готов")

    return result
