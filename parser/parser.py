import requests
from bs4 import BeautifulSoup
import json
data:str
HEADERS = {'User-Agent': 'Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148'}

with open("site.html",'r',encoding="utf-8") as txt:
    data = txt.read()

def getTemp(url):
    r = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(r.text, 'lxml')
    weather = soup.findAll('td', class_="t0")
    allB = weather[1].findAll('b')
    return(str(allB[0].text + allB[1].text))

def getWind(url):
    r = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(r.text, 'lxml')
    wind = soup.findAll('div', class_="wtpo")
    return (wind[1].findAll('b')[2].text, wind[1].findAll('b')[6].text, wind[1].findAll('b')[1].text)

def getLinks():
    soup = BeautifulSoup(data, 'lxml')
    allCityes = soup.findAll('a', class_="mcm")
    totalCityes = []
    totalLinks = []
    for i in allCityes:
        totalCityes.append(i['title'].split()[-1]) #, i['href']
        totalLinks.append(i['href'])
    return(totalCityes, totalLinks)


# print(getWind("https://ru.meteotrend.com/forecast/ir/abadan/"))
totalCityes, totalLinks = getLinks()
totalWeather = {}
k = 0
for i in range(len(totalLinks)):
    print(totalCityes[i])
    Temp = getWind(totalLinks[i])
    WindDirecroty = ''
    for j in Temp[2].split('-'):
        if "сев" in j:
            WindDirecroty += 'N'
        elif "вост" in j:
            WindDirecroty += 'E'
        elif "зап" in j:
            WindDirecroty += 'W'
        elif "ю" in j:
            WindDirecroty += 'S'

    totalWeather.update({totalCityes[i]: {"Temp":getTemp(totalLinks[i])[0:-3],
                                            "WindSpeed":Temp[0],
                                            "WindDirectory":WindDirecroty,
                                            "Humidity":Temp[1]}})
    k += 1
    if k == 1000:
        print(totalWeather)
        break


