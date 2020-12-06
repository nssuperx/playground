#include<iostream>
using namespace std;

struct S
{
    int a;
    int32_t b;
    int c;
};

union U
{
    int a;
    char b;
    int c;
};

enum E
{
    value1,
    value2,
    value3
};

enum class Ec
{
    value1,
    value2,
    value3,
};

int main(){
    S s;
    U u;
    E e = value1;
    Ec ec = Ec::value1;
    
    s.a = 1;
    s.b = 2;
    s.c = 3;
    cout << "s.a:" << s.a << endl;
    cout << "s.b:" << s.b << endl;
    cout << "s.c:" << s.c << endl;
    cout << "&s.a:" << &s.a << endl;
    cout << "&s.b:" << &s.b << endl;
    cout << "&s.c:" << &s.c << endl;

    u.a = 1;
    cout << "u.a:" << u.a << endl;
    cout << "u.b:" << u.b << endl;
    cout << "u.c:" << u.c << endl;

    u.b = 'a';
    cout << "u.a:" << u.a << endl;
    cout << "u.b:" << u.b << endl;
    cout << "u.c:" << u.c << endl;

    cout << "&u.a:" << &u.a << endl;
    cout << "&u.b:" << &u.b << endl;
    cout << "&u.c:" << &u.c << endl;
    return 0;
}