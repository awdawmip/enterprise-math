#!/usr/bin/env python3
"""PREFIX-450 exact signed-X6 path / typed positive-BRC moment-rank certificate.

Pure standard library; no floating point.  Source model: P000 signed native
X6 words; historical sector counts -e1 steps modulo q. The theorem is proved
in the companion note; these finite checks independently test its construction.
"""
from __future__ import annotations
from itertools import product
from math import comb, factorial
from fractions import Fraction

DIM=6
PRIME=1_000_000_007


def multiindices(d, m=DIM):
    if m==1:
        return [(t,) for t in range(d+1)]
    return [(t,)+v for t in range(d+1) for v in multiindices(d-t,m-1)]


def graded_indices(d, m=DIM):
    # Order by degree, then lexicographic; identical row/column order.
    return sorted(multiindices(d,m),key=lambda a:(sum(a),a))


def construct(q,d,r,alpha):
    assert q>=2 and d>=0 and 0<=r<q and len(alpha)==DIM
    assert all(isinstance(x,int) and x>=0 for x in alpha) and sum(alpha)<=d
    word=[(0,-1)]*r+[(0,1)]*(q-1-r)
    for i in range(5): word += [(i,1)]*alpha[i]
    word += [(5,1)]*alpha[5]
    word += [(5,-1)]*(d-sum(alpha))
    return tuple(word)


def read_word(word, q):
    x=[0]*DIM; negative_first=0
    for axis,sgn in word:
        assert 0<=axis<6 and sgn in (-1,1)
        x[axis]+=sgn
        negative_first+=axis==0 and sgn==-1
    return negative_first%q,tuple(x)


def x_closed(q,d,r,a):
    return (q-1-2*r+a[0],a[1],a[2],a[3],a[4],-d+sum(a[:5])+2*a[5])


def value(x,b):
    p=1
    for xi,bi in zip(x,b):p*=xi**bi
    return p


def det_mod(mat,p=PRIME):
    a=[[int(z)%p for z in row] for row in mat]
    n=len(a); ans=1
    assert all(len(row)==n for row in a)
    for j in range(n):
        h=next((i for i in range(j,n) if a[i][j]),None)
        if h is None:return 0
        if h!=j:
            a[j],a[h]=a[h],a[j];ans=-ans
        pivot=a[j][j];ans=ans*pivot%p
        v=pow(pivot,-1,p)
        row=a[j]
        for i in range(j+1,n):
            if a[i][j]:
                scale=a[i][j]*v%p
                ai=a[i]
                for k in range(j+1,n):ai[k]=(ai[k]-scale*row[k])%p
                ai[j]=0
    return ans%p


def theoretical_det(d,prime=PRIME):
    idx=graded_indices(d)
    exponent=comb(d+6,7) if d>=1 else 0
    result=pow(2,exponent,prime)
    for beta in idx:
        for b in beta: result=result*factorial(b)%prime
    return result


def lower_polynomial(q,n,x):
    if n<q-1:return None
    total=sum(x)
    y=1
    for h in range(q-1,n+1):y*=total-(n-2*h)
    return y


def reachable(n,q):
    states={(0,(0,)*6)}
    for _ in range(n):
        nxt=set()
        for r,x in states:
            for axis in range(6):
                for sg in (-1,1):
                    y=list(x);y[axis]+=sg
                    nxt.add(((r+(axis==0 and sg==-1))%q,tuple(y)))
        states=nxt
    return [set(x for r,x in states if r==sector) for sector in range(q)]


def run():
    testcases=0
    for d in range(0,5):
        idx=graded_indices(d)
        size=comb(d+6,6)
        assert len(idx)==size
        mod_expect=theoretical_det(d)
        for q in (2,3,4):
            xmatrices=[]
            for r in range(q):
                points=[]
                for a in idx:
                    w=construct(q,d,r,a)
                    rr,x=read_word(w,q)
                    assert rr==r and len(w)==q+d-1
                    assert x==x_closed(q,d,r,a)
                    points.append(x)
                assert len(set(points))==size
                matrix=[[value(x,b) for b in idx] for x in points]
                observed=det_mod(matrix)
                assert observed==mod_expect,(q,d,r,observed,mod_expect)
                xmatrices.append(observed)
                testcases+=1
            print(f'PASS q={q} d={d} N={q+d-1} sectors={q} '
                  f'per_sector_dim={size} total_rank={q*size} det_mod={mod_expect}')

    exhaustive=0
    for q in (2,3,4):
        for d in range(0,4):
            limit=q+d-1
            for n in range(limit):
                eps=reachable(n,q)[q-1]
                if n<q-1:
                    assert len(eps)==0
                else:
                    assert all(lower_polynomial(q,n,x)==0 for x in eps)
                    assert 1<=n-q+2<=d
                exhaustive+=1
    print(f'PASS lower-bound sector support for {exhaustive} (q,d,n) finite cases')

    # Exact future BRC branch readout: affine X6 effects, positive rational mass,
    # two distinct state-conditioned edges, direct weighted source vs moment law.
    q,d=3,3
    idx=graded_indices(d)
    sample={}
    for r in range(q):
        for j,a in enumerate(idx[:17]):
            x=read_word(construct(q,d,r,a),q)[1]
            sample[r,j]=(x,Fraction(j+2,13+r))
    # Edge r -> (r+1) mod q; y_1=x_1+x_2+1/2, y_i=x_i for i>1.
    # A translation-plus-shear affine map, not a native primitive step claim.
    def effect(x):
        return (x[0]+x[1]+Fraction(1,2),)+tuple(Fraction(z) for z in x[1:])
    direct={}
    for (r,j),(x,w) in sample.items():
        s=(r+1)%q
        z=effect(x);mass=Fraction(r+2,r+3)*w
        for b in idx:
            direct[s,b]=direct.get((s,b),Fraction())+mass*value(z,b)
    # The binomial substitution is the typed BRC polynomial port action:
    # (x1+x2+1/2)^a1 * product_{i>1} x_i^ai.
    from math import comb as nck
    old={(r,b):sum(w*value(x,b) for (rr,_),(x,w) in sample.items() if rr==r)
         for r in range(q) for b in idx}
    propagated={}
    for r in range(q):
        s=(r+1)%q; edgeweight=Fraction(r+2,r+3)
        for b in idx:
            total=Fraction()
            for i in range(b[0]+1):
                for j in range(b[0]-i+1):
                    k=b[0]-i-j
                    u=(i,b[1]+j,b[2],b[3],b[4],b[5])
                    factor=nck(b[0],i)*nck(b[0]-i,j)*Fraction(1,2)**k
                    total+=factor*old[r,u]
            propagated[s,b]=edgeweight*total
    assert direct==propagated
    print(f'PASS exact positive Fraction affine-BRC observer transport: '
          f'{len(sample)} distinct source terms and {q*len(idx)} moment outputs')
    print('PASS PREFIX-450 exact certificate; native upstream ControlPacket import not executed')

if __name__=='__main__':run()
