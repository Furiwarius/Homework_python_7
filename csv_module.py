import pandas as pd


def csv_read():
    try:
        read_handbook = pd.read_csv('storage\csv_handbook.csv', sep=',')
        return read_handbook
    except FileNotFoundError:
        new_handbook = pd.DataFrame({'name':[], 'number':[], 'city':[]})
        return new_handbook


def csv_write(new_handbook):
    new_handbook.to_csv('storage\csv_handbook.csv', index =False)
