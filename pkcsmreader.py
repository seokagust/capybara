#!/usr/bin/python
# -*- coding: utf-8 -*-
import csv

def promptInput(prompt):
    try:
        return raw_input(prompt)  # Python 2 compat (rare)
    except NameError:
        return input(prompt)      # Python 3

file_input = promptInput("Nome do arquivo de entrada (com extensão .csv): ")
file_output = promptInput("Nome do arquivo de saída (com extensão .csv): ")
INPUT = file_input  # arquivo de entrada
OUTPUT = file_output  # arquivo de saída    
VALUE_INDEX = 5  # coluna que contém o valor nas linhas
PROPINDEX = 4 # coluna que contém o nome da propriedade

def parse_float(s):
    try:
        return float(s)
    except (ValueError, TypeError):
        return None

def normalize(s):
    return (s or "").strip().strip('"')

def classify(property_name, raw_value):
    prop = (property_name or "").lower()
    val = normalize(raw_value)

    if "water solubility" in prop:
        v = parse_float(val); 
        if v is None: return None
        if v > -2: return "High Water solubility"
        if -4 <= v <= -2: return "Moderate water solubility"
        return "Low water solubility"

    if "caco2 permeability" in prop:
        v = parse_float(val); 
        if v is None: return None
        return "High Caco2 Permeability" if v > 0.90 else "Low Caco2 Permeability"

    if "intestinal absorption (human)" in prop:
        v = parse_float(val); 
        if v is None: return None
        return "High Intestinal absorption (human)" if v > 30 else "Low Intestinal absorption (human)"

    if "skin permeability" in prop:
        v = parse_float(val); 
        if v is None: return None
        return "High Skin Permeability" if v > -2.5 else "Low Skin Permeability"

    if "p-glycoprotein substrate" in prop:
        return "Is a P-glycoprotein substrate" if val.lower() == "yes" else "Is not a P-glycoprotein substrate"

    if "p-glycoprotein i inhibitor" in prop:
        return "Is a P-glycoprotein I inhibitor" if val.lower() == "yes" else "Is not a P-glycoprotein I inhibitor"

    if "p-glycoprotein ii inhibitor" in prop:
        return "Is a P-glycoprotein II inhibitor" if val.lower() == "yes" else "Is not a P-glycoprotein II inhibitor"

    if "vdss (human)" in prop:
        v = parse_float(val); 
        if v is None: return None
        if v < -0.15: return "Low VDss (human)"
        if -0.15 <= v <= 0.45: return "Moderate VDss (human)"
        return "High VDss (human)"
    
    if "fraction unbound (human)" in prop:
        v = parse_float(val);
        if v is None: return None
        # v is expected to be the fraction bound/unbound value (0-1). Guard against None.
        fractionUnboundPercent = (1-v)*100
        if fractionUnboundPercent >= 99: return "Extremely high plasmatic protein binding (human)"
        if 99 > fractionUnboundPercent >= 90: return "High plasmatic protein binding (human)"
        if 90 > fractionUnboundPercent >= 70: return "Moderate plasmatic protein binding (human)"   
        return "Low plasmatic protein binding (human)"

    if "total clearance (human)" in prop:
        v = parse_float(val); 
        if v is None: return None
        if v < 500: return "Low Total clearance (human)"
        # corrected range: moderate between 500 and 1000
        if 500 <= v < 1000: return "Moderate Total clearance (human)"
        return "High Total clearance (human)"   
    
    if "Oral Rat Acute Toxicity (LD50)" in prop:    
        v = parse_float(val); 

        if v is None: return None
        if v < 5: return "  Extremaly high Oral Rat Acute Toxicity (LD50)"
        if 5 <= v < 50: return "  High Oral Rat Acute Toxicity (LD50)"
        if 50 <= v < 500: return "  Moderate Oral Rat Acute Toxicity (LD50)"
        if 500 <= v < 5000: return "  Low Oral Rat Acute Toxicity (LD50)"
        return "  Very Low Oral Rat Acute Toxicity (LD50)"   
    
