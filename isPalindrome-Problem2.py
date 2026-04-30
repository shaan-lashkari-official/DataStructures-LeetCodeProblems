class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        values = list(map(str, str(x)))
        list_b = values[::-1]

        return values == list_b
