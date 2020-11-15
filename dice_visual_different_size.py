from plotly.graph_objects import Bar, Layout
from plotly import offline
from Kosc_do_gry.die import Die

#utworzenie kosci typu D6 i D10
die_1 = Die()
die_2 = Die(10)

#wykonanie pewnej liczby rzutow i umieszczenie wynikow na liscie
results = []
for roll_num in range(50_000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

#analiza wynikow
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2,max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

#wizualizacja wynikow
x_values = list(range(2, max_result+1))
data = [Bar(x=x_values, y=frequencies)]
x_axis_config = {'title': 'Wynik', 'dtick': 1}
y_axis_config = {'title': 'Czestotliwosc wystepowania wartosci'}
my_layout = Layout(title='Wynik rzuacania dwiema koscia D6 i D10 50_000 razy', xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data':data, 'layout': my_layout}, filename='d6_d10.html')