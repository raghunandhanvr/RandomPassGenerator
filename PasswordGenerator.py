import random

capital_letter    = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"     #UpperCase lettrs
small_letter      = capital_letter.lower()           #Or add small letters
digits            = "0123456789"                     #Numerical char
symbols           = "()[]{,.:/}\|/?#@!%^&*"          #Symbols

upper, lower, nums, sym = True, True, True, True     #You can set unwanted stuffs to false

all = " " 

if upper:
    all += capital_letter
if lower:
    all += small_letter
if nums:
    all += digits
if sym:
    all += symbols

length = 20                                          #set the length of the password
amount = 2                                           #set how many pasword required

for x in range(amount):
    password = "".join(random.sample(all, length))
    print(password)
