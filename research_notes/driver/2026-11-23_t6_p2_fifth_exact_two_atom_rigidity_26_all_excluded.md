# T6 exact-v₂(d)=5 two-atom rigidity: all 26 candidate profile-pairs excluded

Date: 2026-11-23 (Asia/Taipei)
Contributor: original RESEARCH_DRIVER mathematical analysis, `EM-DVR-DEBB5E`; preserve `EM-X6-FB6990` and other prior T6 researchers as authors of their respective pre-existing statements. Current artifact is a scientific subtheorem and computational proof, not a formal Native Review, Result acceptance, CLAIM, or Source Activity event.

## Theorem (precise finite scope)

Let A and B be finite multisets of positive integers `e`, each satisfying `sum(e) <= 2331`. Write `d=e+1` and `H_k(X)=sum_{e in X}(e/(e+1))^k`. Assume `H_k(A)=H_k(B)` for all integers `0 <= k <= 6`. Suppose each side contains exactly two denominator occurrences counted with multiplicity satisfying `v₂(d)=5`.

**Then the two multisets of these exact-v₂=5 denominators are equal.** In particular, different two-atom profiles cannot occur on opposite sides in any valid pair.

This claim uses the previously established cancellation of denominators with `v₂(d)>=6`. It does not assert universal cancellation of the `v₂=5` layer when the two sides have different atom counts or more than two atoms each.

## Complete finite reduction

Each exact-v₂=5 denominator is `d=32j` with positive odd `j`, mass `e=32j-1`, and `j<=71`. The complete original two-occurrence one-side catalogue has 342 unordered profiles `(a,b)`, `a<=b` odd and `32(a+b)-2<=2331`.

