# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import random

data=[]
while len(data) !=6:
    n=random.randint(1, 49)
    if data.count(n)==0:
        data.append(n)

print(data)

data.sort()

print(data)
