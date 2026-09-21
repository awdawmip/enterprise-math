from fractions import Fraction
from math import comb

N = 23
R_PRIMARY = 16
R_BONF = 17

def bin_tail(n, r):
    return sum(Fraction(comb(n, k), 2**n) for k in range(r, n + 1))

def arbitrary_dependence_sup(n, r):
    # Xi are Bernoulli indicators with only P(Xi=1)<=1/2 known.
    # Markov on S=sum Xi gives P(S>=r)<=min(1,n/(2r)).
    return min(Fraction(1, 1), Fraction(n, 2 * r))

def witness(n, r):
    # Exchangeable sharp witness:
    # if r<=n/2, choose a uniformly random r-subset with probability 1.
    # if r>n/2, with p=n/(2r) choose a uniformly random r-subset,
    # otherwise choose the empty set.
    p = arbitrary_dependence_sup(n, r)
    marginal = p * Fraction(r, n)
    return p, marginal

# Frozen 91D4E7 independent-cycle calibration.
assert bin_tail(23, 16) == Fraction(763, 16384)
assert bin_tail(23, 17) == Fraction(145499, 8388608)

# Sharp marginal-only arbitrary-dependence envelope.
assert arbitrary_dependence_sup(23, 16) == Fraction(23, 32)
assert arbitrary_dependence_sup(23, 17) == Fraction(23, 34)
assert arbitrary_dependence_sup(23, 23) == Fraction(1, 2)

# The sharp witness has legal marginals <=1/2 and attains the bound.
for n in range(1, 65):
    for r in range(1, n + 1):
        p, marginal = witness(n, r)
        assert marginal <= Fraction(1, 2)
        assert p == arbitrary_dependence_sup(n, r)
        # For r>n/2 the construction saturates every marginal at 1/2.
        if 2 * r > n:
            assert marginal == Fraction(1, 2)
        else:
            assert p == 1

# No success-count threshold on 23 cycles can have alpha <= .05
# under marginal validity alone; the best is all 23 positive, worst-case size 1/2.
assert min(arbitrary_dependence_sup(23, r) for r in range(1, 24)) == Fraction(1, 2)
assert all(arbitrary_dependence_sup(23, r) > Fraction(1, 20) for r in range(1, 24))

# Under an intersection-union target, one component can be null while the
# other is deterministically true, so the same marginal-only supremum applies.
iut_worst = arbitrary_dependence_sup(23, 16)
assert iut_worst == Fraction(23, 32)

# Inflation over the independent-binomial primary reference.
assert iut_worst / bin_tail(23, 16) == Fraction(11776, 763)

print({
    "status": "PASS",
    "n_cycles": N,
    "primary_r": R_PRIMARY,
    "independent_primary_tail": str(bin_tail(N, R_PRIMARY)),
    "arbitrary_dependence_primary_sup": str(arbitrary_dependence_sup(N, R_PRIMARY)),
    "arbitrary_dependence_min_over_all_thresholds": str(min(arbitrary_dependence_sup(N, r) for r in range(1, N+1))),
    "inflation_ratio_vs_independent_primary": str(arbitrary_dependence_sup(N, R_PRIMARY) / bin_tail(N, R_PRIMARY)),
    "alpha_0_05_attainable_from_marginals_only": False,
})
