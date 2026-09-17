# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        l = 1
        u = n
        mid = (l+u)//2
        print(mid)
        ans = guess(mid)
        lower = guess(l)
        upper = guess(u)
        if lower == 0:
            return l
        if upper == 0:
            return u
        while ans != 0:
            print(mid, l, u, ans)
            
            if ans == -1:
                u = mid
            elif ans == 1:
                l = mid
                print(l)
            mid = (l+u)//2
            ans = guess(mid)
        return mid

        