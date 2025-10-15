file=open("pkcsm.csv")
for lineNumber,line in enumerate(file,1):
    listage=line.split(",")
    value=listage[5].replace("\"", "")

    if line.find("Water solubility")!=-1:
        waterSolubility=float(value)

        if waterSolubility >-2:
            print("High Water solubility")
        elif -4 <=  waterSolubility <= -2:
            print("Moderate water solubility")
        else:
            print("Low water solubility")

    elif line.find("Caco2 permeability")!=-1:
        caco2Permeability=float(value)
        if caco2Permeability > 0.90:
            print("High Caco2 Permeability")
        else:
            print("Low Caco2 Permeability")
       

    elif line.find("Intestinal absorption (human)")!=-1:
        intestinalAbsorptionHuman=float(value)
        if intestinalAbsorptionHuman > 30:
            print("High Intestinal absorption (human)")
        else:
            print("Low Intestinal absorption (human)")

    elif line.find("Skin Permeability")!=-1:
        skinPermeability=float(value)
        if skinPermeability > -2.5:
            print("High Skin Permeability")
        else:
            print("Low Skin Permeability")

    elif line.find("P-glycoprotein substrate")!=-1:
        pglycoproteinSubstrate=value
        if pglycoproteinSubstrate=="Yes":
            print("Is a P-glycoprotein substrate")
        else:
            print("Is not a P-glycoprotein substrate")

    elif line.find("P-glycoprotein I inhibitor")!=-1:
        if value=="Yes":
            print("Is a P-glycoprotein I inhibitor")   
        else:
            print("Is not a P-glycoprotein I inhibitor")

    elif line.find("P-glycoprotein II inhibitor")!=-1:
        if value=="Yes":
            print("Is a P-glycoprotein II inhibitor")   
        else:
            print("Is not a P-glycoprotein II inhibitor")
        
    elif line.find("VDss (human)")!=-1:
        vdssHuman=float(value)
        if vdssHuman < -0.15:
            print("Low VDss (human)")
        elif -0.15 <= vdssHuman <= 0.45:
            print("Moderate VDss (human)")
        else:
            print("High VDss (human)")  

    # elif line.find("Fraction unbound (human)")!=-1:
    #     fractionUnboundHuman=float(value)
    #     if fractionUnboundHuman < 0.01:                     
    #         print("Low Fraction unbound (human)")
    #     elif 0.01 <= fractionUnboundHuman <= 0.1:
    #         print("Moderate Fraction unbound (human)")  

    elif line.find("BBB permeability")!=-1:
        bbbPermeability=float(value)
        if bbbPermeability > 0.3:
            print("Can cross the BBB")
        else:
            print("Cannot cross the BBB")

    elif line.find("CNS permeability")!=-1:
        cnsPermeability=float(value)
        if cnsPermeability > -2:
            print("Can cross the CNS")
        else:
            print("Cannot cross the CNS")


    elif line.find("CYP2D6 substrate")!=-1:
        if value=="Yes":
            print("Is a CYP2D6 substrate")   
        else:
            print("Is not a CYP2D6 substrate")  

    elif line.find("CYP3A4 substrate")!=-1:
        if value=="Yes":
            print("Is a CYP3A4 substrate")   
        else:
            print("Is not a CYP3A4 substrate")  

    elif line.find("CYP1A2 inhibitior")!=-1:
        if value=="Yes":
            print("Is a CYP1A2 inhibitior")   
        else:
            print("Is not a CYP1A2 inhibitior") 

    elif line.find("CYP2C19 inhibitior")!=-1:
        if value=="Yes":
            print("Is a CYP2C19 inhibitior")   
        else:
            print("Is not a CYP2C19 inhibitior")    

    elif line.find("CYP2C9 inhibitior")!=-1:
        if value=="Yes":
            print("Is a CYP2C9 inhibitior")   
        else:
            print("Is not a CYP2C9 inhibitior") 

    elif line.find("CYP2D6 inhibitior")!=-1:
        if value=="Yes":
            print("Is a CYP2D6 inhibitior")   
        else:
            print("Is not a CYP2D6 inhibitior") 

    # elif line.find("Total Clearance")!=-1:
    #     totalClearance=float(value)
    #     if totalClearance < 0.5:
    #         print("Low Total Clearance")
    #     elif 0.5 <= totalClearance <= 2:
    #         print("Moderate Total Clearance")
    #     else:
    #         print("High Total Clearance")   

    elif line.find("Renal OCT2 substrate")!=-1:
        if value=="Yes":
            print("Is a Renal OCT2 substrate")   
        else:
            print("Is not a Renal OCT2 substrate")  

    elif line.find("AMES toxicity")!=-1:
        if value=="Yes":
            print("Is AMES toxic")   
        else:
            print("Is not AMES toxic")

    elif line.find("Max. tolerated dose (human)")!=-1:
        maxToleratedDoseHuman=float(value)
        if maxToleratedDoseHuman < 0.477:
            print("Low Max. tolerated dose (human)")
        elif 0.477 <= maxToleratedDoseHuman <= 0.903:
            print("Moderate Max. tolerated dose (human)")  
        else:
            print("High Max. tolerated dose (human)")

    elif line.find("hERG I inhibitor")!=-1:
        if value=="Yes":
            print("Is a hERG I inhibitor")   
        else:
            print("Is not a hERG I inhibitor")  

    elif line.find("hErg II inhibitor")!=-1:
        if value=="Yes":
            print("Is a hERG II inhibitor")   
        else:
            print("Is not a hERG II inhibitor") 

    # elif line.find("Oral Rat Acute Toxicity (LD50)")!=-1:
    #     oralRatAcuteToxicityLD50=float(value)
    #     if oralRatAcuteToxicityLD50 < 2.0:
    #         print("High Oral Rat Acute Toxicity (LD50)")
    #     elif 2.0 <= oralRatAcuteToxicityLD50 <= 3.5:
    #         print("Moderate Oral Rat Acute Toxicity (LD50)")  
    #     else:
    #         print("Low Oral Rat Acute Toxicity (LD50)") 


    # elif line.find("Oral Rat Chronic Toxicity (LOAEL)")!=-1:
    #     oralRatChronicToxicityLOAEL=float(value)
    #     if oralRatChronicToxicityLOAEL < 1.875:
    #         print("High Oral Rat Chronic Toxicity (LOAEL)")
    #     elif 1.875 <= oralRatChronicToxicityLOAEL <= 3.5:
    #         print("Moderate Oral Rat Chronic Toxicity (LOAEL)")  
    #     else:
    #         print("Low Oral Rat Chronic Toxicity (LOAEL)")  

    elif line.find("Hepatotoxicity")!=-1:
        if value=="Yes":
            print("Is Hepatotoxic")   
        else:
            print("Is not Hepatotoxic") 

    elif line.find("Skin Sensitisation")!=-1:
        if value=="Yes":
            print("Is Skin Sensitiser")   
        else:
            print("Is not Skin Sensitiser") 


    elif line.find("T.Pyriformis toxicity")!=-1:    
        tPyriformisToxicity=float(value)
        if tPyriformisToxicity > -0.5:
            print("High T.Pyriformis toxicity")
        else:
            print("Low T.Pyriformis toxicity")

    elif line.find("Minnow toxicity")!=-1:
        minnowToxicity=float(value)
        if minnowToxicity > -0.3:
            print("High Minnow toxicity")
        else:
            print("Low Minnow toxicity")    