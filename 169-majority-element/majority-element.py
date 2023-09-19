class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = {num: 0 for num in nums}
        needed = len(nums) // 2
        for num in nums:
            d[num] += 1
        
        for num, occu in d.items():
            if occu > needed:
                return num
        
        return -1
                





        