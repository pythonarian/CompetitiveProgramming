# https://leetcode.com/problems/running-sum-of-1d-array/description/

class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        res = list()
        res.append(nums[0])
        for i in range(1, len(nums)):
            res.append(res[i-1] + nums[i])
        return res;

    
n = Solution()
nums = [1,2,3,4]
print(n.runningSum(nums))
