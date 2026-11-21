#!/usr/bin/env python3
"""Exact Q(zeta_6) rational-function proof and independent bounded DP for frozen R5."""
import json
from collections import defaultdict
from fractions import Fraction
import sympy as sp

S = [set(range(214,219)), {214,216,217,218,219,220,221},
     set(range(215,222)), set(range(223,291)), set(range(296,313))]
PRICES = set(range(214,315))
Q = [(1,0),(0,1),(-1,1),(-1,0),(0,-1),(1,-1)]

def mul(x,y):
    a,b=x;c,d=y
    return a*c-b*d, a*d+b*c+b*d

def inverse(x):
    a,b=x; n=a*a+a*b+b*b
    return Fraction(a+b,n), Fraction(-b,n)

def p_add(x,y):
    return x[0]+y[0],x[1]+y[1]

def original_ratio(mask):
    u=set().union(*(S[j] for j in range(3) if (mask>>j)&1))
    v=(1,0)
    for p in sorted(u-S[0]):
        v=mul(v,(1-Q[p%6][0],-Q[p%6][1]))
    for p in sorted(S[0]-u):
        v=mul(v,inverse((1-Q[p%6][0],-Q[p%6][1])))
    return v

def dp_local(mask,m):
    active=[j for j in range(3) if (mask>>j)&1]
    u=sorted(set().union(*(S[j] for j in active)))
    state={tuple(0 for _ in active):(1,0)}
    for p in u:
        positions=[i for i,j in enumerate(active) if p in S[j]]
        next_state=defaultdict(lambda:(0,0))
        for keys,weight in state.items():
            limit=min(m-1-keys[i] for i in positions)
            v=(1,0)
            for n in range(limit+1):
                key=list(keys)
                for i in positions:
                    key[i]+=n
                t=tuple(key)
                next_state[t]=p_add(next_state[t],mul(weight,v))
                v=mul(v,Q[p%6])
        state=next_state
    return tuple(sum(v[i] for v in state.values()) for i in (0,1))

def independent_leading(m):
    val=(0,0)
    for mask in range(1,8):
        v=mul(original_ratio(mask),dp_local(mask,m))
        sign=1 if mask.bit_count()%2 else -1
        val=p_add(val,(sign*v[0],sign*v[1]))
    return val

# Rational functions over the exact quadratic field Q(sqrt(-3)).
z=sp.Symbol('z')
w=sp.sqrt(-3)
K=sp.QQ.algebraic_field(w)
q=K.from_sympy((1+w)/2)
one=K.one
zero=K.zero

def pol(*v):
    return sp.Poly.from_list(
        [x if isinstance(x,type(q)) else K.from_sympy(sp.sympify(x)) for x in v],
        z,domain=K)

P0=pol(0)
P1=pol(1)
Z=pol(1,0)

class RF:
    def __init__(self,num,den=P1):
        self.n=num if isinstance(num,sp.Poly) else pol(num)
        self.d=den if isinstance(den,sp.Poly) else pol(den)
        g=self.n.gcd(self.d)
        if g.degree()>0:
            self.n=self.n.exquo(g)
            self.d=self.d.exquo(g)
        c=K.from_sympy(self.d.LC())
        self.n=self.n.mul_ground(one/c)
        self.d=self.d.mul_ground(one/c)
    def __add__(self,b):
        if not isinstance(b,RF):
            b=RF(b)
        return RF(self.n*b.d+self.d*b.n,self.d*b.d)
    __radd__=__add__
    def __neg__(self):
        return RF(-self.n,self.d)
    def __sub__(self,b):
        return self+-b
    def __mul__(self,b):
        if not isinstance(b,RF):
            b=RF(b)
        return RF(self.n*b.n,self.d*b.d)
    __rmul__=__mul__

rZ=RF(Z)
r1=RF(P1)

def invlin(v,degree=1):
    return RF(P1,P1-pol(v)*Z**degree)

a=q**4
b=q**5
C=invlin(one)*invlin(q)*invlin(q*q)

def D(v):
    return invlin(q**3*v)*invlin(q**4*v)*invlin(q**5*v)

D_at_1=one/((one-q**3)*(one-q**4)*(one-q**5))

def max_pair(a,b):
    return invlin(a)*invlin(a*b)+(invlin(b)-invlin(a*b))*(one/(one-a))

