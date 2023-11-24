#!/bin/usr/env python3.6

import time
from time import localtime, mktime, strftime

# Importing time library
# start_time = time.localtime()
# print(f"Timer started at {time.strftime('%X', start_time)}")
# Only importing what we are going to use from a library
start_time = localtime()
print(f"Timer started at {strftime('%X', start_time)}")

# Importing time library
# Wait for user to stop timer
# input("Press 'Enter' to stop timer ")

# stop_time = time.localtime()
# difference = time.mktime(stop_time) - time.mktime(start_time)

# print(f"Timer stopped at {time.strftime('%X', stop_time)}")
# print(f"Total time: {difference} seconds")

# Only importing what we are going to use from a library
# Wait for user to stop timer¬
input("Press 'Enter' to stop timer ")

stop_time = localtime()
difference = mktime(stop_time) - mktime(start_time)
 
print(f"Timer stopped at {strftime('%X', stop_time)}")
print(f"Total time: {difference} seconds") 
