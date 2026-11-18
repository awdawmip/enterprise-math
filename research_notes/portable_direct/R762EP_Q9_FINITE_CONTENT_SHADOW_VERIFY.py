#!/usr/bin/env python3
"""R762EP: exact finite q=9 BRC content/shadow certificate.

Six named positive branches are retained as explicit coordinate shifts.
All operations are in Z/3^340 Z[(Z/9)^3]; projection to q=3 is checked
at every time. No floating point, pi, or native signed-event inference.
"""
import hashlib
import json

Q = 9
CAP = 340
MAX_N = 1007
SHIFT = ((0,0,0),(1,0,0),(0,0,1),
         (1,1,0),(0,1,1),(1,1,1))
MOD = 3 ** CAP
P3 = [3**k for k in range(CAP+1)]

def address(i,j,k,q):
    return (i*q+j)*q+k

def shift_maps(q):
    return [
        [address((i-di)%q,(j-dj)%q,(k-dk)%q,q)
         for i in range(q) for j in range(q) for k in range(q)]
        for di,dj,dk in SHIFT
    ]

def step(a, maps):
    b = [0]*len(a)
    for perm in maps:
        for i, j in enumerate(perm):
            b[i] += a[j]
    return [z % MOD for z in b]

def rank3_and_relation(vectors):
    pivots = {}
    for ci, vector in enumerate(vectors):
        v = list(vector)
        coeff = [0]*len(vectors)
        coeff[ci] = 1
        for pivot in sorted(pivots):
            if v[pivot]:
                old, witness = pivots[pivot]
                m = v[pivot]
                v = [(x-m*y)%3 for x,y in zip(v,old)]
                coeff = [(x-m*y)%3 for x,y in zip(coeff,witness)]
        first = next((i for i,x in enumerate(v) if x),None)
        if first is None:
            return len(pivots), coeff, sorted(pivots)
        if v[first] == 2:
            v = [2*x%3 for x in v]
            coeff = [2*x%3 for x in coeff]
        pivots[first] = (v, coeff)
    return len(pivots), None, sorted(pivots)

def main():
    p9, p3 = shift_maps(9), shift_maps(3)
    to3 = [address(i%3,j%3,k%3,3)
           for i in range(9) for j in range(9) for k in range(9)]
    a9 = [0]*729
    a3 = [0]*27
    a9[0] = a3[0] = 1
    six_power = 1
    base = []
    period_checks = 0
    largest_k = 0
    for n in range(MAX_N+1):
        # Independent consistency checks, over the same exact quotient ring.
        assert sum(a9)%MOD == six_power, ("mass",n)
        projected = [0]*27
        for idx,v in enumerate(a9):
            j = to3[idx]
            projected[j] = (projected[j]+v)%MOD
        assert projected == a3, ("q9 to q3 reduction",n)
        k = max(0,n//3-2)
        largest_k = max(largest_k,k)
        assert k < CAP
        d = P3[k]
        assert all(x%d == 0 for x in a9), ("content lower",n)
        shadow = bytes((x//d)%3 for x in a9)
        assert any(shadow), ("content upper witness",n)
        if n >= 9:
            if n < 27:
                base.append(shadow)
            else:
                assert shadow == base[(n-9)%18], ("period-18 shadow",n)
                period_checks += 1
        if n < MAX_N:
            a9 = step(a9,p9)
            a3 = step(a3,p3)
            six_power = 6*six_power%MOD
    assert len(base)==18 and period_checks==MAX_N-26
    rank,relation,pivots = rank3_and_relation(base)
    assert rank == 17
    assert relation == [0,0,2,0,0,1,0,0,0,0,0,1,0,0,0,0,0,1]
    rows=[]
    for offset,shadow in enumerate(base):
        first=next(i for i,x in enumerate(shadow) if x)
        u,r=divmod(first,81)
        v,w=divmod(r,9)
        rows.append({
            "n":9+offset,
            "support":sum(bool(x) for x in shadow),
            "ones":shadow.count(1), "twos":shadow.count(2),
            "witness_uv_w":[u,v,w],
            "witness_mod3":shadow[first],
            "sha256":hashlib.sha256(shadow).hexdigest()
        })
    print(json.dumps({
        "schema":"R762EP_Q9_BRC_FINITE_EVIDENCE_V1",
        "source_model":"P=1+X+Z+XY+YZ+XYZ in Z[(Z/9)^3]",
        "max_n_inclusive":MAX_N,
        "horizons_checked":MAX_N+1,
        "coefficient_positions_per_horizon":729,
        "modulus":"3^340",
        "largest_exact_content_valuation":largest_k,
        "exact_content_formula":"v3(content(P^n))=max(0,floor(n/3)-2)",
        "period_from":9, "period":18,
        "period_equality_checks":period_checks,
        "shadow_rank_mod3":rank,
        "shadow_linear_relation":relation,
        "period_block_sha256":hashlib.sha256(b''.join(base)).hexdigest(),
        "mass_checks":MAX_N+1, "q3_projection_checks":MAX_N+1,
        "rows":rows,
        "verification":"PASS; exhaustive finite domain only",
        "review":"NOT_REVIEWED",
        "native_signed_event":"NOT_TESTED"
    },indent=2,ensure_ascii=False))

if __name__=="__main__":
    main()
