import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import random
import pandas as pd
import csv

df = pd.read_csv("data.csv")
data = df["temp"].tolist()

population_mean = statistics.mean(data)
std_deviation=statistics.stdev(data)
print("population mean:- ", population_mean)
print("standard deviation:- ", std_deviation)

def show_fig(mean_list):
    df = mean_list
    fig = ff.create_distplot([data], ["temp"], show_hist=False)
    fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 1], mode="lines", name="MEAN"))

    fig.show()

#dataset = []
# i in range(0, 1000):
#rando




