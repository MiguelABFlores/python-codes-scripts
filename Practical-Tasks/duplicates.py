#!/usr/bin/env python3
# ------------------------------------------------------------------------------
"""
Instructions:
Given a list of integers. Remove duplicates from the list and create a tuple. 
Find the minimum and maximum number.
"""
# ------------------------------------------------------------------------------
import os
# ------------------------------------------------------------------------------
def Remove_Duplicates():
    new_usr_list = list(dict.fromkeys(usr_list))
    new_tuple = tuple(list(dict.fromkeys(usr_list)))
    print("Your initial list:", usr_list)
    print("Your list without duplicates:", new_usr_list)
    print("Your new tuple:", new_tuple)
    Find_MinMaxValues(new_tuple)

def Find_MinMaxValues(newlist):
    minvalue = min(newlist)
    maxvalue = max(newlist)
    print("Minimum value:", minvalue, "\nMaximum value:", maxvalue)
# ------------------------------------------------------------------------------
os.system('clear')
print("This script will help you remove duplicated items from a list and create a tuple.\nAlso to find the minimum and maximum values.")
nElements = int(input("Enter number of elements : "))

usr_list = []
for i in range(0, nElements):
    os.system('clear')
    element = int(input("Element "+str(i+1)+": "))
    usr_list.append(element)

Remove_Duplicates()