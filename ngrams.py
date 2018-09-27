def NGrams(text, n):
    for i in range(len(text)-n+1):
        yield text[i:i+n]
