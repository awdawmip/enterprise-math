"""PREFIX-977: exact fixed-residual positive source-port path verifier."""
from collections import defaultdict
from math import comb, factorial
import json

def source_masks(p):
    d={}
    for i in range(p):
        for j in range(p):
            for s in (1,-1):
                c=(1<<i)-s*(1<<j)
                P,M=d.get(c,(0,0))
                d[c]=(P|(1<<j),M) if s==1 else (P,M|(1<<j))
    return d

def active(pm,x,p):
    P,M=pm; A=((1<<p)-1)&~1
    return ((P&~x)|(M&x))&A

def decompose(pm,x,p):
    P,M=pm; A=((1<<p)-1)&~1
    return ((P&M&A).bit_count(), (active(pm,x,p)&(P^M)&A).bit_count())

def formula(r,q,h):
    return sum(comb(h,l)*factorial(q)//factorial(q-l)*r**(h-l) for l in range(min(h,q)+1))

def aggregate(pm,p,h):
    P,M=pm; A=((1<<p)-1)&~1
    u=((P^M)&A).bit_count(); r=(P&M&A).bit_count()
    return sum(comb(h,l)*factorial(u)//factorial(u-l)*r**(h-l)*2**(p-1-l) for l in range(min(h,u)+1))

def brute(pm,x,p,H):
    state={x:1}; out=[1]
    for _ in range(H):
        nxt=defaultdict(int)
        for y,m in state.items():
            bits=active(pm,y,p)
            while bits:
                b=bits&-bits;bits-=b;nxt[y^b]+=m
        state=nxt;out.append(sum(state.values()))
    return out

def run():
    stats=[];n=0
    for p in range(4,9):
        d=source_masks(p);cases=0
        for c,pm in sorted(d.items()):
            sums=[0]*7
            for x in range(1,1<<p,2):
                r,q=decompose(pm,x,p)
                assert r in (0,1)
                observed=brute(pm,x,p,6)
                assert observed==[formula(r,q,h) for h in range(7)],(p,c,x)
                sums=[a+b for a,b in zip(sums,observed)]
                cases+=1
            assert sums==[aggregate(pm,p,h) for h in range(7)]
        assert {c for c,(P,M) in d.items() if P&M&~1}=={3<<j for j in range(1,p-2)}
        n+=cases;stats.append({"p":p,"residuals":len(d),"cases":cases})
    p=19;d=source_masks(p)
    assert len(d)==499
    assert {c for c,(P,M) in d.items() if P&M&~1}=={3<<j for j in range(1,17)}
    assert decompose(d[0],1,p)==(0,18)
    assert [formula(0,18,h) for h in (0,1,2,3,18,19)]==[1,18,306,4896,factorial(18),0]
    assert brute(d[0],1,p,4)==[1,18,306,4896,73440]
    assert aggregate(d[0],p,3)==160432128
    for j in range(1,17):
        pm=d[3<<j]
        assert decompose(pm,1,p)==(1,0)
        assert decompose(pm,1|(1<<(j+1)),p)==(1,1)
        assert brute(pm,1|(1<<(j+1)),p,4)==[1,2,3,4,5]
        assert aggregate(pm,p,3)==655360
    result={"schema":"PREFIX977_R6_EXACT_RESULTS_V1","status":"EXACT_INTEGER_VERIFIED",
            "scope":"p=4..8 all residuals and odd x, h=0..6; p=19 analytic/specified cases",
            "cases":n,"horizon_checks":7*n,"stats":stats,
            "p19":{"residuals":499,"persistent_residuals":16,"c0_x1_h2":306,
                   "c0_x1_h3":4896,"c0_x1_h4":73440,
                   "c0_x1_h18":factorial(18),"c0_x1_h19":0,
                   "c0_h3_all_odd_x":160432128,"persistent_h3_all_odd_x_each":655360,
                   "persistent_h3_all_odd_x_all16":10485760}}
    print(json.dumps(result,indent=2))
    return result

if __name__=="__main__":run()
