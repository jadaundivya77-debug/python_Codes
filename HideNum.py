n=(input("Enter your mobile number : "))
def hidenum(n):
    return('*'*6 + n[-4: ])

print(hidenum(n))

