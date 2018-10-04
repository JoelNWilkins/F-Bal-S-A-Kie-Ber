import os
import pickle
from collections import Counter

class Chi_Squared:
    def __init__(self, *args, **kwargs):
        if "case" in kwargs.keys():
            self.__case = kwargs.pop("case").upper()
        else:
            self.__case = "NONE"

        if "path" in kwargs.keys():
            path = kwargs.pop("path")
        else:
            path = os.path.expanduser("~\\Documents\\Cipher Challenge\\english_monograms.pkl")

        with open(path, "rb") as f:
            self.expected = pickle.load(f)

    def score(self, text):
        observed = Counter(text)
        length = len(text)
        total = 0
        for char in self.expected.keys():
            if self.__case == "UPPER":
                char = char.upper()
            elif self.__case == "LOWER":
                char = char.lower()

            expected = self.expected[char]*length
            total += (observed[char] - expected)**2 / expected
        return total / length
