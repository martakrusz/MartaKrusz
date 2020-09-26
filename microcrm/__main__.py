import sys
import json

from .parser import csv

for entry in csv(sys.argv[1]):
    print(entry)
