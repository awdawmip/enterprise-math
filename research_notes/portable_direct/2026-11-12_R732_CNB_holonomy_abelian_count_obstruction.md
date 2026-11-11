# R732 — CNB 非交换残差与 V29 累计计数的精确三态修复

2026-11-12 · Author-side exact mathematical result · Parent: `RS-X6-TRIADIC-CLOSURE-DYNAMICS` · Review: UNREVIEWED.

## Frozen science and scoped interface

Frozen task science remains `awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389` (P000 V5, X6 signed Cell, joint observer and primitive three-force balance). Derived abstract carriers use R730 `8fdfef5e3f2097d9e6ebb29682b2b81a6ea0247a`: two 15-arc masks A=`211733226574`, B=`5363347296468`, on three-subsets of five accessible labels 0–4, embedded as a subcarrier of six-axis X6. The V17 slot transition transfers the vacated slot to the entering label. The separate candidate V29 PASS interface is sourced to `research_notes/X6_NETWORK_EVENT_LEDGER_AND_CONTRAST_TRANSDUCER_V29_20260906.md` at `30fb16d39465708fd1b54c70a58d06ad20f310f8` and R731/R731b at `2cc59b2353a16f57c1452e1e87d2faf08467e2cd`; it does not alter the frozen task inputs.

A rooted cyclic-nonbacktracking (CNB) history is `012=S0,S1,...,Sm=012` with every directed arc allowed and `S_(i-1)!=S_(i+1)` cyclically, seam included. The named holonomy `h(w)∈S3` is the final list of original slot IDs ordered by the root triad `012`. The exact nonnegative arc-count vector is `N(w)=(# occurrences of e)_e∈N_0^15`. Each static per-arc V29 PASS word contributes a fixed nonnegative port-count increment `C_e`, so its final cumulative ledger increment is `ΔM(w)=Σ_e N_e(w) C_e`.

## Theorem 1 — Six-step noncommuting CNB witness for each optimum carrier

Use these valid length-three excursions, each rooted and closed at 012:

| Carrier | X | Y | h(X) | h(Y) |
|---|---|---|---|---|
| A | 012>023>013>012 | 012>023>123>012 | 021 | 102 |
| B | 012>023>013>012 | 012>123>013>012 | 021 | 210 |

All concatenations `XY` and `YX` satisfy cyclic nonbacktracking. Their ordered arc multisets coincide exactly because `N(XY)=N(X)+N(Y)=N(YX)`. Yet:

| Carrier | h(XY) | h(YX) | R731b four-port PASS events per history |
|---|---|---|---|
| A | 201 | 120 | 12 |
| B | 120 | 201 | 12 |

Hence no deterministic function of the complete arc-count vector, or of **any static additive per-arc V29 cumulative port-count ledger**, can recover named V17 holonomy on all allowed histories. This statement applies regardless of the number of PASS ports or length of a fixed per-arc code. It is a positive BRC history witness, not an amplitude-cancellation argument.

**Proof.** Adding arc multisets commutes, whereas the two noncommuting V17 excursion permutations compose in opposite orders. The explicit strings above have legal adjacency, legal seam and distinct transported slot permutations. Any purported map from counts to holonomy would assign two distinct outputs to the same input. ∎

The exact verifier exhaustively enumerates all rooted CNB histories of lengths 1–6 for A and B. For lengths 1–5 each arc-count fiber carries at most one named holonomy; at length 6 the first differing-holonomy collision appears. The minimum is scoped to these carriers and the fixed root 012.

## Theorem 2 — One identical count fiber contains all three even holonomies

Consider all six permutations of the four-excursion multiset `{X,X,Y,Y}`:

| Word | Carrier A | Carrier B |
|---|---|---|
| XXYY | 012 | 012 |
| XYXY | 120 | 201 |
| XYYX | 012 | 012 |
| YXXY | 012 | 012 |
| YXYX | 201 | 120 |
| YYXX | 012 | 012 |

