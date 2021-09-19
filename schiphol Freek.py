import matplotlib.pyplot as plt ## plotting package
import pandas as pd ## tabel package
import csv
import requests
from bs4 import BeautifulSoup

# Basis URL zonder offset
URL = 'https://www.schiphol.nl/en/departures/?query=&date=2021-09-19&offset='

# Define vlucht class met 4 object variables
class Vlucht:
    nummer = ""
    maatschappij = ""
    tijd_gepland = ""
    bestemming = ""


def ophalen(rij):
    vlucht = Vlucht()
    # Vluchtnummer ophalen. De tekst bestaat uit vluchtnummer + maatschappij in format "KL 1234 KLM"
    nr_comp = rij.find("span", {"class" : "card-flight__number"}).text
    nr_comp = nr_comp.split(" ")
    nr_comp = [i for i in nr_comp if len(i) != 0]

    vlucht.nummer = nr_comp[1] + nr_comp[2]
    maatschappij = " ".join(nr_comp[3:])
    vlucht.maatschappij = maatschappij[0:maatschappij.find("/")]

    # geplande vertrektijd ophalen
    tijden = rij.find_all('time')
    tijd_text = tijden[0].text
    tijd_gepland = ""
    for char in tijd_text:  ## lelijke manier om de data op te schonen
        if char.isdigit() or char == ":":
            tijd_gepland += char
    vlucht.tijd_gepland = tijd_gepland

    # # bestemming ophalen
    bestemming = rij.find("b", {"class" : "card-flight__airport"}).text
    vlucht.bestemming = bestemming

    return vlucht


vluchten = [] # Lijst voor alle vlucht objecten

# Dictionary om de data van alle vluchten op te slaan. Wordt later omgezet in dataframe
d = {"tijd" : [],
     "maatschappij" : [],
     "nummer" : [],
     "bestemming" : []}

offset = 0


""" Haalt iteratief alle pagina's op, tot het einde is bereikt. Als alle pagina's zijn afgegaan
wordt er een error gethrowsd en is de loop ten einde. """

while True and offset < 201: ## offset limiet om te testen
    try:
        page = requests.get(URL + str(offset)) # modify URL to include offset
        soup = BeautifulSoup(page.content, 'html.parser')
        rijen = soup.find_all('li', {"class" : "card-flight"})

        for rij in rijen:
            vlucht = ophalen(rij)
            vluchten.append(vlucht)
            d['tijd'].append(vlucht.tijd_gepland)
            d['maatschappij'].append(vlucht.maatschappij)
            d['nummer'].append(vlucht.nummer)
            d['bestemming'].append(vlucht.bestemming)

        offset += 50

    except:
        print("Einde bereikt")
        break

#### dit allemaal aan het einde: ###

print("Aantal vluchten: " + str(len(vluchten)))

df = pd.DataFrame(data = d)

maatschappijen = df.maatschappij.unique()

mdict = {}

for m in maatschappijen:
    mdict[m] = 0

for v in vluchten:
    mdict[v.maatschappij] += 1


# for key in mdict:
#     print(key + ": " + str(mdict[key]))
