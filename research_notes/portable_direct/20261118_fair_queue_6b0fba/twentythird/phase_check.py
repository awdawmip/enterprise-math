"""Exact cyclotomic scans and same-label readout products. No angle is sampled."""
import argparse
import json
import sys
from functools import cache
from fractions import Fraction as F
from itertools import combinations, product
from math import gcd, lcm, comb
from pathlib import Path


def divisors(n):
    return [d for d in range(1,n+1) if n%d==0]


def divide(x,y):
    r=list(x); q=[0]*max(1,len(r)-len(y)+1)
    for j in reversed(range(len(r)-len(y)+1)):
        q[j]=r[j+len(y)-1]
        for i,a in enumerate(y): r[j+i]-=q[j]*a
    return q,r[:len(y)-1]


@cache
def phi(n):
    p=[-1]+[0]*(n-1)+[1]
    for d in divisors(n)[:-1]:
        p,r=divide(p,phi(d))
        assert not any(r)
    return tuple(p)


@cache
def root(m,e):
    return tuple(divide([0]*(e%m)+[1],phi(m))[1]+[0]*max(0,len(phi(m))-2-e%m))


def multiply(m,x,y):
    z=[0]*(len(x)+len(y)-1)
    for i,a in enumerate(x):
        for j,b in enumerate(y):z[i+j]+=a*b
    return tuple(divide(z,phi(m))[1])


def scan(m,a,s,r):
    # Four times the plus-port probability.
    v=root(m,a*r+s); w=root(m,-a*r-s); identity=root(m,0)
    return tuple(2*i+x+y for i,x,y in zip(identity,v,w))


def addrank(basis,v):
    v=list(map(F,v))
    for j,w in sorted(basis.items()):
        if v[j]:
            t=v[j];v=[x-t*y for x,y in zip(v,w)]
    j=next((j for j,x in enumerate(v) if x),None)
    if j is not None:basis[j]=[x/v[j] for x in v]


