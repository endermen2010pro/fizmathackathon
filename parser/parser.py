import requests
from bs4 import BeautifulSoup
import json
data:str
with open("site.html",'r',encoding="utf-8") as txt:
    data = txt.read()
# url = "https://ru.meteotrend.com/forecast/"

# def parseText(url):
#     r = requests.get(url)
#     allProducts = {}
#     soup = BeautifulSoup(r.text, 'lxml')
#     # for i in soup.findAll('span', class_="content-title"):
#     #     allTitles.append(i.text)
#     # for i in (soup.findAll('span', class_="price")):
#     #     allPrices.append(i.text)
#     # for i in range(len(newUrls)):
#     #     allProducts.update({i + 1 + iterac * 12: {"title":allTitles[i], "price":allPrices[i], "img":newUrls[i]}})
#     return allProducts


# r = requests.get(url)
soup = BeautifulSoup(data.text, 'lxml')
print(soup)
