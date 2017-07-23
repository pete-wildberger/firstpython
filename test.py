#!/usr/bin/python
def checkName(name):
    checkName = input("Are you " + name + "? ")

    if checkName.lower() == "yes":
        print("Hello ", name)
    else:
        print("We're sorry about that.")
def checkAge():
    age = input("How old are you?")
    print("Peter is ", age, " years old")
checkName("Peter")
checkAge()
