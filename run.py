def find_min(nums):
    # TODO: implement the function to find the minimum number from a list
    min_element = nums[0]
    for element in nums:
        if element < min_element:
            min_element = element 
    return min_element
    
list = [35, 21, 47, 41, 59, 19, 22, 65, 56, 30, 51]
print(find_min(list))