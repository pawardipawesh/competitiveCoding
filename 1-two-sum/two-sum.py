class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_indices = {}
        for i, num in enumerate(nums):
            if num in nums_indices:
                nums_indices[num].append(i)
            else:
                nums_indices[num]= [i]
        
        for i, num in enumerate(nums):
            look_for_1 = target - num

            if look_for_1 in nums_indices:
                indices = nums_indices[look_for_1]
                index = [j for j in indices if j != i][0]  if len(indices) > 1 else indices[0]

                if num == look_for_1 and index == i:
                    continue
                
                return [i, index]
        
        return [-1, -1]
        