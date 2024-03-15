print("enter num of hours")
Hour=int(input())
Min=int(input())
if(Hour>7):
    print("Invalid Input")
elif Hour>=5:
    amount=200
    Hour=Hour-5
    amount=amount+Hour+50*Min
    print(amount)
