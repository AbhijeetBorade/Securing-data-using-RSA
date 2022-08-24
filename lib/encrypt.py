
from lib.utils import convert_to_ascii


def encrypt(plain_text: str, e: int, n: int) -> list[int]:
    ascii_message = convert_to_ascii(plain_text)

    return [(i**e) % n for i in ascii_message]
