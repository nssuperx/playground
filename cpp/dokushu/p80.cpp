#include <iostream>
using namespace std;

struct S {
    int x;
    int y;
};

struct Ss
{
    short xs;
    short ys;
};


struct S2 {
    int x2;
    int y2;
};

union U {
    S s;
    S2 s2;
    Ss ss;
    int a;
    int b;
};

int main() {
    U u = {};
    u.s.x = 10;
    u.s.y = 20;

    u.s2.x2 = 30;
    u.s2.y2 = 40;

    u.a = 50;
    u.b = 60;

    u.ss.xs = 70;
    u.ss.ys = 80;

    cout << u.s.x << endl;
    cout << u.s.y << endl;
}