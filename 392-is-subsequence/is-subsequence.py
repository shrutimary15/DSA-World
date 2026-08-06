class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        match = 0
        for letter in t:
            if i < len(s):
                if s[i] == letter:
                    i += 1
                    match += 1
        if match == len(s):
            return True
        return False

        