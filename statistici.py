import csv
def numarPersoane():
    with open('Curs15/tema/persoane.csv','r',newline='') as csvFile:
        reader=csv.reader(csvFile)
        count=0
        for row in reader:
            count+=1
        print(f'Sunt {count} persoane inregistrate.')
# numarPersoane()

def youngestPerson():
    with open('Curs15/tema/persoane.csv','r',newline='') as csvFile:
        reader=csv.reader(csvFile)
        next(reader)
        firstRow=next(reader)
        min=int(firstRow[-1])
        nume=firstRow[0]
        prenume=firstRow[1]
        for row in reader:
            row[-1]=int(row[-1])
            if min>row[-1]:
                min=row[-1]
                nume=row[0]
                prenume=row[1]
        print(f'{nume} {prenume} este cel mai tanar, avand {min} ani.')
youngestPerson()