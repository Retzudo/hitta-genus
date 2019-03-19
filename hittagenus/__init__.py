import re
import requests
import sys

headers = {"User-Agent": "hitta-genus/1.0.0"}


def get_genus(word):
    url = "https://svenska.se/tri/f_saol.php?sok={word}".format(word=word)
    response = requests.get(url, headers=headers)
    text = response.text

    try:
        if text.index('~et'):
            return "ett", "et"
    except ValueError:
        pass

    try:
        if text.index('~en'):
            return "en", "en"
    except ValueError:
        pass

    try:
        if text.index('inga svar'):
            return None
    except ValueError:
        pass

    raise RuntimeError(
        "Something went wrong with the request. Could not extract information.",
        response.text,
    )


def print_genus(word, genus_info):
    if not genus_info:
        print("{word}: inga svar".format(word=word))
        return

    article, suffix = genus_info
    print(
        "{word}: \u001b[4m{article}\u001b[0m {word}, {word}\u001b[4m{suffix}\u001b[0m".format(
            word=word, article=article, suffix=suffix
        )
    )
