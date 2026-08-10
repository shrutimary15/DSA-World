class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        answer = []
        distinct1 = []
        distinct2 = []
        nums1 =set(nums1)
        nums2 = set(nums2)
        for i in nums1:
            if i not in nums2:
                distinct1.append(i)
        for i in nums2:
            if i not in nums1:
                distinct2.append(i)
        answer.append(distinct1)
        answer.append(distinct2)
        return answer
        