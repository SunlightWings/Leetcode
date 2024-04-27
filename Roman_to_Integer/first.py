class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        answer = 0
        previous = 0
        reverse = s[::-1]                         # reverse the string. (to subtract if the small comes first)
        dict = {'I' : 1, 'V' : 5, 'X' : 10, 'L' : 50, 'C' : 100, 'D' : 500, 'M' : 1000}
        
        for char in reverse:
            if dict[char] < previous:             # dict[char] = value of the key 'char'
                answer = answer - dict[char]
            else:
                answer = answer + dict[char]
            previous = dict[char]
        return answer
            
