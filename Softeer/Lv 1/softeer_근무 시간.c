#include <stdio.h>


int main(void)
{
	int h1, m1, h2, m2;
	int i; //반복문
	int hour, minute; //시간, 분
	int total=0; //전체 시간(분)

	for(i=0; i<5; i++)
	{
		scanf("%d:%d %d:%d", &h1, &m1, &h2, &m2);

		hour = h2 - h1;
		minute = m2 - m1;

		if(minute < 0)
		{
			hour -= 1;
			minute += 60;
		}

		total += hour * 60 + minute;

	}

	printf("%d", total);

	return 0;
}