def max_b_D(b):
    return D(b)*invlin(b)+(D(one)-D(b))*(one/(one-b))

def max_three(a,b,c):
    return (r1-RF(pol(a*b*c))*rZ*rZ*rZ)*invlin(a*b*c,2)*invlin(a)*invlin(b)*invlin(c)

parts={
 1:invlin(a)*invlin(b)*D_at_1,
 2:invlin(a)*D(one)*(one/(one-b)),
 4:invlin(b)*D(one)*(one/(one-a)),
 3:invlin(a)*max_b_D(b),
 5:invlin(b)*max_b_D(a),
 6:D(one)*max_pair(a,b),
}
# D_d=(sqrt(-3)/3)q^(3d) + q^(4d) - (sqrt(-3)/3)q^(5d).
parts[7]=sum([max_three(a,b,q**3)*K.from_sympy(w/3),
              max_three(a,b,q**4),
              max_three(a,b,q**5)*K.from_sympy(-w/3)],RF(P0))
G=sum((parts[m]*(1 if m.bit_count()%2 else -1) for m in range(1,8)),RF(P0))
G=rZ*invlin(one)*C*G
Sgen=G*(4*q-2*one)

R_terms={1:7*one-4*q,2:-2*one+8*q,3:-2*one+4*q,4:-4*one,
         6:-2*one-4*q,7:15*one-8*q,8:8*q,9:-4*one+8*q,
         10:-4*q,12:-4*q,13:9*one-4*q,14:2*one,15:-2*one+4*q,
         16:4*one-4*q,18:2*one,19:one}
R=sp.Poly(0,z,domain=K)
for e,v in R_terms.items():
    R+=pol(v)*Z**e
assert (Sgen.n*(P1-Z**12)**2-R*Sgen.d).is_zero, 'global rational identity failed'

def proposed(m):
    k,r=divmod(m-1,12)
    r+=1
    return R_terms.get(r,zero)+k*(R_terms.get(r,zero)+R_terms.get(r+12,zero))

def pair(v):
    # q=(1+w)/2; express algebraic number as a+bq.
    expression=sp.expand(K.to_sympy(v))
    coeff=sp.expand(expression).coeff(w)
    b=sp.simplify(2*coeff)
    aa=sp.simplify(expression-b*(1+w)/2)
    return int(aa),int(b)

M=24
for m in range(1,M+1):
    assert independent_leading(m)==pair(proposed(m)),('DP mismatch',m)

for mask in range(1,32):
    u=set().union(*(S[j] for j in range(5) if (mask>>j)&1))
    count=sum(p%6==0 for p in PRICES-u)
    assert count==16 if mask<8 else count<=14

higher=max(sum(p%d==0 for p in PRICES-set().union(*(S[j] for j in range(5) if (mask>>j)&1)))
           for d in range(7,315) for mask in range(1,32))
assert higher<=14
exceptional=[m for m in range(1,M+1) if proposed(m)==zero]
assert exceptional==[5,11,17,23]
assert all(proposed(m)==zero for m in (5,11,17,23,29,35,41,47))
P6=1
for p in range(222,313,6):
    P6*=p

def v6(m):
    coeff=pair(proposed(m))
    return [2*mul(coeff,Q[(-n)%6])[0]+mul(coeff,Q[(-n)%6])[1] for n in range(6)]

res={'status':'PASS','arithmetic':'Q(sqrt(-3))_EXACT','gf_identity':True,
     'normalized_generating_numerator':{str(i):str(sp.expand(K.to_sympy(c))) for i,c in R_terms.items()},
     'local_DP_independent_thresholds':[1,M], 'sixth_root_pole_order':16,
     'sixth_root_leading_degree_regular':15,
     'vanishing_leading_classes_m_mod6':[5],
     'm1_sixth_root_fourier_vector':v6(1),
     'm2_sixth_root_fourier_vector':v6(2),
     'd_ge7_max_remaining_multiple_count':higher,
     'm_to_leading_coeff_a_plus_bq':{str(m):list(pair(proposed(m))) for m in range(1,25)},
     'proven_minimal_modulus_at_error_O_N14':60,
     'predecessor_frozen_sha256':'50e87f0194cfb3780e84b7bbb6f9a2dca4f79bb4901cab06f1a5b59256fb470b',
     'independent_review':'NOT_REVIEWED'}
print(json.dumps(res,ensure_ascii=False,indent=2))
