class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        nums3 = [0] * (m + n)
        i = 0
        j = 0
        k = 0
        while i < m and j < n:
            if nums1[i] <= nums2[j]:
                nums3[k] = nums1[i]
                i += 1
                k += 1
            else:
                nums3[k] = nums2[j]
                j += 1
                k += 1
        
        # print(i, j, k, nums3)

        if i >= m and j >=n:
            pass
        elif i < m:
            for e in nums1[i:m]:
                nums3[k] = e
                k += 1
        else:
            for e in nums2[j:n]:
                nums3[k] = e
                k += 1
        
        for i, e in enumerate(nums3):
            nums1[i] = e



            
        