from itertools import combinations
from VERIFY_R5_28_CUT_SPECTRUM import cost_frontier,convolution

def brute(x):
    ans={}
    for k in range(1,len(x)+1):
        for centers in combinations(x,k):
            d=[min(abs(y-z) for z in centers) for y in x]
            if max(d)>2:continue
            total=sum(d)
            ans[k]=min(total,ans.get(k,10**8))
    return ans

cases=0
for n in range(2,8):
    for t in combinations(range(1,11),n-1):
        x=(0,)+t
        a=cost_frontier(x)
        b=brute(x)
        assert a==b,(x,a,b)
        blocks=[];s=0
        for q in range(1,n):
            if x[q]-x[q-1]>2:
                blocks.append(x[s:q]);s=q
        blocks.append(x[s:])
        combo=convolution([cost_frontier(q) for q in blocks],limit=n)
        assert combo==b,(x,combo,b)
        cases+=1
print('PASS_EXACT_DP_AND_MINPLUS',cases)
