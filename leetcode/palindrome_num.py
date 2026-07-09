class Solution:
    def isPalindrome(self, x: int) -> bool:
        reversed_x = int(str(abs(x))[::-1])
        if x == reversed_x:
            return True
        else:
            return False

'''
# OR EVEN SHORTER VERSION

class Solution:
    def isPalindrome(self, x: int) -> bool: 
        return x == int(str(abs(x))[::-1])

NOTES/ 
learned:
polindrome number is any number that reads the exact same forward and backwards.
[::-1] is used to reverse a string

'''