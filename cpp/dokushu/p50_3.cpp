#include<iostream>
int main(){
    int i = 0;
    int* ptr;
    ptr = &i;
    *ptr = 42;
    std::cout << i << std::endl;
}