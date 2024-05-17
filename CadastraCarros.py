
import re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from bs4 import BeautifulSoup
import requests
import time

prices = []

def raspaLinks():
    print("Raspando links...")
    url= "https://www.usadosbr.com/carros/br/honda"
    pagina = requests.get(url)
    time.sleep(1)
    soup = BeautifulSoup(pagina.text, 'html.parser')
    divs = soup.find_all('div', class_="css-fgokga")

    pr = soup.find_all('div', class_=['css-1e6famu'])
    for p in pr:
        prices.append(p.text)

    i = -1
    links = []
    for div in divs:
        i+=1
        if i < 10:
            links.append(div.find("a")["href"])
        else:
            break

    return links

def raspaAtributos():
    
    carList = []
    links = raspaLinks()

    print("Raspando atributos...")

    print("Raspando links...")
    url= "https://www.usadosbr.com/carros/br/honda"
    pagina = requests.get(url)
    time.sleep(1)
    soup = BeautifulSoup(pagina.text, 'html.parser')

    for link in links:

        url= "https://www.usadosbr.com" + link
        pagina = requests.get(url)
        time.sleep(1)
        soup = BeautifulSoup(pagina.text, 'html.parser')
        
        

        divs = soup.find_all('div', class_=['css-0'])
        atributes = []

        brandModel = soup.find('h1', class_=['css-1qoglf9']).text
        atributes.append(brandModel)

        
        #atributes.append(value)
        for d in divs:       
            txt = d.find('p', class_='chakra-text')
            title = d.find('h6', class_='chakra-heading css-1dklj6k')
            if txt and title:
                if title.text in {'ANO', 'CÂMBIO', 'CARROCERIA', 'COR', 'CIDADE'}:
                    txt = txt.text
                    atributes.append(txt)
            else:
                continue

        del atributes[1]
        carList.append(atributes)
        print("Item raspado.")
        
    return carList

#def formataAtributos
matriz = raspaAtributos()
for i in range(10):
    matriz[i][5] = prices[i]
for l in matriz:
    print(l)

