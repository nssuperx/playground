#include <stdio.h>

typedef struct{
    unsigned bf1: 6;
    unsigned bf2: 7;
}Boolean;

int main() {
    Boolean b;
    b.bf1 = 125;
    printf("%d\n" , b.bf1);
    printf("%x\n" , b.bf1);

    b.bf2 = 125;
    printf("%d\n" , b.bf2);
    printf("%x\n" , b.bf2);

    return 0;
}