class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        min_l_str = strs[0]
        for str_ in strs[1:]:
            if len(min_l_str) > str:
                min_l_str = str
        
        for i in range(len(min_l_str), 0, -1):
            cp = min_l_str[0:i]

            success = True
            for str_ in strs:
                if str_.startswith(cp):
                    continue
                else:
                    success = False
                    break
            
            if success:
                return cp
        
        return ''




        