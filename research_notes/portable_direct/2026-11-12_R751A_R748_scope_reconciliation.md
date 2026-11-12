# R751A — Exact R748 scope reconciliation after native Run checkpoint 4

The R748 artifact is PR #2163, not the R747B adaptive selector. Its exact model has 60 unordered signed-Port pair vertices and 960 directed edges, adjacency requiring one identical signed port and three distinct unsigned axes in the union. Its deterministic fixed-source C1 shift on directed edges is (v,w) -> (w, v △ w), with exact period 3. Its independent resampling Markov kernel is P=A/16, degree 16, and its all-horizon source residual is a different question from V1R's C12 internal law.

Therefore R751's support-orbit obstruction applies to the R747 **one-unused-axis replacement grammar**, not automatically to the R748 fixed-source C1 three-cycle. For a directed edge v={p,q}, w={q,r}, the fixed-source C1 shift has triadic union support {p,q,r} before and after, so it is support-preserving. R751's obstruction cannot rule this shift out. The R748 *resampling* graph step can change the underlying three-port source; that must be separately tested with provenance.

A sharper remaining test is to compare the R748 fixed-source shift (period 3 on 960 directed edges) with V1R's signed-frame C12 update (period 12 on 1920 mode states). They are not literally the same typed map; a possible quotient/lift must be specified and checked for successor commutation and native permission. No such identification or Cell/Link/Port coupling is asserted here.

Source: awdawmip/enterprise-math PR #2163, files R748_X6_SIGNED_PAIR_BRC_SPECTRUM_THEOREM_20261112.md and HANDOFF.md. R751 exact support obstruction remains valid only under its stated one-axis replacement hypothesis. R750 correction of R749 closure-truth counterexample remains in force.
