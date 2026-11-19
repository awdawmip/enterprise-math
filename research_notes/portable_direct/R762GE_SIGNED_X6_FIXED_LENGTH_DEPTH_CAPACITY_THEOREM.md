# R762GE — Sharp fixed-length common-depth capacity for signed X6 BRC

**Date:** 2026-11-19. **Task:** RS-X6-TRIADIC-CLOSURE-DYNAMICS, immutable publication TP2-8B7E13C5904A2D6F1142. **Author-side mathematics; independent review:** NOT_REVIEWED. Original researcher provenance: EM-X6-3050F6 / MCP-4b2d70a97f594366a7c94a0f8b45df38.

## Premises, freeze and exact type

Scientific inputs retain the taskbook pin awdawmip/enterprise-math@857280d1012943290d141d1317179c40ec3cbdf8:research_tasks/RS_X6_TRIADIC_CLOSURE_DYNAMICS_20260906.md and P000 source commit a72226e2430ffa4786321ac86e7f0c599d5f0389: p000_reality_foundation.json, definitions/P000_DISCRETE_DIRECTION_TRIADIC_BALANCE_20260905.md, definitions/ENTERPRISE_X6_NATIVE_SPATIAL_CELL_TORSOR_20260905.md. Reuse the three-STAR integral reconstruction theorem in R762GD@2f95e44714101ddc740362fc7eee18fc3158b5fe.

The native X6 signed Cell coordinate carrier is a *chart of an affine torsor* over Z^6. The native primitive coordinate adjacency has twelve step labels (+/-)e_i for i=1,...,6. P000 keeps six native spatial axes, an independent ordered time dimension when needed, PERP_E=120 degrees, and nonzero primitive stable force arity three. Neither an X6 step nor the following coordinate-path BRC is asserted to be a stable TRIADIC_CLOSURE_E event.

An ordered length-m signed coordinate path w, m >= 0, is a word of m letters from the twelve labels and has endpoint z(w)=sum_t epsilon_t e_{i_t}. There are exactly 12^m distinguishable source words (including provenance/order). Define D=(1,1,1,1,1,1), r=can6(z)=z-min(z)D and h=min(z), so z=r+hD.

The four K4 STAR coordinate-selection sets (zero-based indices) are (0,1,2), (0,3,4), (1,3,5), (2,4,5). The joint minimum-zero observations of *any three* determine r by R762GD. These are three-axis observers within the full six-dimensional world, not standalone native planes and not complete Link/Port incidence observations. We now assume the readout additionally retains path length m, but not the full signed word.

## Theorem 1. Exact length-m depth fiber

For each r in Z^6 with nonnegative entries and minimum zero, define s(r)=sum_i r_i, f_r(h)=sum_i |r_i+h| and H_m(r)={h in Z: there exists an ordered signed coordinate word of length m ending at r+hD}. Then:

\[
\boxed{
H_m(r)=
\begin{cases}
\{h\in\mathbb Z:f_r(h)\le m\},&m\equiv s(r)\pmod 2,\\
\varnothing,&m\not\equiv s(r)\pmod 2.
\end{cases}
}
\]

When H_m(r) is nonempty it is a **finite consecutive interval of integers**.

*Proof.* The shortest signed coordinate word ending at a given z takes ||z||_1 = sum_i |z_i| steps. Any additional *even* number of steps is added as adjacent backtracking pairs +e_j,-e_j; a path of exact length m exists precisely when ||z||_1 <= m and m-||z||_1 is even. As |v|=v (mod 2), f_r(h) = s(r)+6h = s(r) (mod 2), independent of h. This yields the formula. The function f_r(h) is convex on the real line and diverges when h tends to either infinity; its integer sublevel set is finite and consecutive. QED.

## Theorem 2. Sharp maximum hidden-depth count and conditional encoding

For every fixed m>=0,

\[
\boxed{\max_{\text{reachable }r}|H_m(r)|=\lfloor m/3\rfloor+1.}
\]

Therefore, given the exact length and the three-STAR relative readout, a fixed maximum-width **conditional endpoint-repair field** requires and suffices with

\[
\boxed{B_{\mathrm{depth}}(m)=\left\lceil\log_2(\lfloor m/3\rfloor+1)\right\rceil\ \text{bits}.}
\]

The bound concerns the worst relative-coordinate fiber, **not** an optimal joint code for all readouts and not full source-word encoding.

