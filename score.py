import os
import pickle
from text import Text

class Chi_Squared:
    def __init__(self, path=None):
        if path == None:
            path = os.path.expanduser("~\\Documents\\Cipher Challenge\\english_monograms.pkl")
        with open(path, "rb") as f:
            self.dist = pickle.load(f)
