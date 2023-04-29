import sys
input = sys.stdin.readline

light = {
	'0': '1111110',
	'1': '0110000',
    '2': '1101101',
    '3': '1111001',
    '4': '0110011',
    '5': '1011011',
	'6': '1011111',
	'7': '1110010',
	'8': '1111111',
	'9': '1111011',
	' ': '0000000'
}

t = int(input())

for _ in range(t):
	a, b = input().split()	# a='9881', b='10724'

	a = (5-len(a))* ' ' + a
	b = (5-len(b))* ' ' + b

	total = 0
	for i in range(5):
		for j in range(7):
			total += (light[a[i]][j] != light[b[i]][j])

	print(total)