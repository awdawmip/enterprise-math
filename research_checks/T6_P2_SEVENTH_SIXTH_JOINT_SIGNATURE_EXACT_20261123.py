#!/usr/bin/env python3
"""Exact six-moment 2-adic joint v2(d)=7/6 certificate for T6.

Both original sides have exponent-mass <=2331. Equal multiplicities at
v2(d)>=8 come from the separately proven cancellation lemma. No floating point.
"""
from collections import defaultdict

CAP = 2331
J7 = tuple(range(1, (CAP + 1) // 128 + 1, 2))
J6 = tuple(range(1, (CAP + 1) // 64 + 1, 2))
WEIGHTS = tuple(128*j - 1 for j in J7) + tuple(64*u - 1 for u in J6)
N7 = len(J7)
MODULI = tuple(1 << (2*k) for k in range(1, 7))
COEFFICIENTS = tuple(
    tuple(pow(j, -k, 1 << (2*k)) for k in range(1, 7)) for j in J7
) + tuple(
    tuple((1 << k)*pow(u, -k, 1 << (2*k)) for k in range(1, 7))
    for u in J6
)


def enumerate_profiles():
    current = [0]*len(WEIGHTS)
    sig = [0]*6

    def visit(i, remaining):
        if i == len(WEIGHTS):
            yield tuple(current), tuple(sig)
            return
        old = tuple(sig)
        for n in range(remaining//WEIGHTS[i]+1):
            current[i] = n
            for k in range(6):
                sig[k] = (old[k]+n*COEFFICIENTS[i][k])%MODULI[k]
            yield from visit(i+1, remaining-n*WEIGHTS[i])
        current[i] = 0
        sig[:] = old

    yield from visit(0, CAP)


def dp_count():
    dp = [0]*(CAP+1)
    dp[0] = 1
    for w in WEIGHTS:
        for mass in range(w, CAP+1):
            dp[mass] += dp[mass-w]
    return sum(dp)


def independent_ambiguous_pair_test():
    """Second path: all 253 exact-v7 profiles and residual v6 pair feasibility."""
    def tuples_for(weights, budget):
        vec = [0]*len(weights)
        def walk(i, remainder):
            if i == len(weights):
                yield tuple(vec)
                return
            for c in range(remainder//weights[i]+1):
                vec[i] = c
                yield from walk(i+1, remainder-c*weights[i])
            vec[i] = 0
        yield from walk(0, budget)

    w7 = tuple(128*j-1 for j in J7)
    groups = defaultdict(list)
    for a in tuples_for(w7, CAP):
        sig = tuple(
            sum(n*pow(j,-k,1<<k) for n,j in zip(a,J7))%(1<<k)
            for k in range(1,7)
        )
        groups[sig].append(a)
    assert sum(map(len, groups.values())) == 253
    pairs = [(a,b) for g in groups.values() for i,a in enumerate(g)
             for b in g[i+1:]]
    assert len(pairs) == 26

    for a,b in pairs:
        ra = CAP-sum(x*w for x,w in zip(a,w7))
        rb = CAP-sum(x*w for x,w in zip(b,w7))
        assert ra == rb
        allowed = [(u,64*u-1) for u in J6 if 64*u-1 <= ra]
        uu = [u for u,w in allowed]
        low_sigs = {
            tuple(sum(c*pow(u,-k,1<<k) for c,u in zip(p,uu))%(1<<k)
                  for k in range(1,7))
            for p in tuples_for([w for u,w in allowed], ra)
        }
        high = tuple(
            (sum((x-y)*pow(j,-k,1<<(2*k)) for x,y,j in zip(a,b,J7))
             %(1<<(2*k)))//(1<<k)
            for k in range(1,7)
        )
        for s in low_sigs:
            t = tuple((s[k-1]+high[k-1])%(1<<k) for k in range(1,7))
            assert t not in low_sigs, (a,b,s,t)
    return len(pairs)


def main():
    assert J7 == (1,3,5,7,9,11,13,15,17)
    assert J6 == tuple(range(1,36,2))
    owners = {}
    repeated = 0
    total = 0
    for vec,sig in enumerate_profiles():
        total += 1
        high = vec[:N7]
        if sig in owners:
            repeated += 1
            assert owners[sig] == high, ('differing v7', owners[sig], high)
        else:
            owners[sig] = high
    assert total == dp_count() == 37836
    assert len(owners) == 23956
    assert repeated == 13880
    assert independent_ambiguous_pair_test() == 26
    print('PASS: 37836 joint v6/v7 profiles; 23956 signatures;')
    print('      13880 repeated signatures; zero differing-v7 pairs')
    print('PASS: independent 253 v7 / 26 candidate-pair exhaustive check')


if __name__ == '__main__':
    main()
