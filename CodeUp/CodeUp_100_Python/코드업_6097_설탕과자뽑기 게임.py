h, w = map(int, input().split())

check = []

check = [[0 for col in range(w)] for row in range(h)]

n = int(input())

for _i in range(n):
    l, d, x, y = map(int, input().split())

    for i in range(l):
        if (d == 0):
            check[x - 1][y - 1 + i] = 1
        else:
            check[x - 1 + i][y - 1] = 1

for i in range(h):
    for j in range(w):
        print(check[i][j], end=' ')
    print()