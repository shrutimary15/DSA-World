class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maximum = max(candies)
        final = [True]*len(candies)
        for i in range(len(candies)):
            if candies[i]+extraCandies<maximum:
                final[i] = False
        return final
        