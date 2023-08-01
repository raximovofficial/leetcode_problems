class Solution:
    def getConcatenation(self, nums: list[int]) -> list[int]:
        ans = nums + nums
        return ans

nums = [1,2,1]
a = Solution()
print(a.getConcatenation(nums))