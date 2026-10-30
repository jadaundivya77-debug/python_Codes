def table(n, a=11):
    if a==1:
        return 1

    print(n, '*', a-1, '= ', n*(a-1))
    return table(n, a-1)

print(table(4))




'''def tab(n, t):
    if (n==11):
        return
    print(n*t)
    return tab(n+1, t)

print(tab(1, 11))'''