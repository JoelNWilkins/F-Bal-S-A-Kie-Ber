from urllib.request import urlopen
from bs4 import BeautifulSoup
from text import Text

class Challenge:
    generic_url = "https://www.cipherchallenge.org/challenges/challenge-{}/"
    
    def __init__(self, n):
        self.__n = n
        self.__url = self.generic_url.format(n)
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

    @property
    def url(self):
        return self.__url

    @property
    def a(self):
        content = soup.find_all("div", attrs={"class": "challenge__content"})
        return Text(content[0].text.strip())

    @property
    def b(self):
        content = soup.find_all("div", attrs={"class": "challenge__content"})
        return Text(content[1].text.strip())
