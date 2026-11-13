#!/usr/bin/env python3
"""R124: exact rational lifting of arbitrary directed half-open S23 arcs.

The checker enumerates integer lifts only for small validation inputs. The
claimed large-parameter algorithm is the fixed-dimension integer-program
reduction, not this finite checker.
"""
from fractions import Fraction as F
from itertools import product
from random import Random
from json import dumps
from pathlib import Path


def floor(x): return x.numerator // x.denominator

def frac(x): return x-floor(x)

def kval(x,j,a,c,t,z):
    u=frac(F(a)*z);v=frac(F(c)*z);w=frac(x+F(t-j)*z)
    return int((u<v and u<=w<v) or (u>v and (w>=u or w<v)))

# An affine quantity represented as slope * theta + intercept.
def af(a,b=0): return (F(a),F(b))
def add(v,w): return (v[0]+w[0],v[1]+w[1])
def neg(v): return (-v[0],-v[1])
def sub(v,w):return add(v,neg(w))

def feasible(constraints,L,H):
    # Each constraint (A, B, strict): A*theta+B >= 0, strict if flagged.
    lo,hi=F(L),F(H);lo_open=hi_open=True
    for (a,b), strict in constraints:
        if a==0:
            if b<0 or (strict and b==0):return None
            continue
        cut=-b/a
        if a>0:
            if cut>lo:lo,lo_open=cut,strict
            elif cut==lo:lo_open |= strict
        else:
            if cut<hi:hi,hi_open=cut,strict
            elif cut==hi:hi_open |= strict
        if lo>hi or (lo==hi and (lo_open or hi_open)): return None
    return (lo+hi)/2 if lo<hi else lo

def floor_candidates(a,L,H):
    v,w=F(a)*F(L),F(a)*F(H)
    return range(floor(min(v,w))-1,floor(max(v,w))+2)

def y_candidates(x,a,L,H):
    v,w=x+F(a)*L,x+F(a)*H
    return range(floor(min(v,w))-1,floor(max(v,w))+2)

def lift_witness(x,j,a,c,N,d,m,L,H,bits):
    """A *small-input* exhaustive verifier of the 4-int linear lifting."""
    aa,cc=af(a),af(c)
    queries=0
    for r,s,n,k in product(floor_candidates(a,L,H),floor_candidates(c,L,H),
                           y_candidates(x,N-j,L,H),floor_candidates(d,L,H)):
        u=sub(aa,af(0,r));v=sub(cc,af(0,s));beta=sub(af(d),af(0,k))
        base=[(u,False),(sub(af(0,1),u),True),
              (v,False),(sub(af(0,1),v),True),
              (beta,False),(sub(af(0,1),beta),True)]
        # Eliminate integer floor labels incompatible with any theta first.
        base += [(sub(af(N-j,x),af(0,n)),False),
                 (sub(af(0,n+1),af(N-j,x)),True)]
        if feasible(base,L,H) is None:continue
        yy=[af(N+i*d-j,x) for i in range(m)]
        for qs in product(*[range(i+1) for i in range(m)]):
            # q0 is necessarily zero
            z=[sub(y,af(0,n+i*k+qs[i])) for i,y in enumerate(yy)]
            con=base+[(w,False) for w in z]+[(sub(af(0,1),w),True) for w in z]
            if feasible(con,L,H) is None:continue
            for order in (-1,0,1):
                # -1 means u < v; +1 means u > v
                order_con= [(sub(v,u),True)] if order==-1 else ([(sub(u,v),True)] if order==1 else [(sub(u,v),False),(sub(v,u),False)])
                if order==0 and any(bits):continue
                if feasible(con+order_con,L,H) is None:continue
                arcs=[]
                for bit,w in zip(bits,z):
                    if order==-1:
                        options=[[(sub(w,u),False),(sub(v,w),True)]] if bit else [[(sub(u,w),True)],[(sub(w,v),False)]]
                    elif order==1:
                        options=[[(sub(w,u),False)],[(sub(v,w),True)]] if bit else [[(sub(w,v),False),(sub(u,w),True)]]
                    else:
                        options=[[]]
                    arcs.append(options)
                for selected in product(*arcs):
                    cs=con+order_con+[item for seg in selected for item in seg]
                    queries+=1
                    w=feasible(cs,L,H)
                    if w is not None:
                        assert all(kval(x,j,a,c,N+i*d,w)==bits[i] for i in range(m))
                        assert F(L)<w<F(H)
                        return w,queries
    return None,queries


