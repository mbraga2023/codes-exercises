answer = input("Greeting: ")
if answer[0:5] == "Hello":
    print ("$0")
elif answer != "Hello":
    if answer[0] == "H":
        print ("$20")
    else:
        print ("$100")
