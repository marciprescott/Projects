"""Given an array nums. We define a running sum of an 
array as runningSum[i] = sum(nums[0]…nums[i]).
Return the running sum of nums
Input = [1,2,3,4]
Output = [1,3,6,10]
"""


def runningSum(nums):
    new_list = []
    j = 0

    for i in range(0, len(nums)):
        j += nums[i]
        new_list.append(j)
    return new_list


nums = [1, 4, 66, 88]
print(runningSum(nums))
