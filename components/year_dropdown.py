"""
Dropdown component to select a year.
"""
from typing import List

from dash import Dash, dcc, html

from components import ids


def render(app: Dash, years: List[int]) -> html.Div:
    """
    Render a dropdown of years.
    Maximum year is set by default.

    :param app: Dash app.
    :param years: List of years.

    :return: HTML div.
    """
    return html.Div(
        children=[
            html.H6('Year'),
            dcc.Dropdown(
                id=ids.YEAR_DROPDOWN,
                options=[{'label': year, 'value': year} for year in years],
                value=max(years)
            )
        ]
    )
