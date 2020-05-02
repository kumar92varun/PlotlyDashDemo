import numpy as np
import plotly.graph_objs as go		# Used to create the graph
import plotly.offline as po			# Used to create an html file to store the graph offline

random_x = np.random.randint(1, 101, 100)
random_x2 = np.random.randint(-101, 0, 200)
random_y = np.random.randint(1, 101, 100)
random_y2 = np.random.randint(-101, 0, 200)


plots = []
# Creating a scatter type of plot
scatter_plot1 = go.Scatter(
	x=random_x,
	y=random_y,
	mode='markers',
	marker={
		'size':20,
		'color':'#FFFFFF',
		'symbol':'hexagon',
		'line':{
			'width':4,
			'color':'red'
		}
	}
)
plots.append(scatter_plot1)

scatter_plot2 = go.Scatter(
	x=random_x2,
	y=random_y2,
	mode='markers',
	marker={
		'size':16,
		'color':'purple',
		'symbol':'pentagon',
		'line':{
			'width':5,
			'color':'yellow'
		}
	}
)
plots.append(scatter_plot2)

# Defining the layout settings of the graph
graph_layout = go.Layout(
	title="My first scatter plot",
	xaxis=dict(title='Random X Values'),
	yaxis=dict(title='Random Y Values'),
	hovermode='closest'
)

# Creating the plot
figure = go.Figure(plots, graph_layout)
# Showing the plot on browser
figure.show()


# Saving the plot in a file
po.plot(figure, filename='scatter.html')
