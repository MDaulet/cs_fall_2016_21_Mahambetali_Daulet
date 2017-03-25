#include <stdio.h>
#include <string.h>

int main()
{
    int j=0, i=0, l=0;
    char a[1000], b[1000], c;
    printf("Введите строку:\n");
    while((c=getchar())!='\n'){
        a[i]=c;
        ++l;
        ++i;
    }
    for (i=1; i<=l;++i){
        if(a[i-1]!=a[i]){
            b[j]=a[i-1];
            ++j;
        }
    }
    printf("%s\n", b);
    return 0;
}
