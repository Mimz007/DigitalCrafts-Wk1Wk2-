bill_amount = 0
while bill_amount == 0:
    
    try:
        bill_amount = float(input('How much was the bill?\n'))
    except ValueError:
        print('You did not give a valid number.')

service_level = input('How was the service? Good, fair, bad \n')
tip = 0
if service_level == "good":
     tip = bill_amount*.2
elif service_level == "fair":
     tip = bill_amount*.15
elif service_level == "bad":
     tip = bill_amount*.10
else:
    tip = float(input("Please Enter Specific Amount"))

print(f"Tip Amount: {tip}")
# OR YOU CAN PRINT THIS WAY
# print(f"Total Amount: {bill_amount+tip}")
# OR use interprelation
print('Total Amount %s :' % (bill_amount+tip))

# Split The Tip
people = int(input("How many to split with?\n)"))
total = bill_amount+tip
split_amount = total/people

print('The amount of each individual is : %s' %split_amount)


