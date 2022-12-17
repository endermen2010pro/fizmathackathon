import requests
from bs4 import BeautifulSoup
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

app = FastAPI()

class parser:
    data:str
    HEADERS = {'User-Agent': 'Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148'}
    totalCityes:list = []
    totalLinks:list = []

    def get_data_from_name(self, name:str):
        for i in range(len(self.totalLinks)):
            if self.totalCityes[i] == name:
                wind_temp = self.getWind(self.totalLinks[i])
                temp = self.getTemp(self.totalLinks[i])[0:-3]

                WindDirecroty = ''
                for j in wind_temp[2].split('-'):
                    if "сев" in j:
                        WindDirecroty += 'N'
                    elif "вост" in j:
                        WindDirecroty += 'E'
                    elif "зап" in j:
                        WindDirecroty += 'W'
                    elif "ю" in j:
                        WindDirecroty += 'S'

                return {self.totalCityes[i]: {"Temp":temp,
                                    "WindSpeed":wind_temp[0],
                                    "WindDirectory":WindDirecroty,
                                    "Humidity":wind_temp[1]}}


    def getTemp(self, url):
        r = requests.get(url, headers=self.HEADERS)
        soup = BeautifulSoup(r.text, 'lxml')
        weather = soup.findAll('td', class_="t0")
        allB = list(map(str,weather[1].findAll('b')))
        allC = [i[3:-4] for i in allB]
        # average = sum(allB)/len(allB)
        return(str(allC[0]+"|"+ allC[1]))

    def getWind(self, url):
        r = requests.get(url, headers=self.HEADERS)
        soup = BeautifulSoup(r.text, 'lxml')
        wind = soup.findAll('div', class_="wtpo")
        vlajnost_temp_1 = wind[1].text
        vlajnost_temp_2 = vlajnost_temp_1[vlajnost_temp_1.find("Относительная влажность воздуха: ")+len('Относительная влажность воздуха: '):]
        humidity = vlajnost_temp_2[:vlajnost_temp_2.find('%')]
    

        return (wind[1].findAll('b')[2].text, humidity, wind[1].findAll('b')[1].text)


    def __init__(self) -> None:
        with open("site.html",'r',encoding="utf-8") as txt:
            self.data = txt.read()
        self.getLinks()


    def getLinks(self) -> None:
        soup = BeautifulSoup(self.data, 'lxml')
        allCityes = soup.findAll('a', class_="mcm")
        for i in allCityes:
            self.totalCityes.append(i['title'].split()[-1]) #, i['href']
            self.totalLinks.append(i['href'])
pr = parser()

print(pr.get_data_from_name("Ааргау"))

@app.get("/")
def root(name):
    # return "yes"
    return str(pr.get_data_from_name(name))