#include<iostream>
#include<string>

int main(){
    char str1[] = {'a', 'b', 'c', '\0', 'd', 'e'};
    std::cout << str1 << std::endl;

    std::string str2{'a', 'b', 'c', '\0', 'd', 'e'};
    std::cout << str2 << std::endl;
    return 0;
}