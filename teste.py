file=open("pkcsm.csv")
for lineNumber,line in enumerate(file,1):
    listage=line.split(",")
    if line.find("Water")!=-1:
        value=listage[5].replace("\"", "")
        waterSolubility=float(value)
        if waterSolubility >-2:
            print("High Water solubility"+str(waterSolubility))
        elif -4 <=  waterSolubility <= -2:
            print("Moderate water solubility"+str(waterSolubility))
        else:
            print("Low water solubility"+str(waterSolubility))

