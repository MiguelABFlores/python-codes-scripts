#!/usr/bin/env python3
# ------------------------------------------------------------------------------
"""
Instructions:
Write a script that gets system information like distro info, 
memory(total, used, free), CPU info (model, core numbers, speed), 
current user, system load average, and IP address. Use arguments for 
specifying resources. (For example, -d for distro -m for memory, -c for 
CPU, -u for user info, -l for load average, -i for IP address).
"""
# ------------------------------------------------------------------------------
import os
import platform
import argparse
import psutil
import getpass
import socket
# ------------------------------------------------------------------------------
def Get_Arguments():
    parser.add_argument('--distro', '-d', action='store_const', const=1, default=0, help='Distro information.')
    parser.add_argument("-m", "--memory", action='store_const', const=1, default=0, help="System memory information (total, used, free).")
    parser.add_argument("-c", "--cpu", action='store_const', const=1, default=0, help="CPU information (model, core numbers, speed).")
    parser.add_argument("-u", "--user", action='store_const', const=1, default=0, help="Current User.")
    parser.add_argument("-l", "--load", action='store_const', const=1, default=0, help="System Load Average.")
    parser.add_argument("-i", "--ip", action='store_const', const=1, default=0, help="IP Address.")
    args = vars(parser.parse_args())

    distro = args["distro"]
    memory = args["memory"]
    cpu = args["cpu"]
    user = args["user"]
    load = args["load"]
    ip = args["ip"]

    if distro == 1:
        distro1 = platform.system()
        distro2 = platform.machine()
        distro3 = platform.version()
        distro4 = platform.platform()
        print("Distro:",distro1,distro2,distro3,distro4,sep=os.linesep)
        print('-'*100)
    if memory == 1:
        mem = psutil.virtual_memory()
        print("Memory:",str(mem)+"Bytes",sep=os.linesep)
        print('-'*100)
    if cpu == 1:
        cpux = psutil.cpu_times()
        cpucount = psutil.cpu_count()
        cpufreq = psutil.cpu_freq()
        cpumodel = platform.processor()
        print("CPU:","Model: "+str(cpumodel),cpux,"Cores: "+str(cpucount),cpufreq,sep=os.linesep)
        print('-'*100)
        if user == 1:
            userx = getpass.getuser()
            print("Current user: ",userx,sep=os.linesep)
            print('-'*100)
    if load == 1:
        sysload = [x / psutil.cpu_count() * 100 for x in psutil.getloadavg()]
        print("System Load Average:","Every 1, 5 and 10 minutes.",str(sysload)+" %",sep=os.linesep)
        print('-'*100)
    if ip == 1:
        hostname = socket.gethostname()
        ip_address = socket.gethostbyname(hostname)
        print("Network Information:","Hostname: "+str(hostname),"IP Address: "+str(ip_address),sep=os.linesep)
        print('-'*100)
# ------------------------------------------------------------------------------
os.system('clear')
parser = argparse.ArgumentParser(description='This script can get system information for you.')
Get_Arguments()