def subset_sum(nums, target, index=0):
    if target == 0:
        return True
    if index >= len(nums) or target < 0:
        return False
    
    include = subset_sum(nums, target - nums[index], index + 1)
    exclude = subset_sum(nums, target, index + 1)
    
    return include or exclude

# Example usage:
nums = [3, 34, 4, 12, 5, 2]
target = 9