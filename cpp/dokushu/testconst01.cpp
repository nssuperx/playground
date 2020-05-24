#include<iostream>

int main(){
    const int a = 42;
    const int b = 0;

    const int* ptr = &a;
    std::cout << *ptr << std::endl;
    ptr = &b;
    std::cout << *ptr << std::endl;
}