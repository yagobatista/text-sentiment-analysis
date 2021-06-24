from functools import reduce
from typing import Callable


import liwc


def clean(word: str) -> str:
    invalid_caracters = ["\n", ",", ","]

    caracters = filter(
        lambda caracter: caracter not in invalid_caracters,
        word,
    )
    normalized = map(lambda caracter: caracter.lower(), caracters)

    return "".join(normalized)


def validToken(word: str) -> bool:
    return word not in ("", "\n")


def tokenize(text: str) -> [str]:
    tokens = filter(validToken, text.split(" "))
    clean_tokens = map(clean, tokens)
    return list(clean_tokens)


def count_category(category, tokens: [str], parser: Callable) -> int:

    return reduce(
        lambda count, token: count + (1 if category in parse(token) else 0), tokens, 0
    )


parse, category_names = liwc.load_token_parser("LIWC2007_Portugues_win.dic")

text = open("entry.txt", "r").read()
text = text.replace("\n", "")
counter = {
    "swear": 0,
    "anx": 0,
    "negemo": 0,
    "posemo": 0,
}
tokens = tokenize(text)

counter = dict(
    map(
        lambda item: (item[0], count_category(item[0], tokens, parse)),
        counter.items(),
    )
)
# for token in tokens:
#     for category in parse(token):
#         if category in counter.keys():
#             counter[category] = counter[category] + 1

count = len(tokens)
posemo_ratio = counter["posemo"] * 100 / count
negemo_ratio = counter["negemo"] * 100 / count

print(
    f"""
1. Total de palavra é {count}
2. a. Total de palavras ofensivas {counter["swear"]}
2. b. Total de palavras ansiedade {counter["anx"]}
3. Total o tom positovo do texto é {posemo_ratio}% e o tom negativo é {negemo_ratio}%
"""
)
