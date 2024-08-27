# Time: O(N)
# Space: O(N)

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        len_s, l, r, max_len = len(s), 0, 0, 0
        cur_set = set(s[l:r + 1])
        while r < len_s:
            cur_len = len(cur_set)
            max_len = cur_len if cur_len > max_len else max_len
            if r == len_s - 1:
                break
            r += 1
            if s[r] in cur_set:
                while s[l] != s[r]:
                    cur_set.remove(s[l])
                    l += 1
                l += 1
            else:
                cur_set.add(s[r])
        return max_len
