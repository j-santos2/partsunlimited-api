from django.test import TestCase

from parts.views import words_from_text


class TestPartViews(TestCase):
    def test_words_from_text(self):
        text = "This is a test. It contains punctuation and both, lower and upper case characters, making up 18 words!"
        words = words_from_text(text)
        assert len(words) == 18
