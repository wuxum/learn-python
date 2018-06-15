#!/usr/bin/python

# website: https://pythonbasics.org/constructor/

class Bug:
   def __init__(self):
       self.wings = 4

class Human:
   def __init__(self):
       self.legs = 2
       self.arms = 2

bob = Human()
tom = Bug()

print(tom.wings)
print(bob.arms)
