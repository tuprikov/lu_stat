"""
Main module.
"""
from os.path import exists

from data_processing import process_source
from visualization import visualize_matplotlib


def main() -> None:
    lu_data = process_source('data/result.csv') if exists('data/result.csv') \
        else process_source('data/LU1_DF_B1113_1.0.csv', 'data/result.csv')
    visualize_matplotlib(lu_data)


if __name__ == '__main__':
    main()
