import csv
from datetime import datetime

from django.utils import timezone

from django.shortcuts import render
import plotly.graph_objects as go
from plotly.offline import plot

from plots.models import Data


# Create your views here.

def simple_plot(request):

    request.session["my_session"] = "my_value"

    print(request.COOKIES)
    cookie_alx = request.COOKIES.get("alx")
    print(cookie_alx, type(cookie_alx))
    x_data = [1, 2, 3, 4, 5]
    y_data = [1, 4, 9, 16, 25]
    y2_data = [2, 6, 13, 1, 45]
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x_data, y=y_data, name="y1"))
    fig.add_trace(go.Scatter(x=x_data, y=y2_data, name="y2"))
    fig.update_layout(title="Simple plot", xaxis_title="x", yaxis_title="y")
    plot_div = plot(fig, output_type='div')

    context = {"plot_div": plot_div}
    response = render(
        request,
        "plots/plot.html",
        context
    )
    response.set_cookie("alx", str("Zażółć gęślą jaźń".encode("utf-8")))
    return response
def simple_cookie_view(request):
    print(request.COOKIES)
    response = render(request, "plots/cookie.html", {})
    response.set_cookie("my_cookie", "my_value")
    return response

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


def import_data_to_model(csv_file):
    decoded_file = csv_file.read().decode("utf-8").splitlines()
    csvreader = csv.DictReader(decoded_file, delimiter=";")
    data_importu = timezone.now()
    objects = []
    for row in csvreader:
        r =int(row["rok"])
        m = int(row["miesiac"])
        w = float(row["wartosc"].replace(",", "."))
        objects.append(Data(rok=r, miesiac=m, wartosc=w, data_importu=data_importu))
    Data.objects.bulk_create(objects)



def prepare_plot(data):
    fig = go.Figure()
    for rok in data:
        fig.add_trace(go.Bar(x=data[rok]['x'], y=data[rok]['y'], name=rok))

    fig.update_layout(title="Simple plot", xaxis_title="x", yaxis_title="y")
    plot_div = plot(fig, output_type='div')
    return plot_div

def prepare_agregated_plot(series):
    aggregated_data = {"x": [], "y": []}
    for rok, values in series.items():
        aggregated_data["x"].append(rok)
        aggregated_data["y"].append(sum(values["y"]))
    fig = go.Figure()
    fig.add_trace(go.Bar(x=aggregated_data["x"], y=aggregated_data["y"], name="agregated"))
    fig.update_layout(title="Zagregowane dane", xaxis_title="Lata", yaxis_title="suma")
    plot_div = plot(fig, output_type='div')
    return plot_div

def simple_import(request):
    data = request.session.get("my_session")
    print(data)
    context = {}
    if request.method == "POST":
        csv_file = request.FILES["file"]
        import_data_to_model(csv_file)

    imports = Data.objects.values_list("data_importu", flat=True).distinct()
    context["imports"] = imports
    return render(
        request,
        "plots/import.html",
        context
    )

def get_data_from_db(import_date):
    data = Data.objects.filter(data_importu=import_date)
    series = {}
    for item in data:
        rok = item.rok
        miesiac = item.miesiac
        wartosc = item.wartosc

        if rok not in series:
            series[rok] = {"x": [], "y": []}

        series[rok]["x"].append(miesiac)
        series[rok]["y"].append(wartosc)
    return series


def simple_import_details(request, import_date):
    series = get_data_from_db(import_date)
    plot_div = prepare_plot(series)
    agregated_plot_div = prepare_agregated_plot(series)
    context = {"plot_div": plot_div, "agregated_plot_div": agregated_plot_div}
    return render(
        request,
        "plots/import.html",
        context
    )