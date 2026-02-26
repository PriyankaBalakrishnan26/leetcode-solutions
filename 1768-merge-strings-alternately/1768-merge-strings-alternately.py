class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        from itertools import zip_longest
        
        result = ""
        
        for ch1, ch2 in zip_longest(word1, word2, fillvalue=""):
            result += ch1 + ch2
        
        return result

