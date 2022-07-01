class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        
        # ["flower","flow","flight"]
        # fl
        # not just similar letters
        # get the first n letters that are the same in each word
        # most we have to explore = min(len(s)), where s is a string from list
        # get the smallest string and compare the first x letters
        
        # sort the arrays and look at first and last strings
        strs = sorted(strs)
        minLen = strs[0]
        maxLen = strs[len(strs)-1]
        res = ""
        for i in range(len(minLen)):
            if minLen[i] == maxLen[i]:
                res += minLen[i]
            else:
                break
        return res
