class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dictionary = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        total = 0
        for i in range(len(s) - 1):
            if dictionary[s[i]] < dictionary[s[i+1]]:
                total -= dictionary[s[i]]
            else:
                total += dictionary[s[i]]
        total += dictionary[s[-1]]
        return total