#include<iostream>
int main(){
    float f = 100.001f;
    f -= 100.0f;
    std::cout << f << std::endl;
}