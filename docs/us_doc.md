# Example of script usage
```
python .\src\main.py --files .\test\test_data\corrupted_col.csv  .\test\test_data\corrupted_sep.csv .\test\test_data\fine_file.csv .\test\test_data\fine_file2.csv --report sum-population --groupby year continent --v 1 --encoding utf8 --d 1
```

# Flags explanation
## `--files`\\`-f`
Accepts one or more paths to CSV files.

## `--report`\\`-r` 
Accepts a report type in the format: keyword of report-kind with separation from calculated column with short dash.  
For example: `--report sum-king-col`, here we are calcing sum on `king-col`-column. The calculation agregates on `--groupby`.  
Expected key-words: 
- sum - calculates sum on specified column;
- avg - calculates average value on specified column;
- count - calculates repeats of value on specified column;
- mode - calculates mode-value on specified column.

## `--groupby`\\`-gb` 
Aggregates CSVs-files on extra columns. By default its a `country`.

## `--validation`\\`-v` 
Validates CSV-files on having needed columns from `--report` and `--groupby` flags.  
Exclude pathes to CSV with lost column(-s) from calculations.  
Arguments "False" или "0" turns it off. All other aruments activate validation.

## `--separator`\\`-s` 
Help to input custom separator for CSVs. From long seps there will be used only first symbol. 
Wrong seperator would lead to wrong calculations.  
By default its a comma. 

## `--encoding`\\`-e` 
Help to input custom encoding for CSVs. Non-existing encoding leads to stop processing.  
Wrong encoding affects of results of calculations. 
By default its a utf8.

## `--descending`\\`-desc` 
Help to sort output by report-column. If argument "False" or "0" so sorting would be ascending.  
By default it sorts descending. 

### Bugs and recommendations are welcome -  [issues tab](https://github.com/trytryhard/csv_processing/issues)