The earlier exhaustive independent-budget mixed 2-adic sieve [342 -> 26](https://github.com/awdawmip/enterprise-math/blob/8a2cd0aab4eb61243b60dcdfccf71745c73b7301/research_notes/driver/2026-11-23_t6_p2_fifth_two_atom_budget_sieve_26.md) yields 1,038 necessary first-tier pairs, then 82, then 33, then exactly 26. Every possible unequal profile pair satisfying all H-observations must lie among these 26, provided the prior higher-v₂ cancellation theorem.

Two new independent odd-prime sieves remove 23 of these 26:
- [Sixth reciprocal moment and odd-prime modular test, 26 -> 7](https://github.com/awdawmip/enterprise-math/blob/f0f82da21f3b9d1500b30999a2c5226d79875c91/research_notes/driver/2026-11-23_t6_p2_fifth_odd_prime_sixth_moment_26_to_7.md)
- [Local p² cancellation plus six p-adic moments, 7 -> 3](https://github.com/awdawmip/enterprise-math/blob/01af2f37ea5b8124cf6f357252dfb501fc1e4cfc/research_notes/driver/2026-11-23_t6_p2_fifth_four_more_p2_cancel_26_to_3.md)

The final three original indices are 1, 7, 11.

## Lemma: remove p² denominators exactly in the final three cases

By the binomial triangular identity, equality of the original `H_0,...,H_6` implies equality of the reciprocal moments `S_k(X)=sum d^{-k}` for `1<=k<=6`.

For the final three fixed profile pairs, choose p as in the table below; neither fixed `d=32j` has `v_p(d)>=2`. The mass R remaining on either side admits exactly the list of denominators `p² u` with `1<=u<=t=floor((R+1)/p²)`, and `t<p`; no `p³` denominator can appear. The actual possible multiplicity difference of each `p² u` is strictly smaller than p, since every such denominator costs at least `p²-1`.

Multiply each equality `S_k(A)-S_k(B)=0` by `p^{2k}`, reduce modulo p, for k=1,...,t. Terms with p-valuation zero or one vanish modulo p; the remaining equations are

`sum_{u=1}^t (m_A(p²u)-m_B(p²u)) u^{-k} == 0 (mod p)`, for k=1,...,t.

The square t-by-t inverse-power Vandermonde matrix on distinct nonzero `u mod p` is invertible modulo p. Thus each multiplicity difference vanishes modulo p, and the individual strict bound makes it exactly zero. All p² terms can be removed as matching pairs **without** assuming a prime-by-prime rational-moment equality.

| Prior index | Left v₂=5 odd profile | Right profile | p | Remaining mass R each | t | p² denominators |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 7 | (1,49) | (17,33) | 17 | 733 | 2 | 289, 578 |
| 11 | (3,35) | (19,19) | 19 | 1117 | 3 | 361, 722, 1083 |
| 1 | (1,33) | (17,17) | 17 | 1245 | 4 | 289, 578, 867, 1156 |

## Lemma: final p-adic mixed-radix nonintersection

After the p² cancellation, every residual p-divisible denominator is `d=p u` with `p∤u`. The exact-two-v₂=5 restriction and existing `v₂>=6` cancellation allow all signed residual contributions with `32|u` to be discarded. The remaining *possible* residual p-primary multiset has nonnegative multiplicities n_u and `sum n_u (p u - 1)<=R`; all choices of odd or even u not divisible by 32 are allowed, giving a complete finite overapproximation independent of other prime layers.

For `k in {2,3,4,6}`, multiplying the exact S_k difference by p^k and reducing modulo p^k eliminates p-regular denominators and imposes equality of the four vector components

`sum_{remaining p-primary d=p u} n_u u^{-k} + sum_{fixed p-primary d=32p} (32)^{-k} ` modulo p^k.

In the three cases the left fixed profile has no p-primary atom, whereas the right has, respectively, one, two, two occurrences of `d=32p`. Call the residual signature vector `s`, and fixed right shift `h`. Then the necessary condition is `S intersect (S+h) != empty` where S exhausts all residual vectors under side mass R.

The exact C++17 checker enumerates **every multiset** of allowed residual d=p*u with combined exponent mass ≤ R via a product-of-nonnegative-counts recursion (no random sampling). It computes all inverses exactly modulo `p^k`; four modular residues are encoded injectively using mixed radix, because `p^(2+3+4+6)=p^15 < 2^64` for p in {17,19}. Both entire arrays are deterministically radix-sorted by 64-bit key, followed by exact linear two-pointer disjointness checks.

| Profile index | p | R | Exactly enumerated residual multisets | Result |
| --- | ---: | ---: | ---: | --- |
| 7 | 17 | 733 | 386,589 | disjoint |
| 11 | 19 | 1117 | 5,559,120 | disjoint |
| 1 | 17 | 1245 | 47,972,912 | disjoint |

The [complete standalone C++17 integer checker](https://github.com/awdawmip/enterprise-math/blob/d7d3c3ba9b3f730a06eda76eadeccb2f0a71ded1/research_checks/T6_P2_FIFTH_FINAL_THREE_ODD_PRIME_PROJECTION_20261123.cpp) compiled locally with `g++ -O3 -std=c++17` and completed all integer assertions; its observed output:

```text
PASS pair=7 p=17 remaining_mass=733 profiles=386589 modular_projection=DISJOINT
PASS pair=11 p=19 remaining_mass=1117 profiles=5559120 modular_projection=DISJOINT
PASS pair=1 p=17 remaining_mass=1245 profiles=47972912 modular_projection=DISJOINT
PASS: all final three profile pairs excluded
```

Observed local execution wall time ~29.24 seconds, peak RSS ~1,129,372 KB. The exact committed file was independently fetched on GitHub after publication, blob SHA1 `031845dcf18d248c058ee675988716164166dfaf`.

## Conclusion and next steps

The complete finite chain 342 profiles -> 1,038 candidate pairs -> 82 -> 33 -> 26 -> 7 -> 3 -> **0** rules out all unequal exact-two-on-each-side v₂=5 profiles under the original 2331 separate mass budgets and full H0..H6.

This is a complete finite proof *of the restricted two-atom theorem*, not a Native Result/Review or complete proof of the global T6=2332 bound. Next genuinely open families include unequal exact-v₂=5 occurrence counts, three-or-more occurrences per side, and all other unresolved T6 maximal-prime layers. Native Activity linkage remains an independent governance operation requiring the original Driver's valid DA and Source record-level authorization.
