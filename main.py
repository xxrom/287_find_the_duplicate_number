from typing import List

# time O(N*logN)/ memory O(1)


class Solution:

  def findDuplicate(self, nums: List[int]) -> int:
    # first 0 for edge case with [1,1,2]
    # because ans always should be the high number ...
    low = 0
    high = len(nums) - 1
    mid = low + (high - low) // 2
    count = 0

    while high - low > 1:
      # Important to get int value, not float,
      # otherways it will break everything ... =(
      mid = low + (high - low) // 2
      # print('low %.2f, mid %.2f, high %.2f' % (low, mid, high))

      count = 0
      for num in nums:
        if mid < num <= high:
          count += 1

      # print('count %d' % count)
      if count > high - mid:
        # ans from [mid, high]
        low = mid
      else:
        # ans from [low, mid]
        high = mid

    # print('low %.2f, mid %.2f, high %.2f' % (low, mid, high))
    return high


my = Solution()
n = [1, 1, 2]
# n = [3, 1, 3, 4, 2]
# n = [1, 3, 4, 2, 2]
ans = my.findDuplicate(n)
print("ans", ans)

# Runtime: 72 ms, faster than 40.63% of Python3 online submissions for Find the Duplicate Number.
# Memory Usage: 16.3 MB, less than 7.14% of Python3 online submissions for Find the Duplicate Number.
'''
explanation:
URl: https://leetcode.com/problems/find-the-duplicate-number/discuss/73022/Python-Solution-with-O(1)-space-and-O(nlogn)-time
[1 2 3 4 5 5]
SOLUTION - like binary search but with numbers from [1 to n]

# 0
low = 1
high = 5
mid = 3

count = 0
for num in nums:
  if mid < num <= high:
    count += 1
count = 4,5,5 = 3
(3 > 2 (high - mid (5-3=2)))=> solution from [mid to high] numbers
=> low = mid (elif => high = mid)

# 1
low = 3
high = 5
mid = 4

for num in nums:
  if mid < num <= high:
    count += 1
count = 5,5 = 2
(2 > 1 (high - mid (5-4=1))) => solution from [mid to high] numbers

# 2
low = 4
high = 5
mid = 4.5

for num in nums:
  if mid < num <= high:
    count += 1
count = 5,5 = 2
(2 > 0.5 (high - mid (5 - 4.5 = 0.5))) => solution from [mid to high] numbers
low = mid (4.5)

END (high - low < 1) => ans - high
'''
