#!/usr/bin/env python3
# ------------------------------------------------------------------------------
"""
Instructions:
Create a script that reads the access log from a file. 
The name of the file is provided as an argument. 
An output of the script should provide the total number of different 
User Agents and then provide statistics with the number of requests from 
each of them. Here is a link to an example access.log file.
"""
# ------------------------------------------------------------------------------
import os
import re
# import numpy as np
from collections import Counter
# ------------------------------------------------------------------------------
def Find_UserAgents():
    completeuserlist = []
    with open(str(logfile), 'r') as file:
        fi = file.readlines()
    re_ip = re.compile("\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}")
    for line in fi:
        ip = re.findall(re_ip,line)
        completeuserlist.append(str(ip))
    new_usr_list = list(dict.fromkeys(completeuserlist))
    Print_Lists(new_usr_list, completeuserlist)

def Print_Lists(new_usr_list, completeuserlist):
    # new_usr_list = np.array(new_usr_list)
    # result = np.transpose(new_usr_list)
    # for i in result:
    #     print("User: " + str(i), "\nActions: ", elements)
    userscount = Counter(completeuserlist)
    print("Total actions: ", userscount.total(),"\nUsers:", userscount)
    # list(userscount)

# ------------------------------------------------------------------------------
os.system('clear')
print("This script will check a log file, check number of user agents and provide statistics with number of requests.")
# logfile = input("Which file you want to check?\n")
logfile = "access.log.5"
Find_UserAgents()