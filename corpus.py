from collections import Counter
from text import *

def Corpus(n, files):
    grams = {}
    for file in files:
        t = Text(path=file)
        freq = Counter(t.ngrams(n))
        for gram, number in freq.items():
            if gram in grams.keys():
                grams[gram] += number
            else:
                grams[gram] = number
    prob = {}
    total = sum(grams.values())
    for gram, number in grams.items():
        prob[gram] = number / total
    return prob
