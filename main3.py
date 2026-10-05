import json, csv
        
for q in "domains", "fileHashes", "ips", "processes":
    with open(f"csv/{q}.csv", "w", newline='') as file:
        csv.writer(file).writerow(["alertId", "machineId", "firstActivity", q]) 
        for i in json.load(open("incident.json", "r" ))["alerts"]:
            for x in i["entities"][q]:
                csv.writer(file).writerow([i["alertId"], i["machineId"], i["firstActivity"], x])