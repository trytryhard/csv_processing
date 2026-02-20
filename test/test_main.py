"""Test for main.py from ../src/"""

import sys

import pytest  # pylint disable=C0413

sys.path.append(r"../src/")
from main import main  # pylint: disable=C0413


def test_avg():
    """test AVERAGE-report"""
    res_avg = [
        ["continent", "population(avg)"],
        [
            ["Asia", 495.3333],
            ["South America", 215.0],
            ["North America", 171.7273],
            ["Europe", 65.7586],
            ["Oceania", 26.0],
        ],
    ]

    res_func = main(
        files=[
            r".\test_data\corrupted_col.csv",
            r".\test_data\corrupted_sep.csv",
            r".\test_data\fine_file.csv",
            r".\test_data\fine_file2.csv",
        ],
        report="avg-population",
        groupby=["continent"],
        encoding="utf8",
        descending="1",
        separator=",",
        validation="1",
    )

    assert res_avg == res_func


def test_cnt():
    """test COUNT-report"""
    res_cnt = [
        ["year", "continent", "country(cnt)"],
        [
            ["2023", "Europe", 10],
            ["2023", "Asia", 8],
            ["2022", "Asia", 5],
            ["2022", "Europe", 5],
            ["2021", "Asia", 5],
            ["2021", "Europe", 5],
            ["2023", "North America", 4],
            ["2023", "South America", 2],
            ["2023", "Oceania", 2],
            ["2022", "North America", 2],
            ["2022", "South America", 2],
            ["2021", "North America", 2],
            ["2021", "South America", 2],
            ["2022", "Oceania", 1],
            ["2021", "Oceania", 1],
        ],
    ]

    res_func = main(
        files=[r".\test_data\fine_file.csv", r".\test_data\fine_file2.csv"],
        report="cnt-country",
        groupby=["year", "continent"],
        encoding="1251",
        descending="1",
        separator=",",
    )

    assert res_cnt == res_func


def test_sum():
    """test SUM-report"""
    res_sum = [["year", "gdp_growth(sum)"], [["2022", 42.7], ["2023", 46.800000000000004], ["2021", 79.49999999999999]]]

    res_func = main(
        files=[r".\test_data\fine_file.csv", r".\test_data\fine_file2.csv"],
        report="sum-gdp_growth",
        groupby=["year"],
        encoding="1251",
        descending="0",
        separator=",",
    )

    assert res_sum == res_func


def test_mode():
    """test MODE-report"""
    res_mode = [
        ["continent", "year(mode)"],
        [
            ["North America", "2023"],
            ["Asia", "2023"],
            ["Europe", "2023"],
            ["Oceania", "2023"],
            ["South America", "2023, 2022, 2021"],
        ],
    ]

    res_func = main(
        files=[r".\test_data\fine_file.csv", r".\test_data\fine_file2.csv"],
        report="mode-year",
        groupby=["continent"],
        encoding="utf8",
        descending="0",
        separator=",",
    )

    assert res_mode == res_func


def test_err_encoding():
    """test with wrong encoding-value"""
    with pytest.raises(NameError) as exc_info:
        main(
            files=[r".\test_data\fine_file.csv"],
            report="mode-year",
            groupby=["continent"],
            encoding="ERR_ENCODING",
            descending="0",
            separator=",",
        )
    assert str(exc_info.value) == "Please check inputted encoding-value"


def test_err_wrong_sep():
    """test with wrong separator"""
    with pytest.raises(NameError) as exc_info:
        main(
            files=[r".\test_data\fine_file.csv"],
            report="count-year",
            groupby=["continent"],
            separator="wrong",
            validation=True,
        )
    assert str(exc_info.value) == "Please check common cols and separator for files"


def test_err_wrong_col():
    """test with wrong col-name"""
    with pytest.raises(NameError) as exc_info:
        main(
            files=[r".\test_data\fine_file.csv"],
            report="count-year_wrong",
            groupby=["continent_wrong"],
            separator=",",
            validation=True,
        )
    assert str(exc_info.value) == "Please check common cols and separator for files"


def test_err_report_flag():
    """test with wrong report-flag"""
    with pytest.raises(NameError) as exc_info:
        main(
            files=[r".\test_data\fine_file.csv"],
            report="WRONG_FLAG-year",
            groupby=["continent"],
            encoding="utf8",
            descending="0",
            separator=",",
        )
    assert str(exc_info.value) == "Please check report-flag"


def test_err_content():
    """test with corrupted numeric content"""
    with pytest.raises(NameError) as exc_info:
        main(
            files=[r".\test_data\corrupted_content.csv"],
            report="avg-year",
            groupby=["continent"],
            encoding="utf8",
            descending="0",
            separator=",",
        )
    assert str(exc_info.value) == "Corrupted numeric value"