*Proof of upper bound.* Let h_- and h_+ denote the extremes of any nonempty H_m(r). For each i, |r_i+h_-|+|r_i+h_+| >= h_+-h_-. Summing over six axes gives

\[
2m\ge f_r(h_-)+f_r(h_+)\ge 6(h_+-h_-).
\]

Thus h_+-h_- <= floor(m/3). By Theorem 1 every integer between them is feasible, so there are at most floor(m/3)+1 possibilities.

*Sharp construction.* Write m=3a+b with a=floor(m/3) and 0<=b<=2. Take

\[
r=(0,0,0,a,a,a+b).
\]

Then s(r)=m and f_r(0)=f_r(-a)=m. Convexity implies f_r(h)<=m for each integer -a<=h<=0, and all these h have the correct parity for exact length-m paths. There are a+1 depths. The upper bound excludes any others in this relative fiber. This argument includes m=0,1,2. QED.

At m=3 the maximum depth ambiguity is two, agreeing with the complementary signed-triad pairs from R762GD. The theorem extends the quantified loss to **arbitrary signed path lengths including backtracks**.

## Theorem 3. Signed-branch imbalance restores the full Cell endpoint

Let p be the number of positive signed-axis letters in a length-m word, so the number of negative letters is m-p. Its signed step imbalance equals

\[
\delta=p-(m-p)=2p-m=\sum_i z_i.
\]

Since z=r+hD, the full endpoint is reconstructed from (r,m,p) by the *integer* equation

\[
\boxed{h=\frac{2p-m-s(r)}{6},\qquad z=r+hD.}
\]

This identity holds for every valid signed coordinate word; a proposed combination with nonintegral h is invalid. Given m and relative r, retaining p is sufficient for the *spatial endpoint* but need not be bit-optimal; Theorem 2 gives the tight maximum conditional depth-field bit width. Neither method repairs named Port/Link relationships or the ordered BRC source trace.

For a positive uniform twelve-branch BRC, write N_m(z) for the number of ordered length-m words ending at z (the signed-axis count formula already defined in the pinned X6 torsor source). Disjoint exact path counting gives

\[
P_m(r)=12^{-m}\sum_{h\in H_m(r)}N_m(r+hD),
\]

and, setting h=(2p-m-s(r))/6,

\[
P_m(r,p)=\begin{cases}12^{-m}N_m(r+hD),& h\in H_m(r)\text{ and integral},\\0,&\text{otherwise}.\end{cases}
\]

These are exact BRC **positive masses**; no signed-force cancellation is inferred. A simple source-order witness is the two words (+e_1,+e_2) and (+e_2,+e_1): their endpoints and (r,m,p) coincide while their final input-axis labels differ. A *hypothetical* history-sensitive port gate could distinguish them; its legality is not established by this coordinate result.

## Validation, limits and remaining question

Companion R762GE_VERIFY.py uses integer-only standard-library dynamic programming to enumerate all reachable endpoints and accumulate exact signed source-word multiplicity for m=0,...,8. It independently checks the relative-depth fiber formula, all four choices of three STAR observer reconstructions for each endpoint, the signed-positive count repair, the upper bound and sharp witness, and the conservation of exactly 12^m ordered words. At m=8 it covers 26,577 full endpoints, 15,069 relative classes and 429,981,696 ordered words by integer counts; every checked length passes. General statements are established by the proofs above, not extrapolated from this finite domain. Companion JSON records the exact checked scope. Reviewer: NOT_REVIEWED; this is not a formally admitted Result or P000 update.

The remaining *native dynamics* dependency is material: frozen P000 fixes primitive arity, canonical equal-quantum triadic closure and the Cell coordinate laws, but leaves detailed signed Cell/Link/Port permitted transitions and the full TRIADIC_CLOSURE_E predicate under construction. Neither the twelve coordinate-step words nor a depth-sensitive future gate are automatically legal stable force events. The current note proves a precise observer-compression theorem within the pinned coordinate adjacency model. Fourth STAR non-coordinate carrier relations and full path provenance are retained.

**Next test:** derive or explicitly construct a permitted typed signed triadic event predicate with Cell attachment and named Port/Link incidence respecting P000. Then test on the R762GD complementary pairs whether each permitted future gate factors through three-STAR relative coordinates, or whether the exact depth field from this theorem is operationally required. Preserve the independent q9 full-vector period/lift research frontier.
