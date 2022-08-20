"""
Main module.
"""
from os.path import exists

from data_processing import dataframe_filter, process_source
from visualization import visualize


def main() -> None:
    lu_data = process_source('data/result.csv') if exists('data/result.csv') \
        else process_source('data/LU1_DF_B1113_1.0.csv', 'data/result.csv')
    lu_data = dataframe_filter(lu_data, 2022, 6500)
    #visualize('matplotlib', lu_data)
    visualize('dash', lu_data)


if __name__ == '__main__':
    main()
