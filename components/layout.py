"""
Main page layout.
"""
from dash import Dash, html
from pandas import DataFrame

from components import pie_chart, year_dropdown


def create_layout(app: Dash, data: DataFrame) -> html.Div:
    """
    Main page layout creation.

    :param app: Dash application.
    :param data: Pandas dataframe.
    :return: Div block.
    """
    return html.Div(
        className='app-div',
        children=[
            html.H1(app.title),
            html.Hr(),
            year_dropdown.render(app, data.Year.unique()[::-1].tolist()),
            pie_chart.render(app, data)
        ]
    )