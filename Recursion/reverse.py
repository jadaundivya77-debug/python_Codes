def rev(a, r=0):
    
    if a == 0:
        return r
    return rev(a//10, r *10 + a%10)

print(rev(674453))