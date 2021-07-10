import csv
with open('ResidenciasSanitarias.csv', newline='') as csvbdd:
    lectordatos = csv.reader(csvbdd,  delimiter=' ', quotechar='|' )
    for i in lectordatos:
        print(', '.join(i))

