# S23/AV finite-future sign observer: exact N(h) for h=81,...,90

Date: 2026-11-07. Status: AUTHOR_SIDE_EXACT_FINITE_PROOF; independent review and native task admission pending.
Frozen scientific input: `awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34`. This is an independent continuation of Draft PR #1777 at `0f6db8aedb43506b258d90e2efb17e7be93c10a1`.

## Fixed experiment

Use the lawful two-point S23/AV experiment `theta0=(1/2,1/2)` and `theta1=(5/7,7/8)`. On output labels `(1,3,4)`, the single-step laws are `P0=(1/2,1/4,1/4)` and `P1=(5/7,1/4,1/28)`. Their compressed Bernoulli observation is identically `z=1/4`.

For a prefix containing `k` labels 1 and `ell` labels 4, its likelihood ratio is

`Lambda(k,ell) = 7^ell (7/10)^k = 7^(k+ell)/10^k`.

A suffix with counts `(i,j)` multiplies the likelihood by `7^j (7/10)^i`. For suffix length at most `h`, its reciprocal threshold is `T(i,j)=10^i/7^(i+j)` with `i,j >= 0` and `i+j <= h`. All `M_h=binom(h+2,2)` thresholds are distinct, by unique factorization of 7 and 10. Equality with any suffix threshold occurs only for the all-label-3 prefix and suffix, at 1. Every other minimal deterministic future-sign state is one occupied open interval between consecutive thresholds. Let `N(h)` be the least prefix length whose padded prefix count states meet every one of the `M_h+1` open intervals. Padding with label 3 preserves the likelihood.

## Exact new result

**Theorem.** For the experiment above:

```
N(81)=443;
N(82)=448; N(83)=453; N(84)=459; N(85)=464;
N(86)=470; N(87)=475; N(88)=481; N(89)=486; N(90)=492.
```

Thus the interior-gap plateau already present at h=80 persists at h=81, followed by a return to the extreme-left-threshold minimum at each integer h=82,...,90.

### Lower bounds

For h=81, an exhaustive exact computation finds the open gap bounded by the suffix threshold pairs `(i,j)=(0,67)` and `(11,69)` still empty at prefix length 442; its index is 96 in zero-based interval ordering. Hence `N(81)>=443`.

For every h>=1, the smallest threshold is `7^(-h)` and every feasible prefix with `k+ell<=n` obeys `Lambda(k,ell)>= (7/10)^n`. Consequently the leftmost interval `(0,7^(-h))` cannot be occupied unless `7^(n+h)<10^n`. Let `n_tail(h)` be the least positive integer satisfying that exact inequality. This gives `N(h)>=n_tail(h)`. For each h=82,...,90, the integer test yields the n shown in the theorem. This inequality is strict; equality for h,n>0 is impossible by unique prime factorization.

### Matching upper bounds

`VERIFY.py` constructs all thresholds with `Fraction(10**i,7**(i+j))`, sorts them, and checks their pairwise distinctness. For each proposed n, it enumerates **every** nontrivial count pair `(k,ell)` with `k+ell<=n`, computes the exact likelihood `Fraction(7**(k+ell),10**k)`, and locates its interval by exact binary search. These count pairs exhaust the finite prefix output space after label-3 padding. The script certifies that every threshold interval is occupied for n=443 at h=81 and for n=`n_tail(h)` at each h=82,...,90. Coupling these exhaustive upper bounds with the lower bounds proves the theorem.

All comparisons use exact arbitrary-precision integers and `fractions.Fraction`. The code has no floating-point tolerances. The stdout in `RUN_EVIDENCE.txt` was produced by executing the accompanying `VERIFY.py` locally with Python 3. The finite checks establish precisely the ten displayed values. No extrapolation to h>90 is claimed.

## BRC interpretation

The branch carrier is the ordered three-label output, reduced only to the **joint** `(k,ell)` counts because future likelihood multiplication is a function of those counts. The target observer is the sign of the two-hypothesis likelihood difference under every suffix of length `<=h`; the quotient into threshold-sign cells is exact only for that declared future horizon. A sign-only or marginal-count observer loses future-discriminating joint information. This is a `REUSE_APPLIED` instance of the existing likelihood/future-operation observer interface, not a new native X6 dynamics theorem.

## Open work

Determine whether interior gaps reappear at h>=91 and relate exceptional horizons to continued fractions for `log(7)/log(10/7)`. Seek a certified non-enumerative bound or formula for `N(h)`; preserve separate open work on full-lawful four-observation minimax `delta4` and the six-source ten-label mother-model observation bridge.
