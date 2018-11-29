from score import *
from text import *
from monoalphabetic import Shift

class Vigenere:
    def __init__(self, text, scorer=Chi_Squared()):
        self.__text = text
        self.__chars = self.__text.chars
        self.__length = len(self.__chars)
        self.__scorer = scorer

    def encode(self, key):
        n = len(key)
        output = [Shift(self.__text.section(n, i)).encode(self.__chars.index(key[i]))
            for i in range(n)]
        text = [output[i % n][i // n] for i in range(len(self.__text))]
        return Text(self.__text.format(text), chars=self.__chars)

    def decode(self, key=None, n=None, brute_force=False):
        if key != None:
            n = len(key)
            output = [Shift(self.__text.section(n, i)).decode(self.__chars.index(key[i]))
                for i in range(n)]
            text = [output[i % n][i // n] for i in range(len(self.__text))]
            return Text(self.__text.format(text), chars=self.__chars)
        else:
            if not brute_force:
                if n == None:
                    n = self.period()
                    print(n)
                output = [Shift(self.__text.section(n, i), scorer=self.__scorer).decode()
                    for i in range(n)]
                text = [output[i % n][i // n] for i in range(len(self.__text))]
                return Text(self.__text.format(text), chars=self.__chars)
            else:
                if n == None:
                    n = self.period()
                    print(n)
                scorer = ngrams_Score()
                best_text = self.__text.copy()
                best_score = scorer.score(best_text)
                key = [0]*n
                for i in range(self.__length**n):
                    key[-1] += 1
                    for j in range(n):
                        if key[-j-1] == self.__length:
                            key[-j-1] = 0
                            try:
                                key[-j-2] += 1
                            except:
                                pass
                        else:
                            break
                    text = self.decode("".join([self.__chars[k] for k in key]))
                    score = scorer.score(text)
                    if scorer.best({score: text, best_score: best_text}) == text:
                        best_score = score
                        best_text = text.copy()
                        print(best_text)
                return best_text

    def period(self, start=1, stop=20):
        length = len(self.__text)
        scorer = Index_Of_Coincidence(chars=self.__chars)
        scores = {}
        for n in range(start, stop+1):
            score = sum([len(self.__text.section(n, i))*scorer.score(self.__text.section(n, i))
                for i in range(n)]) / length
            scores[score] = n
        return scorer.best(scores)
