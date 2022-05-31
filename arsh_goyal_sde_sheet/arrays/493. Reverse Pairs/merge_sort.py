class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        def mergeSort(nums):
            if len(nums) < 2: return nums
            mid = len(nums) // 2
            left = mergeSort(nums[:mid])
            right = mergeSort(nums[mid:])
            return merge(left, right)
        
        def merge(nums1, nums2):
            if not nums1: return nums2
            if not nums2: return nums1
            
            nonlocal ans
        
            j = 0
            for n in nums1:
                while j < len(nums2) and n > nums2[j] * 2:
                    j += 1
                ans += j
            
            i = j = pointer = 0
            temp = nums1 + nums2
            
            while i < len(nums1) and j < len(nums2):
                if nums1[i] < nums2[j]:
                    temp[pointer] = nums1[i]
                    pointer += 1
                    i += 1
                else:
                    temp[pointer] = nums2[j]
                    pointer += 1
                    j += 1
            
            while i < len(nums1):
                temp[pointer] = nums1[i]
                pointer+=1
                i += 1
            
            while j < len(nums2):
                temp[pointer] = nums2[j]
                pointer += 1
                j += 1
            
            return temp
        
        ans = 0
        mergeSort(nums)
        return ans
            