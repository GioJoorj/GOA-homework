month = int(input("შეითყვანეთ თვე :"))
if month == 1 or month == 2 or month == 12:
    print("winter")
elif month == 3 or month == 4 or month == 5:
    print("spring")
elif month == 6 or month == 7 or month == 8:
    print("summer")
elif month == 9 or month == 10 or month == 11:
    print("autumn")
else:
    print("wrong number")
