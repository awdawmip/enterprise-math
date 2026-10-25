#!/usr/bin/env python3
"""Source-alignment regression, D25 LIFT: exact modular arithmetic, not native H0/B0/Frobenius benchmark."""
from sympy import primerange, isprime


def one(p):
    assert isprime(p) and p >= 7 and p % 6 == 1
    m = (p-1)//6
    mod = p**3
    inv = lambda a, q: pow(a % q, -1, q)
    B = Wn = 1
    M = N = W = 0
    lows = []
    tops = []
    for n in range(p):
        if n <= m:
            lows.append(B % p)
        if p <= 211:
            tops.append(B)
        M = (M + B) % mod
        N = (N + n*B) % mod
        W = (W + (6*n+1)*Wn) % mod
        if n+1 < p:
            B = B*(6*n+1)*(3*n+1)*inv(36*(n+1)**2,mod) % mod
            Wn = Wn*(2*n+1)*(3*n+1)*(3*n+2)*inv(36*(n+1)**3,mod) % mod
    h = (M+12*N) % mod
    Q = (M*h-W) % mod
    assert Q % (p*p) == 0, ("tail valuation",p)

    # Source C_r, independently check the reflected top B_(p-r)/p^2 when small.
    C = []
    cur = 1
    for r in range(1,m+1):
        if r == 1:
            cur = inv(10,p)
        else:
            j = r-1
            cur = cur*36*j*j*inv((6*j+5)*(3*j+2),p) % p
        C.append(cur)
        if p <= 211:
            assert tops[p-r] % (p*p) == 0
            assert tops[p-r]//(p*p) % p == cur, ("Source top reflection",p,r)

    # Original Source nested sum, independently recomputed for small p.
    R_direct = None
    if p <= 211:
        R_direct = (2*sum(
            lows[i]*sum((1+6*(i-r))*C[r-1] for r in range(1,i+1))
            for i in range(1,m+1))) % p

    # O(m) source-aligned reflected recurrence and two distinct moment ports.
    V = J = R_fast = 0
    for i in range(1,m+1):
        V = (V+C[i-1]) % p
        J = (J+i*C[i-1]) % p
        R_fast = (R_fast+2*lows[i]*((6*i+1)*V-6*J)) % p
    if R_direct is not None:
        assert R_fast == R_direct, ("frozen nested vs prefix",p)
    assert Q//(p*p) == R_fast, ("frozen R vs Clausen cutoff",p)

    result = dict(p=p,m=m,R_frozen=R_fast,Q_div_p2=Q//(p*p),
        W_mod_p3=W,M_mod_p=M%p,CM0=(M%p==0),
        source_double_checked=(R_direct is not None))
    if p % 24 in (13,19):
        assert M % p == 0, ("accepted CM0 regression",p)
        assert W % (p*p) == p, ("accepted UR regression",p)
        G = M//p
        z = (G*h-1) % (p*p)
        assert z % p == 0, ("unit reciprocity",p)
        delta = z//p
        defect = (delta-R_fast) % p
        assert defect == (W-p)//(p*p) % p, ("D25 frozen observer",p)
        result.update(G_divided_mod_p2=G%(p*p),
            H_weighted_mod_p2=h%(p*p),
            G_times_H_mod_p2=(G*h)%(p*p),
            Delta=delta,Delta_minus_R=defect,
            original_W_defect=((W-p)//(p*p))%p)
    return result


if __name__ == "__main__":
    primes = [int(p) for p in primerange(7,1501) if p%6==1]+[19963]
    out = [one(p) for p in primes]
    target = [r for r in out if r["p"]%24 in (13,19)]
    print("SOURCE_BRIDGE_VERIFIED",len(out),"PRIMES",len(target),
          "D25_TARGETS DIRECT_NESTED",sum(x["source_double_checked"] for x in out))
    print("TARGET_DEFECTS_NONZERO",sum(bool(x["Delta_minus_R"]) for x in target))
    for p in [7,13,19,37,211,373,19963]:
        print("EXAMPLE",one(p))
