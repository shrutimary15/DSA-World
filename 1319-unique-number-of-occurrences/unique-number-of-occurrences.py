class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        hm = {}
        count = []
        for i in arr:
            if i in hm:
                hm[i] = hm[i]+1
            else:
                hm[i] = 1
        for i in hm:
            if hm[i] in count:
                return False 
            else:
                count.append(hm[i])
        return True
        
            