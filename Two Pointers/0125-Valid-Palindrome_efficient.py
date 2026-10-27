# Problem: 125. Valid Palindrome . This is a more efficient solution as it uses C-code machinery
# Time Complexity: O(n) - where n is the length of the string, as we traverse it once.
# Space Complexity: O(1) - utilizing constant extra space with pointers.
# Runtime = 5ms
class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean= re.sub(r'[^a-zA-Z0-9]',"",s).lower()
        return clean==clean[::-1]
