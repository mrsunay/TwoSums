class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        solution_dictionary = {}
        for index, value in enumerate(nums):
            solution = target - value
            # See if solution exists in solution_dictionary
            if solution in solution_dictionary:
                return [index, solution_dictionary[solution]]
            
            # Otherwise add to solution_dictionary
            solution_dictionary[value] = index
