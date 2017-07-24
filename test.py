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

sentence = raw_input('Enter a word:')
output = []

sentArr = sentence.split( )
print sentArr



def pigLatin(original):
    if len(original) > 0 and original[0] in ('a', 'e', 'i', 'o', 'u') and original.isalpha():
        word = original.lower()
        new_word = word + pyg
        return new_word
    elif len(original) > 0 and original.isalpha():
        word = original.lower()
        vowel_indices = [idx for idx, ch in enumerate(original) if ch.lower() in 'aeiou']
        splitIdx = vowel_indices[0]
        first = original[0 : splitIdx]
        new_word = word[splitIdx: len(word)] + first + pyg
        return new_word
    else:
        print 'empty'

for item in sentArr:
    output.append(pigLatin(item))
answer = ' '.join(output)
print answer
