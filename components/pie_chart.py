"""
Pie chart component.
"""
import plotly.express as px

from dash import Dash, dcc, html
from pandas import DataFrame

from components import ids


def render(app: Dash, data: DataFrame) -> html.Div:
    fig = px.pie(data_frame=data, values='Qty', names='Nationality')
    return html.Div(
        dcc.Graph(figure=fig, id=ids.PIE_CHART)
    )
