def palindrome(a):
    if a==a[::-1]:
        return True
    else:
        return False
print(palindrome("Divya"))