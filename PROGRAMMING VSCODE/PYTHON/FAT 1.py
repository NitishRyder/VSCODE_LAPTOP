income=760000
tax=0
if income < 500000:  
    tax = 0
elif (income>0 and income<250000):
    tax=income*0
elif (income>250000 and income<500000):
    tax=(income-250000)*0.05
elif (income>500000 and income<1000000):
    tax=12500+(income-500000)*0.2
else:
    tax=income*0.3
print(int(tax))