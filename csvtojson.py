import pandas as pd
import json

profil = pd.read_csv('ProfilCalon.csv')
dana = pd.read_csv('danapaslon.csv')
tahapan = pd.read_csv('tahapan.csv')
t = json.dumps(dict(persiapan=json.loads(tahapan.groupby('tahapan').get_group('Persiapan').to_json(orient='records')),
                    penyelenggaraan=json.loads(tahapan.groupby('tahapan').get_group('Penyelenggaraan').to_json(orient='records'))))

p = profil.to_json( orient="records")
d = dana.to_json(orient = "records")

gab = {}
gab["profilpaslon"] = json.loads(p)
gab['profilpaslon'][0]['visimisi'] = visimisi['ganjaryasin']
gab['profilpaslon'][1]['visimisi'] = visimisi['sudirmanida']
gab["danapaslon"] = json.loads(d)
gab["tahapanpilgub"] = json.loads(t)


# gab = json.dumps(gab)

with open('data01.json', 'w') as ofile:
    ofile.write(json.dumps(gab, ofile))


vm = {}
vm['visi'] = json.loads(visi['VISI'].dropna().to_json(orient='records'))[0]
vm['misi'] = json.loads(visi['MISI'].dropna().to_json(orient='records'))
vm['program'] = json.loads(visi['PROGRAM'].to_json(orient='records'))
vm['detail'] = json.loads(visi['DETAILS'].to_json(orient='records'))

visimisi = {}
visimisi['ganjaryasin'] = vm
visimisi['sudirmanida'] = vm

ra0 = json.loads(pd.read_csv('rekapanggaran.csv'))
ra1 = json.loads(pd.read_csv('ra2017.csv'))
ra2 = json.loads(pd.read_csv('ra2018.csv'))

#########################################

l = []
for r in json.loads(ra0):
    for n in json.loads(ra1):
        r['ra2017'] = n
    for k in json.loads(ra2):
        r['ra20018'] = k
    l.append(r)

d = json.load(open('data.json'))

d['rekap.anggaran.kampanye'] = l

with open('data00.json','w') as ofile:
    ofile.write(json.dumps(d, ofile))