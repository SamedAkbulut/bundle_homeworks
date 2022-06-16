x = int(input("Lütfen bir sayı giriniz : "))
y = int(input("Lütfen bir sayı giriniz : "))
z = input(" Lütfen yaptırmak istediğiniz işlemi ( + , - , * , / ) seçiniz : ")

if z== "+":
    Toplama = lambda x,y : x + y
    print(f'Girdiğiniz sayıların toplamı {Toplama (x,y)} eder.')

elif z== "-":
    Çıkarma = lambda x,y : x - y
    print(f'Girdiğiniz sayıların farkı {Çıkarma (x,y)} eder.')

elif z== "*":
    Çarpma = lambda x,y : x * y
    print(f'Girdiğiniz sayıların çarpımı {Çarpma (x,y)} eder.')
    
elif z== "/":
    Bölme = lambda x,y : x / y
    print(f'Girdiğiniz sayıların bölümü {Bölme (x,y)} eder.')
