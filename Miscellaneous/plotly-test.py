from re import template
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objects as go
import pandas as pd
df = pd.read_csv('India-2019.csv')
y = df['Age']
x1 = df['M']
x2 = df['F'] * -1
fig = go.Figure()
fig.add_trace(go.Bar(
    y=y,
    x=x1,
    name='Male',
    orientation='h'
))

fig.add_trace(go.Bar(
    y=y,
    x=x2,
    name='Female',
    orientation='h'
))

fig.update_layout(
    template = 'plotly_white',
    title = 'Age Pyramid of India 2019',
    title_font_size = 24,
    barmode = 'relative',
    bargap = 0.0,
    bargroupgap = 0,
    xaxis=dict(
        tickvals=[-60000000, -40000000, -20000000, 0, 20000000, 40000000, 60000000],
        ticktext=['60M', '40M', '20M', '0', '20M', '40M', '60M'],
        title='Population',
        title_font_size=14

    )
)

fig.show()
