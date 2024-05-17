
import re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from bs4 import BeautifulSoup
import requests
import time

links = []

def raspaLinks():
    url= "https://www.usadosbr.com/carros/br/honda"
    pagina = requests.get(url)
    time.sleep(1)
    soup = BeautifulSoup(pagina.text, 'html.parser')
    divs = soup.find_all('div', class_="css-fgokga")

    i = -1
    
    for div in divs:
        i+=1
        if i < 10:
            links.append(div.find("a")["href"])
        else:
            break

raspaLinks()

def raspaAtributos():
    carList = []
    for link in links:
        print("ta indo")
        url= "https://www.usadosbr.com" + link
        pagina = requests.get(url)
        time.sleep(1)
        soup = BeautifulSoup(pagina.text, 'html.parser')

        divs = soup.find_all('div', class_=['css-0'])
        infos = []

        for d in divs:       
            txt = d.find('p', class_='chakra-text')
            title = d.find('h6', class_='chakra-heading css-1dklj6k')
            if txt and title:
                if title.text in {'ANO', 'CARRO', 'CARROCERIA', 'COR', 'CIDADE'}:
                    txt = txt.text
                    infos.append(txt)
            else:
                continue
            
        carList.append(infos)

    
    return carList
    
lista = raspaAtributos()
for l in lista:
    print(l)

