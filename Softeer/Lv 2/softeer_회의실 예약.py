# 회의실 수:n, 예약된 회의수:m
n, m = map(int, input().split())

room = {}
for i in range(n):
    name = input()
    room[name] = [0] * 18

for i in range(m):
    name, start, end = input().split()
    start = int(start)
    end = int(end)

    for j in range(start, end):
        room[name][j] = 1

room = sorted(room.items())

for i in range(n):
    current = 1
    temp = []
    for j in range(9, 18):
        if current == 1 and room[i][1][j] == 0:
            sTime = j
            current = 0
        elif current == 0 and room[i][1][j] == 1:
            fTime = j
            current = 1
            temp.append([sTime, fTime])

    if current == 0:
        temp.append([sTime, 18])

    print(f'Room {room[i][0]}:')
    if len(temp) == 0:
        print("Not available")
    else:
        print(len(temp), 'available:')
        for j in range(len(temp)):
            print(f'{temp[j][0]:02d}-{temp[j][1]}')

    if i != n-1:
        print("-----")  