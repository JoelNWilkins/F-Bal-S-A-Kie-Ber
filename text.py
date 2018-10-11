import re
import score
import characters

class Text:
    def __init__(self, *args, **kwargs):
        if "chars" in kwargs.keys():
            self.__chars = kwargs.pop("chars")
        else:
            self.__chars = characters.uppercase

        if "score" in kwargs.keys():
            self.__score = kwargs.pop("score")
        else:
            self.__score = score.Chi_Squared(chars=self.__chars)

        if "path" in kwargs.keys():
            self.__path = kwargs.pop("path")
            with open(self.__path, "r") as f:
                self.__set__(f.read(), *args, **kwargs)
        else:
            self.__path = None
            self.__set__(*args, **kwargs)

    def __repr__(self):
        if len(self.__text) > 79:
            return "{}(\"{}...\")".format(self.__class__.__name__, self.__text[:76])
        return "{}(\"{}\")".format(self.__class__.__name__, self.__text)

    def __str__(self):
        return self.__temp.format(*list(self.__text))

    def __get__(self):
        return self.__text

    def __getitem__(self, key):
        if isinstance(key, int):
            return self.__text[key]
        elif isinstance(key, slice):
            return self.__text[key.start:key.stop]

    def __set__(self, *args, **kwargs):
        if len(args) == 1:
            text = args[0]
            self.__text = self.__chars(text)
            p = re.compile("[{}]".format(str(self.__chars)))
            self.__temp = "{}".join(p.split(text))
        else:
            print(args, kwargs)
            raise ValueError("{} only takes one argument".format(self.__class__.__name__))

    def __setitem__(self, key, value):
        if isinstance(key, int):
            self.__text[key] = value
        elif isinstance(key, str):
            text = list(self.__text)
            for i, char in enumerate(self.__text):
                if char == key:
                    text[i] = value
                elif char == value:
                    text[i] = key
            self.__text = "".join(text)

    def __len__(self):
        return len(self.__text)

    def swap(self, char1, char2):
        self.__setitem__(char1, char2)

    def score(self):
        return self.__score.score(self.__text)

    def copy(self):
        return Text(self.__text)

    def shift(self, n):
        self.__text = "".join([self.__chars[(self.__chars.index(char)+n)%len(self.__chars)] for char in self.__text])

    def reverse(self):
        self.__text = "".join(list(reversed(self.__text)))

    def reverse_words(self, sep=" "):
        self.__text = sep.join(["".join(list(reversed(word))) for word in self.__text.split(sep)])

    def save(self, path=None):
        if path != None:
            self.__path = path
        elif self.__path == None:
            raise ValueError("no path specified")

        with open(self.__path, "w") as f:
            f.write(self.__str__())
