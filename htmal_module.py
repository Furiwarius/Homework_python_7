import pandas as pd


def html_read():
    try:
        with open(r"storage\html_handbook.htm", "r") as html_file:
            line_list = [val.replace('\t', '').replace('\n', '').replace('<br>', '') for val in html_file if '<br>' in val]

            name_list = [val[val.find(':')+2:-1] for val in line_list if 'name' in val]
            number_list = [val[val.find(':')+2:-1] for val in line_list if 'number' in val]
            city_list = [val[val.find(':')+2:-1] for val in line_list if 'city' in val]

            read_handbook = pd.DataFrame({'name':name_list, 'number': number_list, 'city': city_list})
        return read_handbook

    except FileNotFoundError:
        new_handbook = pd.DataFrame({'name':[], 'number':[], 'city':[]})
        return new_handbook


def html_write(new_handbook):
    my_template = '''<!DOCTYPE html>\n<html>\n
    <head>\n
        <meta charset="utf-8">\n
        <title>Handbook</title>\n
    </head>\n
    <body>\n'''
    my_template+=creation_body(new_handbook)
    with open("storage\html_handbook.htm", "w") as file:
        for val in my_template:
            file.write(val)


def creation_body(new_hb):
    body = ''
    for name, number, city in zip(new_hb['name'], new_hb['number'], new_hb['city']):
        body+=f'''\n\t\tname: {name}<br>\n\t\tnumber: {number}<br>\n\t\tcity: {city}<br><br>\n'''
    else:
        body+="\t</body>\n</html>\n"
    return body
