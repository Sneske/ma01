import csv
import json

with open("incident.json", "r" ) as f:
    data = json.load(f)


with open("csv/domains.csv", "w", newline='') as file:
    writer = csv.writer(file)
    writer.writerow("alertId", "machineId", "firstActivity", "domains") 
    for i in data["alerts"]:
        for x in i["entities"]["domains"]:
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


