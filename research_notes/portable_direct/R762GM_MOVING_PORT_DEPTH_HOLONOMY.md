# R762GM — Moving named-Port gate restores nonzero signed STAR depth holonomy

Research date: 2026-11-20 (Asia/Shanghai). Task: `RS-X6-TRIADIC-CLOSURE-DYNAMICS`, publication `TP2-8B7E13C5904A2D6F1142`. Frozen scientific P000 source: `awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389:p000_reality_foundation.json`. Frozen taskbook: `857280d1012943290d141d1317179c40ec3cbdf8`. Antecedent R762GL: `PR #2826@f0ec8fb3413e3bb14b26025decd7cdefd3a726fb`. Original prior researcher lineage: `EM-X6-3050F6`; this portable file does not assert current CLAIM or possession of the original session capability. Author-side finite exact checks: PASS. Independent review: NOT_REVIEWED.

## Statement and candidate model

The tetrahedral vertices are V={0,1,2,3}. The six signed X6 Cell coordinates are indexed by undirected edges E=[01,02,03,12,13,23]. For each v define STAR S_v as its three incident edges (ordered by the other endpoint), H_v as the signed-axis indicator of S_v, and g_v as the cyclic permutation of those three edge labels. As in R762GI/R762GK, a signed **composite three-axis event** is

    T(v,s)=(s H_v,g_v^s), s∈{+1,-1}, in G=Z^6 ⋊ A6,

with group law (x,p)(y,q)=(x+p·y,pq). Each event represents a typed ordered native-axis composite and its associated candidate orientation update, not a new primitive spatial direction.

**New joint-state rule.** Choose the registered *initial* named Port edge e0=01. At state (x,p), the current named Port edge is e=p(e0). An event T(v,s) is **permitted** precisely when v is an endpoint of e, and its update is the usual semidirect right multiplication. Equivalently, the joint state is (x,p,e0) and the visible moving edge is derived as p(e0). The rule is a **candidate**, not the frozen native `TRIADIC_CLOSURE_E` event license. It deliberately differs from R762GL's static gate `v∈e0`.

The observer studied here asks whether the **complete affine state** after m admitted events equals (kD,id), D=(1,1,1,1,1,1), while preserving the admitted signed word as BRC source evidence. Let C_m(k) count ordered admitted m-letter histories with that exact product, and give each admitted letter conditional probability 1/4 at each step. The complete affine-state observer fixes e0 throughout the comparison.

## Theorem — first moving-Port nonzero diagonal loop

1. Every reachable joint state has exactly four permitted signed candidate letters (two endpoints times two signs); hence there are exactly 4^m ordered admitted histories of length m.
2. If the complete affine product is (kD,id), then m is even and the signed-letter count obeys `sum_t s_t=2k`. In particular `|k|≤m/2`, with equality iff all letters have sign sign(k).
3. For every m<12 and every k≠0, C_m(k)=0. At m=12, the exact complete-affine return distribution is

       C_12(0)=142616, C_12(+6)=8, C_12(-6)=8,
       C_12(k)=0 for all other k.

   Thus the **sharp first nonzero joint relative-depth return length is 12 candidate events**, attaining depth ±6. For the stipulated uniform, conditionally admitted positive BRC distribution,

       Pr[(X_12,P_12)=(kD,id) for some k≠0] = 16 / 4^12 = 1 / 1,048,576.

4. In contrast, the fixed named-edge license of R762GL has C_m(k)=0 for every m and k≠0. Therefore whether the Port edge is fixed or transported by the orientation register is an actual dynamical distinction: keeping the named Port update can restore nonzero depth return.

The exact finite-dynamic-program proof of point 3 is a **finite exhaustive certificate for all horizons 0≤m≤12**. It does not claim an all-horizon formula for C_m(k) or validate the candidate as the native force-balance law.

### Proof

