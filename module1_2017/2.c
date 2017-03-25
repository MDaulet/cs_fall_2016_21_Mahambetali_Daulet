#include <stdio.h>

int main()
{
	int day = 9, month = 4;
	int a = day;
	printf("0%i.%i\n", day, month);
	day = month;
	month = a;
	printf("%i.0%i\n", day, month);
	return 0;
}
