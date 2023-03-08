import requests
from bs4 import BeautifulSoup


def clean(word=""):
    if word == "":
        return None
    else:
        return word[1:]


def extract_names(url="https://www.google.com/"):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'lxml')
    names = str(soup.text)
    names = names[49:]
    char = '01'
    idx = 0
    if char in names:
        idx = names.index(char)
    names = names[:idx]
    print(names)


if __name__ == '__main__':
    extract_names('https://playvalorant.com/en-us/agents/')
