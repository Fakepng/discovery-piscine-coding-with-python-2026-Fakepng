#!/usr/bin/python

age = int(input("Please tell me your age: "))

print(f"You are currently {age} years old.")
for i in range(10, 31, 10):
    future_age = age + i
    print(f"In {i} years, you will be {future_age} years old.")