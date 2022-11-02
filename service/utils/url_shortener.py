from random import randint, choice

from service.utils.constants import (
    SHORT_URL_PREFIX, SHORT_URL_CHAR_AMOUNT,
    CHARACTER_RANGES
)


def generate_random_short_url() -> str:
    """Generates random short url.

    Returns:
        str - random short url string.
    """
    short_url = ""

    for _ in range(SHORT_URL_CHAR_AMOUNT):
        random_character_range = choice(CHARACTER_RANGES)
        random_character = chr(randint(*random_character_range))
        short_url += random_character

    return f"{SHORT_URL_PREFIX}/{short_url}"
