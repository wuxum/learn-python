#!/usr/bin/env python

# website: https://pythonbasics.org/read-file/

filename = "file.py"

with open(filename) as f:
    content = f.readlines()

print(content)
