import requests
from bs4 import BeautifulSoup


def fetchAndSaveToFile(url, path):
    r = requests.get(url)
    with open(path, "w") as f:
        f.write(r.text)


url = "https://timesofindia.indiatimes.com/topic/world-university-rankings"

fetchAndSaveToFile(url, "data/times.html")

with open("data/times.html", "r") as f:
    html_doc = f.read()

soup = BeautifulSoup(html_doc, 'html.parser')


print(soup.prettify())
print(soup.title.string)