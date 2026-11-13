#!/usr/bin/env python3
"""R127 affine-clock two-integer exact checker (Python 3, Fraction-only)."""
from fractions import Fraction as F
from math import floor, ceil, gcd
import random, json

def egcd(a,b):
    if b == 0:
        return (abs(a),1 if a>=0 else -1,0)
    g,s,t=egcd(b,a%b)
    return g,t,s-(a//b)*t

def shortest_relation(A,d,E):
    g=gcd(A,d)
    if g==0:
        return (0,0) if E==0 else None
    if E%g: return None
    gg,u0,v0=egcd(A,d)
    u0*=E//gg;v0*=E//gg
    su=d//g;sv=-A//g
    candidates={0}
    for q0,step in ((u0,su),(v0,sv)):
        if step:
            val=F(-q0,step)
            for t in (floor(val)-1,floor(val),ceil(val),ceil(val)+1):
                candidates.add(t)
    vals=[(abs(u0+su*t)+abs(v0+sv*t),abs(u0+su*t),abs(v0+sv*t),u0+su*t,v0+sv*t) for t in candidates]
    val=min(vals)
    return val[3],val[4]

def floor_range(slope,bias,l,h):
    return range(floor(min(bias+slope*l,bias+slope*h))-1, floor(max(bias+slope*l,bias+slope*h))+2)

def exact_interval(conditions,l,h):
    # condition: (slope, intercept, strict) means affine >=0 / >0
    low,hi=l,h
    lc,hc=True,True  # the input J=(l,h) has strict endpoints
    for slope,bias,strict in conditions:
        if slope==0:
            if bias<0 or (bias==0 and strict): return None
            continue
        bnd=-bias/slope
        if slope>0:
            if bnd>low: low=bnd;lc=strict
            elif bnd==low: lc=lc or strict
        else:
            if bnd<hi: hi=bnd;hc=strict
            elif bnd==hi: hc=hc or strict
        if low>hi or (low==hi and (lc or hc)): return None
    if low<hi:return (low+hi)/2
    return low if not (lc or hc) else None

def add_interval(conds,slope,bias,lo,hi):
    conds.extend(((slope,bias-lo,False),(-slope,hi-bias,True)))

def local_feasible(x,A,d,E,m,l,h,bits,u,v):
    assert A*u+d*v==E
    L=min(0,u)+min(0,v)-u*x
    U=max(0,u)+max(0,v)-u*x
    hs=range(floor(L),floor(U)+1)
    vocab=[]
    for z in range(1<<(m-1)):
        cur=0;w=[0]
        for i in range(m-1):cur+=(z>>i)&1;w.append(cur)
        vocab.append(w)
    systems=0
    for n in floor_range(A,x,l,h):
      for k in floor_range(d,F(0),l,h):
       for t in hs:
        r=u*n+v*k+t
        for w in vocab:
            systems+=1
            conds=[]
            add_interval(conds,A,x-n,0,1)
            add_interval(conds,d,F(-k),0,1)
            add_interval(conds,E,F(-r),0,1)
            for i in range(m):
                zsl=A+i*d; zbi=x-n-i*k-w[i]
                add_interval(conds,zsl,zbi,0,1)
                sl=E-zsl; bi=-r-zbi
                if bits[i]: conds.append((sl,bi,True))
                else: conds.append((-sl,-bi,False))
            witness=exact_interval(conds,l,h)
            if witness is not None:
                return witness,systems
    return None,systems

def member(x,A,d,E,m,theta):
    L=(E*theta)%1
    return tuple(int((x+(A+i*d)*theta)%1 < L) for i in range(m))

def full_reference(x,A,d,E,m,l,h):
    cuts={l,h}
    for i in range(m):
        t=A+i*d
        for sl,bi in ((t,x),(E,F(0)),(t-E,x)):
            if not sl:continue
            lower=min(sl*l+bi,sl*h+bi)
            upper=max(sl*l+bi,sl*h+bi)
            for n in range(ceil(lower),floor(upper)+1):
                pt=(F(n)-bi)/sl
                if l<pt<h: cuts.add(pt)
    sortedcuts=sorted(cuts)
    reps=[(p+q)/2 for p,q in zip(sortedcuts,sortedcuts[1:])]+sortedcuts[1:-1]
    sigs={member(x,A,d,E,m,theta) for theta in reps}
    return sigs,len(reps)

def main():
    rr=random.Random(12720261113)
    stats={'cases':0,'words':0,'candidate_systems':0,'critical_representatives':0,'positive_witnesses':0,'short_relation_checks':0,'huge_signed_witnesses':0,'nonproportional_e_d':0}
    for _ in range(64):
        A=rr.randint(-5,5);d=rr.randint(-5,5); u0=rr.randint(-3,3); v0=rr.randint(-3,3)
        E=u0*A+v0*d
        if A==d==0:continue
        u,v=shortest_relation(A,d,E)
        if E and d and E%d:stats['nonproportional_e_d']+=1
        assert A*u+d*v==E
        g=gcd(A,d)
        for t in range(-40,41):
            assert abs(u)+abs(v)<=abs(u+d//g*t)+abs(v-A//g*t)
        stats['short_relation_checks']+=1
        m=rr.randint(2,4)
        x=F(rr.randint(-5,5),rr.randint(2,7)); l=F(rr.randint(-6,-1),4);h=F(rr.randint(1,6),4)
        reference,nreps=full_reference(x,A,d,E,m,l,h)
        stats['critical_representatives']+=nreps
        for mask in range(1<<m):
            bits=tuple((mask>>i)&1 for i in range(m))
            witness,systems=local_feasible(x,A,d,E,m,l,h,bits,u,v)
            stats['candidate_systems']+=systems;stats['words']+=1
            assert (witness is not None)==(bits in reference), (x,A,d,E,m,l,h,u,v,bits,witness)
            if witness is not None:
                assert member(x,A,d,E,m,witness)==bits
                stats['positive_witnesses']+=1
        stats['cases']+=1
    for _ in range(600):
        A=rr.randint(-80,80);d=rr.randint(-80,80);E=rr.randint(-80,80)
        sol=shortest_relation(A,d,E)
        if sol is None:
            assert (gcd(A,d)==0 and E!=0) or (E%gcd(A,d))
            continue
        u,v=sol
        assert A*u+d*v==E
        g=gcd(A,d)
        if g:
            for t in range(-10,11):
                assert abs(u)+abs(v)<=abs(u+d//g*t)+abs(v-A//g*t)
        stats['short_relation_checks']+=1
    for sign in (1,-1):
        A=sign*(10**120+7)
        d=sign*(10**120+9)
        E=A-d
        u,v=shortest_relation(A,d,E)
        assert A*u+d*v==E and abs(u)+abs(v)<=2
        x=F(2,7);m=4
        theta=F(19,10**123+37)
        bits=member(x,A,d,E,m,theta)
        n=floor(x+A*theta);k=floor(d*theta)
        h=floor(E*theta-u*n-v*k)
        r=u*n+v*k+h
        assert r==floor(E*theta)
        for i in range(m):
            wi=floor(((x+A*theta)%1)+i*((d*theta)%1))
            z=x+(A+i*d)*theta-n-i*k-wi
            assert F(0)<=z<1
            assert (z<(E*theta-r))==bool(bits[i])
        stats['huge_signed_witnesses']+=1
    print('R127_AFFINE_TWO_INTEGER_PASS')
    print(json.dumps(stats,indent=2))
    with open('verification_r127.json','w') as f:
        json.dump({'status':'R127_AFFINE_TWO_INTEGER_PASS','seed':12720261113,'result':stats,'reference':'independent complete affine critical cuts including singleton crossings; exact Fraction inequalities and signed boundary semantics','note':'bounded exact enumerator, not a production fixed-dimensional integer programming solver'},f,indent=2)

if __name__=='__main__':main()
