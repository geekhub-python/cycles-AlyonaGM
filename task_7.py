#!/usr/bin/env python3

first_day = 10
sum = 0
for i in range(1, 11):
	if i < 8:
		sum = sum + first_day
	first_day = first_day * 1.1
	print(first_day)
print("Пробег за первые 7 дней - ", sum)




