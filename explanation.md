## Explanation:
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].


## Approach (Using Hashmap)

We solve this problem efficiently with a **hashmap**.

1. Create an empty dictionary to store numbers and their indices.  
2. Loop through the array using `enumerate` to get both index and number.  
3. For each number `x`, calculate its complement: `y = target - x`.  
4. If `y` exists in the dictionary, return the stored index of `y` and the current index `i`.  
5. Otherwise, store `x` with its index in the dictionary.  

This way, we only loop once through the array.

---

## Complexity
- **Time Complexity:** O(n)  
- **Space Complexity:** O(n)  

---

## Python Solution
```python
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dct = {}
        for i, x in enumerate(nums):
            y = target - x
            if y in dct:
                return [dct[y], i]
            dct[x] = i
