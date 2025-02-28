from typing import List

nums1 = [1,2,3]
nums2 = [2,4,6]


def find_difference(nums1: List[int], nums2: List[int]) -> List[List[int]]:
    set1 = set(nums1)
    set2 = set(nums2)

    answer = [list(set1 - set2), list(set2 - set1)]

    return answer


print(find_difference(nums1, nums2))