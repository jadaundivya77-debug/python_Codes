def TOH(n, a, b, c):
    if (n>0):
        TOH(n-1, a, c, b)
        print("Disk move to end")
        return TOH(n-1, b, a, c)

    }