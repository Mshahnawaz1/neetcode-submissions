class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        total = len(A) + len(B)
        half = total // 2 
        # smaller of two lists
        if len(A) > len(B):
            A, B = B, A
        
        l, r = 0, len(A)-1

        while True:

            mid = (l + r) //2
            R2 = half-mid - 2
            
            Aleft = A[mid] if mid>=0 else float("-infinity")
            Aright = A[mid+1] if mid+1 < len(A) else float("infinity")
            Bleft = B[R2] if R2 >= 0 else float('-infinity')
            Bright = B[R2+1] if R2+1 < len(B) else float('infinity')

            # check if partition is correct
            if Aleft <= Bright and Aright >= Bleft:
                # even
                if (total % 2):
                    return min(Aright, Bright)
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
                
            elif Aleft > Bright: 
                r = mid-1
            else: 
                l = mid+1