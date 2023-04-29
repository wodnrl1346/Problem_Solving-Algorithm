# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
x, y = map(int, input().split())

d = int(input())

# 진우 / 선우
# 진우가 밤 증에 자신의 식량 절반을 선우에게 가져다 주었다
# 그 다음날 밤, 선우는 자신의 식량 절반을 진우에게 가져다 주었다
# 가지고 있는 식량의 양이 홀수이면, 그 식량을 통째로 넘겨준다
# 처음에 두 형제는 모두 식량을 100개 씩 가지고 있다.

#	진우	선우
#	100		100
#	50		150
#	125		75
#	62		138

tem = 0

for _ in range(d):
	if tem == 0:	# x가 절반을 나눠줄 때		
		if x % 2 == 0:
			y += x // 2
			x -= x // 2
		else:
			y += (x // 2 + 1)
			x -= (x // 2 + 1)
		
		tem = 1
		continue
		
	elif tem == 1:	# y가 절반을 나눠줄 때
		if y % 2 == 0:
			x += y // 2
			y -= y // 2
		else:
			x += (y // 2 + 1)
			y -= (y // 2 + 1)	
		tem = 0
		continue

print(x, y)

''' 
1 1

0 2
1 1
0 2
1 1
0 2
1 1
0 2
1 1
0 2
'''
