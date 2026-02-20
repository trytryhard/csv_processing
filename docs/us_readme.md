# Скрипт для обработки csv-файлов  

links: readme(us), docs(us), docs(ru)

# Функционал
- Взаимодействие с несколькими csv-файлами, их агрегация для вычесления: average, sum, mode, count;
- Доступны расчеты по единственной колонке следующих значений: average, sum, mode, count;
- Группировка в ходе расчета по нескольким атрибутам (group by sql-like);
- Валидвация файлов и сигнализирование пользователю о выявленной ошибке в окне консоли
- Встроенный help
- Использование пользовательского разделителя и кодировки
- Сортировка результата по усмотрению пользователя


# Установка зависимостей
``` pip install -r requirements.txt ```

# Пример текстового запроса в коносль 
``` python ./src/main.py --files ./data/economic1.csv ./data/economic2.csv --report mode-population --groupby year continent --descending 0  --encoding 1251 ```  
# Изображение результата использования
![resulted_image](/docs/img/00_custom_res.png)



# В процессе:
- линтеры (github/actions)
- RU\EN документация в процессе разработки