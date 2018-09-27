class NGrams:
    def __init__(self, text, n):
        self.text = text
        self.n = n
        if len(self.text) < self.n:
            raise ValueError("the length of the text must be larger than n")

    def __iter__(self):
        self.count = -1
        self.limit = len(self.text) - self.n + 1
        return self

    def __next__(self):
        self.count += 1
        if self.count < self.limit:
            return self.text[self.count:self.count+self.n]
        else:
            raise StopIteration()
