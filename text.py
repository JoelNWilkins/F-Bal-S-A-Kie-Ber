import re
import string

def ngrams(text, n, overlap=True):
    if len(text) < n:
        raise ValueError("the length of the text must be larger than n")
    if overlap:
        for i in range(len(text)-n+1):
            yield text[i:i+n]
    elif not overlap:
        for i in range(int(len(text)//n)):
            yield text[i*n:(i+1)*n]

class Text:
    def __init__(self, text, chars=string.ascii_uppercase, case="auto"):
        self.__chars = chars
        self.__case = case.lower()

        if self.__case == "auto":
            if self.__chars == string.ascii_uppercase:
                text = text.upper()
            elif self.__chars == string.ascii_lowercase:
                text = text.lower()
        elif self.__case == "upper":
            text = text.upper()
        elif self.__case == "lower":
            text = text.lower()

        self.__text = [char for char in text if char in self.__chars]
        p = re.compile("[{}]".format(self.__chars))
        self.__temp = "{}".join(p.split(text))

    def __repr__(self):
        return "".join(self.__text)

    def __str__(self):
        return self.__temp.format(*self.__text)

    def __get__(self):
        return self.__repr__()

    def __getitem__(self, key):
        if isinstance(key, int) or isinstance(key, slice):
            return "".join(self.__text[key])
        else:
            raise TypeError("{} indices must be integers or slices, not {}"
                .format(self.__class__.__name__, key.__class__.__name__))

    def __setitem__(self, key, value):
        if isinstance(key, str):
            for i, char in enumerate(self.__text):
                if char == key:
                    self.__text[i] = value
                elif char == value:
                    self.__text[i] = key
        elif isinstance(key, int) or isinstance(key, slice):
            self.__text[key] = value
        else:
            raise TypeError("{} indices must be integers, slices or strings, not {}"
                .format(self.__class__.__name__, key.__class__.__name__))

    def __len__(self):
        return len(self.__text)

    def __iter__(self):
        self.__count = -1
        self.__length = self.__len__()
        return self

    def __next__(self):
        self.__count += 1
        if self.__count < self.__length:
            return self.__text[self.__count]
        else:
            raise StopIteration

    def reverse(self):
        # can also call reversed method with a Text object as an argument
        self.__text = list(reversed(self.__text))

    def reverse_words(self, sep=" "):
        self.__text = sep.join(["".join(list(reversed(word)))
            for word in self.__repr__().split(sep)])

    def shift(self, n):
        self.__text = [self.__chars[(self.__chars.index(char)+n) % len(self.__chars)]
            for char in self.__text]

    def ngrams(self, n, overlap=True):
        return ngrams(self.__repr__(), n, overlap=overlap)

    def copy(self):
        return Text(self.__repr__())

    @property
    def chars(self):
        return self.__chars
