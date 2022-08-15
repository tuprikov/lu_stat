"""
Data visualization module.
"""
import matplotlib.pyplot as plt

from dash import Dash


def visualize_matplotlib(lu_data: "pd.DataFrame") -> None:
    """
    Visualization using Matplotlib.

    :param lu_data: Pandas dataframe.
    :return:
    """
    lu_data_2022 = lu_data.loc[lu_data.Year == 2022]
    qty_margin = 6500
    qty_margin_2 = 1900
    lu_data_2022_minor = lu_data_2022[lu_data_2022.Qty < qty_margin].copy()
    lu_data_2022.loc[lu_data_2022.Qty < qty_margin, 'Nationality'] = 'Minor nationalities'
    lu_data_2022 = lu_data_2022.groupby('Nationality')['Qty'].sum().reset_index()

    lu_data_2022_minor.loc[lu_data_2022_minor.Qty < qty_margin_2, 'Nationality'] = \
        f'Minor nationalities (less than {qty_margin_2} people)'
    lu_data_2022_minor = lu_data_2022_minor.groupby('Nationality')['Qty'].sum().reset_index()

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))
    ax1_labels = [f'{i}: {j}' for i, j in list(zip(lu_data_2022.Nationality, lu_data_2022.Qty))]
    ax1.pie(lu_data_2022.Qty, labels=ax1_labels, autopct='%1.1f%%', textprops={'fontsize': 9})
    ax1.title.set_text('Major nationalities')

    ax2_labels = [f'{i}: {j}' for i, j in list(zip(lu_data_2022_minor.Nationality, lu_data_2022_minor.Qty))]
    ax2.pie(lu_data_2022_minor.Qty, labels=ax2_labels, textprops={'fontsize': 8})
    ax2.title.set_text(f'Minor nationalities (less than {qty_margin} people)')

    fig.canvas.manager.set_window_title('Luxembourg statistics')
    plt.show()
