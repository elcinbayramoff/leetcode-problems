class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dict1 = {}
        len1 = len(nums1)
        len2 = len(nums2)
        result = []
        for i in range(len1):
            if dict1.get(nums1[i])!=None:
                dict1[nums1[i]]+=1
            else:
                dict1[nums1[i]]=1

        for i in range(len2):
            if dict1.get(nums2[i])!=None and dict1.get(nums2[i])>0:
                dict1[nums2[i]]-=1
                result.append(nums2[i])
        return result