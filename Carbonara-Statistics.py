import csv

path=""
filename="Carbonara_Merged.csv"

with open(path+filename, "rt") as inp, open(path+"hosts_2.csv", "wt") as out:
    writer = csv.writer(out)
    sortedListD=[]
    sortedListB=[]
    sortedListC=[]
    sortedList=[]
    for row in csv.reader(inp):
        print(row)
        if row[1] in sortedListD:
            index=sortedListD.index(row[1])
            sortedListB[index]=sortedListB[index]+int(row[3])
            sortedListC[index]=sortedListC[index]+float(row[4])
        else:
            sortedListD.append(row[1])
            sortedListB.append(int(row[3]))
            sortedListC.append(float(row[4]))
    for i in range(len(sortedListD)):
        sortedList.append([sortedListD[i],sortedListB[i],sortedListC[i]])
    sortedList.sort(key=lambda x:x[1], reverse=True)
    hosts=[]
    for i in range(0,150):
        print(sortedList[i][0])
        writer.writerow((sortedList[i][0],sortedList[i][1]/1024/1024,sortedList[i][2]/1000))
    