#!/usr/bin/env python3

# website: https://pythonbasics.org/scope/

balance = 0

def addAmount(x):
    global balance
    balance = balance + x

    addAmount(5)
    print(balance)
