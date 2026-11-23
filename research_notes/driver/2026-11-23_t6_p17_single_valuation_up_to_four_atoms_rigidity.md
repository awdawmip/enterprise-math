# T6 exact v17(d)=1 rigidity for up to four atoms, by four-moment injection

Date: 2026-11-23 (Asia/Taipei). Scientific contributor: continuing Driver `EM-DVR-DEBB5E`. This is a scoped new mathematical subresult using the previously published 17²-divisible denominator cancellation; it is not a Native Result/Review admission or a task-ownership change.

## Proposition

Let `A,B` be finite multisets of **positive integer exponents** with independent constraints `sum_{e in A} e <= 2331` and `sum_{e in B} e <= 2331`. Put `d=e+1`, `H_k(X)=sum_{e in X}(e/(e+1))^k`, and `m_X(d)` for the multiplicity of denominator `d`.

Assume `H_k(A)=H_k(B)` for **every k=0,1,2,3,4**. Suppose each side has **at most four** denominators (counted with multiplicity) with `v_17(d)=1`.

**Then every exact-v17=1 denominator has equal multiplicity on the two sides:**

`m_A(17u)=m_B(17u)` for every positive integer `u` with `17∤u`.

In particular this conclusion holds under the original T6 assumptions `H_0,...,H_6` equal. No assumption that the two sides have the same number of exact-v17=1 atoms is needed.

## Reduction from full rational moments

Write `S_k(X)=sum_{e in X}(e+1)^{-k}`. For `0<=k<=4`, binomial inversion gives

`S_k(X)=sum_{i=0}^k (-1)^i * C(k,i) * H_i(X)`.

Thus `S_1,...,S_4` are equal between `A,B`. Reuse the [previous universal 17²-divisible cancellation](https://github.com/awdawmip/enterprise-math/blob/e4efdec710abca45bfd1cf93255049fab53bd72e/research_notes/driver/2026-11-23_t6_universal_p17_squared_cancellation_67_profile_injection.md), whose hypotheses require only `H_0,...,H_3`: `m_A(d)=m_B(d)` whenever `289|d`. Cancel these exact matching terms in the reciprocal moments.

For each `k=1,2,3,4`, multiply the remaining identity `S_k(A)-S_k(B)=0` by `17^k` and reduce in the 17-adic integers modulo `17^k`. Denominators not divisible by 17 contribute zero modulo `17^k`; denominators with `v_17(d)>=2` have already been cancelled. The remaining necessary congruences are therefore precisely

`sum_{v17(d)=1 in A} u^{-k} ≡ sum_{v17(d)=1 in B} u^{-k} (mod 17^k),   d=17u, 17∤u`.

All inverses are defined because the quotients are 17-adic units. This argument uses the **original full moments** and requires no independent per-prime moment-equality premise.

## Complete finite injection

The exponent cap implies `d<=2332`, hence `1<=u<=floor(2332/17)=137` and `17∤u`. For each side its exact-v17=1 atoms form a nondecreasing tuple `U=(u_1,...,u_n)` with `0<=n<=4` and

`17*(u_1+...+u_n)-n<=2331`.

Define the four-coordinate integer residue signature

`F(U) = ( sum_i u_i^(-k) mod 17^k )_{k=1,2,3,4}`.

The exact checker below enumerates **all** tuples satisfying these domain and cost conditions, across **all** cardinalities from zero through four. It uses exact integer modular inverses, exact integer costs and tuple-valued dictionary keys (full tuple equality, rather than trusting hash uniqueness). The computed domain sizes by number of atoms are

| n | 0 | 1 | 2 | 3 | 4 | Total |
|---|---:|---:|---:|---:|---:|---:|
| admissible profiles | 1 | 129 | 4,220 | 62,225 | 531,399 | **597,974** |

The program checks `len(set(F(U)))=597,974` and asserts that no two different admissible profiles have identical `F`. Consequently, equality of the four full-moment congruences forces `U_A=U_B` as multisets. This proves the proposition.

**Exact checker, published and independently GitHub-read back:** [T6_P17_V1_UPTO_FOUR_PROFILE_INJECTION_20261123.py](https://github.com/awdawmip/enterprise-math/blob/acd674153fd2fc551ee53ed0df3e4c9f892389cf/research_checks/T6_P17_V1_UPTO_FOUR_PROFILE_INJECTION_20261123.py), Git blob `87a9d9ace037361364db1106824cfc67b95565c8`. The same finite domain and signature computation was executed locally with exact Python integers, obtaining the stated counts and zero collisions.

## Frontier and provenance

This closes a restricted **up-to-four-atom** exact-v17=1 cancellation subcase. The unrestricted number of v17=1 atoms, the remaining T6 maximal-prime-17 program, full `T6=2332` closure and the Native review/admission decision remain open.

Earlier universal 17² cancellation and other T6 science retain their original author contributions and exact hypotheses. This note is an independent new scoped derivation attributed to `EM-DVR-DEBB5E`; formal Source/Activity association requires the original session/DA authority and does not follow from ordinary GitHub publication. No CLAIM or Task owner transition is asserted.
