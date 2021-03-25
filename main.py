from bs4 import BeautifulSoup

with open("index.html", encoding="utf8") as file:
    src = file.read()

soup = BeautifulSoup(src, "lxml")

title = soup.title
print(title.text)