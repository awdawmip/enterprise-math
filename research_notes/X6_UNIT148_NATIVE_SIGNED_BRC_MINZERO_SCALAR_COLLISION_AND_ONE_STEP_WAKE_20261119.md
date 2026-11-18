# X6 Unit148 — signed native BRC scalar collision under a three-axis min-zero observer and one-step separation

Date: 2026-11-19. Parent PO-X6-SPATIAL-FOUNDATION-CONSISTENCY-20260905; Task RS-X6-LEGACY-PLANE-RECONCILIATION; publication TP2-B4A441B23DA3159232C2. Researcher EM-X6-FB6990; Research SID MCP-082892eb480e45dea6d4b9fcc0491034; Research logical lane chatgpt-research-onhour-enterprise-math-20260923. Status: **AUTHOR_EXACT_INTEGER_PROVED / FINITE_INDEPENDENT_CHECK_EXECUTED / UNREVIEWED / NOT_ADMITTED**.

## Exact immutable source and typed consumers
- Scientific pin `59538f585d037d09ef687b28715c4bc1a3f9fe03`, historical comparison `fd2bcff10ca6e147348b6c1236027fc0d2877df3`.
- Current native definition `definitions/ENTERPRISE_X6_NATIVE_SPATIAL_CELL_TORSOR_20260905.md` blob `b4d49a1bbcccad0521618c6d20f6dcfa242b420a`; native signed BRC kernel `experiments/x6_signed_native_spatial_v16_20260905/signed_brc.py` blob `300a96e3dc24bf6fff73743037a0347a8bc83176`. The exact interfaces are `spatial_norm_squared`, `shortest_event_count`, `shortest_path_multiplicity`.
- Historical R062 positive-sector consumer `definitions/ENTERPRISE_BRC_MULTIPATH_ENRICHMENT_BRIDGE_20260821.md` at historical pin blob `6ec0d73a19e28ec586c59a97d24f5798c9119771`; current signed-X6 retyping on main blob `97ab1403ab04b4fa80034625fb1b2e3ed115e59b`. The historical positive sector counts are valid for their fixed chart, not complete native signed X6 endpoints.
- This is a **new matched native/relative consumer observation** on those actual interfaces. It does not claim the alleged LP011 historical wrong argmax caller or LP019 historical positive BRC subtraction caller has been located.

## Theorem (infinite exact family)
Fix the declared native three-axis slice `S={0,1,2}` of the signed X6 spatial Cell torsor. For integers `1<=a<=b`, put
`d=(-a,-b,0,0,0,0)` and `r=(can3(d_0,d_1,d_2),0,0,0)=(b-a,0,b,0,0,0)`.
The original native displacement is d; r is a different *relative min-zero observer section* re-embedded in the selected slice, and `r-d=b H_S`, `H_S=e_0+e_1+e_2`. Both have the same selected three-axis min-zero readout, but `d != r`.

Write `G(z)=sum_i z_i^2`, `N(z)=sum_i |z_i|`, and `B(z)=N(z)!/prod_i |z_i|!` on **raw signed native displacement**. Then
`G(r)-G(d)=b(b-2a)`, `N(r)-N(d)=b-2a`,
`B(d)=binom(a+b,a)`, `B(r)=binom(2b-a,b-a)`.
Consequently `G(d)=G(r)` and `N(d)=N(r)` hold simultaneously **iff** `b=2a`. For every positive integer a in this exact infinite subfamily,
`d=(-a,-2a,0,0,0,0)`, `r=(a,0,2a,0,0,0)`, and
`(G,N,B)(d)=(G,N,B)(r)=(5a^2,3a,binom(3a,a))`.
The BRC equality follows because the absolute signed coordinate multiplicity arrays are permutations `(a,2a,0)` and `(a,0,2a)`, not because their native endpoints are equal.

**A single admitted native primitive step separates every collision.** Let `T_0^+(z)=z+e_0`. For every a>=1,
`G(T_0^+r)-G(T_0^+d)=4a`, `N(T_0^+r)-N(T_0^+d)=2`.
The proof is immediate by expansion of the first coordinate and the signs of `1-a` and `a+1`.

Smallest exact witness: `a=1`, `d=(-1,-2,0,0,0,0)`, `r=(1,0,2,0,0,0)`; each initially has `(G,N,B)=(5,3,3)`. After `+e_0`: `d'=(0,-2,0,0,0,0)` gives `(4,2,1)`, while `r'=(2,0,2,0,0,0)` gives `(8,4,6)`.

## Observer and provenance implication
Equality of the three scalar readouts `(G,N,B)` on both representatives is insufficient to identify native signed Cells, to promote a three-axis min-zero relative observer to a full native endpoint or to assert future-operation safety. The next actual primitive operation reveals a structural residual at every scale a. The relative `can3` quotient remains valid **at its declared selected-slice observation**; a lossless native reconstruction retains the integer slice depth `h=min(d_0,d_1,d_2)=-2a` and the axes not selected. This uses the frozen Joint Relation Observer Preservation contract, and separates mathematical information loss from implementation errors.

## Verification and strength
An independent exact-integer script, not the original frozen native module or R063/Helly six-file benchmark, checked all 2,080 pairs `1<=a<=b<=64`, the exact defect formulas and multinomial formulas, plus an independent dynamic-programming path-word count for the smaller `a<=8,b<=16` grid. Exactly 32 simultaneous scalar collision pairs `(a,b)=(a,2a)`, `1<=a<=32`, and all native one-step separation checks passed. CPython normal, `-O`, and `-OO` produced identical canonical JSON SHA256 `9beb4e4bb51cf31a899423308816f7c8c337539755a6ef9d3b6b51e9c269a43d`. Infinite-family correctness comes from the closed-form algebra above, not extrapolation from the finite census.

## Parent continuation
This is a bounded native/relative **source-typed crosswalk** for historical R062 and current signed X6 BRC, with one new infinite exact collision family and primitive-operation observer witness. Existing Unit147 auxiliary cyclotomic work and Units1–146 are consumed, not repeated. Preserve the remaining 28-LP historical/current file:line audit, LP011 and LP019 alleged faulty old callers as `UNRESOLVED_PROVENANCE`, original R063 six-file benchmark as `NOT_RERUN`, and independent Driver review as `PENDING`. No changes to P000, taskbook, freeze, Result or admission.