def direct_signature_set(x,j,a,c,N,d,m,L,H):
    # Independent direct fractional condition, cutting ALL phase crossings.
    slopes=[a,c,a-c]
    for i in range(m):
        t=N+i*d
        slopes += [t-j,t-j-a,t-j-c]
    points={L,H}
    # Explicit crossings for each phase, including x offsets.
    phases=[(F(a),F(0)),(F(c),F(0)),(F(a-c),F(0))]
    for i in range(m):
        t=N+i*d
        phases += [(F(t-j),x),(F(t-j-a),x),(F(t-j-c),x)]
    for slope,intercept in phases:
        if not slope:continue
        v0=slope*L+intercept;v1=slope*H+intercept
        for n in range(floor(min(v0,v1))-1,floor(max(v0,v1))+3):
            q=(n-intercept)/slope
            if L<q<H:points.add(q)
    pts=sorted(points)
    # Open interval, no L/H themselves; all interior singleton crossings included.
    candidates=pts[1:-1]+[(pts[i]+pts[i+1])/2 for i in range(len(pts)-1)]
    result={}
    for z in candidates:
        bits=tuple(kval(x,j,a,c,N+i*d,z) for i in range(m))
        result.setdefault(bits,z)
    return result,len(candidates)


def run():
    rng=Random(1242026)
    total_queries=0; total_cases=0; total_sigs=0; cuts=0
    targets=[
      (F(1,3),0,0,0,2,1,2),  # equal endpoints empty
      (F(1,3),0,1,1,0,2,2),  # equal all theta
      (F(0),0,0,1,1,1,2),    # endpoint inclusion
      (F(1,5),1,2,-1,1,-2,3),
      (F(3,7),-1,-2,3,-2,1,3),
      (F(2,5),1,-1,2,1,-1,4),
      (F(-1,7),-2,2,-3,2,1,4),
    ]
    for _ in range(80):
        x=F(rng.randint(-4,4),rng.randint(2,8))
        j=rng.randint(-2,2)
        a=rng.randint(-3,3)
        c=rng.randint(-3,3)
        N=rng.randint(-3,3)
        d=rng.choice([-2,-1,1,2])
        m=rng.choice([2,3])
        targets.append((x,j,a,c,N,d,m))
    for x,j,a,c,N,d,m in targets:
        L,H=F(0),F(1)
        real,ns=direct_signature_set(x,j,a,c,N,d,m,L,H)
        cuts+=ns
        reached={}
        for bits in product((0,1),repeat=m):
            witness,num=lift_witness(x,j,a,c,N,d,m,L,H,bits)
            total_queries+=num
            assert (witness is not None)==(bits in real), (x,j,a,c,N,d,m,bits,witness,real)
            if witness is not None:reached[bits]=witness
            total_sigs+=1
        assert set(reached)==set(real)
        total_cases+=1
    # Signed, extremely large times: verify an exact *positive* lift without
    # claiming to run a large-coefficient integer feasibility solver.
    huge=[]
    for N,d in ((10**100+7,-(10**90+5)),(-(10**110+9),10**105+3)):
        x,j,a,c,theta=F(2,7),2,-3,5,F(37,101)
        n=floor(x+F(N-j)*theta);k=floor(F(d)*theta)
        r=floor(F(a)*theta);s=floor(F(c)*theta)
        alpha=x+F(N-j)*theta-n;beta=F(d)*theta-k
        qs=tuple(floor(alpha+i*beta) for i in range(4))
        z=[x+F(N+i*d-j)*theta-(n+i*k+qs[i]) for i in range(4)]
        assert all(F(0)<=w<F(1) for w in z)
        assert 0<=F(a)*theta-r<1 and 0<=F(c)*theta-s<1
        assert tuple(kval(x,j,a,c,N+i*d,theta) for i in range(4)) == tuple(int(((F(a)*theta-r)<(F(c)*theta-s) and (F(a)*theta-r)<=w<(F(c)*theta-s)) or (((F(a)*theta-r)>(F(c)*theta-s)) and (w>=(F(a)*theta-r) or w<(F(c)*theta-s)))) for w in z)
        huge.append({'N_digits':len(str(abs(N))),'d_digits':len(str(abs(d))), 'q':qs})
    return {'large_signed_certificate_samples':huge,'status':'R124_PASS' ,'cases':total_cases,'complete_signature_checks':total_sigs,
            'lift_disjunct_checks':total_queries,'direct_atom_samples':cuts,
            'scope':'m in {2,3}, small signed integer j,a,c,N,d and rational x, theta in (0,1)',
            'seed':1242026}
if __name__=='__main__':
    result=run();print(dumps(result,sort_keys=True))
    Path(__file__).with_name('verification_r124_generated.json').write_text(dumps(result,indent=2,sort_keys=True)+'\n')
