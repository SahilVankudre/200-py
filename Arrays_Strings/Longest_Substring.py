# 4. Longest Substring Without Repeating Characters

def frec(nums):

    n = len(nums)

    left = [1] * n
    for i in range(1, n):
        left[i] = left[i-1] * nums[i-1]


    right = [1] * n
    for i in range(n-2, -1, -1):
        right[i] = right[i+1] * nums[i+1]

    answer = [left[i] * right[i] for i in range(n)]
    return answer

nums = [2,3,9,7,8,35,28,100]
print(frec(nums))
