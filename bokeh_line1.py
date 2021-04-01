from bokeh.layouts import gridplot
from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource, Legend
from bokeh.models import HoverTool

import numpy as np
import pandas as pd


infile = open("bachelors.csv", 'r')
tempList = []
for line in infile:
    tempList.append(line.rstrip())
print("tempList:", tempList)
num_entries = len(tempList)
newList = []
for i in range(0, num_entries):
    newList.append(tempList[i].split(","))

print("newList: ", newList)


index_01 = newList[0].index("Business")
index_02 = newList[0].index("Computer Science")
index_03 = newList[0].index("Engineering")



legends = [newList[0][index_01], newList[0][index_02], newList[0][index_03]]
data_00 = []
data_01 = []
data_02 = []
data_03 = []

for i in range (1, num_entries):
    data_00.append(newList[i][0])
for i in range (1, num_entries):
    data_01.append(newList[i][index_01])
for i in range (1, num_entries):
    data_02.append(newList[i][index_02])
for i in range (1, num_entries):
    data_03.append(newList[i][index_03])


data_01 = [float(x) for x in data_01]
data_02 = [float(x) for x in data_02]
data_03 = [float(x) for x in data_03]

source = ColumnDataSource(
    data={
        'Year': data_00,
        legends[0]: data_01,
        legends[1]: data_02,
        legends[2]: data_03,
})


f2 = figure()
f2.line(x='Year', y=legends[0], source=source, color="blue", legend_label=legends[0])
f2.line(x='Year', y=legends[1], source=source, color="red", legend_label=legends[1])
f2.line(x='Year', y=legends[2], source=source, color="gray", legend_label=legends[2])
# f2.line(x='x_values', y='y_values', source=source, color="gray", legend_label="y values")




# show(gridplot([[f2]]))

hover = HoverTool(tooltips =[
     ('group','@Year'),('x','@legends[0]{%F}')])
f2.add_tools(hover)
show(f2)
