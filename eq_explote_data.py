import json

#analiza struktury danych
filename= 'earth_quake.json'
with open(filename) as f:
    all_eq_data = json.load(f)

all_eq_dicts = all_eq_data['features']

#wyodrebnienie magnitudy trzesien
mags, dl_geos, szer_geos = [], [], []
for eq_dict in all_eq_data:
    print(eq_dict)



