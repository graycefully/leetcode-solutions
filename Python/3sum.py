# Time: O(N^2)
# Space: O(1)

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n, result = len(nums), []
        nums.sort()
        for i in range(0, n - 2):
            if i != 0 and nums[i] == nums[i - 1]:
                continue
            l, r = i + 1, n - 1
            while l < r:
                cur_sum = nums[i] + nums[l] + nums[r]
                if cur_sum == 0:
                    result.append([nums[i], nums[l], nums[r]])
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                    l += 1
                    r -= 1
                elif cur_sum < 0:
                    l += 1
                else:
                    r -= 1
        return result
        
