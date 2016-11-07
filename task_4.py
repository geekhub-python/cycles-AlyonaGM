#!/usr/bin/env python3

mass = []
a = range(2,11)
x = range(1, 30000)
for elem in x:
	if elem % 11 == 0:
		mass.append(elem)
# print(mass)
for elem1 in mass:
	if elem1 % 2 == 1 and elem1 % 3 == 1 and elem1 % 4 and elem1 % 5 == 1 and elem1 % 6 == 1 and elem1 % 7 == 1 and elem1 % 8 == 1 and elem1 % 9 == 1 and elem1 % 10 == 1:
		print(elem1)
		break 