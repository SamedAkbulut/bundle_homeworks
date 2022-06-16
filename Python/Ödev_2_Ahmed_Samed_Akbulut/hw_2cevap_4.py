a=str(input("Bir değer giriniz:"))
b=str(input("Bir değer giriniz:"))
c=str(input("Bir değer giriniz:"))
d=str(input("Bir değer giriniz:"))
e=str(input("Bir değer giriniz:"))
s=[a,b,c,d,e]
x=5
y=x
z=0
for i in range (1,x+1):
    for j in range(0,y):
        print(s[z],end="")
    z = z+1
    y = y-1
    print()