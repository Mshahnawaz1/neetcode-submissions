class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        out = []
        for i in range(len(firstList)):
            for j in range(len(secondList)):
                l1 = firstList[i][0] if firstList[i] else float('-inf')
                l2 = secondList[j][0] if secondList[j] else float('-inf')
                r1 = firstList[i][1] if firstList[i] else float('inf')
                r2 = secondList[j][1] if secondList[j] else float('inf')

                curr = [max(l1,l2), min(r1,r2)]
                if curr[1] >= curr[0]:
                    out.append(curr)
        return out