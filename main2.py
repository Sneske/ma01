import csv
import json

with open("incident.json", "r" ) as f:
    data = json.load(f)

entries = ["domains", "fileHashes", "ips", "processes"]

for q in entries:
    with open(f"csv/{q}.csv", "w", newline='') as file:
        writer = csv.writer(file)
        writer.writerow("alertId", "machineId", "firstActivity", q) 
        for i in data["alerts"]:
            for ip in i["entities"][q]:
                writer.writerow([i["alertId"], i["machineId"], i["firstActivity"], ip])


