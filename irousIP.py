#!/usr/bin/env python3

# imports
import argparse
import requests, json
import sys
from sys import argv
import os
from termcolor import colored

print (colored("""'


  _____ _____   ____  _    _  _____     _____ _____  
 |_   _|  __ \ / __ \| |  | |/ ____|   |_   _|  __ \ 
   | | | |__) | |  | | |  | | (___ ______| | | |__) |
   | | |  _  /| |  | | |  | |\___ \______| | |  ___/ 
  _| |_| | \ \| |__| | |__| |____) |    _| |_| |     
 |_____|_|  \_\\____/ \____/|_____/     |_____|_|     
                                           
                                           
                             :CP THE VIRUS
                                          IG- @jblfxe
                                                     



    
      """, 'green'))

# parser
parser = argparse.ArgumentParser()

parser.add_argument("-v", help="target/host IP address", type=str, dest='target', required=True)

args = parser.parse_args()


# colors
red = '\033[31m'
yellow = '\033[93m'
lgreen = '\033[92m'
clear = '\033[0m'
bold = '\033[01m'
cyan = '\033[96m'

# banner
def banner():
    print (red+"IROUS-IP")


banner()

ip = args.target

api = "http://ip-api.com/json/"

try:
        data = requests.get(api+ip).json()
        sys.stdout.flush()
        a = lgreen+bold+"[$]"
        b = cyan+bold+"[$]"
        print (a, "[Victim]:", data['query'])
        print(red+"<--------------->"+red)
        print (b, "[ISP]:", data['isp'])
        print(red+"<--------------->"+red)
        print (a, "[Organisation]:", data['org'])
        print(red+"<--------------->"+red)
        print (b, "[City]:", data['city'])
        print(red+"<--------------->"+red)
        print (a, "[Region]:", data['region'])
        print(red+"<--------------->"+red)
        print (b, "[Longitude]:", data['lon'])
        print(red+"<--------------->"+red)
        print (a, "[Latitude]:", data['lat'])
        print(red+"<--------------->"+red)
        print (b, "[Time zone]:", data['timezone'])
        print(red+"<--------------->"+red)
        print (a, "[Zip code]:", data['zip'])
        print (" "+yellow)

except KeyboardInterrupt:
        print ('Terminating, Bye'+lgreen)
        sys.exit(0)
except requests.exceptions.ConnectionError as e:
        print (red+"[~]"+" check your internet connection!"+clear)
sys.exit(1)