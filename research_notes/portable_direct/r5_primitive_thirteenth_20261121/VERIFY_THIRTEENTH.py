#!/usr/bin/env python3
"""Exact primitive-13 coefficient check, finite input / no floating point."""
from fractions import Fraction
import json

P=13
D=P-1
R=(6,7,8,9,10)
COMPLEMENT=(1,2,3,4,5,11,12)
ZERO=(0,)*D
ONE=(1,)+(0,)*(D-1)

def add(a,b):
    return tuple(x+y for x,y in zip(a,b))

def neg(a):
    return tuple(-x for x in a)

def mul(a,b):
    c=[0]*P
    for i,x in enumerate(a):
        if x:
            for j,y in enumerate(b):
                if y:
                    c[(i+j)%P]+=x*y
    return tuple(c[i]-c[D] for i in range(D))

def mon(k):
    k%=P
    if k==D:
        return (-1,)*D
    return tuple(int(j==k) for j in range(D))

def scalar(a,s):
    return tuple(x*s for x in a)

def sub(a,b):
    return add(a,neg(b))

# coeffs [t^j] prod_{r in complement}(1-z^r*t)
coef=[ONE]
for r in COMPLEMENT:
    nxt=[ZERO]*(len(coef)+1)
    for j,v in enumerate(coef):
        nxt[j]=add(nxt[j],v)
        nxt[j+1]=sub(nxt[j+1],mul(v,mon(r)))
    coef=nxt
assert len(coef)==8
assert all(any(v) for v in coef)

# Independent coefficient DP of H(t)=prod_{r=6}^{10} (1-z^r t)^(-1)
MAX_M=78
h=[ZERO]*MAX_M
h[0]=ONE
for r in R:
    zr=mon(r)
    for j in range(1,MAX_M):
        h[j]=add(h[j],mul(zr,h[j-1]))
B=ZERO
for m in range(1,MAX_M+1):
    B=add(B,h[m-1])
    target=coef[(m-1)%P] if (m-1)%P<=7 else ZERO
    assert B==target, (m,B,target)

# Independent direct enumeration of five multiplicities for m<=12
for m in range(1,13):
    table=[ZERO]*m
    def rec(i,spent,phase):
        if i==5:
            table[spent]=add(table[spent],mon(phase))
            return
        for x in range(m-spent):
            rec(i+1,spent+x,phase+x*R[i])
    rec(0,0,0)
    got=ZERO
    for a in table:
        got=add(got,a)
    expect=coef[(m-1)%P] if m<=8 else ZERO
    assert got==expect, m

# Inverse of (1-z^r) in Q[z]/Phi_13 via cyclotomic identity
def inverse_1minus(r):
    s=ZERO
    for j in range(1,P):
        s=add(s,scalar(mon(j*r),-j))
    s=scalar(s,Fraction(1,P))
    assert mul(sub(ONE,mon(r)),s)==ONE
    return s

counts={r:sum(p%P==r for p in range(219,315)) for r in range(P)}
assert counts[0]==8 and all(counts[r] in (7,8) for r in range(1,13))
extra=[r for r in range(1,P) if counts[r]==8]
assert extra==[1,2,11,12]
H=scalar(ONE,Fraction(1,P**7))
for r in extra:
    H=mul(H,inverse_1minus(r))

def trace(a):
    return 12*a[0]-sum(a[1:])

profiles={}
for m in (1,2,7,8,9,13,14):
    v=coef[(m-1)%P] if (m-1)%P<=7 else ZERO
    f=[trace(mul(H,mul(v,mon(-N)))) for N in range(P)]
    assert sum(f)==0
    assert bool(any(f)) == bool(any(v))
    profiles[m]=[str(x) for x in f]

sets=[set(range(214,219)),{214,216,217,218,219,220,221},set(range(215,222)),set(range(223,291)),set(range(296,313))]
free=[p for p in range(214,315) if p%P==0]
assert free==[221,234,247,260,273,286,299,312]
pole_sizes={}
for mask in range(1,1<<5):
    union=set().union(*(sets[i] for i in range(5) if mask>>i&1))
    pole_sizes[str(mask)]=len(set(free)-union)
assert pole_sizes['1']==8 and max(pole_sizes[str(mask)] for mask in range(2,32))<=7

out={
  'result_schema':'R5_PRIMITIVE_THIRTEENTH_EXACT_V1',
  'field':'Q(zeta_13), integral Z[z]/Phi13 basis coefficient order 0..11',
  'Q_0_to_Q_7':[list(x) for x in coef],
  'primitive_root_13_nonzero_m_mod_13':[1,2,3,4,5,6,7,8],
  'primitive_root_13_zero_m_mod_13':[9,10,11,12,0],
  'local_DP_m_range':[1,78],
  'direct_enumeration_m_range':[1,12],
  'pole_orders_by_event_mask':pole_sizes,
  'free_13_multiples':free,
  'nonmultiple_H13_extra_residues':extra,
  'Fourier_profiles_m':profiles,
  'P13':str(__import__('math').prod(free)),
  'validation':'PASS',
  'limitation':'Author exact finite arithmetic, not an independent review; no complete F_m modulus at O(N^6) claimed.'
}
if __name__=='__main__':
    print(json.dumps(out,ensure_ascii=False,sort_keys=True,indent=2))
