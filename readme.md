# Скрипт для обработки csv-файлов  

# Установка 
``` pip install -r requirements.txt ```

# Пример использования 
``` python ./src/main.py --files ./data/economic1.csv ./data/economic2.csv --report mode-population --groupby year continent --descending 0  --encoding 1251 ```  
# Изображение использования
![resulted_image](/docs/img/00_custom_res.png)

# Функционал
- Взаимодействие с несколькими csv-файлами;
- Доступны расчеты по единственной колонке следующих значений: average, sum, mode, count;
- Группировка в ходе расчета по нескольким атрибутам (group by sql-like);
- Валидвация файлов
- Встроенный help
- Использование пользовательского разделителя и кодировки
- Сортировка результата по усмотрению пользователя

# RU\EN документация в процессе разработки