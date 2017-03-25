#include <stdio.h>

int main()
{
    int x = 0;
    int i = 0;
    unsigned long int f = 1;
    printf("Введите число\n");
    scanf("%d", &x);
    if ((x==0) || (x==1)){
        printf("Факториал = %d\n", f);
    }
    else{
        for (i=1;i<=x;++i){
            f*=i;
        }
        printf("Факториал = %d\n", f);   
    }
    
    return 0;
}
