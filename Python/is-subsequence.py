# Time: O(N)
# Space: O(1)

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        slen, tlen = len(s), len(t)
        sp = tp = 0
        while sp < slen and tp < tlen:
            if s[sp] == t[tp]:
                sp += 1
            tp += 1
        return sp == slen
        
