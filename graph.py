import pickle
from matplotlib import pyplot as plt
from collections import Counter
from text import *
from score import *

def plot_letter_freq(text, expected=None, width=1, show_expected=True,
    show_average=False, reorder=False, fig=plt,
    path=os.path.expanduser("~/Documents/Cipher Challenge/Data/english_monograms.pkl")):
    if expected == None:
        with open(path, "rb") as f:
            expected = pickle.load(f)
    freq = Counter(text)
    length = len(text)
    if reorder:
        inverse = {}
        for char in text.chars:
            inverse[freq[char]] = char
        heights = list(reversed(sorted([freq[char] for char in text.chars])))
        labels = []
        labs = {}
        for i in range(len(text.chars)):
            char = inverse[heights[i]]
            if not char in labels:
                labels.append(char)
                labs[char] = 1
            else:
                letters = [char for char in text.chars
                    if freq[char] == freq[inverse[heights[i]]]]
                print(letters)
                labels.append(sorted(letters)[labs[char]])
                labs[char] += 1
        inverse = {}
        for char in text.chars:
            inverse[expected[char]] = char
        expected_heights = list(reversed(sorted([expected[char] for char in text.chars])))
        expected_labels = [inverse[expected_heights[i]] for i in range(len(text.chars))]
    for i, char in enumerate(text.chars):
        if show_expected:
            if reorder:
                fig.bar(i-(width/4), heights[i], color="#FFFFFF",
                    edgecolor="#000000", hatch="////", width=width/2)
                fig.bar(i+(width/4), length*expected_heights[i],
                    color="#FFFFFF", edgecolor="#000000", hatch="\\\\\\\\",
                    width=width/2)
            else:
                fig.bar(i-(width/4), freq[char], color="#FFFFFF",
                    edgecolor="#000000", hatch="////", width=width/2)
                fig.bar(i+(width/4), length*expected[char], color="#FFFFFF",
                    edgecolor="#000000", hatch="\\\\\\\\", width=width/2)
        else:
            if reorder:
                fig.bar(i, heights[i], color="#FFFFFF", edgecolor="#000000",
                    hatch="////", width=width)
            else:
                fig.bar(i, freq[char], color="#FFFFFF", edgecolor="#000000",
                    hatch="////", width=width)
    if reorder:
        if show_expected:
            x = []
            for i in range(len(text.chars)):
                x.extend([i-(width/4), i+(width/4)])
            labels.extend(expected_labels)
            fig.xticks(x, labels)
            for tick in plt.gca().xaxis.get_major_ticks():
                tick.label.set_fontsize(6)
        else:
            fig.xticks(list(range(len(text.chars))), labels)
    else:
        fig.xticks(list(range(len(text.chars))), list(text.chars))
    if show_average:
        fig.plot([-1, len(text.chars)],
            [len(text)/len(text.chars), len(text)/len(text.chars)], "k--")
        fig.xlim([-1, len(text.chars)])
    return fig

def plot_sections_ic(text, start=1, stop=20, width=1, fig=plt):
    scorer = Index_Of_Coincidence(chars=text.chars)
    for n in range(start, stop+1):
        fig.bar(n, sum([len(text.section(n, i))*scorer.score(text.section(n, i))
            for i in range(n)]) / len(text), color="#FFFFFF", edgecolor="#000000",
            hatch="////", width=width)
    fig.xticks(list(range(start, stop+1)), list(range(start, stop+1)))
    return fig

ciphertext = Text(path="Challenges/2018/challenge-2b-question.txt")
plot_letter_freq(ciphertext, width=0.6, show_expected=False, show_average=True, reorder=True).show()
plot_sections_ic(ciphertext, width=0.6).show()
