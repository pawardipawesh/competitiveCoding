class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        ls = len(s)

        mid = len(s)//2

        i = 0
        for j in range(mid, i-1, -1):

            lss = j + 1
            if ls % lss == 0:
                m = ls // lss

                if m == 1:
                    continue

                ss = s[i:j+1]

                if s == ''.join([ss] * m):
                    return True
        
        return False
        