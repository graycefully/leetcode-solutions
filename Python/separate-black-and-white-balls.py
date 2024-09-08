# Time: O(N)
# Space: O(1)

class Solution:
    def minimumSteps(self, s: str) -> int:
        swaps, result = 0, 0
        for i in s:
            if i == '1':
                swaps += 1
            else:
                result += swaps
        return result
        
