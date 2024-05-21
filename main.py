import json
import csv
def informatiiPersoane():
    n=int(input('n= '))
    dictionarPersoane={
        'nume':'',
        'prenume':'',
        'varsta':''
    }
    with open('Curs15/tema/persoane.json','w') as jsonFile:
        jsonFile.write('[')
        for persoana in range(n):
            dictionarPersoane['nume']=input('Numele: ')
            dictionarPersoane['prenume']=input('Prenumele: ')
            dictionarPersoane['varsta']=input('Varsta: ')
            json.dump(dictionarPersoane,jsonFile)
            if persoana<n-1:
                jsonFile.write(',')
        jsonFile.write(']')
# informatiiPersoane()

def jsonTocsv():
    with open('Curs15/tema/persoane.json','r') as jsonFile:
        continut=json.load(jsonFile)
        numeColoane=continut[0].keys()
        with open('Curs15/tema/persoane.csv','w',newline='') as csvFile:
            writer=csv.DictWriter(csvFile,fieldnames=numeColoane)
            writer.writeheader()
            writer.writerows(continut)
jsonTocsv()

