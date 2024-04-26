class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        reverse = str(x)[::-1]                # covert to string, then reverse by slicing
        return (str(x) == reverse)            # compare the strings
