"""entrance point \\ main.py"""

import argparse
import os
import pathlib
from encodings import aliases as enc

import to_log
from csv_processing import CSVProcessing
from file_validation import cols_validation

csv_prc_instance = CSVProcessing()


def report_menu(func: str) -> list:
    """
    :param func: report-type string
    :return: result of CSV_Processing's method
    """
    reports_dict = {
        "avg": csv_prc_instance.avg_func,
        "average": csv_prc_instance.avg_func,
        "sum": csv_prc_instance.sum_func,
        "summation": csv_prc_instance.sum_func,
        "cnt": csv_prc_instance.cnt_func,
        "count": csv_prc_instance.cnt_func,
        "mode": csv_prc_instance.mode_func,
    }

    if func not in reports_dict:
        to_log.log_message(f"===Wrong report-value - {func}===\n")
        to_log.log_message("You should use name from these keywords:\n")
        to_log.log_message(f"{', '.join(list(reports_dict.keys()))}\n")
        raise NameError("Please check report-flag")

    return reports_dict[func]()


def main(**kwargs: list | str | bool) -> list:
    """Entrance to logic"""
    path_to_file: list = []
    val_flag: bool = False

    # prepare atributes
    for name, value in kwargs.items():
        if name == "files":
            path_to_file = [x for x in value if os.path.exists(x)]

        elif name == "report":
            csv_prc_instance.report = value.split("-")[0]
            csv_prc_instance.digital_col = "-".join(value.split("-")[1::])

        elif name == "groupby":
            csv_prc_instance.groupby = value or ["country"]

        elif name == "validation":
            val_flag = value not in ["0", "False"]

        elif name == "separator":
            if not value:
                to_log.log_message("Found empty separator, program gonna use comma as sep\n")
            if len(value) > 1:
                to_log.log_message(
                    f"There was a long sep - '{value}', with length {len(value)}, "
                    f"so program gonna use first symbol {value[0]} instead\n"
                )
            csv_prc_instance.sep = value[0] if value else ","

        elif name == "encoding":
            if value not in [x for y in enc.aliases.items() for x in y]:
                to_log.log_message("===Wrong encoding===")
                to_log.log_message(f"Encoding {value} not found in :{list(enc.aliases.items())}\n")
                raise NameError("Please check inputted encoding-value")
            csv_prc_instance.encoding = value

        elif name == "descending":
            csv_prc_instance.descending = value not in ["0", "False"]

    if val_flag:
        # validate files by needed cols names
        path_to_file = cols_validation(
            path_to_file,
            needed_cols=[csv_prc_instance.digital_col] + csv_prc_instance.groupby,
            sep_val=csv_prc_instance.sep,
            enc_val=csv_prc_instance.encoding,
        )
    csv_prc_instance.files = path_to_file

    return report_menu(csv_prc_instance.report)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Helper with csv-files.",
        epilog="Examples of usage via console: "
        "\n\tfrom src dir: python main.py --files file1.csv file2.csv --report average-gdp"
        "\n\tfrom repository dir: "
        "python .\\src\\main.py --files .\\data\\economic1.csv .\\data\\economic2.csv "
        "--report mode-population --groupby year continent --descending 0  --encoding 1251"
        "\nIf you got some errors - report it into issue-seciton via link: "
        r"https://github.com/trytryhard/csv_processing/issues",
        formatter_class=argparse.RawTextHelpFormatter,
    )

    parser.add_argument(
        "-f",
        "--files",
        help="Takes path to needed csv. "
        "You can add list of pathes with separation by space."
        "\nIMPORTANT: Required argument. "
        "Obtain pathes to files separated with space."
        "\n\tIf there is no correct files provided with filepath - these files"
        " will be dropped from processing by True --validation flag"
        "\n\n",
        type=pathlib.Path,
        nargs="+",
        required=True,
    )

    parser.add_argument(
        "-r",
        "--report",
        help="Define kind of report and work-column."
        "\nFirst word before separator should be kind of report, "
        "second part - name of column."
        "\nList of report:"
        "\n\t average - calculate average value;"
        "\n\textra: sum - calculate sum of col.; median - calc median value; "
        "mode - calc mode value"
        "\nIMPORTANT: Required argument. Obtain string-value. "
        "Strictly one col-name"
        "\n\tIf there is no column with this name, these files "
        "will be dropped from processing by True --validation flag"
        "\n\n",
        type=str,
        required=True,
    )

    parser.add_argument(
        "-gb",
        "--groupby",
        help="Takes an column[-s] to be grouped by them."
        "\nBy default processing grouped by 'country'."
        "\nIMPORTANT: Optional argument. Obtain string-value ."
        "\n\tIf there is no column with this name, these files"
        "will be dropped from processing by True --validation flag!"
        "\n\n",
        type=str,
        nargs="+",
        required=False,
    )

    parser.add_argument(
        "-v",
        "--validation",
        help="Takes an bool-value to deside of usage validation on csv-files."
        "\nValidation drop wrong file from processing."
        "Wrong file is a file that haven't needed column[-s] "
        "or its column content is wrong."
        "\nList of cols decides by groupby argument and --report col-part."
        "\nIMPORTANT: Optional argument. False-value in ['0','False'] "
        "all other are True."
        "\n\tIt may slow a program, but it helps cope with non validated "
        "csv-files."
        "\n\tIf there is no column\\data with this name, these files"
        "will be dropped from processing!"
        "\n\n",
        type=str,
        default=True,
        required=False,
    )

    parser.add_argument(
        "-s",
        "--separator",
        help="Common separator for csv file[-s]. By default is a comma ,. Obtain string-value.",
        type=str,
        default=",",
        required=False,
    )

    parser.add_argument(
        "-e",
        "--encoding",
        help="Common encoding for csv file[-s]. By default is a utf-8. " "Obtain string-value.",
        type=str,
        default="utf8",
        required=False,
    )

    parser.add_argument(
        "-desc",
        "--descending",
        help="The Order of result."
        "\nImportant: Optional argument. "
        "False-value in ['0','False'] all other are True."
        "\n\tBy default: the result orders descending (True).",
        type=str,
        default="1",
        required=False,
    )

    args = parser.parse_args()
    main(**vars(args))
