import random
letters=['a','b','c','d','e','f','g','h','i','j','k','l','m',
         'n','o','p''q','r','s','t','u','v','w','x','y','z',
         'A','B','C','D','E','F','G','H','I','J','K','L','M',
         'N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers=['0','1','2','3','4','5','6','7','8','9']
symbols=['!','@','$','%','&','*','(',')','_','+']
print("Password Generator!")
count_letters=int(input("How many letters need to be there in your password?\n"))
count_symbols=int(input("How many symbols need to be there in your password?\n"))
count_numbers=int(input("How many numbers need to be there in your password?\n"))
password_set=[]
for i in range(1,count_letters+1):
    char=random.choice(letters)
    password_set +=char
for i in range(1,count_numbers+1):
    char=random.choice(numbers)
    password_set +=char
for i in range(1,count_symbols+1):
    char=random.choice(symbols)
    password_set +=char
print(password_set)
random.shuffle(password_set)
print(password_set)
password=""
for char in password_set:
    password +=char
print(password)

                
