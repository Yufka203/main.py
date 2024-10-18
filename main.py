import random

sifre = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

kac = int(input("Kaç haneli olsun: "))

parola = ""

for i in range(kac):
    parola += random.choice(sifre)

print(parola)    
