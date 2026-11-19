# R762GF — X6 relative-depth cocycle, shortest diagonal holonomy, and a typed triadic Port/Link candidate

**Date:** 2026-11-19, Asia/Shanghai. **Task:** RS-X6-TRIADIC-CLOSURE-DYNAMICS, immutable publication TP2-8B7E13C5904A2D6F1142. **Original Researcher/SID:** EM-X6-3050F6 / MCP-4b2d70a97f594366a7c94a0f8b45df38. **Author-side verification:** PASS. **Independent review:** NOT_REVIEWED.

## Frozen science, scope, source distinctions

Scientific P000 input: awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389: `p000_reality_foundation.json`, `definitions/P000_DISCRETE_DIRECTION_TRIADIC_BALANCE_20260905.md`, `definitions/ENTERPRISE_X6_NATIVE_SPATIAL_CELL_TORSOR_20260905.md`. Taskbook/publication pin @857280d1012943290d141d1317179c40ec3cbdf8. Reuse R762GD three-STAR reconstruction and R762GE fixed-length depth-fiber theorem, original proof @7c33bc20db273f92f49c4aba51b6af46b891f0bf.

P000 fixes the native affine Cell torsor over Z^6, signed primitive coordinate adjacency ±e_i, the 120-degree native PERP_E relation on distinct positive native axes, and primitive stable-force arity three. Named Link/Port incidence, event order, BRC provenance and other packet fields are separately typed. This work distinguishes (A) the **established coordinate adjacency graph** from (B) a **new explicitly proposed** equal-quantum three-force Port-cycle completion. Coordinate paths are not automatically admissible stable TRIADIC_CLOSURE_E histories.

## Theorem 1 — exact relative-coordinate cocycle

Let D=(1,1,1,1,1,1), h(z)=min_i z_i, r(z)=z-h(z)D, so min r=0. For a signed primitive coordinate step s=εe_j, ε∈{−1,+1}, define

\[
c_s(r)=\min_i(r_i+\varepsilon\delta_{ij}),\qquad R_s(r)=r+\varepsilon e_j-c_s(r)D.
\]

Then, for every z in Z^6,

\[
\boxed{r(z+s)=R_s(r(z)),\quad h(z+s)=h(z)+c_s(r(z)).}
\]

The correction c is a local integer taking values in {−1,0,+1}. Explicitly:

- c_{−e_j}(r)=−1 iff r_j=0, otherwise 0.
- c_{+e_j}(r)=+1 iff j is the unique zero coordinate of r, otherwise 0.

**Proof.** Substitute z=r+hD into min(z+s). A negative step produces a −1 precisely if the moved coordinate was zero. A positive step raises the minimum from zero to one precisely if that coordinate was the only zero. Subtract the new minimum for the first equation. For a word w=(s_1,...,s_m), iteration yields

\[
\boxed{h_m=h_0+\sum_{t=1}^m c_{s_t}(r_{t-1}),\quad r_t=R_{s_t}(r_{t-1}).}
\]

This is an exact discrete path cocycle. Common depth is a composite coordinate within six-dimensional X6, **not** an additional spatial axis.

## Theorem 2 — a full relative trajectory recovers the signed coordinate word

For every normalized r, its twelve successors R_{±e_j}(r) are pairwise distinct. Consequently the ordered time-labelled relative trajectory (r_0,...,r_m) determines the entire ordered signed-coordinate word, and h_0 plus the cocycle recovers the complete Cell trajectory.

**Proof.** R_s(r)=R_t(r) implies s−t=(c_s−c_t)D. The left side has support on at most two axes. A nonzero multiple of D has support on six axes, so c_s=c_t and s=t. Reconstruct every step from consecutive relative observations.

**BRC typing:** this recovers the signed step letters and their order, not source IDs or independent named ports/links/force quanta absent from the coordinate words. Endpoint-only r does not supply the full trajectory.

## Theorem 3 — shortest nonzero diagonal holonomy

A coordinate word is a relative loop when r(z+w)=r(z). Its displacement then equals kD for some k∈Z, with accumulated c_s=k. If k≠0, its length is at least 6|k| since each of six coordinates must change by k. This bound is attained by the six-step word (+e_1,+e_2,+e_3,+e_4,+e_5,+e_6) for k=1, and the negative analog for k=−1. Thus the attainable loop-holonomy subgroup is Z.

No global potential F(r) satisfies c_s(r)=F(R_s(r))−F(r) for every signed edge: summing this identity around the above closed relative loop would give 0=1. In particular, arbitrary-long absolute Cell recovery cannot use a memoryless endpoint-only correction field.

For the **uniform positive 12-letter BRC** at exactly length six, an exact count of ordered source words returning to the same *relative* state is:

