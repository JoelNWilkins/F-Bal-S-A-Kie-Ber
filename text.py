class Text:
    def __init__(self, *args, **kwargs):
        self.__set__(self, *args, **kwargs)

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
            self.__text = list(args[0])

    def __setitem__(self, char1, char2):
        for i, char in enumerate(self.__text):
            if char == char1:
                self.__text[i] = char2
            elif char == char2:
                self.__text[i] = char1

    def swap(self, char1, char2):
        self.__setitem__(char1, char2)
