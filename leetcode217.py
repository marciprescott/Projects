"""Given an integer array nums, return true if any value appears at 
least twice in the array, and return false if every element is distinct."""


# Insert all the values in the set data structure.
# Check if the size of the set is equal to the array then it means all the elements in the array are unique as the set stores unique elements so return false.
# else array contains the duplicate elements so return true.
def contains_duplicate(nums):
    unique_set = set(nums)

    # so if the array length is greater than the length of set then return True because
    # that means that the value appears more than once.
    if len(nums) > len(unique_set):
        return True
    else:
        return False


nums = [1, 2, 3]
result = contains_duplicate(nums)
print(result)
