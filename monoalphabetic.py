from score import *
from text import *

class Shift:
    def __init__(self, text):
        self.__text = text

    def encode(self, n):
        text = self.__text.copy()
        text.shift(n)
        return text

    def decode(self, n=None):
        if n != None:
            text = self.__text.copy()
            text.shift(len(self.__text.chars)-n)
            return text
        else:
            text = self.__text.copy()
            scorer = Chi_Squared()
            scores = {}
            for i in range(1, len(self.__text.chars)):
                text.shift(1)
                scores[scorer.score(text)] = i
            return self.decode(n=scores[min(scores.keys())]-1)
