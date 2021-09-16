import matplotlib.pyplot as plt ## plotting package
import pandas as pd ## tabel package
import csv
import requests
from bs4 import BeautifulSoup

# Stap 1: get data from RIVM

URL = 'https://www.schiphol.nl/en/departures/?query=&date=2021-09-15&offset=0'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')
# tabel = soup.find('u1')

rijen = soup.find_all('li', {"class" : "card-flight"})


class Vlucht:
    nummer = ""
    maatschappij = ""
    tijd_gepland = ""
    bestemming = ""


def ophalen(rij):
    vlucht = Vlucht()
    # Vluchtnummer ophalen
    nr_comp = rij.find("span", {"class" : "card-flight__number"}).text
    nr_comp = nr_comp.split(" ")
    nr_comp = [i for i in nr_comp if len(i) != 0]

    vlucht.nummer = nr_comp[1] + nr_comp[2]
    vlucht.maatschappij = " ".join(nr_comp[3:])

    # geplande vertrektijd ophalen
    tijd = rij.find('time')
    vlucht.tijd_gepland = tijd.text
    # # bestemming ophalen
    bestemming = rij.find("b", {"class" : "card-flight__airport"}).text
    vlucht.bestemming = bestemming

    return vlucht


vluchten = []


for rij in rijen:
    vlucht = ophalen(rij)
    vluchten.append(vlucht)


tijd = []
maatschappij = []
nummer = []
bestemming = []

for v in vluchten:
    tijd.append(v.tijd_gepland)
    maatschappij.append(v.maatschappij)
    nummer.append(v.nummer)
    bestemming.append(v.bestemming)

d = {"tijd" : tijd,
     "maatschappij" : maatschappij,
     "nummer" : nummer,
     "bestemming" : bestemming}

df = pd.DataFrame(data = d)

print(df)


# Stap 2: convert data to file

# Stap 3: Summarize data

# Stap 4: Visualize data