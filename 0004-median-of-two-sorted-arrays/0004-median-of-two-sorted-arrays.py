class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        low, high = 0, m
        total_left = (m + n + 1) // 2

        while low <= high:
            i = (low + high) // 2
            j = total_left - i

            A_left = nums1[i - 1] if i > 0 else float('-inf')
            A_right = nums1[i] if i < m else float('inf')
            B_left = nums2[j - 1] if j > 0 else float('-inf')
            B_right = nums2[j] if j < n else float('inf')

            if A_left <= B_right and B_left <= A_right:
                if (m + n) % 2 == 1:
                    return float(max(A_left, B_left))
                else:
                    return (max(A_left, B_left) + min(A_right, B_right)) / 2.0

            elif A_left > B_right:
                high = i - 1
            else :
                low = i + 1

        return 0.0