#!/usr/bin/env python3
from __future__ import annotations

from fractions import Fraction
from math import gcd
from itertools import combinations

CHECKS = 0

def check(cond, msg):
    global CHECKS
    CHECKS += 1
    if not cond:
        raise AssertionError(msg)

def prime_factors(n):
    out = {}
    p = 2
    while p * p <= n:
        while n % p == 0:
            out[p] = out.get(p, 0) + 1
            n //= p
        p += 1
    if n > 1:
        out[n] = out.get(n, 0) + 1
    return out

def reduced(a, b):
    d = gcd(a, b)
    return d, a // d, b // d

def rank_q(mat):
    if not mat:
        return 0
    A = [[Fraction(x) for x in row] for row in mat]
    m, n = len(A), len(A[0])
    r = 0
    for c in range(n):
        pivot = next((i for i in range(r, m) if A[i][c]), None)
        if pivot is None:
            continue
        A[r], A[pivot] = A[pivot], A[r]
        q = A[r][c]
        A[r] = [x / q for x in A[r]]
        for i in range(m):
            if i != r and A[i][c]:
                q = A[i][c]
                A[i] = [A[i][j] - q * A[r][j] for j in range(n)]
        r += 1
        if r == m:
            break
    return r

def carrier_stratum(a, b):
    if a == b:
        return "E_EQUALITY"
    d, A, B = reduced(a, b)
    fa, fb = prime_factors(a), prime_factors(b)
    if d == 1:
        if len(fa) == len(fb) == 1:
            ea = next(iter(fa.values()))
            eb = next(iter(fb.values()))
            if ea == eb == 1:
                return "C0_DISTINCT_PRIME_PAIR"
            return "C1_COPRIME_PRIME_POWER_THICK"
        return "C2_COPRIME_MULTISUPPORT"
    ps = sorted(set(fa) | set(fb))
    cols = [(fa.get(p, 0), fb.get(p, 0)) for p in ps]
    rank1 = all(x1 * y2 == y1 * x2 for (x1, y1), (x2, y2) in combinations(cols, 2))
    return "O1_OVERLAP_COMMON_BASE_RANK1" if rank1 else "O2_OVERLAP_RANK2"

