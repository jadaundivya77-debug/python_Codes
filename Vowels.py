name=str(input("Enter the name: "))
count=0
vowels="aeiouAEIOU"
for i in name:
    if i in vowels:
        count+=1
print(count)
    