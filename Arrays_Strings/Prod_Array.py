# 3. Product of Array Except Self (zeros & negatives)
nums = [4, 2, 3]

'''
def skip(nums,n):
    ans = []
    pro = nums[0]
    for i in range(len(nums)):
        if i == n:
            i += 1

        res = nums[i] * pro
        ans.append(res)

    return ans

def helper(nums):
    for i in range(len(nums)):
        skip(nums, i)

print(helper(nums))
'''


def productExceptSelf_verbose(nums):
    n = len(nums)

    # Build left products array
    left = [1] * n
    for i in range(1, n):
        left[i] = left[i - 1] * nums[i - 1]

    # Build right products array
    right = [1] * n
    for i in range(n - 2, -1, -1):
        right[i] = right[i + 1] * nums[i + 1]

    # Combine left and right
    answer = [left[i] * right[i] for i in range(n)]

    return answer

yes = productExceptSelf_verbose(nums)

print(yes)