##python version 3.8

import csv
import json

path_file = "C:\\Users\\mathe\\Desktop\\"

def conversor(csvf,jsonf):
    data = {}

    with open(csvf, encoding='utf-8') as csv_file:
        csv_new = csv.DictReader(csv_file)
        n = 0
        for rows in csv_new:
            key = n
            n = n + 1
            data[key] = rows

    with open(jsonf, 'w', encoding='utf-8') as json_file:
        json_file.write(json.dumps(data, indent=4))


csvf = path_file + 'questao_02.csv'
jsonf = path_file + 'converted.json'
try:
    conversor(csvf, jsonf)
except Exception as e:
    print(str(e))