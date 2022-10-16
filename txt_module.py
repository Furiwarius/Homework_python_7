import pandas as pd


def txt_read():
    try:
        with open(r"storage\txt_handbook.txt", "r") as txt_file:
            file = [val for val in txt_file if val!='\n']
            
            name_list = [val[val.find(':')+2:-1] for val in file if val!='\n' and 'name' in val]
            number_list = [val[val.find(':')+2:-1] for val in file if val!='\n' and 'number' in val]
            city_list = [val[val.find(':')+2:-1] for val in file if val!='\n' and 'city' in val]

            read_handbook = pd.DataFrame({'name':name_list, 'number': number_list, 'city': city_list})
        return read_handbook

    except FileNotFoundError:
        new_handbook = pd.DataFrame({'name':[], 'number':[], 'city':[]})
        return new_handbook


def txt_write(new_hb):
    with open(r"storage\txt_handbook.txt", "w") as file:
        for name, number, city in zip(new_hb['name'], new_hb['number'], new_hb['city']):
            val = f"name: {name}\nnumber: {number}\ncity: {city}\n\n"
            file.write(val)


