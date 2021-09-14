import pandas as pd
import matplotlib as mpl

pok = pd.read_csv("Pokemon.csv")

trimnames = []

# 
for col in pok.columns:
    nm = ""
    for l in col:
        if not l in ". ":
            nm += l
    trimnames.append(nm)

trimnames[0] = "Number"
pok.columns = trimnames

numval = ["HP", "Speed", "Attack", "Defense"]

pok_gen = pd.DataFrame(pok.Generation.unique())
