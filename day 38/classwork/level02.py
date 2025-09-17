def fun1(name):
    if name == "":
        return name
    one = name[0]
    two = name[1:]
    
    one_one = one.upper()
    two_two = two.lower()
    return one_one + two_two