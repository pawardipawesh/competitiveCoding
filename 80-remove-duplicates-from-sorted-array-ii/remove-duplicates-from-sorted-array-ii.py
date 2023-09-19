class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        last_empty = 1
        nr = 1
        nu = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                nr += 1
                if nr > 2:
                    if last_empty == 1:
                        last_empty = i
                else:
                    nu += 1
                    if last_empty != 1:
                        nums[last_empty] = nums[i]
                        last_empty += 1
            else:
                nu += 1
                nr = 1
                if last_empty != 1:
                    nums[last_empty] = nums[i]
                    last_empty += 1
        
        return nu

        