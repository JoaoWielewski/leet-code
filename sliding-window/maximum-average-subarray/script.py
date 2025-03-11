from typing import List

nums = [1,12,-5,-6,50,3]
k = 4


def find_max_average(nums: List[int], k: int) -> float:
    start_index = 1
    max_total = total = sum(nums[:k])

    while start_index < len(nums) - k + 1:
        total = total - nums[start_index - 1] + nums[start_index + k - 1]

        if total > max_total:
            max_total = total
        
        start_index += 1
    
    return max_total / k

print(find_max_average(nums, k))