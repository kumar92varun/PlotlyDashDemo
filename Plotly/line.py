import numpy
import plotly.graph_objs as go		# Used to create the graph

x_values = numpy.linspace(0, 10, 8)
y_values = numpy.random.randint(0, 50, (4, 70))


plots = []
plots.append(go.Scatter(
	x=x_values,
	y=y_values[0,:],
	mode='markers',
	name="Line Plot 1",
	marker={
		'size':10,
		'color':'orange',
		'symbol':'hexagon'
	},
	line={
		'width':1,
		'color':'purple'
	}
))
plots.append(go.Scatter(
	x=x_values,
	y=y_values[1,:],
	mode='lines+markers',
	name="Line Plot 2",
	marker={
		'size':10,
		'color':'red',
		'symbol':'square'
	},
	line={
		'width':1,
		'color':'green'
	}
))
plots.append(go.Scatter(
	x=x_values,
	y=y_values[2,:],
	mode='lines',
	name="Line Plot 3",
	marker={
		'size':10,
		'color':'black',
		'symbol':'circle'
	},
	line={
		'width':2,
		'color':'yellow'
	}
))
plots.append(go.Scatter(
	x=x_values,
	y=y_values[3,:],
	mode='lines+markers',
	name="Line Plot 4",
	marker={
		'size':10,
		'color':'white',
		'symbol':'pentagon'
	},
	line={
		'width':1,
		'color':'brown'
	}
))


# Defining the layout settings of the graph
graph_layout = go.Layout(
	title="My first line plot",
	xaxis=dict(title='Random X Values'),
	yaxis=dict(title='Random Y Values'),
	hovermode='closest'
)

# Creating the plot
figure = go.Figure(plots, graph_layout)
# Showing the plot on browser
figure.show()
