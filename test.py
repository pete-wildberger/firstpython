#!/usr/bin/python

# def checkName(name):
#     checkName = raw_input("Are you " + name + "? ")
#
#     if checkName.lower() == "yes":
#         print("Hello ", name)
#     else:
#         print("We're sorry about that.")
# def checkAge():
#     age = input("How old are you?")
#     print("Peter is ", age, " years old")
# checkName("Peter")
# checkAge()

pyg = 'ay'

original = raw_input('Enter a word:')

if len(original) > 0 and original[0] in ('a', 'e', 'i', 'o', 'u') and original.isalpha():
    word = original.lower()
    first = word[0]
    new_word = word + pyg
    print "if " + new_word
elif len(original) > 0 and original.isalpha():
    word = original.lower()
    first = word[0]
    new_word = word[1: len(word)] + first + pyg
    print "elif " + new_word
else:
    print 'empty'
