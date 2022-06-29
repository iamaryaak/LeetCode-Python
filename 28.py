class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # find needle in haystack
        # search for first needle character in haystack, 
        # found: then look for second right after
        # else keep looking for first character again til end
        # not found: -1
        
        found = -1
        
        for i in range(len(haystack)):
                if needle == haystack[i:i+len(needle)]:
                    found = i
                    break
        
        return found
            
