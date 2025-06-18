#2966. Divide Array Into Arrays With Max Difference
class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        a=sorted(nums)
        b=[]
        for i in range(0,len(a)-2,3):
            if a[i+2]-a[i]>k:
                return []
            b.append(a[i:i+3])
        return b
