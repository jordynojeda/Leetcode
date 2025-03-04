class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        def merge(array, left, middle, right):
            left_array, right_array = array[left:middle+1], array[middle+1:right+1]
            i, j, k = left, 0, 0

            while j < len(left_array) and k < len(right_array):
                if left_array[j] <= right_array[k]:
                    array[i] = left_array[j]
                    j += 1
                else:
                    array[i] = right_array[k]
                    k += 1
                
                i += 1
            
            while j < len(left_array):
                array[i] = left_array[j]
                j += 1
                i += 1

            while k < len(right_array):
                array[i] = right_array[k]
                k += 1
                i += 1

        def merge_sort(array, left, right):
            if left == right:
                return array
            
            middle = (left + right) // 2
            merge_sort(array, left, middle)
            merge_sort(array, middle + 1, right)
            merge(array, left, middle, right)
            return array
        
        return merge_sort(nums, 0, len(nums) - 1)
