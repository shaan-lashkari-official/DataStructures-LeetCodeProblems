class Solution(object):
    def romanToInt(self, s):
        roman_d = {'I':1, 'V':5, 'X': 10, 'L': 50, 'C':100, 'D': 500, 'M': 1000}
        """
        :type s: str
        :type total: int
        :type roman_d: dict
        :type current_char: int
        :type previous_char: int
        :rtype: int

        """
        total = 0
        current_char = 0
        prev_char = 0
        for char in reversed(s):
            current_char = roman_d[char]
            if current_char<prev_char:
                total -= current_char
            else:
                total += current_char
            prev_char = current_char
        return total



        
