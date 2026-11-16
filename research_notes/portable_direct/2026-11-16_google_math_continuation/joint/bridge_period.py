"""Exact reflection of positional exceptional divisors and first/last within one period."""
from math import lcm,comb
from fractions import Fraction
from itertools import count
firsts={60:(2117441088029,29),61:(569181900,50),62:(155275274056,8),63:(216949362182,35),64:(2600001558,22)}
for k,(n,i0) in firsts.items():
    period=lcm(*range(1,k+1))*lcm(*range(1,k//2+1))
    last=period+k-1-n
    def mask(m):
        c=comb(m,k)
        return [i for i in range(k) if c%(m-i)]
    assert mask(n)==[i0] and mask(last)==[k-1-i0]
    print(k,n,last,k-1-i0)
    if k==60:print('P60',period)
# For small k, verify first AND last by searching both ends independently.
for k in range(3,13):
    period=lcm(*range(1,k+1))*lcm(*range(1,k//2+1))
    lo,hi=2*k,period-k-1
    if lo>hi:continue
    def has(m):
        c=comb(m,k)
        return sum(c%(m-i)!=0 for i in range(k))==1
    n=next((x for x in range(lo,hi+1) if has(x)),None)
    end=next((x for x in range(hi,lo-1,-1) if has(x)),None)
    assert (n is end is None) or (end==period+k-1-n)
print('full check for k=3…12')
