# Скрипт для обработки csv-файлов  

links: links: [docs(us)](./docs/us_doc.md), [docs(ru)](./docs/ru_doc.md),  [readme(ru)](/readme.md)

# Functionality
## Data Handling
- Interaction with multiple CSV files;
- Calculations available for a single column: average, sum, mode, count;
## User Settings
Use of custom separator and encoding via --separator and --encoding;
- Grouping during calculation by multiple attributes with --groupby;
- Sorting the result at the user's discretion with --descending;
- Built-in help (--help);
## Reliability
- File validation and notifying the user about detected errors:
  - in the console window;
  - in a log file.

# Dependencies installation
``` pip install -r requirements.txt ```

# Example of call in console
``` python ./src/main.py --files ./data/economic1.csv ./data/economic2.csv --report mode-population --groupby year continent --descending 0  --encoding 1251 ```  
# Image of usage
![resulted_image](/docs/img/00_custom_res.png)

# Project Structure
`src/` – project logic
`logs/` – folder with logs for tracking program failures
`test/` – unit tests
`docs/` – documentation (US/RU)

Please submit all bugs and suggestions to the [issues](https://github.com/trytryhard/csv_processing/issues)