def iff_eq1(a, b, r, s):
    d, A, B = reduced(a, b)
    lhs = b * r == a * s
    rhs = (r % A == 0 and s % B == 0 and r // A == s // B)
    return lhs, rhs

def iff_eq2(a, b, r, s):
    d, A, B = reduced(a, b)
    lhs = a * r == b * s
    rhs = (r % B == 0 and s % A == 0 and r // B == s // A)
    return lhs, rhs

def oriented_typed_resonance(a, b, r, s):
    # row 0 = a, row 1 = b; row/support labels are part of the port identity.
    out = set()
    if b * r == a * s and r != s:
        out.add(frozenset(((1, r), (0, s))))
    if a * r == b * s and r != s:
        out.add(frozenset(((0, r), (1, s))))
    return out

def safe_edges(a, b, R):
    out = set()
    for r, s in combinations(sorted(R), 2):
        out |= oriented_typed_resonance(a, b, r, s)
    return out

class DSU:
    def __init__(self, xs):
        self.p = {x:x for x in xs}
    def find(self, x):
        p = self.p[x]
        if p != x:
            self.p[x] = self.find(p)
        return self.p[x]
    def union(self, x, y):
        x, y = self.find(x), self.find(y)
        if x != y:
            self.p[y] = x

def chain_matrices(a, b, R):
    R = tuple(sorted(R))
    typed = [(row, r) for row in (0,1) for r in R]
    dsu = DSU(typed)
    res = safe_edges(a, b, R)
    for e in res:
        u, v = tuple(e)
        dsu.union(u, v)
    roots = sorted({dsu.find(v) for v in typed})
    rid = {x:i for i,x in enumerate(roots)}
    vid = {v:rid[dsu.find(v)] for v in typed}

    edges = []
    for r in R:
        edges.append(("v", r, None, (0,r), (1,r)))
    for row in (0,1):
        for r,s in combinations(R,2):
            edges.append(("h", row, (r,s), (row,r), (row,s)))
    eid = {(e[0],e[1],e[2]):i for i,e in enumerate(edges)}
    B1 = [[0]*len(edges) for _ in roots]
    for j,e in enumerate(edges):
        u,v=e[3],e[4]
        B1[vid[u]][j] -= 1
        B1[vid[v]][j] += 1
    faces=list(combinations(R,2))
    B2=[[0]*len(faces) for _ in edges]
    for j,(r,s) in enumerate(faces):
        B2[eid[("h",0,(r,s))]][j] += 1
        B2[eid[("v",s,None)]][j] += 1
        B2[eid[("h",1,(r,s))]][j] -= 1
        B2[eid[("v",r,None)]][j] -= 1
    return roots, edges, faces, B1, B2, res

def transpose(M):
    return [list(x) for x in zip(*M)] if M else []

def is_coboundary(B1, alpha):
    A = transpose(B1)
    if not A:
        return not any(alpha)
    aug=[row+[alpha[i]] for i,row in enumerate(A)]
    return rank_q(A)==rank_q(aug)

# 1) Exact iff classification and simultaneous-conflict theorem.
for a in range(2,31):
    for b in range(2,31):
        d,A,B=reduced(a,b)
        for r in range(1,41):
            for s in range(1,41):
                l1,r1=iff_eq1(a,b,r,s)
                l2,r2=iff_eq2(a,b,r,s)
                check(l1==r1, f"eq1 iff failed {(a,b,r,s,A,B)}")
                check(l2==r2, f"eq2 iff failed {(a,b,r,s,A,B)}")
                both=l1 and l2
                check(both == (A==B==1 and r==s),
                      f"simultaneous theorem failed {(a,b,r,s,A,B)}")
                check((a*r==b*r) == (a==b), "same-column row collision failed")

# 2) The two oriented equations give one unordered resonance family for A != B.
for a in range(2,31):
    for b in range(2,31):
        d,A,B=reduced(a,b)
        if A==B:
            continue
        for t in range(1,16):
            p=frozenset((A*t,B*t))
            r,s=sorted(p)
            es=oriented_typed_resonance(a,b,r,s)
            check(len(es)==1, f"expected one normalized typed edge {(a,b,t,r,s,es)}")

# 3) Multiple decorated strata; safe resonance graph is a typed-port matching.
examples = [(2,3),(4,9),(6,35),(4,8),(2,6),(6,6)]
expected = [
    "C0_DISTINCT_PRIME_PAIR",
    "C1_COPRIME_PRIME_POWER_THICK",
    "C2_COPRIME_MULTISUPPORT",
    "O1_OVERLAP_COMMON_BASE_RANK1",
    "O2_OVERLAP_RANK2",
    "E_EQUALITY",
]
check([carrier_stratum(*x) for x in examples]==expected, "strata representatives failed")

for a,b in examples[:-1]:
    d,A,B=reduced(a,b)
    R=set()
    for t in range(1,9):
        R.add(A*t); R.add(B*t)
    es=safe_edges(a,b,R)
    deg={}
    for e in es:
        for v in e:
            deg[v]=deg.get(v,0)+1
    check(max(deg.values(), default=0)<=1, f"typed matching failed {(a,b)}")
    ts={r//A for r in R if r%A==0 and (B*(r//A)) in R}
    check(len(es)==len(ts), f"resonance count mismatch {(a,b,len(es),len(ts))}")

check(len(safe_edges(6,6,{1,2,3,4,5}))==0, "equality generated false cross-column pinch")

# 4) Mixed scalar chains are real only after unsafe row erasure.
a,b=2,3
R={4,6,9}
es=safe_edges(a,b,R)
check(len(es)==2, "2:3 mixed-chain safe edge count")
deg={}
for e in es:
    for v in e: deg[v]=deg.get(v,0)+1
check(max(deg.values())==1, "safe typed chain incorrectly shares a port")
value_edges={frozenset(v[1] for v in e) for e in es}
value_deg={}
for e in value_edges:
    for v in e: value_deg[v]=value_deg.get(v,0)+1
check(value_deg[6]==2, "unsafe value-only quotient did not expose false shared scalar port")

# 5) Homology/cocycle exact regression on clean and resonant finite families.
families=[
    (2,3,{1,2,3,4,6,9}),
    (4,9,{1,4,6,9,12,18,27}),
    (4,8,{1,2,3,4,6,8,12}),
    (2,6,{1,2,3,6,9,18}),
]
for a,b,R in families:
    roots,edges,faces,B1,B2,res=chain_matrices(a,b,R)
    V,E,F=len(roots),len(edges),len(faces)
    r1,r2=rank_q(B1),rank_q(B2)
    beta0=V-r1
    beta1=E-r1-r2
    beta2=F-r2
    k=len(R); m=len(res)
    check(beta0==1, f"beta0 failed {(a,b,R)}")
    check(beta1==(k-1)*(k-2)//2+m, f"beta1 failed {(a,b,beta1,m)}")
    check(beta2==0, f"beta2 failed {(a,b,beta2)}")
    check(V==2*k-m, f"vertex count failed {(a,b,V,k,m)}")
    alpha=[1 if e[0]=="v" else 0 for e in edges]
    for j in range(F):
        check(sum(alpha[i]*B2[i][j] for i in range(E))==0, "height not closed")
    check(is_coboundary(B1,alpha)==(m==0), f"height exactness failed {(a,b,m)}")
    for e in res:
        u,v=tuple(e)
        check(u[0]!=v[0], "resonance did not cross rows")
        check(abs(u[0]-v[0])==1, "row jump wrong")
        check(1 % 2 == 1, "mod2 period wrong")

roots,edges,faces,B1,B2,res=chain_matrices(2,3,{1,5,7,11})
alpha=[1 if e[0]=="v" else 0 for e in edges]
check(len(res)==0 and is_coboundary(B1,alpha), "clean height should be exact")

# 6) Exhaustive safe-matching falsification across a broad finite range.
for a in range(2,25):
    for b in range(2,25):
        if a==b:
            continue
        R=set(range(1,61))
        es=safe_edges(a,b,R)
        deg={}
        for e in es:
            for v in e:
                deg[v]=deg.get(v,0)+1
        check(max(deg.values(), default=0)<=1, f"counterexample to typed matching {(a,b)}")

print(f"PASS checks={CHECKS}")
