"""1. 해시 테이블을 이용한 풀이"""
class Solution(object):
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        hash_table = {}
        cnt = 0

        # stone에서 각 문자의 빈도수 count
        for char in stones:
            if char not in hash_table:
                hash_table[char] = 1
            else:
                hash_table[char] += 1

        # jewel이 stone에서 몇개 있는지 count
        for char in jewels:
            if char in hash_table:
                cnt += hash_table[char]

        return cnt
    
"""2. 해시테이블 + defaultdict을 이용한 비교 생략"""
from collections import defaultdict

class Solution(object):
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        freqs = defaultdict(int) # 존재하지 않는 key 값에 초기값을 반환하는 dictionary
        cnt = 0

        # stone에서 각 문자의 빈도수 count
        for char in stones:
            freqs[char] += 1

        # jewel이 stone에서 몇개 있는지 count
        for char in jewels:
            cnt += freqs[char]

        return cnt