class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        ln = len(nums)
        i = 0
        j = ln - 1

        while i < j:
            while i < ln and nums[i] % 2 == 0:
                i += 1
            
            while j >= 0 and nums[j] % 2 !=0:
                j -= 1
            
            if i > j:
                break
            
            tmp = nums[i]
            nums[i] = nums[j]
            nums[j] = tmp
            i += 1
            j -= 1
        
        return nums
            

        