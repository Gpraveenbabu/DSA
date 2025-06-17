#2566. Maximum Difference by Remapping a Digit
class Solution:
    def minMaxDifference(self, num: int) -> int:
        s=str(num)
        ma=s
        mi=s
        for i in s:
            if i!='9':
                ma=s.replace(i,'9')
                break
        for i in s:
            if i!='0':
                mi=s.replace(i,'0')
                break
        return int(ma)-int(mi)
