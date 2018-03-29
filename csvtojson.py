import pandas as pd
import json

profil = pd.read_csv('ProfilCalon.csv')
dana = pd.read_csv('danapaslon.csv')
p = profil.to_json( orient="records")
d = dana.to_json(orient = "records")

gab = {}
gab["profil"] = p
gab["dana"] = d


with open('data.json', 'w') as ofile:
    ofile.write(json.dumps(d, ofile))


visi[list(visi)[0]].dropna().to_json(orient='split')
