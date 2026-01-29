class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        if (len(nums) == 2 and nums[0] == 1):
            return [1,2]
        
        if (len(nums) == 2 and nums[0] == 2):
            return [2,1]
        listCompare = list(range(1, len(nums)+1))
        diff = list(set(listCompare) - set(nums))

        seen = set()
        duplicates = set()
        for x in nums:
            if x in seen:
                duplicates.add(x)
            else:
                seen.add(x)
        return [*duplicates, *diff]
