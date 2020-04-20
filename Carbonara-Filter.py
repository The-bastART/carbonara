import csv
import os

path=""
destinations=[]

directory = os.fsencode(path)
for file in os.listdir(directory):
    filename=os.fsdecode(file)
    if(os.path.isfile(path+filename)):
        with open(path+filename, "rt") as inp, open(path+"tmp/"+filename, "wt") as out:
            writer = csv.writer(out)
            print("reading file: " + filename)
            for row in csv.reader(inp):
                if row[3]!="Broadcast" and row[3]!="239.255.102.18" and \
                row[3]!="255.255.255.255" and row[3]!="ff02::c" and row[3]!="239.255.255.250" and row[4]!="ARP" and row[4]!="BJNP" and \
                row[4]!="BROWSER" and row[4]!="DHCP" and row[4]!="DHCPv6" and row[4]!="DNS" and row[4]!="HomePlug AV" and row[4]!="ICMP" and \
                row[4]!="ICMPv6" and row[4]!="IGMPv3" and row[4]!="LLC" and row[4]!="LLMNR" and row[4]!="MDNS" and row[4]!="MBNS" and row[4]!="SSDP":
                    io=""
                    host=""
                    if row[2]=="LOCAL NAME":
                        io="o"
                        host=row[3]
                    elif row[3]=="LOCAL NAME":
                        io="i"
                        host=row[2]
                    print(host)
                    co2=(int(row[5]) * 0.000000000072 * 519) + (int(row[5]) * 0.000000000152 * 519)

                    new_row=(row[1][:16],host,io,row[5],co2)

                    writer.writerow(new_row)