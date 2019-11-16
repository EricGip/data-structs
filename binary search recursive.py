#recursion requres 2 things,
#1. a base case (usually 0 or 1 elements in an array)
#2. each recursive call has to be shrinking the size of the DSA.

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        #base cases
        ##if its not a list, return 0 - just to be safe lol 
        if not nums:
            return 0
        ##if length of the list is just 1, and the only element isnt equal to target, return 0
        if len(nums) == 1:
            if nums[0] >= target:
                return 0

        #defining mid, the middle point of the array, python auto rounds down
        mid = len(nums)//2
        ##if mid = target, return mid
        if nums[mid] == target:
            return mid
        ##if mid is greater than the target, run the function again, but
        #only with the numbers up to mid.
        elif nums[mid] > target:
            return self.SearchInsert(nums[:mid], target)
        
