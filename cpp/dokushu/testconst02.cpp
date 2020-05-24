#include<iostream>

int main(){
    int a = 42;
    int b = 0;

    int* const ptr = &a;
    std::cout << *ptr << std::endl;
    //ptr = &b;
    *ptr = 100;
    std::cout << *ptr << std::endl;
}