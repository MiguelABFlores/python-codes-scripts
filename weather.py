#!/usr/bin/env python3.6

import os
import requests
import sys

from argparse import ArgumentParser

parser = ArgumentParser(descrition='Get the current weather information for your zipcode')
parser.add_argument('zip', help='zip/postal code to get weather for')
parser.add_argument('--country', default='us', help='country zip/postal belongs to, default is "us"')

args = parser.parse_args()

api_key = os.getenv("OWM_API_KEY")

if not api_key:
    print("Error: no 'OWN_API_KEY' provided")
    sys.exit(1)
