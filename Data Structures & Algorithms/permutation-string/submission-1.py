class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            # s1, s2 = s2, s1
            return False

        # ws1 = {ws1[x]: 1+ws1.get(x, 0) for x in s1}
        ws1, ws2 = {}, {}
        for x in s1:
            ws1[x] = 1+ws1.get(x, 0)
        for i in range(0, len(s1)):
            ws2[s2[i]] = 1+ws2.get(s2[i], 0)

        r = len(s1)
        while r < len(s2):
            if ws1 == ws2:
                return True
            left = s2[r-len(s1)]
            ws2[left] -= 1
            if ws2[left] == 0:
                del ws2[left]

            ws2[s2[r]] = 1 + ws2.get(s2[r], 0)
            r += 1
        return ws1 == ws2
