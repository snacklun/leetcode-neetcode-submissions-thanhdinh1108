class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        result = []
        current_sum = 0
        for index in range(len(nums)):
            current_sum += nums[index]
            result.append(current_sum)
        
        return result
