list=[10, 20, 30, 40,50]
search=30
count=0
for i in range(len(list)):
    if list[i]==search:
        count+=1
if count>=1:
    print("The Numer is present.")
else: 
    print("The number is not present.")
        
    
               