def qscan(m,A):
    mat={};addrank(mat,[1]*m)
    cols=[[] for _ in range(m)]
    for a in A:
        for s in {0,(m+2)//4}:
            row=[scan(m,a,s,r) for r in range(m)]
            for coeff in zip(*row): addrank(mat,coeff)
            for c,v in zip(cols,row):c.append(v)
    ds={m//gcd(a,m) for a in A}-{1}
    assert len(mat)==1+sum(len(phi(d))-1 for d in ds)
    assert len({tuple(c) for c in cols})==lcm(*ds)
    return len(mat)


def history(m,T):
    settings=(0,(m+2)//4)
    identity=root(m,0)
    gen=[[scan(m,1,s,r) for r in range(m)] for s in settings]
    one=[identity for r in range(m)]
    ranks=[];basis={}
    for t in range(T+1):
        for k in range(t+1):
            row=one
            for v in [gen[0]]*k+[gen[1]]*(t-k):
                row=[multiply(m,x,y) for x,y in zip(row,v)]
            for coeff in zip(*row):addrank(basis,coeff)
        ranks.append(len(basis))
        ds={m//gcd(a,m) for a in range(1,t+1)}-{1}
        assert ranks[-1]==1+sum(len(phi(d))-1 for d in ds)
    return ranks


def radical_sign(a,b):
    if a==0: return (b>0)-(b<0)
    if b==0 or a*b>0:return (a>0)-(a<0)
    return ((a*a>5*b*b)-(a*a<5*b*b))*((a>0)-(a<0))


def min_p5(D):
    best=None;count=0
    for prefix in product(range(-D,D+1),repeat=4):
        c=prefix+(-sum(prefix),)
        if not any(c) or sum(max(v,0) for v in c)>D:continue
        cov=[sum(c[i]*c[(i+j)%5] for i in range(5)) for j in range(3)]
        a,b=2*cov[0]-cov[1]-cov[2],cov[1]-cov[2]
        assert radical_sign(a,b)>0
        if best is None or radical_sign(a-best[0],b-best[1])<0:best=(a,b,c)
        count+=1
    return dict(denominator=D,difference_vectors=count,
                unnormalized_squared_modulus='(a+b*sqrt(5))/2',a=best[0],b=best[1],
                minimizing_difference=best[2],laws=comb(D+4,4))


def witnesses():
    x,y=(0,4),(2,6)
    def probability(tags,a,offsets):
        vals=[]
        for r in tags:
            v=root(8,0)
            for shift in offsets: v=multiply(8,v,scan(8,a,shift,r))
            vals.append(v)
        return tuple(F(sum(c),len(tags)*4**len(offsets)) for c in zip(*vals))
    for shift in range(8):
        assert probability(x,1,[shift])==probability(y,1,[shift])==(F(1,2),0,0,0)
    assert probability(x,1,[0,0])==(F(1,2),0,0,0)
    assert probability(y,1,[0,0])==(F(1,4),0,0,0)
    assert probability(x,2,[0])==(F(1),0,0,0) and probability(y,2,[0])==(F(0),0,0,0)
    one=root(5,0)
    golden=tuple(sum(col) for col in zip(one,root(5,1),root(5,4)))
    neg_inv=tuple(i-a for i,a in zip(one,golden))
    base=tuple(x-y for x,y in zip(root(5,4),one))
    l,h=0,1
    for n in range(21):
        c=(-h,l,0,-l,h)
        coeff=tuple(sum(t*root(5,j)[b] for j,t in enumerate(c)) for b in range(4))
        assert coeff==base
        base=multiply(5,base,neg_inv)
        l,h=h,l+h
    return dict(c8_equal_single_pass_offsets=8,c8_shared_tag_both_plus=['1/2','1/4'],
                c8_double_pass_plus=[1,0],c5_fibonacci_pairs=21)


def third_order():
    cases=0
    for phases in product(range(4),repeat=3):
        re=(1,0,-1,0);im=(0,1,0,-1)
        vals=[]
        for mask in range(8):
            ids=[i for i in range(3) if mask>>i&1]
            vals.append(F(sum(re[phases[i]] for i in ids)**2+
                          sum(im[phases[i]] for i in ids)**2,9))
        assert all(0<=v<=1 for v in vals)
        assert sum((-1)**(3-mask.bit_count())*v for mask,v in enumerate(vals))==0
        cases+=1
    # A detector with fixed law f(x)=x+epsilon*x^2 gives nonzero I3 for all zero labels.
    # Use f(x)=(x+x^2)/2 so its image remains a probability on [0,1].
    closed=[F(k*k,9) for k in range(4)]
    observed=[(x+x*x)/2 for x in closed]
    residual=sum((-1)**(3-i)*comb(3,i)*x for i,x in enumerate(observed))
    assert residual==F(2,9)
    return dict(quadratic_cases=cases,fixed_nonlinear_response='(x+x^2)/2',apparent_I3=str(residual))


def native_subset(repo):
    sys.path.insert(0,str(repo/'src'))
    from enterprise_math.brc_weighted import cwm_edge,cwm_propagate,cwm_recoalesce
    def read(tag,setting):return F((2,1,0,1)[(tag+setting)%4],2)
    def joint(hist,s,t):
        terms=[]
        for tag,mass in hist:
            if not read(tag,s) or not read(tag,t):continue
            terms.append(cwm_propagate(cwm_propagate(cwm_edge(mass),cwm_edge(read(tag,s))),
                                       cwm_edge(read(tag,t))))
        if not terms: return F(0)
        out=terms[0]
        for v in terms[1:]:out=cwm_recoalesce(out,v)
        return out.total
    a=[(0,F(1,2)),(2,F(1,2))];b=[(1,F(1,2)),(3,F(1,2))]
    out=[[str(joint(h,s,t)) for s,t in product(range(4),repeat=2)] for h in [a,b]]
    assert (out[0][0],out[1][0])==('1/2','1/4')
    return dict(cyclic_order=4,calibrated_plus_plus_tables_flat=out)


def main(repo):
    masks=0
    for m in range(3,21):
        ds=divisors(m)[1:]
        for k in range(len(ds)+1):
            for subset in combinations(ds,k):
                qscan(m,tuple(m//d for d in subset));masks+=1
    h={m:history(m,m//2) for m in range(3,15)}
    p5=[min_p5(d) for d in (2,3,5,8)]
    return dict(rational_rank_and_pure_quotient_checks=masks,history_rational_ranks=h,
                exact_p5_gaps=p5,explicit_witnesses=witnesses(),three_path=third_order(),positive_BRC=native_subset(repo))


if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--repo',type=Path,required=True)
    args=parser.parse_args()
    print(json.dumps(main(args.repo.resolve()),indent=2,sort_keys=True))
