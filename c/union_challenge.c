#include<stdio.h>
#define P u.a

union UNION{
    char a;
    char b;
};

typedef union UNION U;

int main(void){
    U u;
    u.a = '1';
    char c = '3';
    printf("u.a:%c, u.b:%c\n", u.a, u.b);
    P = '2';
    printf("u.a:%c, u.b:%c\n", u.a, u.b);
    c++;
    P = c;
    printf("u.a:%c, u.b:%c\n", u.a, u.b);
    return 0;
}