class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        alt = [0]
        for i in gain:
            altitude = i+alt[-1]
            alt.append(altitude)
        return max(alt)
        