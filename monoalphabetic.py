import random
from score import *
from text import *
from scraper import *

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
            scorer = ngrams_Score()
            scores = {}
            for i in range(1, len(self.__text.chars)):
                text.shift(1)
                scores[scorer.score(text)] = i
            return self.decode(n=scores[max(scores.keys())]-1)

class Affine:
    def __init__(self, text):
        self.__text = text

    def encode(self, a, b):
        m = len(self.__text.chars)
        if math.gcd(a, m) != 1:
            raise ValueError("a must be coprime to the number of characters")
        text = [self.__text.chars[(self.__text.chars.index(char)*a+b) % m] for char in self.__text]
        return Text(self.__text.format(text))

    def decode(self, a=None, b=None):
        if a != None and b != None:
            m = len(self.__text.chars)
            if math.gcd(a, m) != 1:
                raise ValueError("a must be coprime to the number of characters")
            for i in range(m):
                if (a*i) % m == 1:
                    break
            return self.encode(i, m-b)
        else:
            m = len(self.__text.chars)
            text = self.__text.copy()
            scorer = Index_Of_Coincidence(self.__text.chars)
            scores = {}
            for a in range(m):
                if math.gcd(a, m) == 1:
                    scores[scorer.score(self.decode(a, 0))] = a
            return Shift(self.decode(scores[max(scores.keys())], 0)).decode()

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
