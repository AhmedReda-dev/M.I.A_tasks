#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    int rows, columns;
    cin >> rows;
    cin >> columns;

    int heros[rows][columns];
    int villains[rows][columns];
    // heros input
    for (int i = 0; i < rows; i++)
    {
        for (int j = 0; j < columns; j++)
        {
            cin >> heros[i][j];
        };
    };
    // villains input
    for (int i = 0; i < rows; i++)
    {
        for (int j = 0; j < columns; j++)
        {
            cin >> villains[i][j];
        };
    };

    int herosScore = 0, villainsScore = 0;
    // get score
    for (int i = 0; i < rows; i++)
    {
        for (int j = 0; j < columns; j++)
        {
            if (heros[i][j] > villains[i][j])
            {
                herosScore += 1;
            }
            else if (heros[i][j] < villains[i][j])
            {
                villainsScore += 1;
            }
        };
    };
    // check score
    if (herosScore > villainsScore)
    {
        cout << "Justice League";
    }
    else if (herosScore < villainsScore)
    {
        cout << "Villains";
    }
    else
    {
        cout << "Tie";
    }

    return 0;
}
