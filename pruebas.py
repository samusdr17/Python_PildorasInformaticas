import csv
with open('ejemplo.csv', newline='') as csvfile:
    miCsv = csv.reader(csvfile, delimiter=';', quotechar='|')
    for row in miCsv:
        print('-'.join(row))