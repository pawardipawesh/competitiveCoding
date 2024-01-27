class Solution:
    def minSwaps(self, data: List[int]) -> int:
        window_size = sum(data)
        
        curr_window_n_ones = sum(data[0:0 + window_size])
        curr_window_n_swaps = window_size - curr_window_n_ones
        for i in range(1, len(data) - window_size + 1):
            curr_window_n_ones = curr_window_n_ones - data[i-1] + data[i + window_size - 1]
            temp_n_swaps = window_size - curr_window_n_ones
            curr_window_n_swaps = temp_n_swaps if temp_n_swaps < curr_window_n_swaps else curr_window_n_swaps
        
        return curr_window_n_swaps

        