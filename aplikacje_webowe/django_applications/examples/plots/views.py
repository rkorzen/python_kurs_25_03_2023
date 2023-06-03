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

def simple_import(request):

    if request.method == "POST":
        print("POST")
        print(request.POST)
        print(request.FILES)

        csv_file = request.FILES["file"]
        print(len(csv_file.read().decode("utf-8").splitlines()))

    else:
        print("GET")



    return render(
        request,
        "plots/import.html",
        {}
    )