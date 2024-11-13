import numpy as np
from bokeh.io import output_file
from bokeh.io import show
from bokeh.layouts import row, column
from bokeh.plotting import figure
fig = figure(plot_width=500, plot_height=300, title='Different Types of plots')
x = np.linspace(0, 10, 100)
y = np.sin(x)
fig.line(x, y, line_width=2, legend_label='Line plot')
fig.vbar(x=x, top=y, legend_label='Bar Chart ', width=0.5, bottom=0)
fig.circle(x, y, size=10, color='red', legend_label='Scatter plot')
fig.xaxis.axis_label = 'X Axis'
fig.yaxis.axis_label = 'Y Axis'
fig.legend.location = 'top_left'
show(fig)