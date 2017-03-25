#include <stdio.h>
#include <stdlib.h>

void copy(char *c,char *x)
{
        FILE *C,*X;
        C=fopen(c,"r");
        X=fopen(x,"w");
        char i;
        while((i=fgetc(C))!=EOF)
        {
                fputc(i,X);
        }
}

int main()
{
        char a[1000],b[1000];
        printf("Введите путь к расположению файла который копируют(Для примера D:\\smb\\1.txt)");
        gets(a);
        printf("Введите расположение файла куда копировать (Для примера D:\\smb\\2.txt)");
        gets(b);
        copy(a,b);
        printf("файл готов");
        return 0;
 }
