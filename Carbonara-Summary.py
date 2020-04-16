import csv
import os

path="/media/tilmann/Archiv/Archiv/FHP-Kd/Semester-02/(11EG-K)_Slow_Planet/U1_Online Energy Consumption Self-Portrait/capture/csv/tmp/"
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
        for k in range(9, len(arr)):
            otherB=otherB+arr[k][1]
            otherC=otherC+arr[k][2]
        new_row=(current,arr[0][0],arr[0][1],arr[0][2], \
                        arr[1][0],arr[1][1],arr[1][2], \
                        arr[2][0],arr[2][1],arr[2][2], \
                        arr[3][0],arr[3][1],arr[3][2], \
                        arr[4][0],arr[4][1],arr[4][2], \
                        arr[5][0],arr[5][1],arr[5][2], \
                        arr[6][0],arr[6][1],arr[6][2], \
                        arr[7][0],arr[7][1],arr[7][2], \
                        arr[8][0],arr[8][1],arr[8][2], \
                        "other", otherB, otherC)
        writer.writerow(new_row)
        print(arr)
        arr=[]
        arrD=[]
        arrB=[]
        arrC=[]

#print(sum)
