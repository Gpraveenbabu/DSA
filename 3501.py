from bisect import bisect_left,bisect_right
import re

class Solution:
    def maxActiveSectionsAfterTrade(self, s: str, queries):
        ones=s.count("1")
        start=[]
        end=[]
        for x in re.finditer("0+",s):
            start.append(x.start())
            end.append(x.end()-1)
        m=len(start)
        if m<2:
            return [ones]*len(queries)
        arr=[]
        for i in range(m-1):
            left=end[i]-start[i]+1
            right=end[i+1]-start[i+1]+1
            arr.append(left+right)
        st=[arr]
        k=1
        while k*2<=len(arr):
            prev=st[-1]
            cur=[]
            for i in range(len(prev)-k):
                cur.append(max(prev[i],prev[i+k]))
            st.append(cur)
            k*=2
        def query(l,r):
            if l>r:
                return 0
            p=(r-l+1).bit_length()-1
            return max(
                st[p][l],
                st[p][r-(1<<p)+1]
            )
        def value(i,l,r):
            ans=arr[i]
            if l>start[i]:
                ans-=l-start[i]
            if r<end[i+1]:
                ans-=end[i+1]-r
            return ans
        ans=[]
        for l,r in queries:
            x = bisect_left(end,l)
            y=bisect_right(start,r) - 2
            if x>y:
                ans.append(ones)
                continue
            best=max(value(x,l,r), value(y,l,r))
            if y-x>=2:
                best=max(best,query(x+1, y-1))
            ans.append(ones+best)
        return ans
