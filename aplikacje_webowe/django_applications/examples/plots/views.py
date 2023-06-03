import csv

from django.shortcuts import render
import plotly.graph_objects as go
from plotly.offline import plot
# Create your views here.

def simple_plot(request):

    x_data = [1, 2, 3, 4, 5]
    y_data = [1, 4, 9, 16, 25]
    y2_data = [2, 6, 13, 1, 45]
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x_data, y=y_data, name="y1"))
    fig.add_trace(go.Scatter(x=x_data, y=y2_data, name="y2"))
    fig.update_layout(title="Simple plot", xaxis_title="x", yaxis_title="y")
    plot_div = plot(fig, output_type='div')

    context = {"plot_div": plot_div}
    return render(
        request,
        "plots/plot.html",
        context
    )


def prepare_data(csv_file):
    decoded_file = csv_file.read().decode("utf-8").splitlines()
    csvreader = csv.DictReader(decoded_file, delimiter=";")
    dane = {}  # {"rok": {"x": [], "y": []}}
    for line in csvreader:
        rok, miesiac, wartosc = line["rok"], line["miesiac"], line["wartosc"]

        if rok not in dane:
            dane[rok] = {"x": [], "y": []}

        dane[rok]['x'].append(int(miesiac))
        dane[rok]['y'].append(float(wartosc.replace(",", ".")))
    return dane


def prepare_plot(data):
    fig = go.Figure()
    for rok in data:
        fig.add_trace(go.Bar(x=data[rok]['x'], y=data[rok]['y'], name=rok))

    fig.update_layout(title="Simple plot", xaxis_title="x", yaxis_title="y")
    plot_div = plot(fig, output_type='div')
    return plot_div


def simple_import(request):

    if request.method == "POST":
        csv_file = request.FILES["file"]
        dane = prepare_data(csv_file)
        plot_div = prepare_plot(dane)
        context = {"plot_div": plot_div}

    else:
        print(request.GET)
        print("GET")
        context = {}


    return render(
        request,
        "plots/import.html",
        context
    )