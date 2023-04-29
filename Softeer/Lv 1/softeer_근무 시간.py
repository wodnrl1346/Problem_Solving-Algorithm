import sys
input = sys.stdin.readline

total = 0

for _ in range(5):
    t1, t2 = map(str, input().split())
    t1 = t1.split(':')
    t2 = t2.split(':')

    hour = int(t2[0]) - int(t1[0])
    minute = int(t2[1]) - int(t1[1])

    if minute < 0:
        hour -= 1
        minute += 60

    total += (hour * 60 + minute)

print(total)