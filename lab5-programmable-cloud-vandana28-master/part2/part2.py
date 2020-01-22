#!/usr/bin/env python

import argparse
import os
import time

import googleapiclient.discovery
from six.moves import input
from pprint import pprint
from googleapiclient import discovery
import google.auth
from oauth2client.client import GoogleCredentials

credentials, project = google.auth.default()
service = googleapiclient.discovery.build('compute', 'v1', credentials=credentials)
project = 'vasr6141-254820'
zone = 'us-west1-b'
disk = 'demo-instance'
bucket = 'lab5vminstance'

snapshot_body = {

    'name' : 'base-snapshot-demoinstance'

}



def wait_for_operation(compute, project, zone, operation):
    print('Waiting for operation to finish...')
    while True:
        result = compute.zoneOperations().get(
            project=project,
            zone=zone,
            operation=operation['name']).execute()
        print(result)

        if result['status'] == 'DONE':
            print("done.")
            if 'error' in result:
                raise Exception(result['error'])
            return result

        time.sleep(1)


def create_instance(compute,project,zone,name,bucket,snapshotname): 
    getsourceSnapshot = compute.snapshots().get(project = project , snapshot = snapshotname).execute()
    source_snapshot = getsourceSnapshot['selfLink']
    #pprint(getsourceSnapshot)

    #source_snapshot = image_response['sourceSnapshot']



    machine_type = "zones/%s/machineTypes/n1-standard-1" % zone
    startup_script = open(
        os.path.join(
            os.path.dirname(__file__), 'startup-script.sh'), 'r').read()
    image_url = "http://storage.googleapis.com/gce-demo-input/photo.jpg"
    image_caption = "Ready for dessert?"

    config = {
            'name': name,
            'machineType': machine_type,

            # Specify the boot disk and the image to use as a source.
            'disks': [
                {
                    
                    'boot': True,
                    'autoDelete': True,
                    'initializeParams': {
                        #'sourceImage': source_disk_image,
                        'sourceSnapshot': source_snapshot
                        
                        
                    }
                }
            ],

            # Specify a network interface with NAT to access the public
            # internet.
            'networkInterfaces': [{
                'network': 'global/networks/default',
                'accessConfigs': [
                    {'type': 'ONE_TO_ONE_NAT', 'name': 'External NAT'}
                ]
            }],

            # Allow the instance to access cloud storage and logging.
            'serviceAccounts': [{
                'email': 'default',
                'scopes': [
                    'https://www.googleapis.com/auth/devstorage.read_write',
                    'https://www.googleapis.com/auth/logging.write'
                ]
            }],

            # Metadata is readable from the instance and allows you to
            # pass configuration from deployment scripts to instances.
            'metadata': {
                'items': [{
                    # Startup script is automatically executed by the
                    # instance upon startup.
                    'key': 'startup-script',
                    'value': startup_script
                }, {
                    'key': 'url',
                    'value': image_url
                }, {
                    'key': 'text',
                    'value': image_caption
                }, {
                    'key': 'bucket',
                    'value': bucket
                }]
            }
        }

    return compute.instances().insert(
    project=project,
    zone=zone,
    body=config).execute()

#def create_snapshot(compute,project,zone,disk,snapshot_body):
request = service.disks().createSnapshot(project = project, zone = zone , disk = disk , body = snapshot_body)
response = request.execute()
    


time_list = []
name1 = 'demo1'
name2 = 'demo2'
name3 = 'demo3'


t0 = time.time()
operation = create_instance(service,project,zone,name1,bucket,snapshot_body['name'])

#pprint(operation)
wait_for_operation(service,project,zone,operation)
t1 = time.time()
diff1 = t1 - t0
time_list.append(diff1)

t2 = time.time()
operation2 = create_instance(service,project,zone,name2,bucket,snapshot_body['name'])
wait_for_operation(service,project,zone,operation2)
t3 = time.time()
diff2 = t3 - t2
time_list.append(diff2)

t4 = time.time()
operation3 = create_instance(service,project,zone,name3,bucket,snapshot_body['name'])
wait_for_operation(service,project,zone,operation3)
t5 = time.time()
diff3 = t5 - t4
time_list.append(diff3)



print(time_list)
with open('TIMING.md','w') as f:
    for item in time_list:
        f.write("%s\n" % item)
