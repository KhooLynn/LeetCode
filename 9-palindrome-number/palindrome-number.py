class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x = str(x)
        for character in range(len(x)):
            #x[-1-character]: get the character character positions from the end of the string.
            if x[character] != x[-1-character]:
                return False
        return True


