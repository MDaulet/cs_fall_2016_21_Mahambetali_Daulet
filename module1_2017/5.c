#include<stdio.h>
#define LOWER 0
#define UPPER 100
#define STEP 10
int main()
{
	int celc;
	for (celc = LOWER; celc <= UPPER; celc = celc + STEP)
		printf("%d %.1f\n",celc, (1.8*celc)+32);
	return 0;

}
