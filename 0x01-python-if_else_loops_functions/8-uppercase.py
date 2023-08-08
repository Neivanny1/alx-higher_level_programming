#!/usr/bin/python3
def uppercase(str):
    word = ""
    for char in str:
        if char >= 'a' and char <= 'z':
            word += chr((ord(char) - 32))
        else:
            word += char
    print("{}".format(word))
