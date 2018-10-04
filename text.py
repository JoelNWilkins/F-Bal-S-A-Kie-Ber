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
            with open(kwargs.pop("path"), "r") as f:
                self.__set__(f.read(), *args, **kwargs)
        else:
            self.__set__(*args, **kwargs)

    def __repr__(self):
        if len(self.__text) > 70:
            return "Text(\"{}...\")".format("".join(self.__text[:70]))
        return "Text(\"{}\")".format(self.__str__())

    def __str__(self):
        return "".join(self.__text)

    def __get__(self):
        return self.__str__()

    def __getitem__(self, key):
        if isinstance(key, int):
            return self.__text[key]
        elif isinstance(key, slice):
            return "".join(self.__text[key.start:key.stop])

    def __set__(self, *args, **kwargs):
        if len(args) == 1:
            text = args[0]
            if self.__case == "UPPER":
                text = text.upper()
            elif self.__case == "LOWER":
                text = text.lower()
            self.__text = [char for char in text]
        else:
            print(args, kwargs)
            raise ValueError("{} only takes one argument".format(self.__class__.__name__))

    def __setitem__(self, char1, char2):
        for i, char in enumerate(self.__text):
            if char == char1:
                self.__text[i] = char2
            elif char == char2:
                self.__text[i] = char1

    def __len__(self):
        return len(self.__text)

    def swap(self, char1, char2):
        self.__setitem__(char1, char2)

    def score(self):
        return self.__score.score(self.__str__())

    def copy(self):
        return Text(self.__str__())

    def reverse(self):
        self.__text = list(reversed(self.__text))

    def reverse_words(self, sep=" "):
        self.__text = list(sep.join(["".join(list(reversed(word))) for word in self.__str__().split(sep)]))
