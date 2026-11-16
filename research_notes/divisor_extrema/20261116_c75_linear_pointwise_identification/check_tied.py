"""Exact checks on exact scalar residuals with tied integer gap lengths."""
from fractions import Fraction as F
from math import prod
import json
from check_pointwise import rate, tail, nu2, rising
from check_macro import closed_two

def record(gaps):
    first,middle,last=gaps
    c=first+middle+last+2
    v,w=c-first,last+2
    rho1,a=rate(c,v,5)
    rho2,b=rate(v,w,3)
    W=F((w+2)*(w+3)*(w+4),840)
    l=F(4**(w-2)*rising(4,w-2),prod(4*h+1 for h in range(3,w+1)))
    params=(a/rho1,b/rho2,l)
    derivatives=closed_two(a,b,W)
    terms=[d*p for d,p in zip(derivatives,params)]
    p_real,p_zero,_=tail(w)
    def report(ps,t,s):
        ends=[]
        for p in (ps[2],ps[0]):
            mid=(1+s*p)/(1+b*p)
            ends.append((1+t*mid)/(1+a*mid))
        return ends[0]/ends[1]
    signed_ratio=report(p_real,params[0],params[1])/report(p_zero,0,0)
    orders=list(map(nu2,terms))
    minimum=min(orders)
    first_sum=nu2(sum(terms))
    measured=nu2(signed_ratio-1)
    if orders.count(minimum)%2:
        assert first_sum==minimum
    assert (first_sum>minimum)==(orders.count(minimum)%2==0)
    return dict(gaps=gaps,stock=[c,v,w],linear_orders=orders,linear_sum=first_sum,
                measured=measured,cancelled_bits=first_sum-minimum)

if __name__=='__main__':
    examples=[(4,2,2),(21,21,26),(26,21,21),(31,43,31),(45,45,45),(5,5,5)]
    rows=[record(g) for g in examples]
    expected=[(7,1),(72,9),(73,8),(101,10),(145,5),(19,0)]
    assert all((r['linear_sum'],r['cancelled_bits'])==pair and r['measured']==r['linear_sum']
               for r,pair in zip(rows,expected))
    print(json.dumps(rows,indent=2))
