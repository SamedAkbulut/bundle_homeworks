#include<stdio.h>

// Ahmed Samed Akbulut

int main(){
    char a[50],s[50];
    int d;
    printf("Adiniz :\n");
    scanf("%s",a);
    printf("Soyadiniz :\n");
    scanf("%s",s);
    printf("Dogum yiliniz :\n");
    scanf("%i",&d);
    printf("%s %s %i", a, s, d);
    system("pause");
    return 0;
} 
