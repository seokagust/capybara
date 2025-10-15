print("helloworld")
arquivo=open("pkcsm.csv")
for linha in arquivo:
    lista=linha.split(",")
    if linha.find("Water solubility"):
        waterSolubility=float(lista[5])
        if waterSolubility >-2:
            print("High Water solubility")
        elif -4 <=  waterSolubility <= -2:
            print("Moderate water solubility")
        else:
            print("Low water solubility")
        print (linha) 





    elif linha.find("Caco2 permeability"):
        print (linha)
    elif linha.find("Intestinal absorption (human)"):
        print (linha)
    elif linha.find("Intestinal absorption (human)"):
        print (linha)
    elif linha.find("Skin Permeability"):
        print (linha)
    elif linha.find("P-glycoprotein substrate"):
        print (linha)
    elif linha.find("P-glycoprotein II inhibitor"):
        print(linha)
    elif linha.find("VDss (human)"):
        print(linha)
    elif linha.find("Fraction unbound (human)"):
        print(linha)
    elif linha.find("BBB permeability"):
        print(linha)
    elif linha.find("CNS permeability"):
        print(linha)
    elif linha.find("CYP2D6 substrate"):
        print(linha)
    elif linha.find("CYP3A4 substrate"):
        print(linha)
    elif linha.find("CYP1A2 inhibitior"):
        print(linha)
    elif linha.find("CYP2C19 inhibitior"):
        print(linha)
    elif linha.find("CYP2C9 inhibitior"):
        print(linha)
    elif linha.find("CYP2D6 inhibitior"):
        print(linha)
    elif linha.find("Total Clearance"):
        print(linha)
    elif linha.find("Renal OCT2 substrate"):
        print(linha)
    elif linha.find("AMES toxicity"):
        print(linha)
    elif linha.find("Max. tolerated dose (human)"):
        print(linha)
    elif linha.find("Toxicity,hERG I inhibitor"):
        print(linha)
    elif linha.find("Toxicity,Oral Rat Acute Toxicity (LD50)"):
        print(linha)
    elif linha.find("Toxicity,Oral Rat Chronic Toxicity (LOAEL)"):
        print(linha)
    elif linha.find("Toxicity,Hepatotoxicity"):
        print(linha)
    elif linha.find("Toxicity,Skin Sensitisation"):
        print(linha)
    elif linha.find("Toxicity,T.Pyriformis toxicity"):
        print(linha)
    elif linha.find("Toxicity,Minnow toxicity"):
        print(linha)











