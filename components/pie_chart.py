"""
Pie chart component.
"""
import datetime

import pandas as pd
import plotly.express as px
import plotly.graph_objs

from dash import Dash, dcc, html
from dash.dependencies import Input, Output
from pandas import DataFrame

from components import ids


def render(app: Dash, data: DataFrame) -> html.Div:
    @app.callback(
        Output(ids.PIE_CHART, 'figure'),
        Input(ids.YEAR_DROPDOWN, 'value')
    )
    def change_year(year: int) -> plotly.graph_objs.Figure:
        pie_data = data.loc[data.Year == year]
        return px.pie(data_frame=pie_data, values='Qty', names='Nationality')

    return html.Div(dcc.Graph(id=ids.PIE_CHART))
