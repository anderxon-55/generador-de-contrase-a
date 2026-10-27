import random
elements = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

password_length = int(input("Enter the lenght of the password"))
password = ""
for i in range(password_length):
    password +=random.choice(elements)

    print("your new password is:", password)
