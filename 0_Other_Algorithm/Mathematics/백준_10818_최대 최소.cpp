// 1. vector
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main(){
  int n;
  cin >> n;
  vector<int> v;

  int number;
  for (int i=0; i<n; i++){
    cin >> number;
    v.push_back(number);
  }

  sort(v.begin(), v.end());

  cout << v[0] << " " << v[n-1];
}

//2. array
#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int main(){
  int n;
  cin >> n;
  int array[1000001];

  for (int i=0; i<n; i++){
    cin >> array[i];
  }

  sort(array, array+n);

  cout << array[0] << " " << array[n-1];

  return 0;
}