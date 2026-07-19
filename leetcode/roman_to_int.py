class Solution:
    def romanToInt(self, s: str) -> int:
        # {s: i}
        roman = {"I": 1, "V": 5, "X": 10,
            "L": 50, "C": 100, "D": 500, "M": 1000}
        
        result = 0
        for i in range(len(s)):
            current_value = roman[s[i]]
            next_value = roman[s[i+1]] if i+1 < len(s) else 0
            
            if current_value < next_value:
                result -= current_value
            else:
                result += current_value
        return result 