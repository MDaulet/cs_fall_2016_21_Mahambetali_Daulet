#include <stdio.h>


int main()
{
	setlocale(0, "russian");
	float a, b, x, y, d, k;
	printf("Введите значения сопротивлений в виде a+bi x+yi: ");
	scanf("%f+%fi %f+%fi", &a, &b, &x, &y);
	d = (a*a*x + a*x*x + a*y*y + b*b*x) / ((a + x)*(a + x) + (b + y)*(b + y));
	k = (a*a*y + b*b*y + b*x*x + b*y*y) / ((a + x)*(a + x) + (b + y)*(b + y));
	printf("Ответ: %.4f+%.4fi", d, k);
	return 0;
}
