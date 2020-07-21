while True:
    try:
        a=int(input("enter your phone number: ")) #reads from keyboroad!!!
        print("your number with cyprus code is: +357",a)
        break
    except ValueError:
        print("you have wrongly entered a letter character!!!! Please enter your phone nuber again")
