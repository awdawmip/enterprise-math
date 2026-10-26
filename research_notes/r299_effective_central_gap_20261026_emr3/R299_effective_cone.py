#!/usr/bin/env python3
"""R299 exact infinite certificate, Python stdlib Fraction only; R294 source bridge author-only."""
import json
from fractions import Fraction as Q
LOW=Q(2617,1000); HIGH=Q(2619,1000); START=10000; M=START+8; LAST=M+5
K=(1,-2,1,-8,6,-3,7,-5,1)
PL=(-1,1,-8,4,-6,11,-6,1)
S=tuple((PL[i] if i<len(PL) else 0)-(PL[i-1] if i>=1 else 0) for i in range(len(PL)+1))
def between(n,d,lo,hi):
    return d>0 and lo.numerator*d<=lo.denominator*n and n*hi.denominator<=hi.numerator*d
def series(N):
    r=[1]
    for n in range(N):
        at=lambda j:r[j] if 0<=j<=n else 0
        x=(2*n-2)*at(n)+(n-1)*at(n-1)+(2*n-2)*at(n-2)-(n-3)*at(n-3)
        assert x%(n+1)==0,(n,x)
        r.append(x//(n+1))
    v=[-x for x in r];f=[];d=[]
    for n in range(N+1):
        x=sum(k*v[n-j] for j,k in enumerate(K) if n>=j)-(S[n] if n<len(S) else 0)
        z=x-(d[-1] if d else 0)
        assert z%2==0
        f.append(x);d.append(z)
    return v,f,d
def verify():
    v,f,d=series(LAST)
    a=lambda r:0 if r<3 else d[r-3]//2
    assert [a(i) for i in range(8)]==[0,0,0,0,1,1,-2,-3]
    assert a(40)==-727277462 and a(41)==1985689179
    finite_end=M+3
    for r in range(41,finite_end+1):
        assert a(r)>0,("sign",r)
    for r in range(41,finite_end):
        assert a(r+1)>=2*a(r),("double",r)
    slope_lo=Q(2)+1/HIGH+2/HIGH**2-1/LOW**3
    const_lo=-Q(2)-1/HIGH-2/HIGH**2+3/LOW**3
    slope_hi=Q(2)+1/LOW+2/LOW**2-1/HIGH**3
    const_hi=-Q(2)-1/LOW-2/LOW**2+3/HIGH**3
    assert slope_lo>LOW and slope_hi<HIGH
    assert (slope_lo-LOW)*START+(const_lo-LOW)>=0
    assert (HIGH-slope_hi)*START+(HIGH-const_hi)>=0
    for j in (START-2,START-1,START):
        assert between(v[j],v[j-1],LOW,HIGH),(j,v[j],v[j-1])
    alpha=sum((Q(k)/(HIGH if k>0 else LOW)**j for j,k in enumerate(K)),Q())
    beta=sum((Q(k)/(LOW if k>0 else HIGH)**j for j,k in enumerate(K)),Q())
    assert 0<alpha<=beta
    assert LOW*alpha/beta>=Q(5,2) and HIGH*beta/alpha<=Q(11,4)
    assert M>=len(S) and f[M]>0
    assert Q(2,3)*f[M]<=d[M]<=Q(4,5)*f[M]
    assert 1-Q(4,5)/Q(5,2)>=Q(2,3)
    assert 1-Q(2,3)/Q(11,4)<=Q(4,5)
    assert Q(5,2)/Q(4,5)-1>2
    for n in range(M,M+5):
        assert between(v[n],v[n-1],LOW,HIGH)
        assert Q(2,3)*f[n]<=d[n]<=Q(4,5)*f[n]
        assert a(n+4)>=2*a(n+3)>0
    b=lambda j:a(j+2)-a(j+1)-(2*a(j-1) if j>=1 else 0)+(a(j-2) if j>=2 else 0)
    assert all(b(j)>0 for j in range(40,43))
    return {
      "schema":"EM_R299_EFFECTIVE_EVEN_GAP_CONE_V1","status":"PASS",
      "scope":"positive ordered six-edge BRC auxiliary; raw source correspondence uses R294 author-only result",
      "r_range_proved":"a_r>0 and a_(r+1)>=2a_r for ALL integer r>=41",
      "odd_range_proved":"b_r>0 for ALL integer r>=40 using R298 transfer",
      "finite_checked_even_r":f"41..{finite_end}",
      "finite_checked_adjacent_r":f"41..{finite_end-1}",
      "v_ratio_base_indices":[START-2,START-1,START],
      "v_ratio_interval":[str(LOW),str(HIGH)],
      "ratio_induction_start":START,
      "rational_cone_checks":True,
      "d_over_f_invariant":"[2/3,4/5]",
      "tail_adjacent_ratio_lower":"17/8",
      "samples":{"a40":str(a(40)),"a41":str(a(41)),"a42":str(a(42)),
                 "b40":str(b(40)),"b41":str(b(41)),"b42":str(b(42))},
      "limitations":"No all-effect N_peak=81, no original X6 physics, no independent review or native Source Result"
    }
if __name__=="__main__":
    print(json.dumps(verify(),ensure_ascii=False,indent=2))
