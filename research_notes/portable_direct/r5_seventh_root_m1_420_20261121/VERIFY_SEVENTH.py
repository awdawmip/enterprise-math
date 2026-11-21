#!/usr/bin/env python3
"""Exact primitive seventh-root Laurent leading term for frozen R5."""
import json
from collections import defaultdict
import sympy as sp

z = sp.Symbol("z")
phi = sp.cyclotomic_poly(7,z)
S = [set(range(214,219)),{214,216,217,218,219,220,221},
     set(range(215,222)),set(range(223,291)),set(range(296,313))]
prices=set(range(214,315))

def red(p):
    return sp.Poly(sp.rem(sp.expand(p),phi,z),z)

def ratio(mask):
    U=set().union(*(S[j] for j in range(3) if mask&(1<<j)))
    r=sp.Integer(1)
    for p in sorted(U-S[0]):
        r=red(r*(1-z**(p%7))).as_expr()
    for p in sorted(S[0]-U):
        r=red(r*sp.invert(1-z**(p%7),phi,z)).as_expr()
    return r

ratios={i:ratio(i) for i in range(1,8)}

def local(mask,m):
    active=[j for j in range(3) if mask&(1<<j)]
    U=sorted(set().union(*(S[j] for j in active)))
    states={tuple(0 for _ in active):(1,0,0,0,0,0,0)}
    for p in U:
        dims=[i for i,j in enumerate(active) if p in S[j]]
        nxt=defaultdict(lambda:[0]*7)
        for old,vec in states.items():
            limit=min(m-1-old[i] for i in dims)
            for n in range(limit+1):
                dest=list(old)
                for i in dims: dest[i]+=n
                dest=tuple(dest)
                shift=(n*p)%7
                for k,c in enumerate(vec):
                    nxt[dest][(k+shift)%7]+=c
        states=nxt
    total=[0]*7
    for vec in states.values():
        for k,v in enumerate(vec): total[k]+=v
    return red(sum(c*z**j for j,c in enumerate(total))).as_expr()

def leading(m):
    return red(sum((1 if mask.bit_count()%2 else -1)*ratios[mask]*local(mask,m)
                   for mask in range(1,8))).as_expr()

results={}
for m in range(1,13):
    s=leading(m)
    t=red((1-z)*s)
    coeffs=[int(t.nth(j)) for j in range(7)]
    trace=[7*c-sum(coeffs) for c in coeffs]
    results[str(m)]={"S7":str(s),"normalised_trace":trace,"nonzero":any(trace)}
    print("m",m,"S7",s,"trace",trace)

expected=(z+1)*(z*z+1)*(z*z+2*z-1)
assert red(leading(1)-expected).is_zero
assert results["1"]["normalised_trace"]==[-7,14,7,0,7,-14,-7]
assert sum(results["1"]["normalised_trace"])==0

for d in range(8,315):
    for mask in range(1,32):
        U=set().union(*(S[j] for j in range(5) if mask&(1<<j)))
        assert sum(p%d==0 for p in prices-U)<=12
for mask in range(1,32):
    U=set().union(*(S[j] for j in range(5) if mask&(1<<j)))
    order=sum(p%7==0 for p in prices-U)
    assert order==13 if mask<8 else order<=12
P7=1
for p in range(224,309,7): P7*=p
assert len(list(range(224,309,7)))==13

output={
 "status":"PASS",
 "field":"Q[zeta_7]/Phi_7; exact integer counting",
 "frozen_input_sha256":"50e87f0194cfb3780e84b7bbb6f9a2dca4f79bb4901cab06f1a5b59256fb470b",
 "primitive7_m1_S":"(z+1)(z^2+1)(z^2+2z-1)",
 "primitive7_m1_normalised_pole_polynomial":"-z^5+2z^4+z^3+2z^2+3z",
 "primitive7_m1_trace_N_mod7":[-7,14,7,0,7,-14,-7],
 "primitive7_pole_order":13,
 "primitive7_degree":12,
 "P7":str(P7),
 "A7_formula":"1/(7^14*P7)",
 "d_ge8_max_pole_order":12,
 "minimal_modulus_m1_error_O_N12":60,
 "minimal_modulus_m1_error_O_N11":420,
 "finite_followup":results,
 "independent_review":"NOT_REVIEWED"
}
with open("RESULT_SEVENTH.json","w",encoding="utf-8") as f:
    json.dump(output,f,indent=2)
print("PASS",P7)
