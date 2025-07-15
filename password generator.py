import random

print("welcome to random password generator")
randomchar="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*"
noofpasw=int(input("enter the no of password:"))
paswlen=int(input("please enter the lenth of the password needed:"))
print("here are your random passwords:")
for x in range(noofpasw):
    pasw =""
    for chars in range(paswlen):
        pasw=pasw + random.choice(randomchar)
    print(pasw)
