"""Exact Laurent-coefficient verification for PREFIX-1023 (Python 3, stdlib)."""
from collections import defaultdict
import json
from pathlib import Path

D = 6
ZERO = (0,) * D

def mono(i, power=1):
    t = [0] * D
    t[i] = power
    return {tuple(t): 1}

def add(*terms):
    o = defaultdict(int)
    for p in terms:
        for e, a in p.items():
            o[e] += a
    return {e: a for e, a in o.items() if a}

def scale(p, c):
    return {e: a * c for e, a in p.items() if a*c}

def mult(a, b):
    o = defaultdict(int)
    for e, x in a.items():
        for f, y in b.items():
            o[tuple(u+v for u,v in zip(e,f))] += x*y
    return {e:x for e,x in o.items() if x}

def power_s(k):
    p = {ZERO: 1}
    for _ in range(k):
        p = mult(p, S)
    return p

ONE={ZERO:1}
S=add(*(mono(i) for i in range(D)))
U=add(*(mono(i,-1) for i in range(D)))
L=mult(S,U)
L36=add(L,scale(ONE,-36))
S1=add(S,scale(mono(0),-1))

def positive(n,j):
    m=n-4
    zj=mono(j)
    E=add(scale(ONE,72),scale(mult(S,add(mono(0,-1),mono(j,-1))),-6))
    # Note: for j=0, duplicate Laurent terms carry coefficient 2.
    A=add(scale(L36,m+3),E)
    B=mult(zj,add(mult(S1,A),mult(mono(0),L36),scale(mono(0),25)))
    F=mult(power_s(m),B)
    return sum(c*c for c in F.values())

known={
 5:(135110,109490), 6:(2918820,2532792),
 7:(66735540,59610948), 8:(1607486710,1458235054),
 10:(1064532083910,982562886810),
}
values={}
for n in range(5,12):
    vals=[positive(n,j) for j in range(6)]
    assert vals[1:]==[vals[1]]*5, (n,vals)
    values[n]=(vals[0], vals[1])
    if n in known: assert values[n]==known[n], (n,values[n],known[n])

def det2(a,b,c): return a*c-b*b
def det3(a,b,c,d,e):
    return a*(c*e-d*d)-b*(b*e-c*d)+c*(b*d-c*c)

def bareiss(a):
    a=[list(row) for row in a]
    n=len(a); den=1; sign=1
    for k in range(n-1):
        if a[k][k]==0:
            for j in range(k+1,n):
                if a[j][k]:
                    a[k],a[j]=a[j],a[k];sign=-sign;break
            else:return 0
        pivot=a[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                num=a[i][j]*pivot-a[i][k]*a[k][j]
                assert num%den==0
                a[i][j]=num//den
            a[i][k]=0
        den=pivot
    return sign*a[n-1][n-1]

hankel={}
for port in (0,1):
    seq=[values[n][port] for n in range(5,12)]
    hankel[str(port)]={"order2":str(det2(*seq[:3])),"order3":str(det3(*seq[:5])),"order4":str(bareiss([[seq[a+b] for b in range(4)] for a in range(4)]))}

result={
 "scope":"n=5..11 exact integer Laurent check, j=1..6; positive-port terminal k=1 numerator",
 "model":"frozen X6 candidate Stage46 signed W=J12-6I12, Link {0,e1}",
 "values":{str(n):{"axis1":str(a),"other_each":str(b)} for n,(a,b) in values.items()},
 "hankel_finite_only":hankel,
 "all_port_symmetry_checked":True,
 "known_prefix1014_checked":[5,6,7,8,10],
 "counterexample":"other-axis positive-port n0=5 h=3 Hankel determinant is negative; so the PREFIX1022 strict-positive-Hankel claim cannot be transferred",
 "analytic_constants":{"lim_m_to_inf_m^(5/2)_Qplus_over_36^m":"7063875/(4*pi^(5/2))","contrast_leading_coefficient_dependent_on_prefix1017":"1530900/pi^(5/2)"},
 "proof_status":"author analytic Laplace argument; no external mathematical review"
}
with Path(__file__).with_name('PREFIX1023_R6_POSITIVE_HANKEL_EXACT_RESULTS.json').open('w') as f:
    json.dump(result,f,ensure_ascii=False,indent=2)
print(json.dumps(result,indent=2))
