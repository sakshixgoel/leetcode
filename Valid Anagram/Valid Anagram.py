class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s2 = list(s)
        t2 = list(t)
        if sorted(s2) == sorted(t2):
            return True
        else:
            return False
