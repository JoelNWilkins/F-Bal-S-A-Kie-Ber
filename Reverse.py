def ReverseWords(text, sep = " "):
    SplitText = text.split(sep)
    for n in range(len(SplitText)):
        word = SplitText[n]
        holder = ""
        for i in range(len(word) - 1, -1, -1):
            holder += word[i]
        SplitText[n] = holder

    ans = ""
    for word in SplitText:
        ans += word + " "

    return ans

def Reverse(text):
    ans = ""
    for i in range(len(text)-1, -1, -1):
        ans += text[i]

    return ans
