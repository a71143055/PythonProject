def MyFunction(x,y):
    return x * y

a = 100

def func():
    global a
    print(a)

if __name__ == '__main__':
    print(MyFunction(5,5))
    func()
    a = 5
    print(a)
    func()

    myList = []
    for i in range(0,6):
        myList.append(i)
    print(myList)

    myList = []
    i = 0
    while i < 6:
        myList.append(i)
        i+=1
    print(myList)