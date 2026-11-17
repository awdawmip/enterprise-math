"""R259: labelled modular observability; exact all-horizon orbit certificates.
Frozen scientific pin: 43ec6098b1330ae86d0a7863be336c5d97f6ef34.
Python 3 standard library. No external packages / floating-point arithmetic.
"""
import json
from fractions import Fraction as F
from math import gcd, lcm
from functools import reduce

W = (144,576,1440,4320,17280,86400,518400)
CASES = (
 ("R256", F(67,169), 13, 1184397599, 989553240, 3805974000, 2184, (1093,2185)),
 ("R257", F(770,1973), 23, 327870790093, 153448180920, 166791501000, 528, ()),
 ("R258-p23", F(866,2197), 23, 3327364117, 3975468120, 36933000, 12144, ()),
 ("R258-p13", F(866,2197), 13, 3327364117, 3975468120, 36933000, 12, ()),
)
def mask(m):
    return [0]+[i+1 for i in range(6) if (m>>i)&1]
def multiply_linear(f,x):
    g=[F(0)]*(len(f)+1)
    for j,v in enumerate(f):
        g[j]-=v*x
        g[j+1]+=v
    return g
def characteristic(ids,a,b):
    c=[F(1)]
    for i in ids: c=multiply_linear(c,a[i])
    for i in ids:
        z=[F(1)]
        for j in ids:
            if j!=i:z=multiply_linear(z,a[j])
        for j,v in enumerate(z):c[j]-=b[i]*v
    return c

def build(s,J,T,K):
    t=(1691*s-2615)/(2615*s-3539)
    a=[F(1,5), F(1,4),F(3,10),F(9,20),s,F(2,3),t]
    b=[F(13,60)]+[F(5,18)*abs(F(1,2)-a[i]) for i in range(1,7)]
    pi=[b[i]/(1-a[i]) for i in range(7)]
    assert sum(pi)==1
    z=sum(b[i]/(1-a[i])**2 for i in range(7))
    rho=[b[i]/(z*(1-a[i])**2) for i in range(7)]
    assert J==lcm(*((W[m.bit_count()]*rho[i]).denominator
                      for m in range(63) for i in mask(m)))
    C=[]; Q=[]; raw=[]
    for m in range(63):
        ids=mask(m); d=len(ids)
        c=[v*T**(d-j) for j,v in enumerate(characteristic(ids,a,b))]
        assert all(v.denominator==1 for v in c)
        C.append([int(v) for v in c])
        v=[F(1)]*d; h=[]
        for k in range(d+3):
            if k>=3:
                val=J*T**k*W[m.bit_count()]*sum(rho[i]*v[j] for j,i in enumerate(ids))
                assert val.denominator==1
                h.append(int(val))
            ctotal=sum(pi[i]*v[j] for j,i in enumerate(ids))
            v=[a[i]*v[j]+(1-a[i])*ctotal for j,i in enumerate(ids)]
        raw.extend(h)
        Q.append([x//K for x in h])
    assert len(raw)==249 and reduce(gcd,(abs(x) for x in raw))==K
    assert all(x%K==0 for x in raw)
    return C,Q

def orbit(C,Q,p,cap=15000):
    state=tuple(tuple(x%p for x in row) for row in Q)
    seen={}; zeros=[]
    for step in range(cap+1):
        if state in seen:
            return {"preperiod":seen[state],"period":step-seen[state],
                    "states_visited":step,"joint_zero_k":zeros}
        if step>=cap:raise RuntimeError("finite-state cap exceeded")
        seen[state]=step
        if all(row[0]==0 for row in state):zeros.append(step+3)
        nxt=[]
        for row,c in zip(state,C):
            d=len(row)
            v=-sum((c[j]%p)*row[j] for j in range(d))%p
            nxt.append(row[1:]+(v,))
        state=tuple(nxt)
    raise AssertionError("unreachable")

def main():
    output={"schema":"EM_R259_EXACT_GLOBAL_MODULAR_ORBIT_V1",
            "frozen_science_pin":"43ec6098b1330ae86d0a7863be336c5d97f6ef34",
            "domain":"63 labelled scalar masks, k>=3, exact rational parameters",
            "cases":[]}
    cached={}
    for name,s,p,J,T,K,period,zeros in CASES:
        if s not in cached:cached[s]=build(s,J,T,K)
        C,Q=cached[s]
        ans=orbit(C,Q,p)
        assert ans["preperiod"]==0 and ans["period"]==period
        assert tuple(ans["joint_zero_k"])==zeros
        output["cases"].append({"case":name,"parameter":str(s),"prime":p,
             "J":J,"T":T,"K":K,"mask_count":len(Q),
             "total_companion_dimension":sum(map(len,Q)),**ans,"pass":True})
    print(json.dumps(output,indent=2,sort_keys=True))
if __name__=="__main__":main()
