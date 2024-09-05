# Time: O(N)
# Space: O(N)

class Solution:
    def reverseVowels(self, s: str) -> str:
        n = len(s)
        s = list(s)
        l, r = 0, n - 1
        vowels = set('AaEeIiOoUu')
        while l < r:
            while s[l] not in vowels and l < r:
                l += 1
            while s[r] not in vowels and l < r:
                r -= 1
            s[r], s[l] = s[l], s[r]
            r -= 1
            l += 1
        return ''.join(s)
        
