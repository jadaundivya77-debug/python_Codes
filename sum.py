list=[1,2,3,4,5,6,7,8,9,10]
def add(list):
    sum=0
    for i in list:
        sum+=i
    avg=sum/len(list)
    return sum, avg
print(add(list))