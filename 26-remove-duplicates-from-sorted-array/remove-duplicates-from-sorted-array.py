class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        last_empty = 0
        last_seen = nums[0]
        # dummy = nums[0] - 1
        u = 1
        i = 1
        for num in nums[1:]:
            
            if num == last_seen:
                if last_empty == 0:
                    last_empty = i
                # nums[i] = dummy
            else:
                u += 1
                last_seen = nums[i]
                if last_empty != 0:
                    nums[last_empty] = num
                    last_empty += 1
                    # nums[i] = dummy
            i += 1
        return u
            



        