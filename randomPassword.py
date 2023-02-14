#Random Password genrator
import random

characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*"

password_length = int(input("Enter Password length"))
password_count = int(input("Enter Count of Passwords"))

for i in range(0,password_count+1):
    password = ""
    for j in range(0,password_length):
        pass_char = random.choice(characters)
        password = password+pass_char
    print("Random Password is:",password)