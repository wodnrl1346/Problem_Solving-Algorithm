import sys
input = sys.stdin.readline

a, b, c, d, e, f = map(int, input().split())

for x in range(-999, 1000):
  for y in range(-999, 1000):
    if a*x + b*y == c and d * x + e * y == f:
      print(x, y)
      break
    
    

#include <iostream>
#include <vector>

using namespace std;

int main(void) {

	int a, b, c, d, e, f;

	cin >> a >> b >> c >> d >> e >> f;

	for (int i = -999; i <= 999; i++) {
		for (int j = -999; j <= 999; j++) {
			if (a * i + b * j == c) {
				if (d * i + e * j == f) {
					cout << i << " " << j;
					break;
				}
			}
		}
	}
}