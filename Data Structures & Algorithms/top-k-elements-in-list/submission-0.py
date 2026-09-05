class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        has = {}
        for i, x in enumerate(nums):
            has[x] = 1 + has.get(x, 0)
            
        li = []
        for num, count in has.items():
            li.append([count, num])
        li = sorted(li)
        out = []
        while (len(out) < k):
            out.append(li.pop()[1])
        return out