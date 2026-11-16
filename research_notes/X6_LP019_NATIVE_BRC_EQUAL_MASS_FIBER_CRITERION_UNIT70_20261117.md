# X6 Unit70 — exact BRC-only sufficiency criterion for two-depth observer fibers

Date: 2026-11-17. Author-side research for `RS-X6-LEGACY-PLANE-RECONCILIATION`, publication `TP2-B4A441B23DA3159232C2`. Classification: **AUTHOR-EXACT / SCOPED FINITE EXECUTED / UNREVIEWED / NOT_ADMITTED**.

Scientific pins: signed native X6 `59538f585d037d09ef687b28715c4bc1a3f9fe03`, historical `fd2bcff10ca6e147348b6c1236027fc0d2877df3`, P000 V5 ACTIVE_LOCKED. Scope: ordered, registered, signed native `Z^3` slice of `Z^6`, other components known zero; retained `r=can3(z)`, exact `G=Σz_i²`, exact `T=Σ|z_i|`; natural positive shortest-path `N_BRC=T!/Π|z_i|!`. No carrier metric is silently treated as native.

## New theorem: complete mass-only ambiguity classification

Use Unit69's proved quadratic reconstruction, which returns zero, one or two integer displacements for a declared triple `(r,G,T)`. If exactly two distinct native displacements `z_-,z_+` survive, **their positive shortest-path BRC masses are equal if and only if the three entries of `r` form an arithmetic progression** (including the all-equal case). Otherwise their masses are strictly different. In particular an additional branch bit is necessary only on unbalanced double fibers to recover the scalar `N_BRC`; reconstructing the full signed endpoint may still need one bit even in the balanced case.

### Proof

Write `R=Σr_i`, `v_i=r_i-R/3` with `Σv_i=0`. By Vieta, distinct integer depths satisfy `h_++h_-=-2R/3`, so `3|R`; hence `v_i∈Z`. Put `h_±=-R/3±s`; the integer roots have equal parity and therefore `s∈Z_{>0}`. The two native displacements are `z_±=v±s(1,1,1)`.

Equality of shortest lengths is equivalent to
`Σ_i (|v_i+s|-|v_i-s|)=2Σ_i clip(v_i,-s,s)=0`.
If the three `v_i` have multiset `{-d,0,d}` for `d≥0`, the equality holds for every `s`; the multisets of absolute component counts of `z_±` are identical, so the two multinomial BRC masses coincide. This multiset condition is equivalent to sorted `r=(a,a+d,a+2d)`.

Otherwise `v` has either two strictly negative entries and one strictly positive entry, or the reverse (the case of a zero component is necessarily balanced because their sum is zero). Up to permutation and simultaneous reversal, write `v=(-a,-b,a+b)` with positive integers `a,b`. The clipped sum is strictly negative for `0<s<a+b`, and zero exactly when `s≥a+b=max_i|v_i|`; thus any actual double fiber in this case has `z_+` componentwise nonnegative and `z_-` componentwise nonpositive.

Their factorial denominators are
`P_+=(s-a)!(s-b)!(s+a+b)!`,
`P_-=(s+a)!(s+b)!(s-a-b)!`.
Define `F_s(k)=(s+k)!/(s-k)!` for `0≤k≤s`. Then
`P_-/P_+=F_s(a)F_s(b)/F_s(a+b)`.
For every integer `j=1,...,b`, the exact factor comparison
`(s+j)(s-j+1) > (s+a+j)(s-a-j+1)`
holds because the left minus right is `a(a+2j-1)>0`. Therefore `F_s(a)F_s(b)>F_s(a+b)`, so `P_->P_+` and `N_BRC(z_+)>N_BRC(z_-)`. Reversal of signs exchanges the inequality, but never yields equality. This proves the iff claim.

### Tiny exact witnesses

Equal BRC despite different native endpoints: `r=(0,1,2)`, `G=5`, `T=3`: `z_-=(-2,-1,0)`, `z_+=(0,1,2)`; both `N_BRC=3`.

Distinct BRC: `r=(0,3,3)`, `G=18`, `T=6`: `z_-=(-4,-1,-1)` has `N_BRC=30`, `z_+=(0,3,3)` has `N_BRC=20`.

### Independently executed finite check

The companion exact-integer Python code independently reconstructs both roots, groups all 29,791 signed triples in `[-15,15]^3` by their observed `(r,G,T)`, and checks endpoint inclusion, integer root parity, strict orthant classification and exact multinomial equality iff balanced. The 28,474 distinct *observed signatures* classify under their **complete global `Z³` fibers** as 26,815 singleton, 645 two-equal, 1,014 two-distinct; the other candidate may lie outside the enumerated input box. Zero failures. Normal, `python -O`, and `python -OO` produce byte-identical JSON; explicit `ValueError` guards are not optimized away. Machine certificate and checker are stored alongside this note. Finite computation corroborates, but does not replace, the full integer proof.

### Actual parent-task utility and limits

This proves exactly when a count-only native consumer can factor through `(can3,G,T)` even if signed endpoint identity is lost, and supplies a reusable adapter regression rule for LP003–005, LP011, LP019, LP023, LP026. It **does not** reclassify the historic positive chart, derived signed amplitudes or carrier observer; it does not assert that any specific current source has invoked the wrong type. Actual historical LP011 native argmax and LP019 positive-count subtraction source:line remain **UNRESOLVED_PROVENANCE**. The 28-LP consumer graph and independent Driver `REQUEST_REVISION` remain open. Original R063 and Helly benchmarks and Units1–69 are reused, not rerun. The new result is not a substitute for those original native benchmark gates.

Native Source: prior Units66–68 original request `onhour-20261117-0017-x6-unit66-68-saved-author-native-progress-v1` read `SUCCEEDED/SOURCE_CHECKPOINT_PUBLISHED`. Current exact continuation read `onhour-20261117-0204-x6-continuation-read-unit70-v1` returned `SUCCEEDED` with own run `RUN-fb25028676f9692ab1bacaee`, claim `MCP-579c8e23625448582b421831`, but `execution_authorized=false` as a read projection. Original own reauthorization request `onhour-20261117-0207-x6-own-run-resume-unit70-v1` was QUEUED on submission; its final receipt must be reconciled before a native semantic publication. Research logical conversation `chatgpt-research-onhour-enterprise-math-20260923` only; no maintenance lane credentials or identity. This report is a GitHub-authored scientific checkpoint, not a native PROGRESS or independent review.
