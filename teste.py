file=open("pkcsm.csv","r")
linesReplacing=file.readlines()
file.seek(0)    
for lineNumber,line in enumerate(file,1):
    listage=line.split(",")
    value=listage[5].replace("\"", "")
    linesReplacing[lineNumber-1]=line 

    if line.find("Water solubility")!=-1:
        waterSolubility=float(value)

        if waterSolubility >-2:
            print("High Water solubility")
            linesReplacing[lineNumber-1]=line.strip()+" , High Water solubility\n"       
        elif -4 <=  waterSolubility <= -2:
            print("Moderate water solubility")
            linesReplacing[lineNumber-1]=line.strip()+" , Moderate water solubility\n"
        else:
            print("Low water solubility")
            linesReplacing[lineNumber-1]=line.strip()+" , Low water solubility\n"
    elif line.find("Caco2 permeability")!=-1:
        caco2Permeability=float(value)
        if caco2Permeability > 0.90:
            print("High Caco2 Permeability")
            linesReplacing[lineNumber-1]=line.strip()+" , High Caco2 Permeability\n"
        else:
            print("Low Caco2 Permeability")
            linesReplacing[lineNumber-1]=line.strip()+" , Low Caco2 Permeability\n"

    elif line.find("Intestinal absorption (human)")!=-1:
        intestinalAbsorptionHuman=float(value)
        if intestinalAbsorptionHuman > 30:
            print("High Intestinal absorption (human)")
            linesReplacing[lineNumber-1]=line.strip()+" , High Intestinal absorption (human)\n"
        else:
            print("Low Intestinal absorption (human)")
            linesReplacing[lineNumber-1]=line.strip()+" , Low Intestinal absorption (human)\n"
    elif line.find("Skin Permeability")!=-1:
        skinPermeability=float(value)
        if skinPermeability > -2.5:
            print("High Skin Permeability")
            linesReplacing[lineNumber-1]=line.strip()+" , High Skin Permeability\n"   
        else:
            print("Low Skin Permeability")
            linesReplacing[lineNumber-1]=line.strip()+" , Low Skin Permeability\n"

    elif line.find("P-glycoprotein substrate")!=-1:
        pglycoproteinSubstrate=value
        if pglycoproteinSubstrate=="Yes":
            print("Is a P-glycoprotein substrate")
            linesReplacing[lineNumber-1]=line.strip()+" , Is a P-glycoprotein substrate\n"
        else:
            print("Is not a P-glycoprotein substrate")
            linesReplacing[lineNumber-1]=line.strip()+" , Is not a P-glycoprotein substrate\n"

    elif line.find("P-glycoprotein I inhibitor")!=-1:
        if value=="Yes":
            print("Is a P-glycoprotein I inhibitor")
            linesReplacing[lineNumber-1]=line.strip()+" , Is a P-glycoprotein I inhibitor\n"   
        else:
            print("Is not a P-glycoprotein I inhibitor")
            linesReplacing[lineNumber-1]=line.strip()+" , Is not a P-glycoprotein I inhibitor\n"

    elif line.find("P-glycoprotein II inhibitor")!=-1:
        if value=="Yes":
            print("Is a P-glycoprotein II inhibitor")
            linesReplacing[lineNumber-1]=line.strip()+" , Is a P-glycoprotein II inhibitor\n"  
        else:
            print("Is not a P-glycoprotein II inhibitor")
            linesReplacing[lineNumber-1]=line.strip()+" , Is not a P-glycoprotein II inhibitor\n" 
        
    elif line.find("VDss (human)")!=-1:
        vdssHuman=float(value)
        if vdssHuman < -0.15:
            print("Low VDss (human)")
            linesReplacing[lineNumber-1]=line.strip()+" , Low VDss (human)\n"
        elif -0.15 <= vdssHuman <= 0.45:
            print("Moderate VDss (human)")
            linesReplacing[lineNumber-1]=line.strip()+" , Moderate VDss (human)\n"
        else:
            print("High VDss (human)")  
            linesReplacing[lineNumber-1]=line.strip()+" , High VDss (human)\n"

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
            linesReplacing[lineNumber-1]=line.strip()+" , Can cross the BBB\n"
        else:
            print("Cannot cross the BBB")
            linesReplacing[lineNumber-1]=line.strip()+" , Cannot cross the BBB\n"

    elif line.find("CNS permeability")!=-1:
        cnsPermeability=float(value)
        if cnsPermeability > -2:
            print("Can cross the CNS")
            linesReplacing[lineNumber-1]=line.strip()+" , Can cross the CNS\n"
        else:
            print("Cannot cross the CNS")
            linesReplacing[lineNumber-1]=line.strip()+" , Cannot cross the CNS\n"


    elif line.find("CYP2D6 substrate")!=-1:
        if value=="Yes":
            print("Is a CYP2D6 substrate")  
            linesReplacing[lineNumber-1]=line.strip()+" , Is a CYP2D6 substrate\n" 
        else:
            print("Is not a CYP2D6 substrate")  
            linesReplacing[lineNumber-1]=line.strip()+" , Is not a CYP2D6 substrate\n"
    elif line.find("CYP3A4 substrate")!=-1:
        if value=="Yes":
            print("Is a CYP3A4 substrate")  
            linesReplacing[lineNumber-1]=line.strip()+" , Is a CYP3A4 substrate\n" 
        else:
            print("Is not a CYP3A4 substrate")
            linesReplacing[lineNumber-1]=line.strip()+" , Is not a CYP3A4 substrate\n"  

    elif line.find("CYP1A2 inhibitior")!=-1:
        if value=="Yes":
            print("Is a CYP1A2 inhibitior")
            linesReplacing[lineNumber-1]=line.strip()+" , Is a CYP1A2 inhibitior\n"      
        else:
            print("Is not a CYP1A2 inhibitior")
            linesReplacing[lineNumber-1]=line.strip()+" , Is not a CYP1A2 inhibitior\n" 

    elif line.find("CYP2C19 inhibitior")!=-1:
        if value=="Yes":
            print("Is a CYP2C19 inhibitior")
            linesReplacing[lineNumber-1]=line.strip()+" , Is a CYP2C19 inhibitior\n"   
        else:
            print("Is not a CYP2C19 inhibitior")
            linesReplacing[lineNumber-1]=line.strip()+" , Is not a CYP2C19 inhibitior\n"    

    elif line.find("CYP2C9 inhibitior")!=-1:
        if value=="Yes":
            print("Is a CYP2C9 inhibitior")
            linesReplacing[lineNumber-1]=line.strip()+" , Is a CYP2C9 inhibitior\n"   
        else:
            print("Is not a CYP2C9 inhibitior")
            linesReplacing[lineNumber-1]=line.strip()+" , Is not a CYP2C9 inhibitior\n" 

    elif line.find("CYP2D6 inhibitior")!=-1:
        if value=="Yes":
            print("Is a CYP2D6 inhibitior")
            linesReplacing[lineNumber-1]=line.strip()+" , Is a CYP2D6 inhibitior\n"   
        else:
            print("Is not a CYP2D6 inhibitior")
            linesReplacing[lineNumber-1]=line.strip()+" , Is not a CYP2D6 inhibitior\n"

    elif line.find("CYP3A4 inhibitior")!=-1:
        if value=="Yes":
            print("Is a CYP3A4 inhibitior")
            linesReplacing[lineNumber-1]=line.strip()+" , Is a CYP3A4 inhibitior\n"   
        else:
            print("Is not a CYP3A4 inhibitior")
            linesReplacing[lineNumber-1]=line.strip()+" , Is not a CYP3A4 inhibitior\n"

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
            linesReplacing[lineNumber-1]=line.strip()+" , Is a Renal OCT2 substrate\n"   
        else:
            print("Is not a Renal OCT2 substrate") 
            linesReplacing[lineNumber-1]=line.strip()+" , Is not a Renal OCT2 substrate\n"

    elif line.find("AMES toxicity")!=-1:
        if value=="Yes":
            print("Is AMES toxic")
            linesReplacing[lineNumber-1]=line.strip()+" , Is AMES toxic\n"   
        else:
            print("Is not AMES toxic")
            linesReplacing[lineNumber-1]=line.strip()+" , Is not AMES toxic\n"

    elif line.find("Max. tolerated dose (human)")!=-1:
        maxToleratedDoseHuman=float(value)
        if maxToleratedDoseHuman < 0.477:
            print("Low Max. tolerated dose (human)")
            linesReplacing[lineNumber-1]=line.strip()+" , Low Max. tolerated dose (human)\n"
        elif 0.477 <= maxToleratedDoseHuman <= 0.903:
            print("Moderate Max. tolerated dose (human)")  
        else:
            print("High Max. tolerated dose (human)")
            linesReplacing[lineNumber-1]=line.strip()+" , High Max. tolerated dose (human)\n"

    elif line.find("hERG I inhibitor")!=-1:
        if value=="Yes":
            print("Is a hERG I inhibitor") 
            linesReplacing[lineNumber-1]=line.strip()+" , Is a hERG I inhibitor\n"  
        else:
            print("Is not a hERG I inhibitor")
            linesReplacing[lineNumber-1]=line.strip()+" , Is not a hERG I inhibitor\n"  

    elif line.find("hERG II inhibitor")!=-1:
        if value=="Yes":
            print("Is a hERG II inhibitor")
            linesReplacing[lineNumber-1]=line.strip()+" , Is a hERG II inhibitor\n"  
        else:
            print("Is not a hERG II inhibitor")
            linesReplacing[lineNumber-1]=line.strip()+" , Is not a hERG II inhibitor\n" 

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
            linesReplacing[lineNumber-1]=line.strip()+" , Is Hepatotoxic\n"  
        else:
            print("Is not Hepatotoxic") 
            linesReplacing[lineNumber-1]=line.strip()+" , Is not Hepatotoxic\n"

    elif line.find("Skin Sensitisation")!=-1:
        if value=="Yes":
            print("Is Skin Sensitiser")
            linesReplacing[lineNumber-1]=line.strip()+" , Is Skin Sensitiser\n"   
        else:
            print("Is not Skin Sensitiser") 
            linesReplacing[lineNumber-1]=line.strip()+" , Is not Skin Sensitiser\n"


    elif line.find("T.Pyriformis toxicity")!=-1:    
        tPyriformisToxicity=float(value)
        if tPyriformisToxicity > -0.5:
            print("High T.Pyriformis toxicity")
            linesReplacing[lineNumber-1]=line.strip()+" , High T.Pyriformis toxicity\n"
        else:
            print("Low T.Pyriformis toxicity")
            linesReplacing[lineNumber-1]=line.strip()+" , Low T.Pyriformis toxicity\n"

    elif line.find("Minnow toxicity")!=-1:
        minnowToxicity=float(value)
        if minnowToxicity > -0.3:
            print("High Minnow toxicity")
            linesReplacing[lineNumber-1]=line.strip()+" , High Minnow toxicity\n"
        else:
            print("Low Minnow toxicity")
            linesReplacing[lineNumber-1]=line.strip()+" , Low Minnow toxicity\n"    
    
    print(linesReplacing[lineNumber-1])
file.close()
file=open("pkcsm2.csv","w")
for line in linesReplacing:
    file.write(line)
file.close()