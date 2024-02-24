# def find_shortest_sub_array(nums):

nums = [1, 2, 2, 3, 1, 4, 2]
list1 = []
count = 0
for item in nums:
    if item in list1:
        count += 1
    else:
        list1.append(item)
        
print(list1, count)