| Δh | words |
|---:|---:|
| −1 | 720 |
| 0 | 19920 |
| +1 | 720 |
| **Total** | **21360** |

The k=±1 cases require one of each axis with uniform sign, giving 6! paths per sign. The k=0 words have exhaustive distributions: a single axis used 3 times per sign, 6·C(6,3)=120; a four-step axis plus a different two-step axis, (6·5)·6!/(2!2!)=5400; or three axes each once in each sign, C(6,3)·6!=14400. The total is 19920. Consequently

\[
\boxed{\mathbb P(r_6=r_0)=21360/12^6,\quad
\mathbb P(\Delta h\ne0\mid r_6=r_0)=1440/21360=6/89.}
\]

These are exact **positive BRC counts**, not signed-force cancellation. They express the distinction between spatial return, relative return and a time-labelled event return.

## Construction 4 — an explicit, typed P000-compatible candidate triadic event

Define three *positive-axis*, equal-nonzero-quantum force units attached to one X6 Cell z, with distinct axis labels i,j,k and three named ports p0,p1,p2. Retain the three directed links p0→p1, p1→p2, p2→p0. Define candidate `CYCLE_TRIAD_E` to mean exactly this equal-quantum named 3-cycle with distinct axes (hence pairwise PERP_E=120 degrees). Removing a link, repeating an axis, changing a quantum or leaving only two forces destroys this **candidate** primitive closure.

Define a candidate time-ordered event transport that reattaches the linked triad at z+e_i+e_j+e_k, increments a separately typed event-order counter, and records the ordered three primitive steps (i,j,k) and full Link/Port/source labels in the BRC path. The displacement is **composite native transport**: it is not a new primitive diagonal segment, and it need not return to the same Cell. It also does not define equilibrium as Euclidean vector-sum-zero.

For each axis permutation σ∈S6, `σ U(z,i,j,k)=U(σz,σi,σj,σk)` and the candidate cycle predicate is preserved. This follows from permutation-equivariance of coordinate addition, distinct axes, equal quanta and the named port cycle. Therefore the construction supplies a coherent **existence example** for a Cell-attached three-force relational update. Its particular Link/Port gate is **proposed**, not claimed as already canonical TRIADIC_CLOSURE_E. Other signed combinations, force magnitudes and incidence laws remain open.

## Theorem 5 — sharp operation-scope distinction for common depth

**Language A (self-contained relative observation).** Allow only the candidate internal triad event, its composite signed-coordinate trace, and outputs through r(z) together with separately retained named internal ports/links and source annotations. Every enabled operation and output commutes with diagonal translations z↦z+kD (holding the event labels fixed). By induction all finite future operations descend to the quotient Z^6/ZD. For this declared language, r plus the retained non-coordinate fields is a sufficient operational state, even though h remains necessary to reconstruct a raw Cell address without an initial anchor.

**Language B (external named Cell).** Add another named Cell a and a prospective Link incidence gate `LINK_TO_a(z)⇔z−a=e_1`. The gate is invariant under **simultaneous** translation of z and a, so no distinguished global origin is introduced. Let a=0, z=e_1 and z'=e_1+D. Then r(z)=r(z'), with identical internal Port-cycle data, while LINK_TO_a(z) is true and LINK_TO_a(z') is false. The **joint** future Link operation is not constant on the r fiber when a is retained. An explicit depth or equivalent joint relation is necessary.

Both are P000-compatible **candidate legal-operation languages**. Therefore the frozen six-axis coordinate axioms and three-STAR observer alone do not decide whether common depth is redundant for the full future native Cell/Link/Port vocabulary. An exact operation-specific descent certificate or retained relation is required; neither candidate is asserted to be the final licensed native event system.

## Verification, limitations and next step

`R762GF_VERIFY.py` checks all 665 normalized r in {0,1,2}^6 and 7980 signed relative transitions (with 3 raw depth shifts each); integer endpoint dynamic programming at m=1..6 verifies the full BRC masses, including 720/19920/720, separately from the above combinatorial proof; all 120 ordered positive distinct triads and 720 axis permutations give 86,400 covariance checks; it tests the named-anchor counterexample. `R762GF_EVIDENCE.json` holds exact counts. All checks PASS. The general cocycle, edge injectivity and loop length are proved for arbitrary integer coordinates. Independent review: NOT_REVIEWED.

**Next scientific unit:** extract the actual frozen permitted TRIADIC_CLOSURE_E Cell/Link/Port event vocabulary as soon as a precise predicate exists; test whether any legal future gate distinguishes the R762GD complementary diagonal pairs and quantify the smallest extra joint state. Keep the factor-nine q9 full-vector period/lift problem separate and retain original BRC source/provenance. No P000, Foundation, Result or Working Truth promotion is asserted.
