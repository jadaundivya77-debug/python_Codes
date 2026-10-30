def second():
    numbers = []
    largest = 0
    second_largest = 0
    a=int(input("Enter the number of participants: "))
    for i in range(a):
        n=int(input("Enter the score of participant :"))
        numbers.append(n)
	
    for n in numbers:
        if n > largest:
            second_largest = largest
            largest = n
        elif n > second_largest:
            second_largest = n
    print("The second largest score is: ", second_largest)
    if second_largest == 0:
        print("There is no second largest score.")

second()

