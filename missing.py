seats=input("Enter the seats : ")
n=input("Enter a number : ")
def missing(seats, n):
    for i in range(1, int(n)+1):
        if str(i) not in seats:
            return i
print(missing(seats, n))