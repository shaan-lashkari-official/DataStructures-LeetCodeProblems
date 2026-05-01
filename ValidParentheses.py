class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool

        """
        stack = []
        brackets = {"{":"}", "(":")", "[":"]"}
        bracketclosed = {"}":"{", ")":"(", "]":"["}
        if len(s) % 2 != 0:
            return False
        count = 0
        for i in s:
            count += 1
            if i in brackets.keys():
                stack.append(i)
                
            elif i in bracketclosed.keys():
                
                if len(stack) == 0:
                    return False
                if stack[len(stack)-1] == bracketclosed[i]:


                    stack.pop()

                    if len(stack) == 0 and count == len(s):
                        return True

                else :
                    return False
            else:
                return False

        if len(stack) >0:
            return False
