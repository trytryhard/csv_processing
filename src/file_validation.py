"""
Module helps to validate files on compatible  with main logic
"""

import pathlib
import os
import csv


def cols_validation(path_to_csv:list, needed_cols:list, sep_val:str, enc_val:str )->list:
    """
    :param path_to_csv: list of files to validate by col name
    :param needed_cols: list of needed cols to be in file
    :param sep_val: separator for csv
    :param enc_val: encoding for csv
    :return: list of compatible files
    """
    validated = {x:True for x in path_to_csv}
    for csv_file in path_to_csv:
        with open(csv_file, newline="", encoding=enc_val) as с_f:
            reader = csv.DictReader(с_f, delimiter=sep_val)
            header = reader.fieldnames
            for col in needed_cols:
                if col not in header:
                    validated[csv_file] = False
                    break
    return [csv_path for csv_path in validated if validated[csv_path]]


def content_validation(path_to_csv:list, digital_cols:list, sep_val:str, enc_val:str)->list:
    """
    TODO
    :param path_to_csv:
    :param number_cols:
    :param sep_val:
    :param enc_val:
    :return:
    """
    return path_to_csv