import pymorphy2.analyzer
from pymorphy2 import MorphAnalyzer

from constant import var
from service import check_apli, check_key


@check_apli
@check_key
def func(key) -> dict[str, str | int | list[str]]:
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

    match len(key):
        case 1:
            ...
        case _:
            last_word: pymorphy2.analyzer.Parse = morph.parse(key[-1])[0]
            variant: str = last_word.normal_form
            result["last_norm_form"]: list[str] = [variant]

    result["num_words"]: int = len(key)

    return result
