withdrawals=[500, 2000, 15000, 8000, 25000, 1000]
balance=50000
for t in withdrawals:
    if t>0:
        if t%100==00:
            if t<=20000:
                print("transaction Successful")
                balance-=t
            else:
                print("More than 20000")
        else:
            print("Not divisible by 100")
    else:
        print("Less than 0")
print(balance)