import csv

path="/media/tilmann/Archiv/Archiv/FHP-Kd/Semester-02/(11EG-K)_Slow_Planet/U1_Online Energy Consumption Self-Portrait/capture/csv/tmp/"
filename="Carbonara_Merged.csv"
filename1="hosts.csv"

arr=csv.reader(open(path+filename1,"rt"))
hosts=list(arr)
hosts1=[]
hosts2=[]
for k in range(len(hosts)):
    hosts1.append(hosts[k][0])
    hosts2.append(hosts[k][1])

arr=csv.reader(open(path+filename,"rt"))
merged=list(arr)
for i in range(len(merged)):
    if merged[i][1] in hosts2:
        index=hosts2.index(merged[i][1])
        print(hosts1[index]+"--"+merged[i][1])
        merged[i][1]=hosts1[index]
writer=csv.writer(open(path+filename,"wt"))
writer.writerows(merged)
        