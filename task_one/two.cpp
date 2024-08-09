#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


void repeatString (string text, int count) {
    for (int j = 0; j < count; j++)
    {
        cout << text;
    }
}

int main() {
    int hight;
    cin >> hight;

    for (int i = 1; i <= hight; i++)
    {
        repeatString("*", i);
        cout << endl;
    }
    
    return 0;
}
