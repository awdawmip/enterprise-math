# R762BE — Signed-port saturated triads: exact BRC counts and observer loss

**Date:** 2026-11-15. **Task:** `RS-X6-TRIADIC-CLOSURE-DYNAMICS`; publication `TP2-8B7E13C5904A2D6F1142`. **Status:** author-proved; exact checks; `NOT_REVIEWED`.

## Frozen source and model boundary

Frozen P000: `awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389:p000_reality_foundation.json`, `definitions/P000_DISCRETE_DIRECTION_TRIADIC_BALANCE_20260905.md`, `definitions/ENTERPRISE_X6_NATIVE_SPATIAL_CELL_TORSOR_20260905.md`. Task: `awdawmip/enterprise-math@d5eb171f15801f54c0659a2bbf4e42844ba2d527:research_tasks/RS_X6_TRIADIC_CLOSURE_DYNAMICS_20260906.md`. Precursor: [R762BD](https://github.com/awdawmip/enterprise-math/pull/2478) at `d728a81ea0bacd3ad11952ec451b08a020ca583c`.

P000 fixes signed six-axis spatial Cells, pairwise `PERP_E` with native 120 degrees, primitive stable arity three and an actual `TRIADIC_CLOSURE_E` requirement. The *native executable* signed Cell/Link/Port closure predicate has not been specified in the pinned premises. Here we investigate a fully declared **conditional signed incidence candidate**, not an added P000 axiom, native execution permission or classical vector-cancellation law.

At one Cell take `n` **named** equal-quanta on each of two distinct saturated unsigned axes `r,s`, and `n` further named quanta on axes outside `{r,s}`; each record retains its sign, identity and Port. A candidate triad consists of one record from each group and has sign-product **+1**. Thus each triad has three distinct unsigned native axes (hence pairwise `PERP_E`), but arbitrary independently flipped signs are not asserted to be a rotation symmetry. Complete states are **unordered partitions** of all `3n` named records into `n` permitted triads. The resulting positive BRC count is a *combinatorial count of sources*, not an amplitude.

Let `p` be the number of plus signs among `r` records, `q` among `s` records, and `t` among the `n` third-population records. Define `D_n^+(p,q,t)` to count complete named candidate partitions; `D_0^+(0,0,0)=1`, and values outside feasible nonnegative integer ranges are zero.

## BE1 — Exact full signed-port BRC multiplicity and feasibility

Put `x=(t-n+p+q)/2`. For all integers `n>=0`, a complete candidate partition exists **if and only if** `x` is an integer and

`max(0,p+q-n) <= x <= min(p,q)`.

Under those conditions,
`D_n^+(p,q,t) = C(p,x) C(n-p,q-x) q! (n-q)! t! (n-t)!`; otherwise `D_n^+=0`.

**Proof.** Each triad must include exactly one member from `r` and one from `s`, as each axis supplies `n` members and a triad cannot use an axis twice. Every unordered partition is therefore uniquely described by two bijections anchored at named `r` records: one matching them to named `s` records, the other to named third records. Set `x=#(r+,s+)`. The other sign-pair counts are `#(r+,s-)=p-x`, `#(r-,s+)=q-x`, and `#(r-,s-)=n-p-q+x`. The sign-product rule demands a positive third record exactly for a same-sign `r,s` pair, giving `t=n-p-q+2x`. All four cells are nonnegative precisely in the stated interval, proving necessity and feasibility. To count, choose `x` of the `p` positive `r` slots and `q-x` of the `n-p` negative `r` slots to receive positive `s` records; assign the actual named `s+` and `s-` records in `q!(n-q)!` ways. Assign the actual named third positive and negative records to their corresponding slots in `t!(n-t)!` ways. Each named complete partition appears once. QED.

For comparison, the predecessor's unsigned two-saturated-axis relation has `D_n=(n!)^2`; this candidate's sign ledger can restrict its support and multiplicity.

## BE2 — Exact visible pair / hidden signed Port fiber

Fix named `u` on axis `r` with sign `alpha` and named `v` on axis `s` with sign `beta`. For one named third record `w` with sign `gamma`, the number of complete candidate partitions in which `{u,v,w}` is one triad is

`N(u,v,w)=1_{alpha beta gamma=+1} D_{n-1}^+(p-1_{alpha=+}, q-1_{beta=+}, t-1_{gamma=+})`.

If axis `k` outside `{r,s}` has `b_{k,+}` positive and `b_{k,-}` negative named third records, then the number of full partitions in which `u,v` share a triad whose hidden member lies on axis `k` is

`L_k(u,v)=b_{k,alpha beta} D_{n-1}^+(p-1_{alpha=+}, q-1_{beta=+}, t-1_{alpha beta=+})`.

**Proof.** Removing the specified triad leaves two saturated axes of size `n-1` and a third population of size `n-1`; admissibility of residual triples obeys the same rule. Conversely, every allowed residual partition uniquely yields a full partition with the specified triad. Sum over exactly the `b_{k,alpha beta}` eligible, distinct named third records; the residual sign counts are independent of the selected name. QED. The precise axis-resolved support is therefore `{k:L_k(u,v)>0}`.

## BE3 — Globally feasible, smallest two-triad observer-loss witness

For `n=2`, choose two named `r=axis1` records `u+,u'+`, named `s=axis2` records `v+,v'-`, and remaining records `w+` on axis3 and `z-` on axis4. Here `p=2,q=1,t=1,x=1`, giving `D_2^+(2,1,1)=2>0`: there are two complete named partitions.

For the **fixed named visible pair** `(u+,v+)`, the R762BD *unsigned* saturated-axis filter allows both axis3 and axis4. Under the present signed candidate, `N(u,v,w+)=D_1^+(1,0,0)=1`, whereas `N(u,v,z-)=0`. Its positive BRC hidden-axis support is `{3}`, not `{3,4}`. This is a sign-sensitive counterexample to *promoting the unsigned observer quotient into this changed candidate's future signed-Port observer*; R762BD's original unsigned theorem and P000 remain unchanged.

## BE4 — Typed sufficient residual and covariance scope

The full-existence and total-positive-multiplicity observers factor exactly through `(n,p,q,t)` via BE1. For a fixed signed visible pair `(u,v)`, its axis-resolved full lift counts factor exactly through `(n,p,q,t,alpha,beta,(b_{k,+},b_{k,-})_k)` via BE2. For future queries of *named Link membership*, retain complete named partitions/branch identity: these coarse counts do not determine named pairings. All formulae are equivariant under simultaneous pure `S6` axis relabeling of the full typed records. No signed reversal symmetry or native V17/V29/V39 transport is inferred.

## Independent exact check and reproducibility

Run `node research_notes/portable_direct/R762BE_SIGNED_TRIAD_PARITY_VERIFY.js`. It enumerates *every pair of named bijections* (saturated `r` anchoring), for every canonical sign population `(p,q,t)` and `1<=n<=5`, with BigInt integer arithmetic. It counts each full admissible named partition and every specified visible `r[0],s[j],third[k]` pairing, independently comparing them with BE1 and BE2. All assertions passed: **440** sign-population profiles; **3,184,820** complete named bijection candidates; **142,976** admissible partition occurrences summed across profiles; **8,092** pair/third certificate checks. General `n` conclusions follow the symbolic proofs, not extrapolation of the finite checker. The evidence JSON retains per-`n` figures, exact witness and verification boundary. This is an author-side result, **NOT_REVIEWED**.

## Next native question

Retrieve or define the real signed `TRIADIC_CLOSURE_E` Cell/Link/Port permission and the V17 frame transport, V29 PASS/TRANSFER and V39 loop observation actions. Test whether the actual native relation admits an anchored matching law and whether its safe future observer quotient needs full signed/ordered BRC provenance or a smaller exact repair residual. P000 remains frozen; no Working Truth or Foundation promotion is asserted.
