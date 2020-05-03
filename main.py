from typing import List


class Solution:

  def findDuplicate(self, nums: List[int]) -> int:
    obj = {}
    for num in nums:
      if num not in obj:
        obj[num] = 1
      else:
        obj[num] += 1

    for keyNumber in obj.keys():
      if obj[keyNumber] > 1:
        return keyNumber

    return None


my = Solution()
n = [1, 3, 4, 2, 2]
ans = my.findDuplicate(n)
print("ans", ans)
'''
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
