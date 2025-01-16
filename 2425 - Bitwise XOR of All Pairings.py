class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:

        # If both arrays are even the XOR operator will cancel out the number giving a result of 0.
        # If one of the arrays is even and one is odd then you just need to XOR the even array to the result.
        # If both arrays odd then you have to XOR both arrays together because they will not cancel out. 

        result = 0

        if len(nums1) % 2 == 1:
            for number in nums2:
                result ^= number

        if len(nums2) % 2 == 1:
            for number in nums1:
                result ^= number

        return result
