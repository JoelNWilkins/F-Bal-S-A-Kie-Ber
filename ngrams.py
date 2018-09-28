def NGrams(text, n):
    if len(text) < n:
        raise ValueError("the length of the text must be larger than n")
    for i in range(len(text)-n+1):
        yield text[i:i+n]
