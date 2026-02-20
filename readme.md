# Скрипт для обработки csv-файлов  

## links: [readme(us)](./docs/us_readme.md), [docs(us)](./docs/us_doc.md), [docs(ru)](./docs/ru_doc.md)

# Функционал
## Работа с данными 
- Взаимодействие с несколькими CSV-файлами;
- Доступны расчеты по единственной колонке следующих величин: average, sum, mode, count;
## Пользовательские настройки
- Использование пользовательского разделителя и кодировки `--separator` и `--encoding`;
- Группировка в ходе расчета по нескольким атрибутам - `--groupby`;
- Сортировка результата по усмотрению пользователя - `--descending`;
- Встроенный справка (`--help`);
## Надёжность
- Валидвация файлов и сигнализирование пользователю о выявленных ошибках:
  - в окне консоли;
  - в лог-файле.

# Установка зависимостей
` pip install -r requirements.txt `

# Пример текстового запроса в коносль 
` python ./src/main.py --files ./data/economic1.csv ./data/economic2.csv --report mode-population --groupby year continent --descending 0  --encoding 1251 `  
# Изображение отображения резальтата
![resulted_image](/docs/img/00_custom_res.png)

# Структура проекта
- `src/` - логика проекта
- `logs/` - папка с логами для отслеживания сбоев программы
- `test/` - unit-тесты
- `docs/` - документация us\ru

### Все баги и предложения размещать - [issues репозитория](https://github.com/trytryhard/csv_processing/issues)
