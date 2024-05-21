import csv
import json
def numarPersoane():
    with open('Curs15/tema/persoane.csv','r',newline='') as csvFile:
        reader=csv.reader(csvFile)
        count=0
        for row in reader:
            count+=1
        print(f'Sunt {count} persoane inregistrate.')
# numarPersoane()

def youngestPerson():
    with open('Curs15/tema/persoane.json','r') as jsonFile:
        continut=json.load(jsonFile)
        min=int(continut[0]['varsta'])
        nume=continut[0]['nume']
        prenume=continut[0]['prenume']
        for person in continut:
            person['varsta']=int(person['varsta'])
            if min>person['varsta']:
                min=person['varsta']
                nume=person['nume']
                prenume=person['prenume']
        print(f'{nume} {prenume} este cel mai tanar, avand {min} ani.')
youngestPerson()