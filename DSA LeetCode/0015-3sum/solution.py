class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        result = []
        if (len(nums) < 3):
            return result
        
        # len -2 because we have l and r larger than i and prevent out of index
        for index in range(len(nums) - 2):
            l = index + 1
            r = len(nums)-1
            if(index > 0 and nums[index] == nums[index-1]):
                continue
            while l < r:
                if (nums[l] + nums[r] == - nums[index]):
                    result.append([nums[index], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and (nums[l] == nums[l-1]):
                        l += 1
                    while l < r and (nums[r] == nums[r+1]):
                        r -= 1
                else:
                    if (nums[l] + nums[r] > - nums[index]):
                        r -= 1
                    else:
                        l += 1
        return result
