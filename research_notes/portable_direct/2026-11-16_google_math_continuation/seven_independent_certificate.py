"""Exact independent-coordinate certificate for 7 samples using 3 fourth differences.
Search every cutoff down from 1349. A max true-distance anchor turns a
distance comparison into six linear inequalities in the seven raw samples.
For independent input intervals, use monotonicity whenever possible and
bisect remaining finite discrete sets. Every pruning comparison is exact.
"""
from fractions import Fraction
from itertools import product
from math import lcm
from functools import lru_cache
P=(455,-295,-25,185,-25,-295)
w=(1,-4,6,-4,1)
W=tuple(tuple(w[j-i] if 0<=j-i<=4 else 0 for j in range(7)) for i in range(3))
def dot(x,y): return sum(a*b for a,b in zip(x,y))
codes=[[sum(w[t]*P[(a+i+t)%6] for t in range(5)) for i in range(3)] for a in range(6)]
def counts(limit):
    cs=[1]+[0]*limit
    for weight in (1,1,1,2,3,6):
        for k in range(weight,limit+1):
            cs[k]+=cs[k-weight]
    C=[0]+cs
    T=[0]*len(C)
    for q in range(1,len(C)): T[q]=T[q-1]+C[q-1]
    return C,T
C,T=counts(1356)
@lru_cache(maxsize=30)
def choices(q):
    base=18*q**4+54*q**3-345*q*q+2070*q-16315
    arr=[]
    for e,d in product(range(-2,3),repeat=2):
        if C[q]+d>0:
            v=Fraction(36*q**3*(T[q]+e),C[q]+d)-Fraction(base,3)
            arr.append((v,e,d))
    return sorted(arr)
nodes=0
def feasible(ineq,cols):
    global nodes
    def solve(bounds):
        global nodes
        nodes+=1
        active=[]
        for coeff,b in ineq:
            lo=sum(c*vals[i if c>=0 else j] for c,vals,(i,j) in zip(coeff,cols,bounds))
            if lo>b:return None
            hi=sum(c*vals[j if c>=0 else i] for c,vals,(i,j) in zip(coeff,cols,bounds))
            if hi>b: active.append(coeff)
        if not active:return [i for i,j in bounds]
        orient=[]
        for k,(i,j) in enumerate(bounds):
            if i==j:continue
            signs=[c[k] for c in active]
            if min(signs)>=0:orient.append((k,i))
            elif max(signs)<=0:orient.append((k,j))
        if orient:
            bounds=list(bounds)
            for k,v in orient:bounds[k]=(v,v)
            return solve(bounds)
        k=max((k for k,(i,j) in enumerate(bounds) if i<j),
              key=lambda k:(cols[k][bounds[k][1]]-cols[k][bounds[k][0]])*
               max(abs(c[k]) for c in active))
        i,j=bounds[k];mid=(i+j)//2
        for pair in ((i,mid),(mid+1,j)):
            new=list(bounds);new[k]=pair
            val=solve(new)
            if val is not None:return val
        return None
    return solve([(0,len(col)-1) for col in cols])

def fails(r):
    a=r%6
    arr=[choices(r+j) for j in range(7)]
    sc=lcm(*(v.denominator for col in arr for v,_,_ in col))
    cols=[[int(v*sc) for v,_,_ in col] for col in arr]
    s=[[v*sc for v in row] for row in codes]
    true=s[a]
    for anchor in range(3):
        for sign in (1,-1):
            cw=[sign*v for v in W[anchor]]
            u=sum(c*col[-1 if c>=0 else 0] for c,col in zip(cw,cols))-sign*true[anchor]
            for b in range(6):
                if b==a or 2*u<max(abs(x-y) for x,y in zip(true,s[b])): continue
                ineq=[]
                for i,wb in enumerate(W):
                    for t in (1,-1):
                        ineq.append(([t*c-v for c,v in zip(wb,cw)],t*s[b][i]-sign*true[anchor]))
                values=feasible(ineq,cols)
                if values is not None:
                    y=[col[i] for col,i in zip(cols,values)]
                    L=[dot(wi,y) for wi in W]
                    dt=max(abs(x-y) for x,y in zip(L,true))
                    db=max(abs(x-y) for x,y in zip(L,s[b]))
                    assert db<=dt
                    return r,a,b,[col[i][1:] for col,i in zip(arr,values)],str(Fraction(dt,36*sc)),str(Fraction(db,36*sc))
    return None
if __name__=='__main__':
    # At q≥1350 the R749SSA scalar envelope is below 60/16. Each
    # fourth difference has row norm 16 and the codeword half-gap is 60.
    bound=Fraction(63374339249936,28025208984321)
    gap=min(max(abs(u-v) for u,v in zip(codes[a],codes[b])) for a in range(6) for b in range(a))
    assert 2*16*36*bound<gap
    for r in range(1349,0,-1):
        witness=fails(r)
        if witness:
            assert r==394 and witness[1:3]==(4,0)
            print('threshold',r+1,'witness',witness,'nodes',nodes,flush=True);break
    else:
        raise AssertionError('no last failure found')
