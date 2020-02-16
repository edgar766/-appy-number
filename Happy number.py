while True:
    a=str(input("enter a number"))
    if int(a[0]) + int(a[1]) == int(a[2]) + int(a[3]):
        print("happy number")
    else:
        print("Not a happy number")
