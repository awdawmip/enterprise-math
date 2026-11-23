# T6 maximal-p17 q11, split (5,6): full-observer five-adic exact exclusion

Date: 2026-11-24 (Asia/Shanghai). Researcher/author in this logical continuation: `RESEARCH_DRIVER EM-DVR-DEBB5E`, managed SID `MCP-9b4714dc46b948afa4875a86c89c713c`. This is a new **scoped finite mathematical certificate**, not an independent nonauthor review, Native Result admission, Task DONE or global T6 proof.

## Theorem (only the q11 (5,6) split)

In the original T6 integer denomination-multiset model, suppose each side has exponent mass `sum(d-1) <= 2331`, the maximal denominator prime is 17, and the complete observers `H_0,...,H_6` agree. Remove common denominators. Invoke the previously established universal `v_17 >= 2` cancellation result in its original scope. Then a nonempty cancellation-normalized once-17 vertical configuration of total order 11 cannot have split `(q_+,q_-)=(5,6)` or `(6,5)`, **even when arbitrary 17-free lower-prime denominations are allowed on both sides**.

For total vertical order 11, the other feasible split `(4,7)` (or reverse) remains open. The theorem does not eliminate the full order-11 branch.

## Proof reduction

Write the once-17 denominator part as `d=17a`, `17 does not divide a`; separate the other denominators into `L`. The triangular binomial transform of the full observers gives, for `1<=k<=5`,

```
 R_k(U_+) - R_k(U_-) = -17^k [S_k(L_+) - S_k(L_-)],
 R_k(U) = sum_{17a in U} a^{-k}.
```

The `L` terms are 17-adic integers, hence equality of full observers implies equality of the five residues

```
 sigma_5(U) = ( R_1 mod 17, R_2 mod 17^2,
                R_3 mod 17^3, R_4 mod 17^4,
                R_5 mod 17^5 ).
```

The once-17 vertical denominations are `17(17q+r)`, with `q >= 1`, `1 <= r <= 16`, `17q+r` 17-smooth. Their mass is `289q+17r-1`. The remaining q0 denominations are `17j`, `1 <= j <= 16`, with arbitrary nonnegative multiplicities and cost `17j-1`. A vertical side of order 5 has vertical mass at least 1477: at least two vertical atoms give `289*5+16*2=1477`, and a single q5 atom has unsmooth cofactors 86/87 for r=1/2, thus costs at least 1495. A q6 side has no lower mass. Therefore both q5 and q6 side states have q0 cost at most `2331-1477=854`.

The linked exact C++17 checker enumerates all 60 smooth vertical atom types, every nondecreasing vertical atom multiset of total q5 or q6 with mass no greater than 2331, and all 16-component nonnegative q0 multiplicity vectors of cost at most 854; it enforces the original combined per-side budget. Modular inverses are computed with exact integer arithmetic modulo each `17^k`. The five-component key uses mixed-radix bases with maximum value below `17^15 < 2^64`, so it is injective on the residue tuples; the open-address table uses exact key equality, not probabilistic acceptance.

## Exact certificate (performed in this Driver logical context)

```text
atoms=60 v5=8573 v6=11105 q0=1144444
n5=172059801 n6=6992576 distinct6=6992576
duplicates6=0 cross5=0
```

After inserting all 6,992,576 q6 side signatures, **none** of the 172,059,801 q5 side states has the same five-adic signature. Thus the full-observer necessary congruences cannot hold for any q11 split(5,6) collision. Compilation/execution: `g++ -O3 -march=native -std=c++17`, exit 0; measured 14.27 seconds and peak 160,044 KiB in the successful local run. Source byte SHA256: `4985c21c318d5292d7f057777c50ec5cf0a2a16e23be2ce92a2520045d2e6bad`; Git blob SHA1: `25d69bcf4d4bb5eee28a27f1c403e7142f717f81`.

[Exact C++ source at immutable commit](https://github.com/awdawmip/enterprise-math/blob/a2e623b5afb01a241df2825fa9e59d802876961b/research_checks/T6_P17_Q11_SPLIT56_FIVE_ADIC_EXACT_20261124.cpp).

## Prior results, authorship and remaining work

This calculation extends the current Driver author's [q12/q13 five-adic enumeration](https://github.com/awdawmip/enterprise-math/blob/3b6700b460152c45d99b4800b7cd5336cfcfeafd/research_notes/driver/2026-11-24_t6_p17_q12_q13_full_observer_four_five_adic_exclusion.md), reusing its precise atom definition and bounded q0 enumeration. It also relies on the existing [17-squared cancellation certificate](https://github.com/awdawmip/enterprise-math/blob/325747d5661105943c2001abf32057e83ccf5fa5/research_checks/T6_P17_SQUARED_CANCELLATION_67_PROFILE_EXACT_CHECK_20261123.cpp). There is no new independent research identity or claim of independent Native review.

To finish maximal-p17 order 11, check split(4,7) with the true q4 budget: q4 can have vertical cost 1188 (two q2,r1 atoms), hence q0 cost may be as large as `2331-1188=1143`. **Reusing the 854 ceiling for q4 would silently omit legal cases.** This distinct open subcase and lower orders should be owner-/prior-art-checked before formal task allocation. The q11(5,6) theorem itself is mathematical evidence subject to independent Source/Result/review admission.


## Subsequent prior-art reconciliation (2026-11-24)

Original EM-X6-FB6990 author certificates for q11 and q12 already reported exhaustive zero-leaf searches over a larger literal atom roster, including q11(4,7). See [the nonauthor roster audit and scope correction](https://github.com/awdawmip/enterprise-math/blob/7a3b72415d67a6396483503c637f328db5da8026/research_notes/driver/2026-11-24_t6_p17_q11_q12_prior_art_and_smooth_roster_audit.md). For the overlapping q11 and q12 scopes, this Driver's signature certificate is an alternative exact method, not newly eliminated denominator scope. The original q11(4,7) is author-computed, awaiting independent verification, not an unresearched execution target. Preserve both actual contributions and the original frozen bytes; no formal admission implied.
