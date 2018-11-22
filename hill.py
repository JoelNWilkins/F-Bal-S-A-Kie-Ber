import math
from score import *
from text import *
from matrix import Matrix

class Hill:
    def __init__(self, text):
        self.__text = text
        self.__chars = text.chars
        self.__length = len(self.__chars)

    def encode(self, key):
        n = key.shape[0]
        output = ""
        for block in self.__text.ngrams(n, overlap=False):
            if len(block) < n:
                block += (n-len(block))*"X"
            plaintext = Matrix([self.__chars.index(char) for char in block], shape=(1, n))
            ciphertext = (key * plaintext) % self.__length
            output += "".join([self.__chars[i] for i in ciphertext.column(0)])
        return Text(self.__text.format(list(output)), chars=self.__chars)

    def decode(self, key=None, crib=None, n=None):
        if isinstance(key, Matrix):
            return self.encode(key.mod_inv(self.__length))
        else:
            if n == None and crib != None:
                n = int(math.floor((len(crib) + 1.25)**0.5 - 0.5))
            crib_keys = [Matrix([[self.__chars.index(crib[i+n*j+k]) for j in range(n)]
                for i in range(n)]) for k in range(n)]
            scorer = ngrams_Score()
            best_score = -float("inf")
            best_text = self.__text.copy()
            for k in range(len(self.__text)-n+1):
                try:
                    if isinstance(crib_keys[k%n], Matrix):
                        cipher_matrix = Matrix([[self.__chars.index(self.__text[i+n*j+n*((k+n-1)//n)])
                            for j in range(n)] for i in range(n)]).mod_inv(self.__length)
                        key = (crib_keys[k%n]*cipher_matrix) % self.__length
                        attempt = self.encode(key)
                        score = scorer.score(attempt)
                        if score > best_score:
                            best_score = score
                            best_text = attempt.copy()
                except:
                    pass
            return best_text
