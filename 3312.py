class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        mx = max(nums)
        freq = [0] * (mx + 1)
        for x in nums:
            freq[x] += 1
        divCnt = [0] * (mx + 1)
        for g in range(1, mx + 1):
            for multiple in range(g, mx + 1, g):
                divCnt[g] += freq[multiple]
        exact = [0] * (mx + 1)

        for g in range(mx, 0, -1):
            cnt = divCnt[g]
            exact[g] = cnt * (cnt - 1) // 2
            for multiple in range(2 * g, mx + 1, g):
                exact[g] -= exact[multiple]
        prefix = []
        gcdValue = []

        total = 0
        for g in range(1, mx + 1):
            if exact[g] > 0:
                total += exact[g]
                prefix.append(total)
                gcdValue.append(g)
        ans = []
        for q in queries:
            idx = bisect_right(prefix, q)
            ans.append(gcdValue[idx])

        return ans
        
