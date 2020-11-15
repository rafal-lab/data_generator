import json
from plotly.graph_objects import Scattergeo, Layout
from plotly import offline

#analiza struktury danych
filename= 'readable_eq_data.json'
with open(filename) as f:
    all_eq_data = json.load(f)

all_eq_dicts = all_eq_data['features']

#wyodrebnienie magnitudy trzesien
mags, dl_geos, sze_geos ,hover_texts= [], [], [], []

for eq_dict in all_eq_dicts:
    mags.append(eq_dict['properties']['mag'])
    dl_geos.append(eq_dict['geometry']['coordinates'][0])
    sze_geos.append(eq_dict['geometry']['coordinates'][1])
    hover_texts.append(eq_dict['properties']['title'])

#mapa trzesien ziemi
data = [{
    'type': 'scattergeo',
    'lon': dl_geos,
    'lat': sze_geos,
    'text':hover_texts,
    'marker': {
        'size': [5*mag for mag in mags],
        'color': mags,
        'colorscale': 'Viridis',
        'reversescale': True,
        'colorbar': {'title': "Sila"}
    },
}]

my_layout = Layout(title="Trzesienia ziemi na swiecie")

fig = {'data':data, 'layout': my_layout}
offline.plot(fig, filename='global_earth_quake.html')
