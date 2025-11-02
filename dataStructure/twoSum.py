def twoSum(nums, target):
    # nums = [2, 7, 11, 15]
    # target = 17
    seen = {}
    # seen = {2: 0}
    for i, num in enumerate(nums):
        # i = 0
        # num = 2
        if target - num in seen:
            # target - num = 15
            # seen[target - num] = 3
            return [seen[target - num], i]
        # seen[num] = 0
        seen[num] = i
    return []

# entrada fixa
nums = [2, 7, 11, 15]
#nums = [0,1,2,3]
target = 17

print(twoSum(nums, target))

# Input: nums = [2,7,11,15], target = 17
# Output: [0,3]
# Explanation: Because nums[0] + nums[3] == 17, we return [0, 3].

# steps

#nums = [2, 7, 11, 15]
#target = 17
# return [0, 3]

# seen = {}

# repeat for i, num in enumerate(nums): 
# i = 0
# num = 2
# if target - num in seen: (17 - 2 = 15) -> false
# seen[num] = i  -> seen[2] = 0  -> seen =
# repeat for i, num in enumerate(nums):
# i = 1
# num = 7
# if target - num in seen: (17 - 7 = 10) -> false
# seen[num] = i  -> seen[7] = 1  -> seen =
# repeat for i, num in enumerate(nums):
# i = 2
# num = 11
# if target - num in seen: (17 - 11 = 6) -> false
# seen[num] = i  -> seen[11] = 2  -> seen =
# repeat for i, num in enumerate(nums):
# i = 3
# num = 15
# if target - num in seen: (17 - 15 = 2) -> true
# return [seen[target - num], i] -> return [seen[2], 3] -> return [0, 3]