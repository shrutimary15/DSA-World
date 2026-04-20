class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l1 = len(word1)
        l2 = len(word2)
        a=""
        
        l = l1 if l1<l2 else l2
        for i in range(l):
            a += word1[i]
            a += word2[i]
        if l2>l1:
            a += word2[l:]
        else:
            a += word1[l:]
        return a


        