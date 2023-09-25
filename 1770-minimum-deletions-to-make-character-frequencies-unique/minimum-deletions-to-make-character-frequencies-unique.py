class Solution:
    def minDeletions(self, s: str) -> int:
        sc = Counter(s)
        cts = set()
        d = 0
        for s, c in sc.items():
            if c not in cts:
                cts.add(c)
            else:
                d += 1
                c -= 1
                while c in cts and c > 0:
                    d += 1
                    c -= 1
                
                cts.add(c)
        return d
                    





        