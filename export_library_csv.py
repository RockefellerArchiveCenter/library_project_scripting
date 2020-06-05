#!/usr/bin/env python

import os
import json
import csv
from asnake.aspace import ASpace

aspace = ASpace(
              baseurl='http://192.168.50.4:8089',
              user='admin',
              password='admin'
              )
repo = aspace.repositories(2)

###Writes library resources to a csv
def write_library_csv(csvName):
    fieldnames = ['id_0', 'resource_id', 'title']
    with open(csvName, 'w', newline='') as outputFile:
        writer = csv.DictWriter(outputFile, fieldnames=fieldnames)
        writer.writeheader()
        get_library(writer)

###Gets library resources
def get_library(writer):
    for object_type in ['resources']:
        for object in getattr(aspace, object_type):
            if not (object.jsonmodel_type == 'resource' and object.id_0.startswith(("FA", "AC.", "AC", "2"))):
                aspace.get().json()
                #print(object)
                print("resource/{}".format(object.uri.split('/')[-1]))
                writer.writerow({'id_0': (object.id_0), 'resource_id': str(object.uri.split('/')[-1]), 'title': object.title})

csvName = "library_resources.csv"
write_library_csv(csvName)
