#!/usr/bin/env python3

def admin_login(username, password):
    if ((username=="ADMIN") or (username=="admin")) and (password == "12345"):
        return "Access granted"
    else:
        return "Access denied"

def hows_the_weather(temperature):
    if (temperature < 40):
        return "It's brisk out there!"
    elif (temperature > 85):
        return "It's too dang hot out there!"
    elif (temperature > 40 and temperature < 65):
        return "It's a little chilly out there!"
    else:
        return "It's perfect out there!"

def fizzbuzz(num):
    if (not num % 3) and (not num %5):
        return "FizzBuzz"
    elif (not num %3 ):
        return "Fizz"
    elif (not num % 5):
        return "Buzz"
    else:
        return num
 

def calculator(operation, num1, num2):
    # your code here
    pass
