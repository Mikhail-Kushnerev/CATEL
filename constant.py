import re
from pymorphy2.tagset import OpencorporaTag


HDRS: str = "HTTP/1.1 200 OK\r\nContent-Type: application/json; charset=utf-8\r\n\r\n"
PASSWORD: str = "ziax"
CONTENT: str = "application/json"

PATTERN: re.Pattern = re.compile(r"(?P<target>{\n?\s{0,}.*\n?})")

var: frozenset[str] = OpencorporaTag.CASES
