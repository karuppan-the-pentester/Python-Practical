while(True):
    try:
        print("a/b")
        a=int(input("Enter the value for a: "))
        b=int(input("Enter the value for b: "))
        print("The value is ",a/b)
    except Exception as e :
        print(e)
        exit(0)



