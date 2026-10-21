def num(n):
    if n==1:
        return 1
    print(num(n-1))
    return n
    
    
print(num(5))