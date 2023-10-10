class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ln = len(nums)

        k = int(k % ln) if k >= ln else k

        # k, rotate_right = (k, True) if k <= ln // 2 else (ln - k, False)
        # fei, s, e, step = (0, 1, ln, 1) if rotate_right else (-1, -2, -(ln + 1), -1)
        # print(k, rotate_right, fei, s, e, step)

        # fei, s, e, step = (0, 1, ln, 1)

        # for j in range(0, k):
        #     pe = nums[fei]
        #     for i in range(s, e, step):
        #         ce = nums[i]
        #         nums[i] = pe
        #         pe = ce
        #     nums[fei] = pe

        nums_copy = nums[ln-k:]
        # print(nums_copy)

        for i in range(ln-k-1, -1,-1):
            nums[i + k] = nums[i]
        
        for i in range(0, k):
            nums[i] = nums_copy[i]



