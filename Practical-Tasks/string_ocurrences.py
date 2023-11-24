#!/usr/bin/env python3
# ------------------------------------------------------------------------------
"""
Instructions:
Given an input string, count occurrences of all characters within a 
string (e.g. pythonnohtyppy -> p:3, y:3, t:2, h:2, o:2, n:2).
"""
# ------------------------------------------------------------------------------
import os
from collections import Counter
# ------------------------------------------------------------------------------
def Ocurrences():
    ocurrences = Counter(magicword)
    print(ocurrences)
# ------------------------------------------------------------------------------
os.system('clear')
print("This script will count total ocurrences within a string.")
magicword = input("Choose your word: ")
Ocurrences()
