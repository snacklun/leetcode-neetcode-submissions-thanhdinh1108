class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        numbers = list(range(1, len(nums) + 1))
        missing_numbers = list(set(numbers) - set(nums))
        return missing_numbers
