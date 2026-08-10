class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        start, end = 0, len(numbers) - 1

        while (start < end):
            l = numbers[start]
            h = numbers[end]

            if l+h == target:
                return [start+1, end+1]
            elif l+h > target: 
                end -= 1
            elif l+h < target:
                start +=1