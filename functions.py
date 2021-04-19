def say_hi(fName,lName):
    print("Hi " + fName + " " + lName + "!")

name = input("What is your first and last name? (Use a space to separate) ")

x = name.split(" ")

say_hi(x[0], x[1])
print(x)

