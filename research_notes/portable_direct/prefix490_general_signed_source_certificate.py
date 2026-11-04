#!/usr/bin/env python3
"""PREFIX-490: exact native-X6/BRC observer/source/KMP support checks.

Model: s=0; ten signed primitive directions a/A,...,e/E of the five
ordinary axes (sixth special axis held at zero), KMP terminal q=0.
Every state stores full signed direction occupancy, order-sensitive KMP,
and first b/B-versus-c/C source state. Only boolean support is counted.
No external trigonometric or physical propagator is used.
"""
from collections import Counter, defaultdict
from functools import lru_cache
from math import comb

ALPHABET='aAbBcCdDeE'
AXES='abcde'
N,B,C=1,2,4
GATES=('aab','aba')

@lru_cache(None)
def step(q,ch,gate):
    s=gate[:q]+ch
    return next(k for k in range(len(gate),-1,-1) if s.endswith(gate[:k]))

def mask_from_p(m,v,w):
    tag=0
    if v>=w and (v-w)%2==0 and v+w<=2*m: tag|=N
    if w<=m-1 and 1<=v<=2*m-w-1: tag|=B
    if 1<=w<=m and v<=2*m-w-1: tag|=C
    assert tag
    return tag

def boundary_removed(y,gate):
    a,b,c,d,e=y
    if (c,d,e)!=(0,0,0) or a<0 or b<0:return False
    if b==0 and a>=1:return True
    if b==1 and a >= (2 if gate=='aab' else 1):return True
    return False

def mask(y,m,v,w,gate):
    a,b,c,d,e=y
    if m==0:
        assert (v,w)==(0,0)
        if boundary_removed(y,gate):return 0
        return (B if b!=0 else 0)|(C if c!=0 else 0) or N
    mask0=mask_from_p(m,v,w)
    if b and c:return B|C
    if b:return B|(C if mask0&C else 0)
    if c:return C|(B if mask0&B else 0)
    return mask0

def all_y_at_n(n):
    def go(rem,k,prefix):
        if k==5:
            if rem%2==0:yield tuple(prefix),rem//2
            return
        for a in range(-rem,rem+1):
            yield from go(rem-abs(a),k+1,prefix+[a])
    yield from go(n,0,[])

def predicted(n,gate):
    obs={}
    for y,m in all_y_at_n(n):
        for w in range(m+1):
            for v in range(2*m-w+1):
                k=mask(y,m,v,w,gate)
                if k:obs[y,v,w]=k
    return obs

def exact_dp(nmax,gate):
    states={(0,)*10+(0,N)}
    for n in range(nmax+1):
        obs=defaultdict(int)
        for item in states:
            counts,q,tag=item[:10],item[10],item[11]
            if q!=0:continue
            y=tuple(counts[2*i]-counts[2*i+1] for i in range(5))
            p=[min(counts[2*i],counts[2*i+1]) for i in range(5)]
            v=p[1]+2*p[3]+p[4]
            w=p[2]+p[4]
            obs[y,v,w]|=tag
        pred=predicted(n,gate)
        if dict(obs)!=pred:
            bad=[(k,obs.get(k,0),pred.get(k,0)) for k in set(obs)|set(pred) if obs.get(k,0)!=pred.get(k,0)]
            raise AssertionError(('STATE_DISAGREEMENT',gate,n,len(obs),len(pred),bad[:10]))
        print('ORDERED_SUPPORT_DP_PASS',gate,'n',n,'raw_states',len(states),'q0_fibers',len(obs),'masks',dict(sorted(Counter(obs.values()).items())))
        if n==nmax:break
        nxt=set()
        for item in states:
            counts,q,tag=item[:10],item[10],item[11]
            for idx,ch in enumerate(ALPHABET):
                cc=list(counts);cc[idx]+=1
                t=tag
                if tag==N:
                    if ch in 'bB':t=B
                    elif ch in 'cC':t=C
                nxt.add(tuple(cc)+(step(q,ch,gate),t))
        states=nxt

def all_mask_counts(n,gate):
    return Counter(predicted(n,gate).values())

def signed3(k):
    return sum(comb(3,i)*comb(k-i+2,2) for i in range(min(3,k)+1))

def signed5(k):
    return sum(comb(5,i)*comb(k-i+4,4) for i in range(min(5,k)+1))

def total_formula(n,gate):
    def c(a):return comb(a+7,7) if a>=0 else 0
    base=sum(comb(2,j)*(c(n-j)+2*c(n-j-2)) for j in range(3))
    return base-(n>=1)-(n>=3 if gate=='aab' else n>=2)

def check_lattice_and_series():
    for m in range(51):
        total=(m+1)*(3*m+2)//2
        initial=Counter(mask_from_p(m,v,w) for w in range(m+1) for v in range(2*m-w+1)) if m>=1 else Counter({N:1})
        assert sum(initial.values())==total
        if m>=1:
            assert initial==Counter({N:m+2,B:m,C:2*m-1,N|B:m-1,B|C:(m-1)**2,N|B|C:m*(m-1)//2})
            for b,c in ((1,0),(0,-2),(1,1)):
                kinds=Counter(mask((0,b,c,0,0),m,v,w,'aba') for w in range(m+1) for v in range(2*m-w+1))
                if b and c:assert kinds==Counter({B|C:total})
                else:
                    single=B if b else C
                    assert kinds==Counter({single:3*m+1,B|C:m*(3*m-1)//2})
    print('LATTICE_MASK_FORMULAE_M0_TO50_PASS')
    for n in range(41):
        total=sum(signed5(n-2*m)*(m+1)*(3*m+2)//2 for m in range(n//2+1))
        for gate in GATES:
            correction=(n>=1)+(n>=3 if gate=='aab' else n>=2)
            assert total-correction==total_formula(n,gate),(gate,n,total,correction,total_formula(n,gate))
    print('ALL_SIGNED_FIVE_AXIS_RATIONAL_TOTAL_COEFFICIENTS_N0_TO40_PASS')
    for n in (0,1,2,3,4,5,8,12):
        ca=all_mask_counts(n,'aab'); cb=all_mask_counts(n,'aba')
        assert sum(ca.values())-sum(cb.values())==(1 if n==2 else 0)
        d=ca-cb
        print('ALL_SIGNED_COEFFICIENT',n,'aab',sum(ca.values()),'aba',sum(cb.values()),'mask_diff',dict(d))

if __name__=='__main__':
    check_lattice_and_series()
    for gate in GATES:
        exact_dp(7,gate)
    print('ALL_CHECKS_PASS')
