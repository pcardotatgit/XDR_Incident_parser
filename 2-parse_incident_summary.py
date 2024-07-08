'''
    parse the ./incident_summary/incident-summary.json file located into the ./incident-summary subfolder
    and extract from it some important keys and their values :
'''
import json, sys
from datetime import datetime, date, timedelta
import time
import hashlib
from crayons import *
import json
import sys
import requests
import os
import string
import random

# Get global variable from config.py
incident_summary={}
indicator_map={} # map indicator id between old tenant and new tenant
method="config.txt"  # for futur use :  must be either config.txt or ../key  or database  or vault or environment variable

# Get the current date/time
dateTime = datetime.now()

def read_incident_summary():
    file='./incident_summary/incident-summary.json'
    with open(file,'r') as file:
        text_data=file.read()
        json_data=json.loads(text_data)
        #print(cyan(json_data,bold=True))  
    return(json_data)
       
def get_incident_indicators():
    indicator_list=[]
    for item0 in incident_summary[0]['context']['indicators']: 
        print("Indicator :",yellow(item0["title"] ,bold=True))
        print(green(item0,bold=True))
        indicator_list.append(item0)       
    return(indicator_list)
    
def get_incident_sightings():
    sighting_list=[]
    for item0 in incident_summary[0]['context']['sightings']: 
        print("sighting :",yellow(item0["title"] ,bold=True))
        print(green(item0,bold=True))
        sighting_list.append(item0)       
    return(sighting_list)
    
def get_incident_score():
    score=incident_summary[0]['scores']
    print('score :\n',green(score,bold=True))     
    return(score)
    
def get_incident_tactics():
    tactics=incident_summary[0]['tactics']
    print('tactics :\n',green(tactics,bold=True))     
    return(tactics)
    
def get_incident_techniques():
    techniques=incident_summary[0]['techniques']
    print('techniques :\n',green(techniques,bold=True))     
    return(techniques)
    
def get_incident_details():
    details={}
    details['title']=incident_summary[0]['title']
    details["timestamp"]=incident_summary[0]["timestamp"]
    details["description"]=incident_summary[0]["description"]    
    print('details :\n',green(details,bold=True))     
    return(details)
    
def get_incident_observables():
    observables=[]
    for sighting in incident_summary[0]["context"]["sightings"]:
        if 'observables' in sighting.keys():
            for obs in sighting["observables"]:  
                if obs not in observables:
                    observables.append(obs)
    print("observables :",yellow(observables ,bold=True))    
    return(observables)
    
if __name__ == "__main__":
    print(yellow("- Step 0 read incident summary json file",bold=True))
    incident_summary=read_incident_summary()
    print()
    print(yellow("- Step 1 get Incident Indicators and create them into the new tenant ",bold=True))
    print()
    indicator_list=get_incident_indicators()    
    print(yellow("- Step 2 get Incident Indicators and create them into the new tenant ",bold=True))
    print()
    sighting_list=get_incident_sightings()  
    print(yellow("- Step 3 get Incident score ",bold=True))
    print()
    get_incident_score()   
    print(yellow("- Step 4 get Incident tactics ",bold=True))
    print()
    get_incident_tactics()   
    print(yellow("- Step 5 get Incident techniques ",bold=True))
    print()
    get_incident_techniques() 
    print(yellow("- Step 6 get Incident Global Details ",bold=True))
    print()
    get_incident_details()    
    print(yellow("- Step 7 get every observables ",bold=True))
    print()
    get_incident_observables()