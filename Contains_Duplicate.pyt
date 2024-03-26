# Input: nums = [1,2,3] || [1,2,3] -> False
# Input: nums = [1,2,3,1] || [1,2,3] -> True

from typing import List

class Solution:
    def ContainsDup(nums: List[int]) -> bool:
        result = []
        for n in nums:
            if n in result:
                return True
            result.append(n)
        return False
    
numbers = [1,2,3,1]
print(f"{Solution.ContainsDup(numbers)}")
