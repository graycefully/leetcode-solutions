# Time: O(N)
# Space: O(N)

from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        len_s, l, r, result = len(s), 0, len(p) - 1, []
        counter_window = Counter(s[l:r + 1])
        counter_p = Counter(p)
        while r < len_s:
            if counter_window == counter_p:
                result.append(l)
            if r == len_s - 1:
                break
            counter_window[s[l]] -= 1
            counter_window[s[r + 1]] += 1
            l += 1
            r += 1
        return result
        
