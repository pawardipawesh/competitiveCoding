class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        ls = len(s)

        for j in range(len(s)//2, -1, -1):

            lss = j + 1
            if ls % lss == 0:
                m = ls // lss

                if m == 1:
                    continue

                ss = s[0:j+1]

                if s == ''.join([ss] * m):
                    return True
        
        return False
        