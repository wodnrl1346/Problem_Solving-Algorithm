/*for 문으로 구현*/
#include <stdio.h>

int main(){
    int i, n, a;
    scanf("%d", &n);

    a = n;

    for(i=0; i<n; i++)
    {
        a--;
        if(a >= 0)
            printf("%d\n", a);
    }
}

/*while 문으로 구현*/
#include <stdio.h>

int main(){
    int i, n, a;
    scanf("%d", &n);

    while(n!=0)
    {
        n--;
        printf("%d\n", n);
    }
}