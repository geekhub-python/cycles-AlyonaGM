#!/usr/bin/env python3

for i in range (1000,10000):
    x = list(str(i))
    if "6" not in x and "5" not in x:
    	print(i, end = " ")