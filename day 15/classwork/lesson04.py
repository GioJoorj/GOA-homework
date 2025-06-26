age = int(input("enter your age: "))
income = float(input("enter your income: "))
if age < 18 or income < 10000: 
    print("you are free")
else: 
    print("you have to pay")