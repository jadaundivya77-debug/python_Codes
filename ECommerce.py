prices=[1200, 2500, 1800, 3200, 1500]
budget= 4300
for i in range(0, len(prices)):
    for j in range(1, len(prices)):
        if prices[i]+ prices[j]==budget:
            print(i, j)
        break
        