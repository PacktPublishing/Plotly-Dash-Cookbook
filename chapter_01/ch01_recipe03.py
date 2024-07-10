"""Plotly and Dash Cookbook

Chapter 1, recipe 3, Create your first chart with Plotly
"""

# Import the Express module from Plotly as px
import plotly.express as px

# Create your first figure with Plotly!

fig = px.line(x=[1, 2, 3, 4, 5], y=[1, 2, 3, 4, 5], title="Hello Plotly!")

# Show the plot. This will open a new window in your browser.
fig.show()
