class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        # o = ""
        # try:
        #     w1,w2,w3=strs[0],strs[1],strs[2]
        # except:
        #     if len(strs) == 1:
        #         return strs[0]
        #     else:
        #         return o

        # for i in range(2):
        #     l1,l2,l3=w1[i],w2[i],w3[i]
        #     if (l1 == l2 == l3):
        #         o=o+l1
        #     else:
        #         break
        # return o

        # wordlength = {}
        # for l in range(len(strs)):
        #     wordlength[strs[l]] = len(strs[l])
        # values = list(wordlength.values())
        # values.sort()

        # out = {i: wordlength[i] for i in values}
        # return out

        if len(strs) == 0:
            return ""
        if len(strs) == 1:
            return strs[0]

        minmatchedletter = strs[0]

        for outerloop in range(1, len(strs)):
            word1 = minmatchedletter
            word2 = strs[outerloop]
            temp = ""
            for letterbyletter in range(min(len(word1), len(strs[outerloop]))):
                if word1[letterbyletter] == word2[letterbyletter]:
                    temp += word1[letterbyletter]
                else:
                    break
            minmatchedletter = temp
            
            if minmatchedletter == "":
                break
                
        return minmatchedletter
                
            




print(Solution().longestCommonPrefix(["flower", "flow", "flight", "fauck"]))
