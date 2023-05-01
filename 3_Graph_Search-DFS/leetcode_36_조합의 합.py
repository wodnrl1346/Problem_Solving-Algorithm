'''DFS로 중복 조합 그래프 탐색'''

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def dfs(csum, index, path):
            if csum < 0:
                return
            elif csum == 0:
                result.append(path)

            for i in range(index, len(candidates)):
                dfs(csum-candinates[i], i, path+candinates[i])

        dfs(target, 0, [])

        return result