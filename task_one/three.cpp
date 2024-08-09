#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    int size, target;
    cin >> size;
    int arr[size];

    for (int i = 0; i < size; i++){
        cin >> arr[i];
    }

    cin >> target;

    int index;
    for (int i = 0; i < size; i++){
        
        if (arr[i] == target){
            index = i;
            break;
        }else {
            index = -1;
        };
    }
    cout << index;
    return 0;
}
