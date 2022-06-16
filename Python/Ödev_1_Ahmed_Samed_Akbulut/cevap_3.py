x = int(input("Kısa kenar uzunluğunu giriniz :"))
y = int(input("Uzun kenar uzunluğunu giriniz :"))
a = (x**2 + y**2)**0.5
b = x*y
c = 2*(x+y)

print("Köşegen:{}".format(a))
print("Alan:{}".format(b))
print("Çevre:{}".format(c))