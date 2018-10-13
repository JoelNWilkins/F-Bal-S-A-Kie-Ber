import re
import string
import ngrams

class Text:
    def __init__(self, *args, **kwargs):
        if "chars" in kwargs.keys():
            self.__chars = kwargs.pop("chars")
        else:
            self.__chars = string.ascii_uppercase

        if self.__chars == string.ascii_uppercase:
            text = args[0].upper()
        elif self.__chars == string.ascii_lowercase:
            text = args[0].lower()
        else:
            text = args[0]

        self.__text = [char for char in text if char in self.__chars]
        p = re.compile("[{}]".format(self.__chars))
        self.__temp = "{}".join(p.split(args[0]))

    def __repr__(self):
        return "".join(self.__text)

    def __str__(self, *args, **kwargs):
        return self.__temp.format(*self.__text)

    def __get__(self):
        return self.__repr__()

    def __getitem__(self, key):
        return self.__text[key]

    def __setitem__(self, key, value):
        if isinstance(key, str):
            for i, char in self.__text:
                if char == key:
                    self.__text[i] = value
                elif char == value:
                    self.__text[i] = key
        elif isinstance(key, int) or isinstance(key, slice):
            self.__text[key] = value
        else:
            raise TypeError("invalid index of type '{}'".format(key.__class__.__name__))

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
        self.__text = sep.join(["".join(list(reversed(word))) for word in self.__repr__().split(sep)])

    def shift(self, n):
        self.__text = "".join([self.__chars[(self.__chars.index(char)+n) % len(self.__chars)]
            for char in self.__text])

    def ngrams(self, n):
        return ngrams.NGrams(self.__repr__(), n)
