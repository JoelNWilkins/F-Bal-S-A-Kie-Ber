import random
from score import *
from text import *

class Shift:
    def __init__(self, text, scorer=ngrams_Score()):
        self.__text = text
        self.__chars = self.__text.chars
        self.__length = len(self.__chars)
        self.__scorer = scorer

    def encode(self, n):
        text = [self.__chars[(self.__chars.index(char) + n) % self.__length]
            for char in self.__text]
        return Text(self.__text.format(text), chars=self.__chars)

    def decode(self, n=None):
        if n != None:
            return self.encode(self.__length - n)
        else:
            scores = {}
            for i in range(1, len(self.__chars)):
                scores[self.__scorer.score(self.decode(i))] = i
            return self.decode(self.__scorer.best(scores))

class Affine:
    def __init__(self, text, scorer=ngrams_Score()):
        self.__text = text
        self.__chars = self.__text.chars
        self.__length = len(self.__chars)
        self.__scorer = scorer

    def encode(self, a, b):
        if math.gcd(a, self.__length) != 1:
            raise ValueError("a must be coprime to the number of characters")
        text = [self.__chars[(a*self.__chars.index(char) + b) % self.__length]
            for char in self.__text]
        return Text(self.__text.format(text), chars=self.__chars)

    def decode(self, a=None, b=None):
        if a != None and b != None:
            if math.gcd(a, self.__length) != 1:
                raise ValueError("a must be coprime to the number of characters")
            for i in range(self.__length):
                if (a*i) % self.__length == 1:
                    break
            return self.encode(i, self.__length - b)
        else:
            scores = {}
            for a in range(self.__length):
                if math.gcd(a, self.__length) == 1:
                    for b in range(self.__length):
                        scores[self.__scorer.score(self.decode(a, b))] = (a, b)
            return self.decode(*self.__scorer.best(scores))
