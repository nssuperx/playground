#include<stdio.h>
#include<crypt.h>
#include<string.h>
#define BUFFSIZE 256

int main(void){
    char original[BUFFSIZE] = "beforecrypt";
    char salt[BUFFSIZE] = "salt";
    char crypted[BUFFSIZE];
    strcpy(crypted, crypt(original, salt));

    printf("crypted str: %s\n", crypted);
    printf("test: %s\n", crypt(original, crypted));
    printf("test: %s\n", crypt(crypted, salt));

    strcpy(salt, "$6$saltsaltsaltsaltsaltsaltsaltsaltsaltsaltsaltsaltsaltsaltsaltsaltsaltsaltsaltsaltsaltsaltsaltsalt");
    strcpy(crypted, crypt(original, salt));
    printf("crypted str: %s\n", crypted);
    printf("test: %s\n", crypt(original, crypted));
    printf("test: %s\n", crypt(crypted, salt));

    return 0;
}
