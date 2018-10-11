import string

class Characters:
    def __init__(self, *args, **kwargs):
        self.__chars = list(args[0])

        if "case" in kwargs.keys():
            self.__case = kwargs.pop("case").lower()
        else:
            self.__case = None

    def __str__(self):
        return "".join(self.__chars)

    def __getitem__(self, key):
        return self.__chars[key]

    def index(self, element):
        return self.__chars.index(element)

    def __call__(self, text):
        if self.__case == "upper":
            return "".join([char.upper() for char in text if self.__contains__(char)])
        elif self.__case == "lower":
            return "".join([char.lower() for char in text if self.__contains__(char)])
        else:
            return "".join([char for char in text if char in self.__chars])

    def __iter__(self):
        self.__count = -1
        return self

    def __next__(self):
        self.__count += 1
        if self.__count < self.__len__():
            return self.__chars[self.__count]
        else:
            raise StopIteration

    def __len__(self):
        return len(self.__chars)

    def __contains__(self, element):
        if self.__case == "upper":
            return element.upper() in self.__chars
        elif self.__case == "lower":
            return element.lower() in self.__chars
        else:
            return element in self.__chars

uppercase = Characters(string.ascii_uppercase, case="upper")
lowercase = Characters(string.ascii_lowercase, case="lower")
