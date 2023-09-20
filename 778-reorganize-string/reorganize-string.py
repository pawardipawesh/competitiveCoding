class Solution(object):
    def reorganizeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        d = {}
        for char in s:
            if char in d:
                d[char] += 1
            else:
                d[char] = 1
        
        sl = len(s)
        l = [''] * sl
        i = 0
        for char, num_occ in sorted(d.items(), key=lambda x: x[1], reverse=True):
            if num_occ > (sl // 2 if sl%2 == 0 else (sl // 2) + 1):
                return ""
            
            for j in range(num_occ):
                l[i] = char
                i += 2

                if i >= sl:
                    i = 1
        return ''.join(l)
            
            
            
            

            
            




        