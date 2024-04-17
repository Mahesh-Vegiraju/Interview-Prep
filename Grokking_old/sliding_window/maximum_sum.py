# PROBLEM
# Given an array of positive numbers and a positive number ‘k’, find the maximum sum of any contiguous subarray of size ‘k’.

# Example 1:

# Input: [2, 1, 5, 1, 3, 2], k=3 
# Output: 9
# Explanation: Subarray with maximum sum is [5, 1, 3].
# Example 2:

# Input: [2, 3, 4, 1, 5], k=2 
# Output: 7
# Explanation: Subarray with maximum sum is [3, 4].

def max_sum(k, arr):
  # initialize window, left, sum, max
  # for i in indices of arr
  #   subtract left from sum
  #   add arr[i] to sum
  #   if sum > max, max = sum
  # return sum


  left, s, max = 0, sum(arr[0:k]), float('-inf')
  for i in range(k, len(arr)):
    s -= arr[left]
    s += arr[i]
    left += 1
    if s > max:
      max = s

  return max


arr, k = [2, 1, 5, 1, 3, 2], 3
assert max_sum(k, arr) == 9

arr, k = [2, 3, 4, 1, 5], 2
assert max_sum(k, arr) == 7
