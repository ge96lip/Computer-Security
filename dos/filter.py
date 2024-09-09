#!/usr/bin/env python3
# Cycle detection to prevent huge memory alloction 

def filter_text(text):
    # dict with rules 
    rules = {}
    
    for line in text.split("\n"):
        # find rules -> lines starting with # 
        if line.startswith("#"):
            # remove spaces
            (k, v) = map(str.strip, line[1:].split("="))
            rules[k] = v
            
    # look for cycling dependencies
    for key in rules:
        for value in rules.values():
            # key is in value -> would lead to infinite replacements 
            if key in value:
                return False
    return True 
