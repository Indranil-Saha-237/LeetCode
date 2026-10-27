# Problem: 125. Valid Palindrome
# Time Complexity: O(n) - where n is the length of the string, as we traverse it once.
# Space Complexity: O(1) - utilizing constant extra space with pointers.
class Solution:
    def isPalindrome(self, s: str) -> bool:
        num = ""
        for i in s:
            if i.isalnum():
                num += i.lower()

        return num ==num[::-1]