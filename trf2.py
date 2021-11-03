##python version 3.8

import csv
import json
#alterar para o diretorio desejado
path_file = "C:\\Users\\...\\Desktop\\"

def conversor(csvf,jsonf):
    #cria o objeto data
    data = {}
    #percorre o arquivo csv e aloca as linhas
    with open(csvf, encoding='utf-8') as csv_file:
        csv_new = csv.DictReader(csv_file)
        n = 0
        for rows in csv_new:
            key = n
            n = n + 1
            data[key] = rows
    #grava cada linha no json
    with open(jsonf, 'w', encoding='utf-8') as json_file:
        json_file.write(json.dumps(data, indent=4))


csvf = path_file + 'questao_02.csv'
jsonf = path_file + 'converted.json'
try:
    conversor(csvf, jsonf)
except Exception as e:
    print(str(e))