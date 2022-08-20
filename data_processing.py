"""
Data processing module.
"""

import numpy as np
import pandas as pd

from datetime import datetime


def process_source(file_in: str, file_out: str = None) -> pd.DataFrame:
    """
    Initial loading of a data source.

    :param file_in: Source file for processing.
    :param file_out: Output file. If not specified, file_in is expected to be preprocessed.

    :return: Resulting dataframe.
    """
    dt_start = datetime.now()
    if file_out:
        print(f'{dt_start}: Conversion of the source file started...')
        result_data = pd.read_csv(
            file_in,
            usecols=[1, 3, 4],
            names=['Nationality', 'Year', 'Qty'],
        )
        result_data.drop(0, inplace=True)
        result_data.Nationality = result_data.Nationality.apply(lambda s: str(s).split(': ')[-1])
        result_data.drop(result_data[
                             (result_data.Nationality == 'TOTAL POPULATION') |
                             (result_data.Nationality == 'EUROPE') |
                             (result_data.Nationality == 'ASIA') |
                             (result_data.Nationality == 'AFRICA') |
                             (result_data.Nationality == 'AMERICA') |
                             (result_data.Nationality == 'AUSTRALIA AND OCEANIA') |
                             (result_data.Nationality == 'Total foreigners') |
                             (result_data.Nationality == 'Other countries EU') |
                             (result_data.Nationality == 'Other european countries') |
                             (result_data.Nationality == 'North America')
                         ].index, inplace=True)
        # result_data.reindex()
        result_data.Year = result_data.Year.apply(lambda s: str(s).split('-')[0])
        result_data.Year = pd.to_numeric(result_data.Year, downcast='integer', errors='coerce')
        result_data.Qty.fillna(value=0, inplace=True)
        result_data.Qty = pd.to_numeric(result_data.Qty, downcast='integer', errors='coerce')

        result_data.to_csv(file_out, index=False)
        dt_end = datetime.now()
        duration = dt_end - dt_start
        print(f'{dt_end}: Conversion of the source file complete. Duration: {duration.seconds}s')
    else:
        print(f'Loading preprocessed data...')
        result_data = pd.read_csv(
            file_in,
            dtype={
                'Nationality': str,
                'Year': np.int16,
                'Qty': np.int64,
            }
        )

    return result_data


def dataframe_filter(data: pd.DataFrame, year: int = datetime.now().year, qty_margin: int = 0) -> pd.DataFrame:
    """
    Filter the dataframe with the provided parameters.

    :param data: Source dataframe.
    :param year: Year.
    :param qty_margin: Minimum quantity. Lesser quantities are merged into one.

    :return: Filtered dataframe.
    """
    data_filtered = data.loc[data.Year == year]
    data_filtered.loc[data_filtered.Qty < qty_margin, 'Nationality'] = 'Other nationalities'
    return data_filtered.groupby('Nationality')['Qty'].sum().reset_index()
