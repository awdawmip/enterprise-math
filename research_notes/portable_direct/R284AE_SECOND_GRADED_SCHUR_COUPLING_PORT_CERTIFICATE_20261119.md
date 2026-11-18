# R284AE — Second graded Schur coupling: an exact certificate after the first matroid obstruction

**Date:** 2026-11-19. **Status:** AUTHOR_PROVED / EXACT_RATIONAL_CHECK_PASSED / NOT_REVIEWED. **Dependencies:** R284AD (two-matroid first-order/nullity-order certificate), R284AC (rank-defect law), R284AB (stable feedback Port embedding). Frozen scientific pin: `43ec6098b1330ae86d0a7863be336c5d97f6ef34`. All row/column and edit indices remain named and sourced. This is an auxiliary finite Port observer in the Heartbeat X6 substrate, not a separate native lower-dimensional geometry or BRC–Shor computation.

## A universal formula for the next possible degree

Let `A` be an `n×n` matrix over a characteristic-zero field, of rank `r≥1` and nullity `s=n−r≥1`. Let `A(t)=A+\sum_e t_eu_ev_e^T` with independent named rank-one update parameters. Use the exact row/column pivoting and block elimination of R284AD to obtain
\[
S A T=\begin{pmatrix}B&0\\0&0_s\end{pmatrix},\quad
S A(t) T =
\begin{pmatrix}
B+X(t)&Y(t)\\
Z(t)&M(t)
\end{pmatrix},
\]
where `B` is nonsingular `r×r`, `X` is `r×r`, `Y` is `r×s`, `Z` is `s×r`, `M` is `s×s`; each perturbation block is homogeneous linear in the **original** independently named parameters. Set `κ=det(S)^{-1}det(T)^{-1}det B≠0`.

**Theorem AE1 (the first two homogeneous components).** For all such pencils,
\[
\boxed{[\det A(t)]_s=\kappa\det M(t)}
\]
and
\[
\boxed{[\det A(t)]_{s+1}
=\kappa\left(
\operatorname{tr}(B^{-1}X(t))\det M(t)
-\operatorname{tr}\left(\operatorname{adj}(M(t))\,Z(t)B^{-1}Y(t)\right)
\right).}
\]
Both are exact polynomial identities, including `s=1`, for which `adj([m])=[1]`.

**Proof.** Exact block Schur factorization near the constant invertible `B` gives the formal power-series identity
\[
\det A(t)=\det(S)^{-1}\det(T)^{-1}
\det(B+X)\det\big(M-Z(B+X)^{-1}Y\big).
\]
The first prefactor is
\[
\det(B+X)=\det B\big(1+\operatorname{tr}(B^{-1}X)+O(t^2)\big).
\]
The lower Schur factor begins with `M` (total degree 1); its degree-2 term is `-ZB^{-1}Y`. In a determinant of size `s`, choosing exactly one degree-2 entry and `s−1` degree-1 entries gives the degree-`s+1` contribution `-tr(adj(M)ZB^{-1}Y)`. The other degree-`s+1` contribution is the degree-1 correction in the upper prefactor multiplied by `det M`. Products of two or more degree-2 lower corrections and terms of degree three or more contribute only at degree `s+2` and above. The formulas follow. QED.

**Corollary AE2 (when the first possible degree vanishes).** If R284AD's exact dual matroid certificate proves `det M(t)\equiv0`, then
\[
[\det A(t)]_{s+1}
=-\kappa\operatorname{tr}\big(\operatorname{adj}(M) ZB^{-1}Y\big).
\]
Consequently, a nonzero second graded expression is a rigorous witness of **delayed joint activation**. A zero expression rules out degree `s+1` only; it is not a certificate for all higher orders. No signed branch/edge association may be discarded merely from these first two vanished levels.

## Corank-one exact bilinear interaction table

For `s=1`, if all degree-one coefficients vanish, `M(t)\equiv0`, so
\[
\boxed{[\det A(t)]_2=-\kappa Z(t)B^{-1}Y(t).}
\]
Write `Z(t)=\sum_e t_e z_e` and `Y(t)=\sum_e t_e y_e`. For distinct original edit names `e,f`,
\[
\boxed{[t_et_f]\det A(t)
=-\kappa(z_e B^{-1}y_f+z_f B^{-1}y_e).}
\]
The diagonal `t_e^2` coefficients vanish for independently parameterized rank-one single-edge edits; this also follows directly from determinant multi-affinity in each edit parameter. Precomputing `B^{-1}y_f` then testing the cross bilinear products gives an exact `O(m^2r+mr^2+r^3)` arithmetic-operation bound **after the pivot decomposition**, excluding pivot search, exact coefficient bit growth and input/output costs. It is a scoped degree-two detector rather than an unrestricted full determinant identity test.

For R284AD's **strictly positive** baseline `C_0=(1/192)[[1,1,1],[1,2,1],[1,1,1]]` and edits `tE_{21}+uE_{12}`, the left and right nullspace projections make `M(t,u)=0`, while
\[
-\kappa ZB^{-1}Y=-tu/192.
\]
This recovers the exact delayed Port determinant from two matrix-vector coupling channels without expanding the full polynomial. Its previously checked strongly connected, nonnegative, strictly substochastic Port embedding inherits the nonzero quadratic interaction via R284AB's feedback-robust Schur formula.

## Reproducible checks and limitations

Companion script: `research_notes/portable_direct/R284AE_schur_next_order_checker.py`; exact result: `research_notes/portable_direct/R284AE_schur_next_order_verification.json`. Python 3 + SymPy exact rationals, fixed seed `284020`; 40 positive rank-deficient baselines across `n=2..5` and `1≤r<n`, four per rank pair, with up to four independent named single-edge edits. It obtains the two graded pieces independently from a direct symbolic determinant and the stated Schur formulas, and verifies cancellation of repeated-variable powers. Results: 40/40 leading-degree identities, 40/40 next-degree identities, 80 multi-affinity checks, 23 cases with a nonzero next-degree part and one random case without a leading-degree part but with a nonzero next-degree part. The exact positive Port quadratic witness is separately checked. All checks PASS.

The displayed universal proof is algebraic; finite checks support the implementation and examples. The general computational complexity of a full recursive higher-degree solver, physical correspondence, and independent mathematical review remain unresolved.

## Open next scientific unit

Derive and experimentally discriminate a **rank-adaptive, sparse Schur-jet recursion** through degree `s+j`, measuring its actual bit complexity against R284Y complementary-minor enumeration. Determine when a localized zero of the first two graded Port readings is safe to compress under explicitly declared future edit compositions; require a complete observer-fiber certificate before asserting full redundancy. Preserve original named edges, feedback loops and mixed signed coefficients.

**Authorship/source state:** original Researcher `EM-DIRECT-E6B1DD`, session `MCP-8487128c846440d1952bfc6fa44aeb86`; portable author proof, no formal CLAIM/Result/independent Review.
