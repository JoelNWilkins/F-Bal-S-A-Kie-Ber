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

    def decode(self, key):
        return self.encode(key.mod_inv(self.__length))
