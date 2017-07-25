#include <iostream>
#include <vector>
#include <algorithm>
#include <functional>
using namespace std;

int doSomething(const int a, int b){
    b += a * b; // THIS SHOULD BE CAUGHT BY THE INDENTATION CHECKER
  return b;
}

void doSomethingElse(){
  cout << "I don't know what this program does!" << endl;
}

/* Checker shouldn't catch multiline comments
Blah Blah Blah
*/

int main(void){
  int a = 5;
  int b = 10;
  int sum = a + b;
  for (int i = 0; i < 100; i++){
    cout << "Hello, World!" << endl;
    while (i > 25){
      cout << "Entering this weird loop" << endl;
      for (int j = 0; j < 10; j++){
              cout << "This is getting even more weird" << endl; // THIS SHOULD BE CAUGHT BY THE INDENTATION CHECKER
        while (j < 7){
        cout << "Why am I doing this" << endl; // THIS SHOULD BE CAUGHT BY THE INDENTATION CHECKER
          j++;
        }
      }
      i++;
  } // THIS SHOULD BE CAUGHT BY THE INDENTATION CHECKER
  }
  return 0;
}
