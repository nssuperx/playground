#include<stdio.h>

#define BUFASCII 128

int main(void){
    char a[BUFASCII],b[BUFASCII];
    int suuji[BUFASCII];
    for(int i = 0;i<BUFASCII;i++){
        suuji[i] = i;
        a[i] = i;
    }

    printf("suuji['a'] == %d\n",suuji['a']);
    printf("suuji[a[]] == %c\n",suuji[a[suuji['g']]]);
    return 0;
}