For a fixed (x,p), p is a six-edge permutation and p(e0) is exactly one of six tetrahedral edge labels, which has two distinct endpoints. Each endpoint has both signs admitted; their event pairs are distinct. This proves the four-branch statement by induction.

The coordinate-sum functional `sigma(x)=sum_{i=1}^6 x_i` is invariant under any permutation p. Right multiplication by T(v,s) changes sigma by 3s. Starting from zero, a diagonal return has sigma(kD)=6k, proving `3 sum s=6k`. Because sum of m signs has the same parity as m, m is even. The triangle inequality for the signed sum gives `|2k|≤m`; equality forces uniform sign.

For point 3 use the exact recurrence on full (x,p) states

    F_0((0,id))=1;
    F_{m+1}(x+p·sH_v, p g_v^s) += F_m(x,p)
    for v∈endpoints(p(e0)), s∈{−1,+1}.

All other initial counts are zero. Each transition is generated exactly once for each admissible next signed letter, so induction identifies F_m with ordered-word multiplicity. The attached standalone Python checker executes the recurrence with exact integer counts through m=12, verifies `sum F_m=4^m` at every layer, and filters for the **full** product `(kD,id)` rather than an endpoint-only quotient. It finds no nonzero diagonal returns for m<12 and the stated complete histogram at m=12. Two independent depth-12 oracles enumerate every `2^12` admissible all-positive and all-negative vertex-choice history and each find exactly eight valid ±6 returns. Since `|k|=6=m/2` requires uniform sign, those oracles independently verify all nonzero returns at m=12. The checker also validates explicit signed witness words against the gate and full endpoint.

For example, starting with e0=01 and taking **positive** STAR vertices in order

    [0,0,0,1,2,2,2,1,3,3,3,1]

passes every moving-edge incidence check and ends exactly at `(6D,id)`. Its successive admissible named Port edges before the twelve events are

    [01,02,03,01,12,12,12,12,13,13,13,13].

The **negative** witness

    [0,0,0,1,3,3,3,1,2,2,2,1]

ends at `(−6D,id)`. The source histories are preserved verbatim. For the static gate, only vertices 0 and 1 are admitted, so the signed Cell coordinate at edge 23 stays zero under all those events and their associated rotations; a full kD return forces k=0. QED.

## BRC observer and provenance obligations

The exact carrier here is the finite typed, positively counted **signed-word multiset** over four admitted next letters, with deterministic joint transitions (x,p,e0). The dynamic program only aggregates the current full state to calculate the declared terminal observer; it is not an erasure theorem for future provenance-sensitive queries. The witnesses retain ordered vertices, signs, moving Port edges and affine state. Any later observer that queries original named Link/Port identities, event order, time or force incidence must lift from the source word or prove an observer-safe quotient.

An explicit one-step future-distinguishing example: the same initial affine state (0,id) with registered e0=01 permits STAR 0 but with registered e0=23 does not. Therefore the initial named Port label is indispensable for future admissibility under this rule, even though the affine state agrees.

The three-axis composites do not equate with P000 primitive two-force equilibrium or classical zero-vector balance; P000's three-force arity, PERP_E=120°, six-dimensional Cell torsor and independent time are unchanged. No native TRIADIC_CLOSURE_E permission, Result acceptance, or independent mathematical review is asserted.

## Verification and next questions

Checker: `R762GM_VERIFY.py`, Python 3 standard library, exact integers; all 0..12 layers, full state dictionary, and two independent pure-sign DFS enumerations. `R762GM_EVIDENCE.json` records the output and witness. Actual author-side verification PASS, review NOT_REVIEWED.

Next scientific questions: (i) classify whether a **real native** signed Cell/Port/Link event transports the named Port under rotation, fixes it, or uses a third rule, using exact frozen licensed event definitions; (ii) determine the minimum horizon for **unit** depth ±1 under the moving-gate candidate, and its group/Markov invariants; (iii) test future-operation sufficiency of the state (x,p,e0) when named Link histories are relevant. No automatic promotion of this candidate to P000/Working Truth.
