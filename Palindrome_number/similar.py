class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        reverse = 0
        original = x                                 # to compare later
        for i in range(len(str(x))):
            number = x % 10                          # get the last digit
            reverse = reverse * 10 + number           # bring the last digit to the front
            x = x // 10                     # get the front digits (double slash=integer div)
        
        return (reverse == original)


# class Solution:
#     def isPalindrome(self, x: int) -> bool:
#         # Check for negative numbers and numbers ending with 0
#         if x < 0 or (x > 0 and x % 10 == 0):   
#             return False

#         reversedNum = 0
#         while x > reversedNum:
#             reversedNum = reversedNum * 10 + x % 10
#             x = x // 10

#         # At this point, x is either equal to reversedNum or has one less digit
#         return x == reversedNum or x == reversedNum // 10
