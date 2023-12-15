class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Define a dictionary to map Roman numerals to their values
        roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

        result = 0
        prev_value = 0  # To keep track of the previous numeral's value

        # Iterate through the Roman numeral string in reverse
        for char in reversed(s):
            current_value = roman_dict[char]

            # Check if we need to subtract the current value
            if current_value < prev_value:
                result -= current_value
            else:
                result += current_value

            prev_value = current_value

        return result

# Example usage
solution = Solution()
print(solution.romanToInt("III"))       # Output: 3
print(solution.romanToInt("LVIII"))     # Output: 58
print(solution.romanToInt("MCMXCIV"))   # Output: 1994
