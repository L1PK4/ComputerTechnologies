#include <iostream>
#include <string.h>

using namespace std;

int main()
{
    string str;
    cout << "Введите строку: ";
    cin >> str;
    cout << str.substr(str.find('(') + 1, str.find(')') - str.find('(') - 1);
    return 0;
}