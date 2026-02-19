"""Test for file_validation.cols_validation from ../src/"""

import sys

import pytest

sys.path.append(r"../src/")
from file_validation import cols_validation  # pylint: disable=C0413

prep_data = [
    (
        [
            r"test_data/fine_file.csv",
            r"test_data/corrupted_col.csv",
            r"test_data/corrupted_content.csv",
            r"test_data/corrupted_sep.csv",
        ],
        ["gdp", "country"],
        ",",
        "utf8",
    )
]
res = [r"test_data/fine_file.csv", r"test_data/corrupted_content.csv"]


@pytest.mark.parametrize("list_of_files, needs_cols, sep_val, enc_val", prep_data)
def test_cols_validation(list_of_files, needs_cols, sep_val, enc_val):
    """checks correct final pathes to csv"""
    res_func = cols_validation(list_of_files, needs_cols, sep_val, enc_val)

    assert res_func == res
