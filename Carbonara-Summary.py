import csv
import os

path="/media/tilmann/Archiv/Archiv/FHP-Kd/Semester-02/(11EG-K)_Slow_Planet/U1_Online Energy Consumption Self-Portrait/capture/csv/"
destinations=[]

start="2020-04-07 20:00"
end="2020-04-14 19:59"

directory = os.fsencode(path)
for file in os.listdir(directory):
    filename=os.fsdecode(file)
    with open(path+filename, "rt") as inp, open(path+"tmp/"+filename, "wt") as out:
        writer = csv.writer(out)
        for row in csv.reader(inp):
            if row[2]!="DESKTOP-NG6AUIV.local" and row[3]!="DESKTOP-NG6AUIV.local" and row[3]!="Broadcast" and row[3]!="239.255.102.18" and \
            row[3]!="255.255.255.255" and row[3]!="ff02::c" and row[3]!="239.255.255.250" and row[4]!="ARP" and row[4]!="BJNP" and \
            row[4]!="BROWSER" and row[4]!="DHCP" and row[4]!="DHCPv6" and row[4]!="DNS" and row[4]!="HomePlug AV" and row[4]!="ICMP" and \
            row[4]!="ICMPv6" and row[4]!="IGMPv3" and row[4]!="LLC" and row[4]!="LLMNR" and row[4]!="MDNS" and row[4]!="MBNS" and row[4]!="SSDP":
                io=""
                host=""
                if row[2]=="Tilmann-PC1.fritz.box":
                    io="o"
                    host=row[3]
                elif row[3]=="Tilmann-PC1.fritz.box":
                    io="i"
                    host=row[2]
                new_row=(row[1][:16],host,io,row[5])
                
                writer.writerow(new_row)

                if row[3] not in destinations:
                    destinations.append(row[3])

with open("destinations.txt", "w") as txt_file:
    for line in destinations:
        txt_file.write("".join(line) + "\n")