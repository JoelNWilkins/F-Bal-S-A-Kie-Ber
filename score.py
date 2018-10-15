import string
import os
import pickle
from collections import Counter
from text import ngrams

def uniform(chars):
    dist = {}
    n = len(chars)
    for char in chars:
        dist[char] = 1/n
    return dist

class Chi_Squared:
    def __init__(self, expected=None, path=os.path.expanduser("~\\Documents\\Cipher Challenge\\Data\\english_monograms.pkl")):
        if path != None:
            with open(path, "rb") as f:
                self.__expected = pickle.load(f)
        else:
            self.__expected = expected

    def score(self, text):
        observed = Counter(text)
        length = len(text)
        total = 0
        for char in self.__expected.keys():
            expected = self.__expected[char]*length
            total += (observed[char] - expected)**2 / expected
        return total / length

class Measure_Of_Roughness(Chi_Squared):
    def __init__(self, chars=string.ascii_uppercase):
        self.__expected = uniform(chars)

class Index_Of_Coincidence:
    def __init__(self, chars=string.ascii_uppercase):
        self.__chars = chars
        self.__mr = Measure_Of_Roughness(chars=self.__chars)

    def score(self, text):
        return self.__mr.score(text) + (1/len(self.__chars))
