class Solution:
    def isPalindrome(self, s: str) -> bool:
        ptr_one = 0
        ptr_two = len(s) - 1
        while ptr_one <= ptr_two:
            asc_one = s[ptr_one]
            asc_two = s[ptr_two]
            if not (asc_one.isalnum()):
                ptr_one += 1
                continue
            if not asc_two.isalnum():
                ptr_two -= 1
                continue
            if s[ptr_one].casefold() != s[ptr_two].casefold():
                return False
            ptr_one += 1
            ptr_two -= 1
        return True