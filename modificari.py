import csv
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
incrementareaVarsteiCSV()