# 5 mg kg-1 - extremely toxic
# 5-50 mg kg-1 - highly toxic
# 50-500 mg kg-1 - moderately toxic
# 500-5000 mg kg-1 - slightly toxic
# greater than 5000mg kg-1 - practically non toxic

    if "Oral Rat Chronic Toxicity (LD50)" in prop:
        v = parse_float(val);
        if v is None: return None
        chronicToxicityReal = 10 ** v
        if chronicToxicityReal < 5: return "Extremaly high Oral Rat"

    if "bbb permeability" in prop:
        v = parse_float(val); 
        if v is None: return None
        return "Can cross the BBB" if v > 0.3 else "Cannot cross the BBB"

    if "cns permeability" in prop:
        v = parse_float(val); 
        if v is None: return None
        return "Can cross the CNS" if v > -2 else "Cannot cross the CNS"

    # CYP related entries (substrates / inhibitors)
    cyps = [
        ("cyp2d6 substrate", "Is a CYP2D6 substrate", "Is not a CYP2D6 substrate"),
        ("cyp3a4 substrate", "Is a CYP3A4 substrate", "Is not a CYP3A4 substrate"),
        ("cyp1a2 inhibitior", "Is a CYP1A2 inhibitior", "Is not a CYP1A2 inhibitior"),
        ("cyp2c19 inhibitior", "Is a CYP2C19 inhibitior", "Is not a CYP2C19 inhibitior"),
        ("cyp2c9 inhibitior", "Is a CYP2C9 inhibitior", "Is not a CYP2C9 inhibitior"),
        ("cyp2d6 inhibitior", "Is a CYP2D6 inhibitior", "Is not a CYP2D6 inhibitior"),
        ("cyp3a4 inhibitior", "Is a CYP3A4 inhibitior", "Is not a CYP3A4 inhibitior"),
    ]
    for key, yes_label, no_label in cyps:
        if key in prop:
            return yes_label if val.lower() == "yes" else no_label

    if "renal oct2 substrate" in prop:
        return "Is a Renal OCT2 substrate" if val.lower() == "yes" else "Is not a Renal OCT2 substrate"

    if "ames toxicity" in prop:
        return "Is AMES toxic" if val.lower() == "yes" else "Is not AMES toxic"

    if "max. tolerated dose (human)" in prop:
        v = parse_float(val)
        if v is None: return None
        if v < 0.477: return "Low Max. tolerated dose (human)"
        if 0.477 <= v <= 0.903: return "Moderate Max. tolerated dose (human)"
        return "High Max. tolerated dose (human)"

    if "herg i inhibitor" in prop or "herg i" in prop:
        return "Is a hERG I inhibitor" if val.lower() == "yes" else "Is not a hERG I inhibitor"

    if "herg ii inhibitor" in prop or "herg ii" in prop:
        return "Is a hERG II inhibitor" if val.lower() == "yes" else "Is not a hERG II inhibitor"

    if "hepatotoxicity" in prop:
        return "Is Hepatotoxic" if val.lower() == "yes" else "Is not Hepatotoxic"

    if "skin sensitisation" in prop:
        return "Is Skin Sensitiser" if val.lower() == "yes" else "Is not Skin Sensitiser"

    if "t.pyriformis toxicity" in prop:
        v = parse_float(val)
        if v is None: return None
        return "High T.Pyriformis toxicity" if v > -0.5 else "Low T.Pyriformis toxicity"

    if "minnow toxicity" in prop:
        v = parse_float(val)
        if v is None: return None
        return "High Minnow toxicity" if v > -0.3 else "Low Minnow toxicity"

    return None

def process_file(input_path, output_path):
    with open(input_path, "r") as f:
        lines = f.readlines()

    new_lines = []
    for raw_line in lines:
        # usa csv.reader para respeitar aspas e vírgulas internas
        try:
            row = next(csv.reader([raw_line]))
        except Exception:
            row = []
        prop = row[PROPINDEX] if len(row) > PROPINDEX else ""
        val = row[VALUE_INDEX] if len(row) > VALUE_INDEX else ""
        label = classify(prop, val)

        new_line = ""   

        if label:
            new_line = raw_line.strip() + " , " + label + "\n"
            print(new_line)
        else:
            new_line = raw_line
        new_lines.append(new_line)

    with open(output_path, "w") as f:
        f.writelines(new_lines)

if __name__ == "__main__":

    process_file(INPUT, OUTPUT)