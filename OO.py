from typing import Callable
import liwc


class Token:
    __word: str

    def __init__(self, word):
        self.__word = word

    def clean(self) -> str:
        invalid_caracters = ["\n", ",", ","]
        new_word = ""

        for caracter in self.__word:
            if caracter not in invalid_caracters:
                new_word += caracter.lower()

        return new_word


class Tokenizer:
    __text: str
    __tokens: [str]

    def __init__(self, file_name):
        text = open(file_name, "r").read()
        self.__text = text.replace("\n", "")
        self.__tokens = [word for word in self.__text.split(" ") if self.validToken(word)]

    def validToken(self, word: str) -> bool:
        return word not in ("", "\n")

    def get_tokens(
        self,
    ) -> [str]:
        return self.__tokens


class Counter:
    __tokens: [str]
    __parse: Callable

    def __init__(self, tokens: [str]):
        parse, category_names = liwc.load_token_parser("LIWC2007_Portugues_win.dic")
        self.__parse = parse
        self.__tokens = tokens

    def get_tokens(self):
        return self.__tokens

    def count(self):
        counter = {
            "swear": 0,
            "anx": 0,
            "negemo": 0,
            "posemo": 0,
        }
        tokens = self.get_tokens()

        for token in tokens:
            for category in self.__parse(token):
                if category in counter.keys():
                    counter[category] = counter[category] + 1

        return counter, len(tokens)


class CleanCounter(Counter):
    def get_tokens(self):
        tokens = super().get_tokens()
        return [Token(word).clean() for word in tokens]


tokenizer = Tokenizer("entry.txt")

tokens = tokenizer.get_tokens()
counter, total_count = CleanCounter(tokens).count()

posemo_ratio = counter["posemo"] * 100 / total_count
negemo_ratio = counter["negemo"] * 100 / total_count

print(
    f"""
1. Total de palavra é {total_count}
2. a. Total de palavras ofensivas {counter["swear"]}
2. b. Total de palavras ansiedade {counter["anx"]}
3. Total o tom positovo do texto é {posemo_ratio}% e o tom negativo é {negemo_ratio}%
"""
)
