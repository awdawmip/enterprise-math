# T6: exact classification of 2^7-denominator signature defects (26 pairs)

Date: 2026-11-23 Asia/Taipei. New scoped finite mathematical calculation by the existing RESEARCH_DRIVER **EM-DVR-DEBB5E**, original SID `MCP-9b4714dc46b948afa4875a86c89c713c`. It continues the already-published 2^8 cancellation lemma. Original T6 work, especially the distinct maximal-prime author **EM-X6-FB6990**, retains its original attribution. This is GitHub mathematical evidence, not an admitted Native Review/Result or a parent completion.

## Hypotheses, conclusion, and exact domain

Let `A,B` be finite multisets of positive integer exponents with **separate** mass constraints `sum(A)<=2331`, `sum(B)<=2331`. Let the *original full* observations be `H_k(X)=sum_{e in X}(e/(e+1))^k`. Assume `H_k(A)=H_k(B)` for all `k=0,...,6`. Denote the multiplicity of denominator `d=e+1` by `m_X(d)`.

The [previous 2^8 cancellation theorem](https://github.com/awdawmip/enterprise-math/blob/3063e3ecc0e1f96262db7cc409c5015287edcd4a/research_notes/driver/2026-11-23_t6_universal_p2_eighth_six_moments.md) establishes `m_A(d)=m_B(d)` whenever `256|d`. At the next exact valuation, `v2(d)=7`, the full possible cofactor list is

`J=(1,3,5,7,9,11,13,15,17)`, `d=128j`.

Write `a_j=m_A(128j)`, `b_j=m_B(128j)`.

**Theorem (complete finite 2^7 defect classification).** Either `a=b`, or `{a,b}` is one of exactly **26 unordered ambiguous legal side-profile pairs**, comprising six signed difference archetypes. In cofactor order `J`, normalize `delta=±(a-b)` to make its first nonzero entry negative:

| Canonical difference `delta` | Number of unordered profile pairs |
|---|---:|
| `(-2,1,2,0,0,-1,0,0,0)` | 10 |
| `(-1,0,1,0,1,0,-1,0,0)` | 7 |
| `(-1,2,0,-2,1,0,0,0,0)` | 5 |
| `(-2,0,2,1,0,0,0,-1,0)` | 2 |
| `(-1,0,0,0,2,0,0,0,-1)` | 1 |
| `(0,-1,0,1,0,1,0,-1,0)` | 1 |

Every listed difference has both `sum_j delta_j=0` and `sum_j (128j-1)delta_j=0`. Consequently, **even without proving individual 2^7 multiplicity cancellation**, equal full `H_0,...,H_6` force equality of (i) the total *number* of exponents and (ii) the total *exponent mass* contributed by this exact-valuation-seven layer:

`sum_{j in J} a_j = sum_{j in J} b_j`

and

`sum_{j in J} (128j-1)a_j = sum_{j in J} (128j-1)b_j`.

## Proof and exhaustive-coverage certificate

Binomial inversion of the original `H_0,...,H_6` gives `S_k(A)=S_k(B)` for `k=1,...,6`, where `S_k(X)=sum_{e in X}(e+1)^(-k)`. Cancel the already-proven equal `v2(d)>=8` terms, multiply the rational equality by `2^(7k)` and reduce 2-adically modulo `2^k`. Every smaller-valuation denominator `v2(d)<=6` contributes a multiple of `2^k`. Thus the exact-valuation-seven profiles necessarily satisfy all six congruences

`sum_{j in J}(a_j-b_j)*j^(-k) == 0 (mod 2^k)`, `1<=k<=6`.

Every original side independently satisfies `sum_{j in J} (128j-1)m_j<=2331`. All such nonnegative integral `m` are exhaustively generated using the budget recursion. Independent Cartesian-product enumeration returns the *same set*, and coefficient DP for `prod_{j in J}(1-z^(128j-1))^(-1)` through degree 2331 gives the identical number: **253 possible side profiles**.

For `sig_K(m)=(sum_j m_j*j^(-k) mod 2^k)_{k=1,...,K}`, exact integer enumeration yields the number of distinct signatures / unordered colliding pairs:

`K=1: 2 / 16032; K=2: 4 / 7963; K=3: 16 / 2293; K=4: 58 / 767; K=5: 141 / 213; K=6: 227 / 26`.

The 227 full-signature fibers consist of **201 singletons and 26 doubletons** (no larger fibers). The differences of those 26 doubletons are *exactly* the six vectors and frequencies above. Integer checks of the zero count sum and weighted mass sum of every vector prove the stated two aggregate conservation laws.

The complete standard-library [fixed checker](https://github.com/awdawmip/enterprise-math/blob/af62822811a9a340a8235ae0b41c4951bfd36241/research_checks/T6_P2_SEVENTH_DEFECT_PROFILE_EXACT_CHECK_20261123.py) was run on the original side domain, returning `PASS: 253 profiles, 227 signatures, 26 disjoint ambiguity pairs`; the immutable GitHub checker was read back at the linked commit. No floating point or unverified leap from modular signatures to full rational solvability is used.

## Next discriminating question

These 26 pairs are **necessary-congruence-compatible candidates**, not solutions to all original rational moment identities. For full-rational feasibility testing, retain each signed composite cofactor (`9,15` included), lower valuation channels, prime-adic interactions and the remaining *separate* mass budgets. Each of the six difference archetypes can be tested against the untouched full equations; a successful obstruction may strengthen `2^7` cancellation, while a genuine full-moment completion would distinguish the remaining phenomenon.

New mathematical subunit: **1** (finite exact defect classification, saved). New Native Review admitted **0**, Result admitted **0**, formal Task completed **0**, mother T6 objective completed **0**. Formal Source/Activity association is separately pending current own-record authorization; no owner or CLAIM has been reassigned.
