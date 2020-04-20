import csv

path=""
filename="Carbonara_Merged.csv"
destinations=[]

start="2020-04-07 20:00"
end="2020-04-14 20:00"

ds=int(start.split("-")[2].split(" ")[0]) #start day
hs=int(start.split(" ")[1].split(":")[0]) #start hour
ms=int(start.split(" ")[1].split(":")[1]) #start minute

de=int(end.split("-")[2].split(" ")[0]) #end day
he=int(end.split(" ")[1].split(":")[0]) #end hour
me=int(end.split(" ")[1].split(":")[1]) #end minute

dc=ds #counter day
hc=hs #counter hour
mc=ms #counter minute

current=start

arrD=[] #Destination
arrB=[] #Bytes
arrC=[] #CO2
arr=[]

#sum=0.0

reader=csv.reader(open(path+filename, "rt"))
writer=csv.writer(open(path+"Carbonara_Edit.csv", "wt"))
row=next(reader)
#write header
new_row=("Date-Time","No.01 Host","No.01 Traffic in MiB","No.01 CO2 in mg", \
                     "No.02 Host","No.02 Traffic in MiB","No.02 CO2 in mg", \
                     "No.03 Host","No.03 Traffic in MiB","No.03 CO2 in mg", \
                     "No.04 Host","No.04 Traffic in MiB","No.04 CO2 in mg", \
                     "No.05 Host","No.05 Traffic in MiB","No.05 CO2 in mg", \
                     "No.06 Host","No.06 Traffic in MiB","No.06 CO2 in mg", \
                     "No.07 Host","No.07 Traffic in MiB","No.07 CO2 in mg", \
                     "No.08 Host","No.08 Traffic in MiB","No.08 CO2 in mg", \
                     "No.09 Host","No.09 Traffic in MiB","No.09 CO2 in mg", \
                     "Misc Hosts", "Misc Traffic in MiB", "Misc CO2 in mg")
writer.writerow(new_row)

while dc!=de or hc!=he or mc!=me:
    mc=mc+1
    while row[0]==current:
        #sum=sum+float(row[3])
        if row[1] in arrD:
            index=arrD.index(row[1])
            arrB[index]=arrB[index]+int(row[3])
            arrC[index]=arrC[index]+float(row[4])
        else:
            arrD.append(row[1])
            arrB.append(int(row[3]))
            arrC.append(float(row[4]))
        try:
            row=next(reader)
        except:
            break
       
    if mc==60:
        #print(p)
        mc=0
        hc=hc+1
        if hc==24:
            hc=0
            dc=dc+1
    current="2020-04-"+str(dc).zfill(2)+" "+str(hc).zfill(2)+":"+str(mc).zfill(2)
    
    if mc%10==0:
        for i in range(len(arrD)):
            arr.append([arrD[i],arrB[i],arrC[i]])
        arr.sort(key=lambda x: x[1], reverse=True)
        otherB=0
        otherC=0
        print(current)
        for k in range(10, len(arr)):
            otherB=otherB+arr[k][1]
            otherC=otherC+arr[k][2]
        r=[]
        r.append(current)
        for p in range(0,9):
            try:
                r.append(arr[p][0])
                r.append(arr[p][1]/1024/1024)
                r.append(arr[p][2])
            except:
                break
        r.append("various")
        r.append(otherB/1024/1024)
        r.append(otherC/1000)
        new_row=tuple(r)

        writer.writerow(new_row)
        #print(arr)
        arr=[]
        arrD=[]
        arrB=[]
        arrC=[]

#print(sum)
