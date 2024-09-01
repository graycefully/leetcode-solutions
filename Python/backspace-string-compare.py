# Time: O(N)
# Space: O(1)

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def process(st: str) -> int:
            j = 0
            for i in range(len(st)):
                if st[i] != '#':
                    st[j] = st[i]
                    j += 1
                else:
                    j = max(j - 1, 0)
            return j
        
        s, t = list(s), list(t)
        n, m = process(s), process(t)

        if n != m:
            return False
        for i in range(n):
            if s[i] != t[i]:
                return False
        return True
        
