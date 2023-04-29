# 근묵자흑: 검은 먹을 가까이 하면 검어진다
# 여러 숫자를 한곳에 모아두면, 시간이 흘러 모든 숫자가 그 중 가장 작은 수에 맞춰 변하게 된다

# 1~N 정수 -> 연속된 K개의 정수 -> 시간이 지나면, K개 중 가장 작은 정수가 된다
# 주어진 수열을 모두 같은 수로 만들고자 할 때 골라야 하는 최소 횟수?

'''
ex) [2, 3, 1, 4]
K = 3일 때 2, 3, 1 을 고르면, 이들은 그 중 가장 작은 수인 1로 변하게 된다.
따라서 [1, 1, 1, 4]가 된다.

또한, 1, 1, 4을 이어서 고르면, [1, 1, 1, 1]이 된다.
따라서 2번만에 모두 같은 수로 만들 수 있다.

n - 수열의 길이
k - 한번에 연속적으로 골라야 하는 정수의 개수(2 이상 n 이하)

공백으로 구분된 n개의 정수(같은 정수는 두 번 이상 나타나지 않는다)
'''

'''
31 36 20 30 1 9 6 13 3 29 11 25 7 8 2 24 34 18 26 15 23 28 37 19 21 4 32 14 16 10 12 27 22 35 5 17 33
31 36 20 30 1 1 1 1			# 2  
3 29 11 
25 7 8 
2 24 34 
18 26 15 
23 28 37

19 21 4
32 14 16 
10 12 27 
22 35 5
17 33				# 10

'''
import math
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
arr = list(map(int, input().split()))

answer = math.inf

start_idx = arr.index(min(arr))
for i in range(k):
	cnt = 1
	front = arr[:start_idx-i]
	back = arr[start_idx+k-i:]

	front_cnt = len(front)//(k-1) + (1 if len(front) % (k-1) != 0 else 0)
	back_cnt = len(back)//(k-1) + (1 if len(back) % (k-1) != 0 else 0)
	answer = min(answer, cnt + front_cnt + back_cnt)
	
print(answer)
