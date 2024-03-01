import random
a=int(input("enter the length of the password(limit 4 to 6):"))
b=['1','2','3','4','5','6','7','8','9','10']
c=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
d=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
e=["@","$","*","&"]
f=(random.choice(b))
g=(random.choice(c))
s=(random.choice(c))
h=(random.choice(d))
v=(random.choice(d))
k=(random.choice(e))
if a==4:
    p=f+g+h+k
    print(p)
    print("password generated")
elif a==5:
    p=f+g+s+h+k
    print(p)
    print("password generated")
elif a==6:
    p=f+g+s+h+v+k
    print(p)
    print("password generated")
else:
    print("Invalid input")