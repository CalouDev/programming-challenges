#!/usr/bin/python3

usr = int(input("Number: "))
result = 0

for i in range(1, usr):
        if usr % i == 0:
                result += i
        
if result == usr:
        print("Perfect number !")
else:
        print("Not perfect number...")
