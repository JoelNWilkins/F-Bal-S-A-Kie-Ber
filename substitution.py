import sys
import random
from text import *
from score import *

def substitution(text):
    ciphertext = text
    chars = list(ciphertext.chars)
    scorer = ngrams_Score()
    best_score = float("-inf")
    best_text = ciphertext.copy()
    count = 0
    while True:
        char1 = random.choice(chars)
        char2 = random.choice(chars)
        ciphertext[char1] = char2
        for i, char in enumerate(chars):
            if char == char1:
                chars[i] = char2
            elif char == char2:
                chars[i] = char1
        score = scorer.score(ciphertext)
        if score > best_score:
            best_score = score
            best_text = ciphertext.copy()
            best_alpha = chars[:]
            count = 0
        else:
            ciphertext[char1] = char2
            for i, char in enumerate(chars):
                if char == char1:
                    chars[i] = char2
                elif char == char2:
                    chars[i] = char1
            count += 1
            if count == 2000:
                break
    return best_text

if __name__ == "__main__":
    input_path = sys.argv[1]
    if len(sys.argv) > 2:
        output_path = sys.argv[2]
    else:
        output_path = None

    ciphertext = Text(path=input_path)

    plaintext = substitution(ciphertext)

    if output_path != None:
        plaintext.save(output_path)
    else:
        print(str(plaintext))
