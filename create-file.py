while(1):
    f = open("phone-book.txt","a")
    name=input("Enter name: ")
    mobile=input("Enter mobile number: ")
    f.write(name + " " + mobile + "\n")
    f.close()

