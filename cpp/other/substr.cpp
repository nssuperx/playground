#include<iostream>
#include<string>
using namespace std;

int main(){
    string s;
    s = "0123456789";
    cout << s.substr(2, 100) << endl;
}