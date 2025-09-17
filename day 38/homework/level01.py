#შექმენით ფუნქიცა, manual_find, რომელსაც გადაეცემა 
#არგუმენტად სთრინგი და ერთი სიმბოლო, 
#რომელიც უნდა ვიპოვოთ ამ სთრინგში. თუ სიმბოლო
#მოიძებნა დააბრუნეთ მისი ინდექსი, სხვა შემთხვევაში დააბრუნეთ -1
def fun1():
    name = input("enter anything:")
    symbol = input("enter and symbol:")
    print(name.find(symbol))
    if symbol != symbol:
        return(name)
    else:
        return(name[-1])
fun1()