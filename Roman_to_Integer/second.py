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
            current_value = dict[char]               # a variable, takes space, but saves time (no need to check dictionary again and again like in previous code)
            if current_value < previous:             # dict[char] = value of the key 'char'
                answer = answer - current_value
            else:
                answer = answer + current_value
            previous = current_value
        return answer
            
