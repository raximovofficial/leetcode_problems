class Solution:
    def buildArray(self, nums: list[int]) -> list[int]:
        ans = []
        for i in range(len(nums)):
            ans.append(nums[nums[i]])
        return ans

nums = [0,2,1,5,3,4]
a = Solution()
print(a.buildArray(nums))