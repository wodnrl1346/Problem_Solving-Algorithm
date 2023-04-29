/*switch-case 문을 이용한 풀이*/
# include <stdio.h>

int main(){
    int season;
    scanf("%d", &season);

    switch(season)
    {
        case 12:
        case 1:
        case 2:
            printf("winter");
            break;  // switch 문을 종료한다.
        case 3:
        case 4:
        case 5:
            printf("spring");
            break;
        case 6:
        case 7:
        case 8:
            printf("summer");
            break;
        case 9:
        case 10:
        case 11:
            printf("fall");      
            break;
    }

}

/*if 문을 이용한 풀이*/
# include <stdio.h>

int main(){
    int m;

    scanf("%d", &m);

    if(m == 12 || m==1 || m==2)
    {
        printf("winter\n");
    }

    else if(m == 3 || m==4 || m==5)
    {
        printf("spring\n");
    }

    else if(m == 6 || m==7 || m==8)
    {
        printf("summer\n");
    }

    else if(m == 9 || m==10 || m==11)
    {
        printf("fall\n");
    }

    return 0;
}