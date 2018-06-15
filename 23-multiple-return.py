#!/usr/bin/env python3

# website: https://pythonbasics.org/multiple-return/

def getPerson():
    name = "Leona"
    age = 35
    country = "UK"
    return name,age,country

name,age,country = getPerson()
print(name)
print(age)
print(country)
