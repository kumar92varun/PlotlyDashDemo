import pandas
import plotly.graph_objs as go		# Used to create the graph

dataFrame = pandas.read_csv('../SentimentAnalysis.csv')


plots = []
scorePositive = go.Bar(
	x=dataFrame['Text'],
	y=dataFrame['Positive Score'],
	name='Positive Score',
	marker=dict(
		color='green'
	)
)
plots.append(scorePositive)
scoreNegative = go.Bar(
	x=dataFrame['Text'],
	y=dataFrame['Negative Score'],
	name='Negative Score',
	marker=dict(
		color='red'
	)
)
plots.append(scoreNegative)
scoreMixed = go.Bar(
	x=dataFrame['Text'],
	y=dataFrame['Mixed Score'],
	name='Mixed Score',
	marker=dict(
		color='yellow'
	)
)
plots.append(scoreMixed)
scoreNeutral = go.Bar(
	x=dataFrame['Text'],
	y=dataFrame['Neutral Score'],
	name='Neutral Score',
	marker=dict(
		color='cyan'
	)
)
plots.append(scoreNeutral)


graph_layout = go.Layout(
	title="Barmode = group bar plot",
	xaxis=dict(title='Text'),
	yaxis=dict(title='Sentiment Scores'),
	hovermode='closest',
	barmode="group"
)
figure = go.Figure(plots, graph_layout)
figure.show()


graph_layout = go.Layout(
	title="Barmode = relative bar plot",
	xaxis=dict(title='Text'),
	yaxis=dict(title='Sentiment Scores'),
	hovermode='closest',
	barmode="relative"
)
figure = go.Figure(plots, graph_layout)
figure.show()


graph_layout = go.Layout(
	title="Barmode = stack bar plot",
	xaxis=dict(title='Text'),
	yaxis=dict(title='Sentiment Scores'),
	hovermode='closest',
	barmode="stack"
)
figure = go.Figure(plots, graph_layout)
figure.show()
