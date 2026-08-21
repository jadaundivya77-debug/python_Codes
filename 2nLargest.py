numbers = [10, 40, 20, 50, 30]

largest = 0
second_largest = 0

for number in numbers:
	if number > largest:
		second_largest = largest
		largest = number
	elif number > second_largest:
		second_largest = number

print(second_largest)
