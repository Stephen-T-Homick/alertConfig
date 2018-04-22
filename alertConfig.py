#!/usr/bin/python
"""
Steve Homick

Python agentinfoQuery script.

This script will loop through each agent.alertConfig key on the device and parse the JSON.

- If wanting to output to a json do `python alertConfig.py >> foobar.json`

"""

import glob
import json
import os
import subprocess
import sys

# Variables and such
alertConfigData = []
# uncomment once on a datto and remove descending line ->  mainDir = '/bdr/config/keys' 
mainDir = '/Users/shome/git_repos/alertConfig'
extension = ('*.alertConfig')

def main(alertConfigs):
        
        print alertConfigs

        
        

"""
if os.geteuid() != 0:
        print("Got root/sudo ? \n \n Exiting")
        sys.exit()
"""
try:
        os.chdir(mainDir)
        print("alertConfig file listing(JSON):\n")
        for alertConfigs in glob.glob(extension):
                alertConfigData.append(alertConfigs)
                #with open(alertConfigs,'w') as config:
                        
        #device_json = 
        deviceList = json.dumps(alertConfigData,indent=6, sort_keys = True)
        #keys = 
        main(deviceList) # Call main function

except OSError:

        print("%r not an accessible directory \n") % (mainDir)
        print("Make sure this is a bdr appliance")
