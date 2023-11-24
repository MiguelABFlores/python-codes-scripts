#!/usr/bin/env python3
# ------------------------------------------------------------------------------
"""
Instructions:
Create a script that accepts the file name and puts its extension to output. 
If there is no extension - an exception should be raised.
"""
# ------------------------------------------------------------------------------
import os
import glob
import pathlib  
from pathlib import Path
# ------------------------------------------------------------------------------
def File_Validation():
    files = glob.glob(str(filename)+".*")
    if bool(files)!=1:
        files = glob.glob(str(filename))
    if bool(files):
        filetoext = files[0]
        File_Extension(filetoext)
    else:
        files = glob.glob(filename)
        if bool(files):
            print("File does not have an extension, but exists.")
        else:
            print("File does not exist in current directoy.")

def File_Extension(filetoext):
    file_extension = pathlib.Path(str(filetoext)).suffix
    if file_extension != "":
        print("File Extension:", file_extension)
    else:
        print("File "+str(filetoext)+" exists but does not have an extension.")
    
# ------------------------------------------------------------------------------
os.system('clear')
print("This script will help you find if a file exists and its extension.")
filename = input("Enter the file name: ")
cwd = os.getcwd()
File_Validation()