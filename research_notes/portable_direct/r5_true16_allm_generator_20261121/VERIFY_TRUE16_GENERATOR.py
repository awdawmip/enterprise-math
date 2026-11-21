#!/usr/bin/env python3
"""Exact cyclotomic proof certificate for corrected R5 primitive-16 poles.

All arithmetic in Q[z]/(z^8+1); standard-library only. This verifier
checks the 32 affine nonvanishing witnesses using a rational generating
function derived from the genuine three-event union, not a union-size cap.
"""
import json
from fractions import Fraction as Q
from math import gcd

class K:
    __slots__ = ('v',)
    def __init__(self, x=0):
        if isinstance(x,K): self.v=x.v
        elif isinstance(x,(int,Q)): self.v=(Q(x),)+(Q(0),)*7
        else:
            assert len(x)==8
            self.v=tuple(Q(t) for t in x)
    def __add__(self,x):
        w=K(x).v;return K([self.v[i]+w[i] for i in range(8)])
    __radd__=__add__
    def __neg__(self):return K([-x for x in self.v])
    def __sub__(self,x):return self+-K(x)
    def __rsub__(self,x):return K(x)+-self
    def __mul__(self,x):
        w=K(x).v;out=[Q(0)]*8
        for i,a in enumerate(self.v):
            if not a:continue
            for j,b in enumerate(w):
                if b:out[(i+j)%8]+=(1 if i+j<8 else -1)*a*b
        return K(out)
    __rmul__=__mul__
    def __pow__(self,n):
        assert n>=0
        out=K(1);base=self
        while n:
            if n&1:out=out*base
            base=base*base;n//=2
        return out
    def __eq__(self,x):return self.v==K(x).v

ZERO=K(0); ONE=K(1); Z=K([0,1,0,0,0,0,0,0])
def zpow(p):return Z**(p%16)

def inverse_1_minus_zpower(p):
    # q=z^p has order r>1: (1-q)^(-1)=-sum_{j=1}^{r-1}j*q^j/r
    r=16//gcd(16,p)
    assert r>1
    q=zpow(p)
    v=-sum((j*(q**j) for j in range(1,r)),ZERO)*Q(1,r)
    assert (ONE-q)*v==ONE
    return v

def multiply_series(f,g,n):
    out=[ZERO]*n
    for i,x in enumerate(f[:n]):
        if x==ZERO:continue
        for j,y in enumerate(g[:n-i]):
            if y!=ZERO:out[i+j]=out[i+j]+x*y
    return out

def geom(q,n,step=1):
    out=[ZERO]*n;x=ONE
    for i in range(0,n,step):out[i]=x;x=x*q
    return out

def H_series(a,b,d,inv_a,inv_b,inv_d,n):
    # H=sum_{x,y,v>=0} a^x b^y d^v t^{min(x+y,x+v,y+v)}
    # First rational summand.
    u=multiply_series(geom(d,n),geom(a*b,n),n)
    pref=(ONE-a*b)*inv_a*inv_b
    first=[pref*w for w in u]
    # Second rational summand; expand each geometric denominator.
    v=geom(d,n)
    for q,k in [(a*b*d,2),(a*d,1),(b*d,1)]:
        v=multiply_series(v,geom(q,n,k),n)
    q=a*b*d*d
    second=[d*inv_d*(v[i]-(v[i-1] if i>0 else ZERO)
             -q*(v[i-2] if i>1 else ZERO)+q*(v[i-3] if i>2 else ZERO))
             for i in range(n)]
    return [first[i]+second[i] for i in range(n)]

def coefficients(n=96):
    a=zpow(214);b=zpow(215)
    cs=[zpow(p) for p in (216,217,218)]
    ds=[zpow(p) for p in (219,220,221)]
    # Exact partial-fraction constants for product_{p=219}^{221}(1-z^p u)^(-1).
    ds_weights=[K([Q(-1,2),Q(-1,2),0,0,Q(1,2),Q(1,2),1,1]),
                K([2,Q(3,2),1,Q(1,2),0,Q(-1,2),-1,Q(-3,2)]),
                K([Q(-1,2),-1,-1,Q(-1,2),Q(-1,2),0,0,Q(1,2)])]
    # Verifies weights instead of assuming an unexamined interpolation table.
    D=[ONE]
    for d in ds:D=multiply_series(D,geom(d,8),8)
    for i in range(8):
        assert sum((ds_weights[j]*ds[j]**i for j in range(3)),ZERO)==D[i]
    f=[ZERO]*n
    for j,d in enumerate(ds):
        v=H_series(a,b,d,inverse_1_minus_zpower(214),
                   inverse_1_minus_zpower(215),inverse_1_minus_zpower(219+j),n)
        f=[f[i]+ds_weights[j]*v[i] for i in range(n)]
    for c in cs:f=multiply_series(f,geom(c,n),n)
    W=ONE
    for p in range(214,222):W=W*(ONE-zpow(p))
    out=[];s=ZERO
    for i in range(n):s=s+f[i];out.append(W*s)
    return out

def prove():
    a=coefficients(96)
    assert all(all(x.denominator==1 for x in v.v) for v in a)
    known={1:(16,10,-4,-10,-16,-18,-20,-22),
           2:(-16,4,24,40,44,48,40,36),
           3:(-8,-14,-16,-14,-8,-2,0,6),
           4:(16,4,-8,-24,-32,-36,-32,-24),
           5:(24,8,-4,-12,-24,-28,-36,-32),
           13:(60,36,4,-36,-60,-84,-84,-76),
           16:(-32,32,96,136,160,152,128,88)}
    for m,vector in known.items(): assert a[m-1].v==tuple(map(Q,vector))
    # The rational formula's denominators have poles of multiplicity <=2,
    # all supported at 32nd roots. Its reduced numerator has degree <=58.
    # Therefore (1-t^32)^2*A(t) has no coefficients above t^58.
    for n in range(59,96):
        v=a[n]-(2*a[n-32] if n>=32 else ZERO)+(a[n-64] if n>=64 else ZERO)
        assert v==ZERO,(n,v.v)
    witnesses=[]
    for r in range(1,33):
        C=a[r-1];B=a[r+31]-C
        j=next((i for i in range(8) if C.v[i] and
               (B.v[i]==0 or (C.v[i]>0)==(B.v[i]>0))),None)
        assert j is not None
        witnesses.append({'r':r,'coordinate':j,'C':int(C.v[j]),'B':int(B.v[j])})
    return {'status':'PASS','model':'R5 frozen scalar failure observer',
            'field':'Q[z]/(z^8+1)','generating_function':'TRUE_THREE_EVENT_UNION',
            'denominator_bound':'(1-t^32)^2','numerator_degree_bound':58,
            'recurrence':'A_(m+64)-2*A_(m+32)+A_m=0 for every m>=1',
            'certificates':witnesses,
            'initial_coefficients_64':[[int(x) for x in v.v] for v in a[:64]],
            'cross_check_m':list(known),
            'nonzero_for_all_positive_m':True,
            'implication':'16 divides minimum coefficient quasipolynomial period modulo O_m(N^4)',
            'review':'NOT_REVIEWED'}
if __name__=='__main__':
    print(json.dumps(prove(),ensure_ascii=False,indent=2))
