class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        max_arr, left, right, q = [], 0, 0, deque()
        while right < len(nums):
            while q and nums[q[-1]] < nums[right]:
                q.pop()

            q.append(right)

            if left > q[0]:
                q.popleft()

            if right + 1 >= k:
                left += 1
                max_arr.append(nums[q[0]])
            right += 1
        return max_arr
