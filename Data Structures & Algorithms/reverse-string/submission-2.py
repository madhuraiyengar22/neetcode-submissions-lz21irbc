class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l = len(s) - 1 # last element will be l-1 because of 0 indexing
        for i in range(l//2 + 1): # if 2 elements, 0 will be the range, hence +1
            s[i], s[l-i] = s[l-i], s[i]