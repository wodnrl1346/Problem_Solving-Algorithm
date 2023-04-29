import sys
input = sys.stdin.readline

w, n = map(int, input().split())    # 배낭의 무게, 귀금속의 종류

metal_weight_per_price = []

for _ in range(n):
    m, p = map(int, input().split())    # 금속의 무게, 무게 당 가격
    metal_weight_per_price.append((p, m))    

# 그리디 알고리즘
# 무게 당 가격이 높은 거를 높은 기준으로 삼는다.

# 내림차순 정렬
metal_weight_per_price = sorted(metal_weight_per_price, key=lambda x:x[0], reverse=True)

price_sum = 0
left_w = w

for i in range(n):
    left_w = left_w - metal_weight_per_price[i][1]
    if left_w > 0:
        price = metal_weight_per_price[i][0] * metal_weight_per_price[i][1]
        price_sum += price

    elif left_w < 0:
        price = metal_weight_per_price[i][0] * (left_w + metal_weight_per_price[i][1])
        price_sum += price
        break

    else:
        price = metal_weight_per_price[i][0] * metal_weight_per_price[i][1]
        price_sum += price
        break

print(price_sum)
