#1) რა არის გასხვავება for loop სა და while loop შორის ახსენით კომენტარებით და დაწერეთ ისეთი 
# პროგრამა მომხმარებელს პაროლის შეყვანა რომ შეეძლოს სანამ შეყვანილი პაროლი 
# არ იქნება სწორი იქამდე უნდა შევიყვანოთ პაროლი
# for loop იმდეჯერ აკეთებს სადამდეც ვეტყვით
# while loop კიდე სამუდამოდ იმეორებს
while True:
    name = "123"
    user = input('enter password:')
    if name == user:
        print("Correct")
    else:
        print("try again")
    