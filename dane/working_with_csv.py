
#
# with open("dane_03_06.csv", "r") as f:
#     for line in f:
#         line = line.strip().split(";")
#         rok, miesiac, wartosc = line[-3], line[-2], line[-1]
#
#         print(rok, miesiac, wartosc)
#

import csv

with open("dane_03_06.csv", "r") as f:
    csvreader = csv.DictReader(f, delimiter=";")
    dane = {} # {"rok": {"x": [], "y": []}}
    for line in csvreader:
        rok, miesiac, wartosc = line["rok"], line["miesiac"], line["wartosc"]

        if rok not in dane:
            dane[rok] = {"x": [], "y": []}

        dane[rok]['x'].append(int(miesiac))
        dane[rok]['y'].append(float(wartosc.replace(",", ".")))


import plotly.graph_objects as go

fig = go.Figure()
for rok in dane:
    fig.add_trace(go.Bar(x=dane[rok]['x'], y=dane[rok]['y'], name=rok))


fig.update_layout(title="Simple plot", xaxis_title="x", yaxis_title="y")
# plot_div = plot(fig, output_type='div')

fig.show()