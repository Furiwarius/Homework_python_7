import interaction_interface as ii

from csv_module import csv_write, csv_read
from exel_module import exel_write, exel_read
from htmal_module import html_write, html_read
from txt_module import txt_write, txt_read


def form():
    form = ii.form_selection()
    if form == '1':
        handbook = csv_read()
    elif form == '2':
        handbook = exel_read()
    elif form == '3':
        handbook = txt_read()
    elif form == '4':
        handbook = html_read()
    return handbook


def init():
    handbook = form()
    new_handbook = ii.interface(handbook)
    if len(new_handbook)>0:
        csv_write(new_handbook)
        exel_write(new_handbook)
        html_write(new_handbook)
        txt_write(new_handbook)
