class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dct = {}

        for i ,x in enumerate (nums):
            #if (y:= target - x) in dct:
            y = target -x
            if y in dct:
                
                return[dct[y], i]
            dct[x] =i    