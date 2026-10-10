numbers = [10, 40, 20, 50, 30]

largest = 0
second_largest = 0

for n in numbers:
	if n > largest:
		second_largest = largest
		largest = n
	elif n > second_largest:
		second_largest = n

print(second_largest)
