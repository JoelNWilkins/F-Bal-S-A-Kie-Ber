import string
import os
import pickle
import math
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
        if expected == None:
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

    def best(self, scores, rank=1):
        return scores[sorted(scores.keys())[rank-1]]

class Measure_Of_Roughness(Chi_Squared):
    def __init__(self, chars=string.ascii_uppercase):
        Chi_Squared.__init__(self, expected=uniform(chars))

class Index_Of_Coincidence:
    def __init__(self, chars=string.ascii_uppercase):
        self.__chars = chars

    def score(self, text):
        freq = Counter(text)
        length = len(text)
        total = sum([freq[char]*(freq[char] - 1) for char in freq.keys()])
        return total / (length*(length - 1))

    def best(self, scores, rank=1):
        return scores[sorted(scores.keys())[len(scores)-rank]]

class ngrams_Score:
    def __init__(self, probs=None, path=os.path.expanduser("~\\Documents\\Cipher Challenge\\Data\\english_quadgrams.pkl")):
        if probs == None:
            with open(path, "rb") as f:
                self.__probs = pickle.load(f)
        else:
            self.__probs = probs

    def score(self, text):
        total = 0
        for gram in ngrams(text, len(list(self.__probs.keys())[0])):
            if gram in self.__probs:
                total += math.log10(self.__probs[gram])
            else:
                total -= 5
        return total / len(text)

    def best(self, scores, rank=1):
        return scores[sorted(scores.keys())[len(scores)-rank]]
