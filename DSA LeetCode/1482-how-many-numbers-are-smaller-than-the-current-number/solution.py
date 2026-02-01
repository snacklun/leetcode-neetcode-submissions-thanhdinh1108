class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        result = []
        counter = 0
        for i,x in enumerate(nums):
            for j in nums:
               if(j < x and x != j):
                counter = counter +1
            result.append(counter)
            counter = 0
        return result

