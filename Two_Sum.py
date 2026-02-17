# 1. Two Sum variants (indices, count pairs, unique pairs)

# For unsorted lists
def sms(nums, target):
    left = 0
    right = len(nums) - 1

    while left < right:
        current_sum = nums[left] + nums[right]

        if current_sum == target:
            # Found the pair!
            return [left, right]
        elif current_sum < target:
            # Sum too small, need larger number
            left += 1
        else:
            # Sum too large, need smaller number
            right -= 1

    # No solution found
    return [-1]

# For the sorted lists
def hash(nums, target):
    hm = {}
    n = len(nums)

    for i in range(n):
        c = target - nums[i]
        if c in hm:
            return [hm[c],i]
        hm[nums[i]] = i
    return -1


nums = [3,6,4,5,0,8,1,9]
target = 1
print(hash(nums,target))



