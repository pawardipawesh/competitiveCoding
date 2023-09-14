class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        sd = {
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"
        }

        np = 1
        nd = len(digits)

        if nd < 1:
            return []
        
        nr = [1]*(nd)
        for i, digit in enumerate(digits[::-1]):
            nr[nd -1 - i] = np
            np *= 1 if digit not in sd else len(sd[digit])
        

        list_to_return = [""] * np
        for i, digit in enumerate(digits):
            s = sd[digit] if digit in sd else ''
            j = 0
            while j< np:
                for char in s:
                    for _ in range(0, nr[i]):
                        list_to_return[j] += char
                        j += 1
        
        return list_to_return