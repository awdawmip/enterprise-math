"""PREFIX-1016 exact positive-port contrast: symbolic Laurent + integer checks.

Frozen candidate signed X6 BRC, blocked Link {0,e1}, k=1.
Requires Python 3 and sympy. Run python PREFIX1016_R6_POSITIVE_PORT_A6_CLOSURE_CHECK.py.
"""
from collections import defaultdict
from functools import lru_cache
from math import comb
from pathlib import Path
import json
import sympy as sp

SIGNS = {
    "000000": (0,0,0,0,0,0),
    "000011": (1,-1,0,0,0,0),
    "000022": (2,-2,0,0,0,0),
    "000033": (3,-3,0,0,0,0),
    "000112": (2,-1,-1,0,0,0),
    "000123": (3,-2,-1,0,0,0),
    "001111": (1,1,-1,-1,0,0),
    "001113": (3,-1,-1,-1,0,0),
    "001122": (2,1,-2,-1,0,0),
    "011112": (2,1,-1,-1,-1,0),
    "111111": (1,1,1,-1,-1,-1),
}
n,m,t,X,Y = sp.symbols("n m t X Y")

# Exact K+ columns of PREFIX-1014 (distinguished first, other second).
K = {
 "000000":(5*(722*n**2-4834*n+9139),3610*n**2-22826*n+37907),
 "000011":(10*(378*n**2-2503*n+7519),2*(1890*n**2-11723*n+24029)),
 "000022":(-10*(57*n**2-139*n-233),-2*(285*n**2-1271*n+1253)),
 "000033":(10*(2*n**2-3*n-11),2*(10*n**2-39*n-1)),
 "000112":(-80*(63*n**2-316*n+352),-16*(315*n**2-1724*n+2342)),
 "000123":(240*(2*n**2-7*n-3),48*(10*n**2-47*n+27)),
 "001111":(-120*(69*n**2-505*n+961),-24*(345*n**2-2201*n+3515)),
 "001113":(240*(2*n**2-9*n+1),48*(n-1)*(10*n-41)),
 "001122":(1080*(n-5)*(2*n-1),1080*(2*n**2-11*n+11)),
 "011112":(1440*(2*n**2-13*n+9),288*(10*n**2-59*n+69)),
 "111111":(240*(n-1)*(2*n-13),48*(10*n**2-63*n+83)),
}
D={}
for sig,(q1,qstar) in K.items():
    diff=sp.expand(q1-qstar)
    assert sp.degree(diff,n)<=1
    D[sig]=(int(diff.coeff(n)),int(diff.coeff(n,0)))

@lru_cache(maxsize=None)
def H(length,sig):
    delta=SIGNS[sig]
    prev=[int(r+delta[0]>=0) for r in range(length+1)]
    offset=delta[0]
    for axis in range(1,6):
        offset+=delta[axis]
        curr=[]
        for r in range(length+1):
            if r+offset<0:
                curr.append(0)
                continue
            curr.append(sum(comb(r,a)*comb(r+offset,a+delta[axis])*prev[r-a]
                for a in range(r+1) if 0<=a+delta[axis]<=r+offset))
        prev=curr
    return prev[length]

def orbit_contrast(length):
    return sum((a*length+b)*H(length-4,sig) for sig,(a,b) in D.items())

# Differential module of f=g0^6: (q,r) means t^q (d/dt)^r f.
def plus(A,B):
    out=defaultdict(lambda:sp.S(0))
    for key,v in A.items():out[key]+=v
    for key,v in B.items():out[key]+=v
    return {key:sp.cancel(v) for key,v in out.items() if v!=0}

def times(A,c=1,shift=0):
    return {(q+shift,r):sp.cancel(v*c) for (q,r),v in A.items()}

def derive(A):
    out={}
    for (q,r),v in A.items():
        if q:out=plus(out,{(q-1,r):q*v})
        out=plus(out,{(q,r+1):v})
    return out

u=[{(0,0):sp.S(1)},{(0,1):sp.Rational(1,6)}]
for j in range(1,6):
    numer=plus(plus(times(derive(u[j]),shift=1),times(u[j],j)),times(u[j-1],-j))
    u.append(times(numer,sp.Rational(1,6-j),-1))
g={0:X,1:Y,2:(X-Y)/t,3:((t+2)*Y-2*X)/t**2}

