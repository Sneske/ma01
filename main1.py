import csv
import json

with open("incident.json", "r" ) as f:
    data = json.load(f)


#der er lavet en "with, open, as" for hver dokument der skal oprettes
#åbner csv dokumentet i "write mode" og angiver dokumentet en variable ved navn "file"
with open("csv/domains.csv", "w", newline='') as file:
    #bruger funktionen csv med methoden writer, der angiver hvilken type dokument der er tale om og at man gerne ville skrive til csv'en 
    writer = csv.writer(file)
    #laver den første række i csv'en med givende værdier "alertId", "machineId", "firstActivity", "domains"
    writer.writerow("alertId", "machineId", "firstActivity", "domains") 
    #tager ALT data fra json dokumentet og looper igennem alt data inde i alerts dictionary.
    for i in data["alerts"]:
         # der laves et andet loop som går igennem alle værdier (values) fra domains inde i dictionary'en entities
        for x in i["entities"]["domains"]:
            #her skrives en ny række for hver domain (i dette tilfælde)
            writer.writerow([i["alertId"], i["machineId"], i["firstActivity"], x])

with open("csv/fileHashes.csv", "w", newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["alertId", "machineId", "firstActivity", "fileHashes"]) 
    for i in data["alerts"]:
        for x in i["entities"]["fileHashes"]:
            writer.writerow([i["alertId"], i["machineId"], i["firstActivity"], x])

with open("csv/ips.csv", "w", newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["alertId", "machineId", "firstActivity", "ips"]) 
    for i in data["alerts"]:
        for x in i["entities"]["ips"]:
            writer.writerow([i["alertId"], i["machineId"], i["firstActivity"], x])

with open("csv/processes.csv", "w", newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["alertId", "machineId", "firstActivity", "processes"]) 
    for i in data["alerts"]:
        for x in i["entities"]["processes"]:
            writer.writerow([i["alertId"], i["machineId"], i["firstActivity"], x])


