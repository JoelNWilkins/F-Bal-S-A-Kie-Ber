import random
from score import *
from text import *
from scraper import *

class Shift:
    def __init__(self, text):
        self.__text = text
        self.__chars = self.__text.chars
        self.__length = len(self.__chars)

    def encode(self, n):
        text = [self.__chars[(self.__chars.index(char) + n) % self.__length]
            for char in self.__text]
        return Text(self.__text.format(text))

    def decode(self, n=None):
        if n != None:
            return self.encode(self.__length - n)
        else:
            scorer = ngrams_Score()
            scores = {}
            for i in range(1, len(self.__chars)):
                scores[scorer.score(self.decode(i))] = i
            return self.decode(scores[max(scores.keys())])

class Affine:
    def __init__(self, text):
        self.__text = text
        self.__chars = self.__text.chars
        self.__length = len(self.__chars)

    def encode(self, a, b):
        if math.gcd(a, self.__length) != 1:
            raise ValueError("a must be coprime to the number of characters")
        text = [self.__chars[(a*self.__chars.index(char) + b) % self.__length]
            for char in self.__text]
        return Text(self.__text.format(text))

    def decode(self, a=None, b=None):
        if a != None and b != None:
            if math.gcd(a, self.__length) != 1:
                raise ValueError("a must be coprime to the number of characters")
            for i in range(self.__length):
                if (a*i) % self.__length == 1:
                    break
            return self.encode(i, self.__length - b)
        else:
            scorer = ngrams_Score()
            scores = {}
            for a in range(self.__length):
                if math.gcd(a, self.__length) == 1:
                    for b in range(self.__length):
                        scores[scorer.score(self.decode(a, b))] = (a, b)
            return self.decode(*scores[max(scores.keys())])

def substitution(text):
    ciphertext = text
    chars = list(ciphertext.chars)
    scorer = ngrams_Score()
    best_score = float("-inf")
    best_text = ciphertext.copy()
    while True:
        char1 = random.choice(chars)
        char2 = random.choice(chars)
        ciphertext[char1] = char2
        for i, char in enumerate(chars):
            if char == char1:
                chars[i] = char2
            elif char == char2:
                chars[i] = char1
        score = scorer.score(ciphertext)
        if score > best_score:
            best_score = score
            best_text = ciphertext.copy()
            best_alpha = chars[:]
            print(repr(best_text)[:80])
            print(chars)
        else:
            ciphertext[char1] = char2
            for i, char in enumerate(chars):
                if char == char1:
                    chars[i] = char2
                elif char == char2:
                    chars[i] = char1
