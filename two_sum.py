'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict_c_idx = {}
        list_solution = None
        for i,val in enumerate(nums):
            diff = target - val
            if(diff in dict_c_idx.keys()):
                list_solution  = [dict_c_idx[diff], i]
                break
            dict_c_idx[val] = i
        return list_solution
