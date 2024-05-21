import csv
import json
def incrementareaVarsteiCSV():
    dateNoi=[]
    with open('Curs15/tema/persoane.csv','r',newline='') as csvFile:
        reader=csv.reader(csvFile)
        header=next(reader)
        dateNoi.append(header)
        for row in reader:
            row[-1]=str(int(row[-1])+1)
            dateNoi.append(row)
    with open('Curs15/tema/persoane.csv','w',newline='') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerows(dateNoi)
# incrementareaVarsteiCSV()

def incrementareaVarsteiJSON():
    with open('Curs15/tema/persoane.json','r') as jsonFile:
        continut=json.load(jsonFile)
        for person in continut:
            person['varsta'] = str(int(person['varsta']) + 1)
    with open('Curs15/tema/persoane.json', 'w') as jsonFile:
        json.dump(continut, jsonFile)
incrementareaVarsteiJSON()