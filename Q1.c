#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int min (int num1, int num2)
{
	int re;
	re = num1 - num2;
	if (re <= 0)
		return num1;
	else
		return num2;
}

int GCD (int num1, int num2)
{
	int mi, re1, re2;
	re1 = 1;
	re2 = 1;
	mi = min(num1, num2);
	while (re1 = re2 || re1 != 0)
	{
		re1 = num1 % mi;
		re2 = num2 % mi;
		mi--;
	}
	return mi + 1;
}

int main(void)
{
	int res, num1, num2;
	printf("자연수 2개 입력");
	scanf("%d, %d", &num1, &num2);
	res = GCD(num1, num2);
	printf("%d와 %d의 최대공약수는 %d",num1, num2, res);
}
