#include <iostream>
using namespace std;

int main(){
  int x, y, cnt = 0, index;
  cin >> x >> y;

  const char* week[7] = {"SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"};
  int month[13] = {0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};

  for (int i = 1; i<x; i++){
    cnt += month[i];
  }

  y += cnt;

  cout << week[y % 7] << '\n';
  return 0;
}