from urllib.request import urlopen
from bs4 import BeautifulSoup, Tag
import webbrowser
from text import Text

class Challenge:
    __generic_url = "https://www.cipherchallenge.org/challenges/challenge-{}/"

    def __init__(self, n):
        self.__n = n
        self.__url = self.__generic_url.format(n)
        html = urlopen(self.__url)
        self.__soup = BeautifulSoup(html, "html.parser")

    def __iter__(self):
        self.__count = 0
        return self

    def __next__(self):
        self.__count += 1
        if self.__count == 1:
            return self.a
        elif self.__count == 2:
            return self.b
        else:
            raise StopIteration

    def open(self):
        webbrowser.open(self.__url)

    @property
    def url(self):
        return self.__url

    @property
    def A(self):
        content = self.__soup.find_all("div", attrs={"class": "challenge__content"})
        soup = BeautifulSoup(str(content[0]).split("<hr/>")[0], "html.parser")
        return Text(soup.text.strip().replace("\n", "\n\n"))

    @property
    def B(self):
        content = self.__soup.find_all("div", attrs={"class": "challenge__content"})
        soup = BeautifulSoup(str(content[1]).split("<hr/>")[0], "html.parser")
        return Text(soup.text.strip().replace("\n", "\n\n"))
