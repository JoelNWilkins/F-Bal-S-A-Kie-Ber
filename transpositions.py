import random
from text import *
from score import *

class Columnar:
    def __init__(self, text):
        self.__text = text
        self.__length = len(self.__text)

    def encode(self, n, key=None):
        if key != None:
            n = len(key)
        q, r = divmod(self.__length, n)
        columns = ["".join([self.__text[n*i+c] for i in range(q+int(c<r))]) for c in range(n)]
        if key == None:
            return Text(self.__text.format("".join(columns)))

    def decode(self, n=None, key=None):