def marked(sig):
    delta=SIGNS[sig]
    expr=t**(sum(abs(v) for v in delta)//2)
    for v in delta:expr*=g[abs(v)]
    terms=sp.Poly(sp.expand(expr*t**3),t,X,Y)
    out={}
    for (q,r,s),coefficient in terms.terms():
        assert r+s==6
        out=plus(out,times(u[s],coefficient,q-3))
    return out

op={}
for sig,(a,b) in D.items():
    h=marked(sig)
    op=plus(op,times(derive(h),a,1))
    op=plus(op,times(h,4*a+b))

def ratio(a): # m!/(m+a)!
    if a>0:return 1/sp.prod(m+i for i in range(1,a+1))
    if a<0:return sp.prod(m-i for i in range(-a))
    return sp.S(1)

shifts=defaultdict(lambda:sp.S(0))
for (q,r),value in op.items():
    assert r-q>=0
    shifts[r-q]+=value*ratio(-q)*ratio(r-q)
shifts={s:sp.factor(sp.cancel(v)) for s,v in shifts.items() if v!=0}

expected={
 1:-72*(72*m**2+163*m+80)/(5*(m+1)),
 2:2*(144*m**3+1135*m**2+2367*m+1310)/(5*(m+1)*(m+2)),
 3:-2*(m+8)*(2*m+5)/(5*(m+2))
}
assert set(shifts)==set(expected)
for s in expected:assert sp.cancel(shifts[s]-expected[s])==0

def three_shift(length):
    v=sum(H(length-4+s,"000000")*coefficient.subs(m,length-4)
          for s,coefficient in expected.items())
    assert v.q==1
    return int(v)

# Independently expand the full coherent Laurent port packets from PREFIX-1014.
zero=(0,)*6
E=[]
for i in range(6):
    e=[0]*6;e[i]=1;E.append(tuple(e))
def mon(exp,c=1):return {tuple(exp):c}
def add(P,Q):
    out=defaultdict(int,P)
    for k,v in Q.items():out[k]+=v
    return {k:v for k,v in out.items() if v}
def mult(P,Q):
    out=defaultdict(int)
    for a,ca in P.items():
        for b,cb in Q.items():
            out[tuple(x+y for x,y in zip(a,b))]+=ca*cb
    return {k:v for k,v in out.items() if v}
def scale(P,c):return {k:v*c for k,v in P.items() if v*c}
def power(P,r):
    out=mon(zero)
    for _ in range(r):out=mult(out,P)
    return out
S={e:1 for e in E}
U={tuple(-x for x in e):1 for e in E}
a=mon(E[0])
SU=mult(S,U)

def A(length,j):
    return add(add(add(scale(SU,length-1),mon(zero,-36*(length-3))),
               scale(mult(S,mon(tuple(-x for x in E[0]))),-6)),
               scale(mult(S,mon(tuple(-x for x in E[j]))),-6))

def packet(length,j):
    inside=add(add(mult(S,A(length,j)),scale(mult(a,A(length-1,j)),-1)),scale(a,25))
    return mult(power(S,length-4),mult(mon(E[j]),inside))

def norm2(P):return sum(v*v for v in P.values())
direct={}
for length in range(5,10):
    first=norm2(packet(length,0))
    other=norm2(packet(length,1))
    assert first-other==orbit_contrast(length)==three_shift(length)
    direct[str(length)]={"first":str(first),"other":str(other),"difference":str(first-other)}
for length in list(range(5,51))+[75,100]:
    assert orbit_contrast(length)==three_shift(length)

cert={
 "schema":"PREFIX1016_POSITIVE_PORT_THREE_A6_SHIFTS_V1",
 "frozen_science":"enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d:p000_reality_foundation.json",
 "input":"PREFIX-1014 positive Laurent packet, PREFIX-1007 seven-state module",
 "difference_coefficients":{s:{"n":a,"constant":b} for s,(a,b) in D.items()},
 "three_A6_coefficients":{str(s):str(sp.factor(v)) for s,v in expected.items()},
 "differential_operator_terms":{str(key):str(sp.factor(v)) for key,v in sorted(op.items())},
 "direct_port_check_n5_to_n9":direct,
 "all_orbit_and_three_shift_checks":list(range(5,51))+[75,100],
 "selected_exact_differences":{str(q):str(three_shift(q)) for q in [5,6,7,8,10,20,30,40,50,75,100]},
 "theorem":"all n>=5, exact rational A6-shift identity",
 "unresolved":"all-length strict positive sign",
 "status":"AUTHOR_EXACT_SYMBOLIC_PROOF / INTEGER_CHECKED / NOT_REVIEWED"
}
out=Path(__file__).with_name("PREFIX1016_R6_EXACT_RESULTS.json")
out.write_text(json.dumps(cert,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
print("PASS: exact symbolic three-shift identity, five direct port checks, 48 integer orbit checks")
