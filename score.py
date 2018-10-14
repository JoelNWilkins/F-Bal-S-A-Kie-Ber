import os
import pickle
import string
import math
from collections import Counter
from text import ngrams

try:
    path = os.path.expanduser("~\\Documents\\Cipher Challenge\\english_monograms.pkl")
    with open(path, "rb") as f:
        letter_freq = pickle.load(f)
except:
    letter_freq = {}
    for char in string.ascii_uppercase:
        letter_freq[char] = 1/26

class Chi_Squared:
    def __init__(self, expected=letter_freq):
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
        self.__expected = {}
        length = len(self.__char)
        for char in self.__chars:
            self.__expected[char] = 1/length

class Index_Of_Coincidence:
    def __init__(self, chars=string.ascii_uppercase):
        self.__chars = chars
        self.__mr = Measure_Of_Roughness(chars=self.__chars)

    def score(self, text):
        return self.__mr.score(text) + (1/len(self.__chars))
