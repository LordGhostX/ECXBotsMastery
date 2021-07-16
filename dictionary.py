import requests
from bs4 import BeautifulSoup


def find_word_meaning(word):
    r = requests.get(f"https://www.dictionary.com/browse/{word}")
    if r.status_code == 200:
        page = BeautifulSoup(r.text, "html.parser")
        luna_pos = page.find("span", {"class": "luna-pos"}).text
        word_meaning = f"{word} - {luna_pos}\n\n"
        meanings = page.find(
            "div", {"class": "css-1uqerbd e1hk9ate0"}).find_all("div", {"class": "e1q3nk1v2"})
        for i, meaning in enumerate(meanings):
            word_meaning += f"{i + 1} - {meaning.find('span').text}\n\n"

        return word_meaning.strip()
    elif r.status_code == 404:
        return "the specified word does not exist!"
    else:
        return "an error occured while finding word meaning!"


if __name__ == "__main__":
    print(find_word_meaning("intense"))
