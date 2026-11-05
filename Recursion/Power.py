'''base=int(input('Enter the base: '))
power=int(input('Enter the power: '))
print(base**power)'''

#Recursion for the power of a number
def power(a,b):
    if b==0:
        return 1
    return a*power(a,b-1)

print(power(2,3))


def nom(a,b):
    ans=1
    for i in range(1, b+1):
        ans*=i
    return ans

print(nom(2,3))