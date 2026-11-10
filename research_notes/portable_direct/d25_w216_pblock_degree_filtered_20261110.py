"""D25: all-prime p-block degree filtration and exact p² computation.
Author-side, not native H0/B0, and the Dwork recurrence remains experimental.
"""
from math import comb

def unit_remove(n, p):
    v = 0
    while n % p == 0:
        n //= p
        v += 1
    return v, n

def coefficient_stream(p, n, prec):
    """Original A_k mod p**prec, with full valuation, no float arithmetic."""
    mod = p ** prec
    unit, val = 1, 0
    for k in range(n):
        a = unit * pow(p, val, mod) % mod if val < prec else 0
        yield k, a, val
        if k + 1 == n:
            break
        num, numval = 1, 0
        for f in (2*k+1, 2*k+2, 3*k+1, 3*k+2, 3*k+3):
            t, u = unit_remove(f, p)
            numval += t
            num = num * u % mod
        t, u = unit_remove(k+1, p)
        val += numval - 5*t
        assert val >= 0
        den = 216 * pow(u, 5, mod) % mod
        unit = unit * num * pow(den, -1, mod) % mod

def fast_w_p2(p, m=7):
    assert p >= 5 and 1 <= m <= p-1
    prec, mod = m+3, p**m
    big = p**prec
    blocks = [0] * m
    a_first, v_first = [], []
    for k, a, v in coefficient_stream(p, m*p, prec):
        blocks[k//p] = (blocks[k//p] + (6*k+1)*a) % big
        if k < p:
            a_first.append(a % mod)
            v_first.append(v)
    C = []
    for j in range(m):
        aj = next(a for k, a, v in coefficient_stream(p, j+1, prec) if k == j)
        v = v_first[j]
        assert v <= 3 and blocks[j] % p**v == 0 and aj % p**v == 0
        C.append((blocks[j] // p**v) * pow(aj // p**v, -1, mod) % mod)
    differences = C[:]
    q = []
    while differences:
        q.append(differences[0])
        differences = [(differences[j+1]-differences[j]) % mod
                       for j in range(len(differences)-1)]
    assert all(q[j] % p**j == 0 for j in range(m))
    moments = [0] * m
    for a, aa in enumerate(a_first):
        choose = 1
        for j in range(min(m, a+1)):
            moments[j] = (moments[j]+aa*choose) % mod
            choose = choose*(a-j)//(j+1)
    w2 = sum(q[j]*moments[j] for j in range(m)) % mod
    w1 = sum((6*k+1)*a for k,a in enumerate(a_first)) % mod
    chi = 1 if p%3 == 1 else -1
    defect = (w2-chi*p*w1)%mod
    return {"p": p, "m": m, "W_p2": w2, "W_p": w1,
            "defect": defect, "Newton": q, "moments": moments, "anchors": C,
            "base_congruence_observed": (w1-chi*p)%p**3 == 0,
            "base_c": ((w1-chi*p)//p**3)%p if (w1-chi*p)%p**3 == 0 else None,
            "observed_defect_div_p6":
                defect//p**6 if m==7 and defect%p**6 == 0 else None}

def brute_w(p, m=7):
    return sum((6*k+1)*a for k,a,v
               in coefficient_stream(p, p*p, m)) % p**m

if __name__ == "__main__":
    for p in (13,19,37,43,73,109,373,379):
        z = fast_w_p2(p,7)
        assert z["W_p2"] == brute_w(p,7)
        assert z["base_congruence_observed"]
        assert z["base_c"] == z["observed_defect_div_p6"]
        print("P_BLOCK_PROVED_METHOD_CHECK",p,
              "W_p2",z["W_p2"],"q",z["Newton"],
              "FINITE_ONLY_DWORK_c",z["base_c"])

def prime_list(n):
    flags = [True]*(n+1)
    flags[0]=flags[1]=False
    for j in range(2,int(n**0.5)+1):
        if flags[j]:
            for k in range(j*j,n+1,j):
                flags[k]=False
    return [j for j in range(5,n+1) if flags[j]]

if __name__ == "__main__":
    for p in prime_list(3000):
        chi = 1 if p%3==1 else -1
        z = fast_w_p2(p,3)
        # Finite-only first-jet conjecture, not an all-prime theorem.
        assert z["Newton"] == [chi*p % p**3, 6*chi*p % p**3, 0]
    print("FINITE_ONLY_FIRST_JET",428,"PRIMES_THROUGH_2999")
    for p in (10069,10099):
        # These are mathematically certified by the p-block theorem;
        # the O(p**2) independent brute comparison is NOT performed.
        z = fast_w_p2(p,7)
        assert z["base_congruence_observed"]
        assert z["observed_defect_div_p6"] == z["base_c"]
        assert z["Newton"][0] == z["W_p"]
        print("THEOREM_BASED_LARGE_P",p,"W_p2",z["W_p2"],
              "FINITE_ONLY_DWORK_c",z["base_c"])
