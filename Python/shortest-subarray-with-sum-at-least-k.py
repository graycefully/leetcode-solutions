# Time: O(N)
# Space: O(N)

class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if n == 1: 
            return 1 if nums[0] >= k else -1

        '''
        Deques are a generalization of stacks and queues (the name is pronounced “deck” and is short for “double-ended queue”). Deques support thread-safe, memory efficient appends and pops from either side of the deque with approximately the same O(1) performance in either direction.
        '''
        # queue stores indices of prefix.
        queue = collections.deque()
        prefix = [0]
        for num in nums:
            prefix.append(prefix[-1] + num)
        
        min_size = n + 1 
        for index, value in enumerate(prefix): 
            while queue and value <= prefix[queue[-1]]:
                queue.pop()
            while queue and value - prefix[queue[0]] >= k: 
                min_size = min(min_size, index - queue.popleft())
            queue.append(index)

        return min_size if min_size != n + 1 else -1
        
