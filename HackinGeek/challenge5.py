#!/usr/bin/python3

from random import randint

new_string = ""
array = []
string = input("Enter sentence: ")

while len(array) != len(string):
        n = randint(1, len(string))
        if n not in array:
                array.append(n)

print("Order of letters: ", array)

for i in array:
        new_string += string[i-1]

print("New string:\n\t", new_string)
