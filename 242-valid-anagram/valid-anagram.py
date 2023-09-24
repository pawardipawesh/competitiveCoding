from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ls = len(s)
        lt = len(t)
        if ls != lt:
            return False
        
        # sc = Counter(s)
        sc = {}
        for char in s:
            if char not in sc:
                sc[char] = 1
            else:
                sc[char] += 1
        
        for char in t:
            if char not in sc:
                return False
            
            sc[char] -= 1

            if sc[char] < 0:
                return False
        
        sum_sc = sum(sc.values())
        if sum_sc > 0:
            return False
        
        return True
        