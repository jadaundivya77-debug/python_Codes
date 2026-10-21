age=[25, 35, 42, 19, 52]
salary=[30000, 55000, 75000, 25000, 90000]
credit_score = [720, 650, 780, 750, 600]

for i in range(0, 5):
    
    if age[i]>=21:
        if salary[i] >=30000:
            if credit_score[i]>=700:
                print("Customer "+ str(i+1) + " Eligible")
            else:
                print(str(i+1) + " Not Eligible")
                print("Reason: Credit_score less than 700")

        else:
            print(str(i+1)+ " Not Eligible")
            print("Resason: Salary is less than 30000")

    else:
        print(str(i+1)+' Not Eligible')
        print('Reason: Age is less than 21')
                