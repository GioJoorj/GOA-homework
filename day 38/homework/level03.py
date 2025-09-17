def fun1():
    name = input('enter anything:')
    name2 = input('enter anything again:')
    if name not in name2:
        print("error")
    elif name in name2:
        print('no errors')
fun1()
