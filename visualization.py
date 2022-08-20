"""
Data visualization module.
"""
import matplotlib.pyplot as plt

from dash import Dash
from dash_bootstrap_components.themes import BOOTSTRAP
from pandas import DataFrame

from components.layout import create_layout


def visualize(method: str, data: DataFrame) -> None:
    """
    Entry point to select a visualization strategy.

    :param method: Visualization method name.
    :param data: Pandas dataframe to visualize.
    """
    if method in visualization_functions:
        visualization_functions.get(method)(data)
    raise NotImplementedError


def visualize_matplotlib(data: DataFrame) -> None:
    """
    Visualization using Matplotlib.

    :param data: Pandas dataframe.
    """
    fig, ax1 = plt.subplots(1, 1, figsize=(10, 8))
    ax1_labels = [f'{i}: {j}' for i, j in list(zip(data.Nationality, data.Qty))]
    ax1.pie(data.Qty, labels=ax1_labels, autopct='%1.1f%%', textprops={'fontsize': 9})
    ax1.title.set_text('Nationalities of Luxembourg')

    fig.canvas.manager.set_window_title(_TITLE)
    plt.show()


def visualize_dash(data: DataFrame) -> None:
    """
    Visualize using Dash.

    :param data: Pandas dataframe.
    """
    app = Dash(external_stylesheets=[BOOTSTRAP])
    app.title = _TITLE
    app.layout = create_layout(app, data)
    app.run()


visualization_functions = {
    'matplotlib': visualize_matplotlib,
    'dash': visualize_dash,
}

_TITLE = 'Luxembourg statistics'
