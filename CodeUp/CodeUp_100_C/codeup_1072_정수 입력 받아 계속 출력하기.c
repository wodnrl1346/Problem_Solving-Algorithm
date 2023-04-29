/*goto를 이용한 풀이*/
#include <stdio.h>

int main(){
    int n;  // 입력될 정수의 개수
    scanf("%d", &n);

    int a;  // 입력되는 정수
    
    reget:
    scanf("%d", &a);
    printf("%d\n", a);
    if(--n > 0) 
        goto reget;     // 정수를 n개 만큼 입력받아 출력한다. (※반복문 사용 X) goto를 사용하여 구현했다.

}

/*for 문을 이용한 풀이*/
#include <stdio.h>

int main(){
    int n;  // 입력될 정수의 개수
    scanf("%d", &n);

    int i, a;

    for(i=0; i<n; i++)
    {
        scanf("%d", &a);
        printf("%d\n", a);
    }
}