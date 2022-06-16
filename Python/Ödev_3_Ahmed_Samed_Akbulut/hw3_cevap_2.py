parola=input("Parola giriniz :")
def checkPassword(password):
    x=False 
    for letter in password:
        if letter.isupper():
            print("Kucuk harf icermelidir.")
            x=True
            break
    if len(password)<7:
        print("En az 7 karakter olmalı")      
    if x==False and len(password)>7:
        print("Dogru parola")
checkPassword(parola)
        
#dogru parolayı bulana kadar tekrar tekrar sorması anlamı soruda çıkmıyordu.
#bundan dolayı tek sefer output verecek sekilde ayarladım 
