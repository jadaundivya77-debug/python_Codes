s="racecar"
rev=""
for i in s[::-1]:
    rev+=i
if rev==s:
    print("Palindrome")
else:
    print("Not a Palindrome")