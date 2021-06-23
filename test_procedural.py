from unittest import TestCase
from unittest.mock import patch
from procedural import clean, tokenize


class TestClean(TestCase):
    expected = "word"

    def test_comma(self):
        result = clean("word,")
        self.assertEquals(self.expected, result)

    def test_toLowerCase(self):
        result = clean("WORD")
        self.assertEquals(self.expected, result)


class TestTokenize(TestCase):
    expected = ["text", "text2", "text3", "text4"]

    def test_spaces(self):
        result = tokenize("text    text2  text3 text4")
        self.assertEquals(self.expected, result)

    def test_breakLine(self):
        result = tokenize(
            """text    text2

             text3


            text4
            """
        )
        self.assertEquals(self.expected, result)

    @patch("procedural.clean")
    def test_clean_is_called(self, clean_patch):
        result = tokenize("text")
        clean_patch.assert_called_once()
