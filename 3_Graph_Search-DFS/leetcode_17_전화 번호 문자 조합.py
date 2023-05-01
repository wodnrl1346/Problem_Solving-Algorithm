'''모든 조합 탐색'''

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        graph = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        answer = []

        # 예외처리
        if not digits:
            return []

        def dfs(index, path):
            if len(path) == len(digits):
                answer.append(path)

            for i in range(index, len(digits)):
                for j in graph[digits[i]]:
                    dfs(i+1, path+j)

        dfs(0, "")

        return answer