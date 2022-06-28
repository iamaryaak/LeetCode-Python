# 3. Longest Substring Without Repeating Characters
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
	res = 0
	charSet = set() # set disallows duplicates
	
	# add sliding window
	l = 0 # r = right will be moving as we move through the string
	
	# loop through string
	for r in range(len(s)):
		while s[r] in charSet:
			# duplicate detected
			# remove the left most char
			charSet.remove(s[l])
			l = l+1
		# no duplicate
		charSet.add(s[r])
		res = max(res, r-l+1)
	return res
