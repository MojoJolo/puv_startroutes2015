# -*- coding: utf-8 -*-
import csv
from collections import Counter
import requests

puvs = {}

with open('app/static/data/puv.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile)

    for row in reader:
        if row[0] not in puvs:
            puvs[row[0]] = []

        puvs[row[0]].append(row[1])

print "Routes count"

for key, value in puvs.items():
    print "{}: {}".format(key, len(value))