import statistics

class Solution:
    def medianSortedArray(self, array):
        l = len(array)
        if l % 2 == 1:
            return array[l // 2]
        return array[l // 2 - 1] + 1 / 2

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) == 0:
            return self.medianSortedArray(nums2)
        if len(nums2) == 0:
            return self.medianSortedArray(nums1)
        if len(nums1) + len(nums2) == 4:
            return self.fakit(nums1, nums2, 0, 0)
        if len(nums1) < len(nums2):
            nums1, nums2 = nums2, nums1
        partition_len = (len(nums1) + len(nums2)) // 2
        l1 = l2 = 0
        r1 = len(nums1) - 1
        r2 = len(nums2) - 1
        dikens = 10
        while dikens > 0:
            mid1 = (l1 + r1) // 2
            p2 = partition_len - mid1
            while p2 < 0:
                p2 += 1
                mid1 -= 1
            print(f"Nums 1 Mid1:{mid1} P1:{nums1[:mid1]} Nums 1 P2:{nums1[mid1:]}")
            print(f"Nums 2 Mid2:{p2} P1:{nums2[:p2]} Nums 2 P2:{nums2[p2:]}")
            print(f"P1:{mid1} P2:{p2} l1:{l1} r1:{r1} mid:{mid1}")
            first_cond = (p2 > 0 and nums2[p2 - 1] <= nums1[mid1]) or p2 == 0
            second_cond = (
                len(nums2) <= p2
                or (mid1 > 0 and nums1[mid1 - 1] <= nums2[p2])
                or mid1 == 0
            )
            if first_cond and second_cond:
                return self.fakit(nums1, nums2, mid1, p2)
            elif (mid1 < len(nums1) and nums2[p2 - 1] > nums1[mid1]) or mid1 == len(
                nums1
            ):
                l1 = mid1 + 1
            else:
                r1 = mid1 - 1

            dikens -= 1
        return self.fakit(nums1, nums2, mid1, p2)
        return 0

    def fakit(self, nums1, nums2, p1, p2):
        dik = []
        tlen = len(nums1) + len(nums2)
        if tlen == 4:
            return statistics.median([nums1[0], nums1[1], nums2[0], nums2[1]])
        if p2 > 0 and (tlen % 2 == 0 or tlen < 4):
            dik.append(nums2[p2 - 1])
        if p2 < len(nums2):
            dik.append(nums2[p2])
        if p1 > 0:
            dik.append(nums1[p1 - 1])
        if p1 < len(nums1):
            dik.append(nums1[p1])
        # If one of the arrays isnt long enough to be split
        if tlen % 2 == 0 and len(dik) < 4:
            if nums2[0] > nums1[p1]:
                dik.append(0)
            else:
                dik.append(nums1[p1 + 1])
        print(f"Fakit Nums1{nums1} P1:{p1} Nums2{nums2} P2:{p2} dik {dik}")

        return statistics.median(dik)