Every word is a rooted length-12 CNB history and has precisely the **same** `N=2N(X)+2N(Y)`. Consequently, every static additive per-arc V29 cumulative count ledger gives the same final `M` for all six histories. The three even permutations `012,120,201` are all realized in this single count fiber. Any additional finite register enabling named-holonomy recovery from retained arc counts therefore needs at least **three distinguishable states**. ∎

## Theorem 3 — Exactly three residual states suffice over an edge-count-resolving observer

Declare the retained observer to be `(current triad, N)`, or its injective equivalent: the **five-port, one-PASS-per-arc** V29 encoding from R731b has 20 distinct off-diagonal PASS labels and assigns 15 distinct labels, allowing exact recovery of `N`.

Each arc `e` induces a local slot permutation `p_e∈S3`, from sorting its source/target triads and transferring the outgoing slot to the incoming label. Since permutation sign is a homomorphism, the full named holonomy parity is an exact **count-only** function:
\[
\epsilon(w)=\operatorname{parity}(h(w))
=\left(\sum_e N_e(w)\operatorname{parity}(p_e)\right)\bmod 2.
\]

Choose a fixed three-cycle `c` and transposition `t` with `S3=C3 ⋊ C2`. Each holonomy uniquely decomposes as `h=c^k t^\epsilon`, with `k∈{0,1,2}`. Keep the three-valued register `k`; update it deterministically under the exact V17 local permutation composition, using the parity recovered from the updated `N`. Thus `(current triad,N,k)` recovers named holonomy after **every finite valid history**, with no length bound.

Theorem 2 supplies a three-state lower bound on a single reachable count fiber, so the repair is **exactly minimal at cardinality three** for this declared count-resolving observer and named-holonomy output. The V17 noncommutative information retained is the three-cycle component; the sign is already supplied by the additive arc counts.

For the four-port/two-PASS R731b code, the same three-state **lower bound** holds, while the exact minimal full repair additionally depends on whether its 12 final port counters recover all relevant arc counts. The three-state sufficiency statement above uses `N` or a count-injective encoding of it.

## Scope-typed future-observer consequence

A candidate time/order-dependent scheduler that queries whether the named slot relation equals e.g. `120` distinguishes Theorem 1's histories, although their full cumulative V29 counters coincide. It must retain ordered event provenance or the declared sufficient BRC residual. This supplies a concrete memory condition for the next connection to native `PRIMITIVE_FORCE_QUANTUM` and `TRIADIC_CLOSURE_E`. P000's triadic event incidence and native signed-axis force certificate have not yet been specified by the abstract carriers.

## Reproducible exact verification

Run `node R732_BRC_ABELIANIZATION_VERIFY.js > R732_BRC_ABELIANIZATION_RESULTS.json`. The standalone script reconstructs the 60-edge universe and the two 15-edge masks, checks cyclic seams and 6- and 12-arc paths, propagates V17 slot IDs, checks 4-port/two-PASS and 5-port/one-PASS cumulative ledgers, and exhaustively tests every rooted CNB history of lengths 1–6 for both carriers. Exact finite enumeration statistics:

| Length | A histories | A count fibers | A max holonomies per fiber | B histories | B count fibers | B max holonomies per fiber |
|---:|---:|---:|---:|---:|---:|---:|
| 1 | 0 | 0 | 0 | 0 | 0 | 0 |
| 2 | 0 | 0 | 0 | 0 | 0 | 0 |
| 3 | 3 | 3 | 1 | 3 | 3 | 1 |
| 4 | 7 | 7 | 1 | 7 | 7 | 1 |
| 5 | 8 | 8 | 1 | 8 | 8 | 1 |
| 6 | 13 | 10 | 2 | 14 | 11 | 2 |

The local Node.js verifier returned `status=PASS`; the arbitrary-length statement follows the group decomposition and sign identity, rather than finite extrapolation. The next scientific unit is to define a native signed six-axis force-triad incidence, a V29 event scheduler whose legality consumes the appropriate BRC residual, and a rotation-covariant witness under the P000 closure predicate.

**Admission:** independent mathematical review, native CLAIM/Result and a P000 force-event construction remain to be completed.