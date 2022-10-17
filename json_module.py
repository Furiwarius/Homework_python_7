import pandas as pd


def json_read():
    try:
        read_handbook = pd.read_json('storage\json_handbook.txt')
        return read_handbook
    except FileNotFoundError:
        new_handbook = pd.DataFrame({'name':[], 'number':[], 'city':[]})
        return new_handbook


def json_write(new_handbook):
    new_handbook.to_json('storage\json_handbook.txt')
    
