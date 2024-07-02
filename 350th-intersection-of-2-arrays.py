class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        dict1 = {}
        result = []
        for i in nums1:
            dict1[i] = dict1.get(i, 0) + 1

        for i in nums2:
            if dict1.get(i)!=None and dict1.get(i)>0:
                dict1[i]-=1
                result.append(i)
        return result