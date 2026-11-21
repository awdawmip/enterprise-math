#!/usr/bin/env python3
"""Exact R5 m=1 O(N) period: standalone Python 3 / integer arithmetic."""
from math import comb, lcm

PRICES=range(214,315)
S=(set(range(214,219)),
   {214,216,217,218,219,220,221},
   {215,216,217,218,219,220,221},
   set(range(223,291)),set(range(296,313)))
TARGET=(7,9,11,13,17,19,23,25,27,29,31,32,37,43)

def phi(d):
    if d in (9,25,27):
        p={9:3,25:5,27:9}[d]
        return [1 if i%p==0 else 0 for i in range(d-p+1)]
    if d==32:
        return [1]+[0]*15+[1]
    assert d in (7,11,13,17,19,23,29,31,37,43)
    return [1]*d

def canonical(v,d):
    """Monic Euclidean reduction Z[x]/Phi_d."""
    f=phi(d)
    a=list(v)
    for i in range(len(a)-1,len(f)-2,-1):
        c=a[i]
        if c:
            for j in range(len(f)):
                a[i-len(f)+1+j]-=c*f[j]
    return a[:len(f)-1]

def shift(v,p):
    k=p%len(v)
    return v[-k:]+v[:-k] if k else v[:]

def add(a,b): return [x+y for x,y in zip(a,b)]
def sub(a,b): return [x-y for x,y in zip(a,b)]

def mask_support(mask):
    return set().union(*(S[i] for i in range(5) if mask&(1<<i)))

def root_jets(d,order=1):
    """R_1(zeta*(1+t)) mod t^(order+1) in integer cyclic group ring."""
    total=[[0]*d for _ in range(order+1)]
    for mask in range(1,32):
        pieces=[[0]*d for _ in range(order+1)]
        pieces[0][0]=1
        for p in sorted(mask_support(mask)):
            nxt=[[0]*d for _ in range(order+1)]
            for j in range(order+1):
                nxt[j]=add(nxt[j],pieces[j])
                for k in range(j+1):
                    term=shift(pieces[j-k],p)
                    ck=comb(p,k)
                    nxt[j]=sub(nxt[j],[ck*x for x in term])
            pieces=nxt
        s=1 if mask.bit_count()%2 else -1
        for j in range(order+1):
            total[j]=add(total[j],[s*x for x in pieces[j]])
    return [canonical(v,d) for v in total]

def independently_eval_constant(d):
    """Separate cyclic-factor-product evaluator, without jets."""
    out=[0]*d
    for mask in range(1,32):
        v=[0]*d;v[0]=1
        for p in sorted(mask_support(mask)):
            k=p%d
            v=[v[i]-v[(i-k)%d] for i in range(d)]
        s=1 if mask.bit_count()%2 else -1
        out=[a+s*b for a,b in zip(out,v)]
    return canonical(out,d)

def independent_derivative(d):
    """Independent product-rule q*d/dq, via prefix/suffix products."""
    out=[0]*d
    def mul(a,b):
        z=[0]*d
        for i,x in enumerate(a):
            if x:
                for j,y in enumerate(b):
                    if y:z[(i+j)%d]+=x*y
        return z
    for mask in range(1,32):
        ps=sorted(mask_support(mask))
        fs=[];ds=[]
        for p in ps:
            f=[0]*d;f[0]+=1;f[p%d]-=1
            g=[0]*d;g[p%d]-=p
            fs.append(f);ds.append(g)
        pre=[[1]+[0]*(d-1)]
        for f in fs:pre.append(mul(pre[-1],f))
        suf=[[1]+[0]*(d-1) for _ in range(len(fs)+1)]
        for i in range(len(fs)-1,-1,-1):suf[i]=mul(fs[i],suf[i+1])
        s=1 if mask.bit_count()%2 else -1
        for i in range(len(fs)):
            term=mul(mul(pre[i],ds[i]),suf[i+1])
            out=[a+s*b for a,b in zip(out,term)]
    return canonical(out,d)

def verify():
    orders=[d for d in range(2,315) if sum(p%d==0 for p in PRICES)>=3]
    assert len(orders)==39 and max(orders)==44
    ceiling=lcm(*orders)
    assert ceiling==229746052653717600
    witness=[]
    for d in TARGET:
        nj=sum(p%d==0 for p in PRICES)
        v0,v1=root_jets(d)
        assert v0==independently_eval_constant(d)
        assert v1==independent_derivative(d)
        j=0 if any(v0) else 1
        vec=(v0,v1)[j]
        assert any(vec),(d,"need higher jet")
        assert nj-j>=3,(d,nj,j)
        i=next(i for i,x in enumerate(vec) if x)
        witness.append((d,nj,j,nj-j,i,vec[i]))
    assert lcm(*(r[0] for r in witness))==ceiling
    print("UPPER",ceiling,"candidate_orders",len(orders))
    print("d n_d first_j pole_order coordinate coeff")
    for row in witness: print(*row)
    print("EXACT PERIOD",ceiling,"ALL CHECKS PASS")
    return witness

if __name__=="__main__":
    verify()
