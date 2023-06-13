import csv
import pandas as pd
import plotly.figure_factory as ff

df = pd.read_csv("Height and weight.csv")
fig = ff.create_distplot([df["Weight(Pounds)"].tolist()],["Normal distibution of weight is:"],show_hist = False)
fig.show()