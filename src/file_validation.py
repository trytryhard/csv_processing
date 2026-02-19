"""
Module validates files on compatible col-names (todo: content)
"""

import csv
import to_log


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

    if False in validated.values():
        to_log.message("===Columns validation===\n")
        to_log.message(f"These files was dropped from processing (wrong sep or col-name): "
                       f"{[str(x) for x in validated if validated[x] == False]}\n")

    if len([csv_path for csv_path in validated if validated[csv_path]]) == 0:
        to_log.message("===All files dropped after validation===\n")
        to_log.message("There is no files left in queue after validation for processing\n")
        raise NameError("Please check common cols and separator for files")

    return [csv_path for csv_path in validated if validated[csv_path]]


def content_validation(path_to_csv:list, digital_cols:list, sep_val:str, enc_val:str)->list:
    """
    TODO, but implemented in avg and sum function, when calc expected numeric values
    :param path_to_csv:
    :param number_cols:
    :param sep_val:
    :param enc_val:
    :return:
    """
    pass
