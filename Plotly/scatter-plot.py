import pandas
import plotly.express as px
import plotly.graph_objects as go
import plotly.offline as plotly_offline
import numpy



data_x = numpy.random.randint(-1001, 1001, 500)
data_y = numpy.random.randint(-1001, 1000, 500)

figure = px.scatter(x=data_x, y=data_y)
# figure.show()
# plotly_offline.plot(figure, filename='scatter.plot.html')



dataframe = pandas.read_csv('../Pandas/details.csv')
figure = px.scatter(dataframe, x='Name', y='Age')
# figure.show()


figure = go.Figure([
	go.Scatter(
		name="My First Khud Ka Graph",
		x=data_x,
		y=data_y,
		mode="markers"
	)
])
figure.show()
