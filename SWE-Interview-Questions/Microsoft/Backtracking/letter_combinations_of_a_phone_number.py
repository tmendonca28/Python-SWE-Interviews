from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        mapping = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        result = []
        self.dfs(digits, mapping, 0, "", result)
        return result

    def dfs(self, digits, mapping, index, path, result):
        if len(path) == len(digits):
            result.append(path)
            return
        for i in range(index, len(digits)):
            for j in mapping[digits[i]]:
                self.dfs(digits, mapping, i+1, path+j, result)

    

if __name__== "__main__":
    print(Solution.letterCombinations(digits="23"))