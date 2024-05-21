import csv
def numarPersoane():
    with open('Curs15/tema/persoane.csv','r',newline='') as csvFile:
        reader=csv.reader(csvFile)
        count=0
        for row in reader:
            count+=1
        print(f'Sunt {count} persoane inregistrate.')
numarPersoane()