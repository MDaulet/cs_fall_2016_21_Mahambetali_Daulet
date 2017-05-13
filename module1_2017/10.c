#include <stdio.h>


unsigned int rightrot(unsigned int x,unsigned int n)
{
    return (x>>n);
}

int main()
{

	unsigned int x, n;
	printf("Набери x: ");
	scanf("%i",&x);
	printf("Набери n:");
    scanf("%u", &n);
	x = rightrot(x, n);
	printf("%u", x);

	return 0;
}
