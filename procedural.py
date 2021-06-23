from collections import Counter
import liwc


def clean(word: str) -> str:
    invalid_caracters = ["\n", ",", ","]
    new_word = ""

    for caracter in word:
        if caracter not in invalid_caracters:
            new_word += caracter.lower()

    return new_word


def validToken(word: str) -> bool:
    return word not in ("", "\n")


def tokenize(text: str) -> [str]:
    tokens = []
    for word in text.split(" "):
        if validToken(word):
            tokens.append(clean(word))

    return tokens


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
for token in tokens:
    for category in parse(token):
        if category in counter.keys():
            counter[category] = counter[category] + 1

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
