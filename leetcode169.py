"""Given an array nums of size n, return the majority element.
The majority element is the element that appears 
more than ⌊n / 2⌋ times. You may assume that the majority 
element always exists in the array.
"""


def get_majority_element(nums):
    counts = {}
    for num in nums:
        counts[num] = counts.get(num, 0) + 1
    majority_count = max(counts.values())
    for num, count in counts.items():
        if count == majority_count:
            return num


nums = [2, 2, 1, 1, 1, 2, 2]
print(get_majority_element(nums))
