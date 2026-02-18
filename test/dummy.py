"""
todo:
проверить как ведет себя с верными и неверными флагами, значениями (если это разумно)
"""
import csv

file = './test_data/fine_file.csv'
with open(file, newline="") as f:
    reader = csv.DictReader(f, delimiter=',')
    for row in reader:
        print(row['year'])
