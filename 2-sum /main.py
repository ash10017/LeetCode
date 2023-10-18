from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_to_index = {}
        
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_to_index:
                return [num_to_index[complement], i]
            num_to_index[num] = i
            
        return []
    
# Test cases
solution = Solution()

nums1, target1 = [2,7,11,15], 9
print(solution.twoSum(nums1, target1))  # [0, 1]

nums2, target2 = [3,2,4], 6
print(solution.twoSum(nums2, target2))  # [1, 2]

nums3, target3 = [3,3], 6
print(solution.twoSum(nums3, target3))  # [0, 1]