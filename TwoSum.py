def twoSum(nums: list[int], target: int) -> list[int]:
    map = {}
    for i in range(len(nums)):
        if target - nums[i] in map:
            return [map[target - nums[i]], i]
        map[nums[i]] = i
    return [0, 0]


print(twoSum([2,7,11,15],9))