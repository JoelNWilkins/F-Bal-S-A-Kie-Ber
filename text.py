import score

class Text:
    def __init__(self, *args, **kwargs):
        if "case" in kwargs.keys():
            self.__case = kwargs.pop("case").upper()
        else:
            self.__case = "NONE"

        if "score" in kwargs.keys():
            self.__score = kwargs.pop("score")
        else:
            self.__score = score.Chi_Squared(case=self.__case)

        if "path" in kwargs.keys():
            self.__path == kwargs.pop("path")
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
        return self.__text

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
            if self.__case == "UPPER":
                text = text.upper()
            elif self.__case == "LOWER":
                text = text.lower()
            self.__text = "".join([char for char in text])
        else:
            print(args, kwargs)
            raise ValueError("{} only takes one argument".format(self.__class__.__name__))

    def __setitem__(self, key, value):
        if isinstance(key, int):
            self.__text[key] = value
        elif isinstance(key, str):
            for i, char in enumerate(self.__text):
                if char == key:
                    self.__text[i] = value
                elif char == value:
                    self.__text[i] = key

    def __len__(self):
        return len(self.__text)

    def swap(self, char1, char2):
        self.__setitem__(char1, char2)

    def score(self):
        return self.__score.score(self.__text)

    def copy(self):
        return Text(self.__text)

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
