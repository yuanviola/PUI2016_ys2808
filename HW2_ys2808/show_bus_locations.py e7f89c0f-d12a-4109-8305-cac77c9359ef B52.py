from __future__ import print_function
import pandas as pd
import numpy as np
import json
import urllib2 
import os
import sys
api=raw_input('api:')
bus=raw_input('which bus?')
website='http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=' + api
website += '&VehicleMonitoringDetailLevel=calls&LineRef='+ bus
b52=pd.read_json(website)
VehicleActivity=b52['Siri'][u'ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']
pd.DataFrame(VehicleActivity)
buscount=len(VehicleActivity)
vehicleactivity_keys=VehicleActivity[0].keys()
vehicleactivity_data=VehicleActivity[0]
pd.DataFrame(vehicleactivity_data,columns=vehicleactivity_keys)
busname=vehicleactivity_keys=VehicleActivity[0]['MonitoredVehicleJourney']['PublishedLineName']
print('Bus Line : ',busname)
print('Number of Active Buses :',buscount)
buslocation=[]
for i in range(buscount):
    buslocation.append(VehicleActivity[i]['MonitoredVehicleJourney']['VehicleLocation'])
    print('bus',i,'is at Latitude',buslocation[i]['Latitude'],'and at Longitude',buslocation[i]['Longitude'])