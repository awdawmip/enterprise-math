"""PREFIX-449 compact exact cubic BRC readout rank reproducer (Python stdlib)."""
from itertools import combinations, product
from fractions import Fraction
from math import comb

P = 1000000007

def ep(w):
    a = [0]*6
    for s in w: a[abs(s)-1] += 1 if s>0 else -1
    return tuple(a)

def tails():
    # x1=0: 56 cubic-unisolvent sites in five remaining dimensions.
    def ax(i, t):
        if abs(t)==3: return (i if t>0 else -i,)*3
        k = 3 if i==2 else 2
        return (i if t>0 else -i,k,-k)
    s=[ax(2,t) for t in (1,-1,3,-3)]
    for i in range(3,7): s += [ax(i,t) for t in (1,-1,3)]
    for i,j in combinations(range(2,7),2): s += [(i,i,j),(-i,-i,j),(i,j,j)]
    for i,j,k in combinations(range(2,7),3): s.append((i,j,k))
    assert len(s)==56
    # x1=1: 21 quadratic sites; x1=2: 6 linear sites; x1=3: one.
    t=[(1,2,-2)]
    for i in range(2,7): t += [(1,i,i),(1,-i,-i)]
    for i,j in combinations(range(2,7),2): t.append((1,i,j))
    u=[(1,1,2),(1,1,-2)]+[(1,1,i) for i in range(3,7)]
    all_words=s+t+u+[(1,1,1)]
    assert (len(t),len(u),len(all_words))==(21,6,84)
    assert len(set(map(ep,all_words)))==84
    return all_words

def mono(n,d):
    if n==1: return [(k,) for k in range(d+1)]
    return [(k,)+v for k in range(d+1) for v in mono(n-1,d-k)]

def ev(x,a):
    r=1
    for v,k in zip(x,a): r*=v**k
    return r

def detmod(a):
    a=[[x%P for x in row] for row in a]
    n=len(a); assert all(len(row)==n for row in a)
    det=1
    for j in range(n):
        i=next((i for i in range(j,n) if a[i][j]),None)
        assert i is not None
        if i!=j: a[i],a[j]=a[j],a[i]; det=-det
        c=a[j][j]; det=det*c%P; z=pow(c,-1,P)
        for i in range(j+1,n):
            if a[i][j]:
                k=a[i][j]*z%P
                a[i]=[(u-k*v)%P for u,v in zip(a[i],a[j])]
    return det%P

def moments(bag,indices):
    out={}
    for (r,x),mass in bag.items():
        v=out.setdefault(r,{a:Fraction(0) for a in indices})
        for a in indices:v[a]+=mass*ev(x,a)
    return out

def advance(q,bag,M,indices):
    B={}; T={}
    for r in range(q):
        for s,b,weight in ((r,(1,0,0,0,0,0),Fraction(r+2,r+3)),
                           ((r+1)%q,(-1,0,0,0,0,0),Fraction(r+3,r+4)),
                           (r,(0,1,0,0,0,0),Fraction(r+4,r+5))):
            for (old,x),v in bag.items():
                if old==r:
                    y=tuple(xi+bi for xi,bi in zip(x,b))
                    B[s,y]=B.get((s,y),Fraction(0))+v*weight
            if r in M:
                target=T.setdefault(s,{a:Fraction(0) for a in indices})
                for beta in indices:
                    p=Fraction(0)
                    for alpha in indices:
                        if all(k<=t for k,t in zip(alpha,beta)):
                            c=1
                            for be,al,bi in zip(beta,alpha,b):
                                c*=comb(be,al)*bi**(be-al)
                            p+=c*M[r][alpha]
                    target[beta]+=p*weight
    assert moments(B,indices)==T
    return B,T

def main():
    t=tails(); indices=mono(6,3); assert len(indices)==84
    for q in (2,3,4,5,8):
        bags=[]; dets=[]
        for r in range(q):
            pref=(-1,)*r+(1,)*(q-1-r)
            words=[pref+w for w in t]
            assert all(len(w)==q+2 and sum(v==-1 for v in w)%q==r for w in words)
            bags += [(r,w) for w in words]
            dets.append(detmod([[ev(ep(w),a) for a in indices] for w in words]))
        # At N=q+1, sector q-1 has 62 endpoints, 63 for q=2.
        dire=(1,)+(2,-2,3,-3,4,-4,5,-5,6,-6)
        endpoints=set()
        for k in range(q-1,q+2,q):
            for v in product(dire,repeat=q+1-k): endpoints.add(ep((-1,)*k+v))
        assert len(endpoints)==(63 if q==2 else 62)
        seed={}
        for j,(r,w) in enumerate(bags[::3]):
            x=ep(w)
            seed[r,x]=seed.get((r,x),Fraction(0))+Fraction(1,1+j%7)
        M=moments(seed,indices); bag=seed
        for _ in range(3):bag,M=advance(q,bag,M,indices)
        print(f'q={q} Nmin={q+2} words={len(bags)} lower_sector={len(endpoints)} rank={84*q} determinant_mod={dets[0]} BRC_3_steps=PASS')
    print('PASS: exact native-word cubic full-rank witness and typed BRC cubic transport')

if __name__=='__main__': main()
