class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        def isp(x):
            lx = len(x)
            if lx <= 1:
                return True
            
            if x[0] == x[-1]:
                return isp(x[1:lx-1])
            else:
                return False
        
        return isp(str(x))
            
        