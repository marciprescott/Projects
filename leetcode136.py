"""Given a non-empty array of integers nums, every 
element appears twice except for one. Find that single one.
You must implement a solution with a linear 
runtime complexity and use only constant extra space.

Example 1:

Input: nums = [2,2,1]
Output: 1

"""

from collections import Counter

nums = [4, 1, 2, 1, 2]


def single_number(nums):
    # Storing the freq using Counter

    frequency = Counter(nums)
    # Traversing the Counter dictionary
    for num in frequency:
        # check if any value is 1
        if frequency[num] == 1:
            return num


list1 = [13, 1, 13, 33, 13, 1, 1, 21, 33, 21, 21, 33, 71, 88, 71, 99, 88]
print("The element with a single occurrence is ", int(single_number(list1)))
