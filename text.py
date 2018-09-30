class Text:
    def __init__(self, text):
        self.text = list(text)

    def __repr__(self):
        if len(self.text) > 70:
            return "Text(\"{}...\")".format("".join(self.text[:70]))
        return "Text(\"{}\")".format(self.__str__())

    def __str__(self):
        return "".join(self.text)

    def __get__(self):
        return self.__str__()

    def __setitem__(self, char1, char2):
        for i, char in enumerate(self.text):
            if char == char1:
                self.text[i] = char2
            elif char == char2:
                self.text[i] = char1

    def swap(self, char1, char2):
        self.__setitem__(char1, char2)
    
