
slots= [1,0,1,0]
def missing(slots):
    for i in range(len(slots)):
        if slots[i]==0:
            return i+1
print(missing(slots))