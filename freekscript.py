import matplotlib.pyplot as plt ## plotting package
import pandas as pd ## tabel package
import csv
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

"""Scraping stuff"""

URL = 'https://coinmarketcap.com/'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')
tabel = soup.find('tbody')
rijen = tabel.find_all('tr')


class Belegging:
    naam = 'onbekend'
    prijs = -1

beleggingen = []

for rij in rijen[0:10]:
    belegging = Belegging()
    titel = rij.find_all('p')
    belegging.naam = titel[1].text
    prijs = rij.find_all('a')
    belegging.prijs = prijs[1].text
    beleggingen.append(belegging)

print("aantal: " + str(len(rijen)))

for b in beleggingen:
    print(b.naam)
    print(b.prijs)


###############################################################################
"""Pokemon"""
# pok = pd.read_csv("Pokemon.csv")
#
#
# # trimnames = []
# # #
# # for col in pok.columns:
# #     nm = ""
# #     for l in col:
# #         if not l in ". ":
# #             nm += l
# #     trimnames.append(nm)
# #
# # trimnames[0] = "Number"
# # pok.columns = trimnames
#
# ## Lijst van numerieke variabelen
#
# # list of only the numerical values
# numval = ["HP", "Speed", "Attack", "Defense"]
#
# # create dataframe with the generation
# pok_gen = pd.DataFrame(pok.Generation.unique(), columns=["Generation"])
# # pok_gen.columns = ["Generation"]
#
# for col in numval:
#     means = []
#     for gen in pok_gen["Generation"]:
#         genmean = pok[pok.Generation == gen][col].mean()
#         means.append(genmean)
#     pok_gen[col] = means
#
# fig, ax = plt.subplots()
# # ax.set_xlim(0, 6)
# ax.set_ylim(0, 100)
#
# plot1 = ax.bar(pok_gen["Generation"], pok_gen["Attack"], )
#
# plt.show()
"""Cleaned headers"""

# df = pd.read_csv("102_cleaned_header.csv")
#
# # print(df.head)
# colnames = df.columns
#
#
# sex_salary = pd.DataFrame(df.groupby("sex").salary.mean())
#
# sex_salary.columns = ["mean $"]
# sex_salary["std $"] = df.groupby("sex").salary.std()
# sex_salary["median $"] = df.groupby("sex").salary.median()
#
# for col in sex_salary.columns:
#     sex_salary[col] = round(sex_salary[col], 2)
#
# print(sex_salary)
#
# male = df[df.sex == "M"]
# female = df[df.sex == "F"]
#
# p1 = plt.hist([male.salary, female.salary], bins=20)
#
# plt.show()