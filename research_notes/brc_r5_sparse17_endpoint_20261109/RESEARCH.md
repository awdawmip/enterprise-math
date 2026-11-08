# R5 — Endpoint-aware sparse martingale transport: 17-edge universal certificate bound

**Date:** 2026-11-09 Asia/Shanghai. **Status:** AUTHOR_PROVED / EXACT_FRACTION_EXECUTED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY.

**Scientific inputs unchanged:** frozen GK a01383f825ef9d43b4b754254303298c64041568 and EM 86149263e38c22292c9def1e0f69092efa1be77e. Current behavioral-control snapshots read separately: GK main 28b7de917fe2feb069d5eb3189aae7019f6936df and EM main 9857ff2136106e6c0954da609170291a30497c80. P000 and the protected ACTIVE worldview are not modified. The scope is the frozen seven-node P/Q-BRC terminal-observer statistical model, not a native X6 dynamical claim.

## Result

Let n >= 2 and let r_0 < ... < r_(n-1) be distinct real likelihood ratios common to target rows and source columns. Suppose there exists a nonnegative n-by-n array E satisfying

\[
\sum_j E_{ij}=\mu_i,\qquad
\sum_i E_{ij}=\nu_j,\qquad
\sum_i r_i E_{ij}=r_j\nu_j.
\tag{1}
\]

**Theorem:** There exists another E satisfying the same equalities with **at most 3n-4 positive entries**. For the R5 likelihood-ratio grid

\[
r=(1/10,\ 1/2,\ 3/4,\ 1,\ 5/4,\ 3/2,\ 19/10)
\]

the universal upper bound is **17**, improving the 19-edge author-side bound of draft PR #1832 (head 9132b58398d13d0707b0cbb76b68cb10382b620e). If the grid and marginals are rational, the sparse witness can be chosen rational and constructed by finite rational row reduction from an exact rational feasible coupling.

The source and target marginals, likelihood-ratio-weighted column moments and all randomized terminal-declaration observations are preserved. If an R5 source and lawful seedless target already match both stopping times, the reduced kernel therefore preserves all four R5 observations (e_P,e_Q,T_P,T_Q). This is a transport certificate compression result and does not assume or reprove the predecessor's full-parameter feasibility claims.

## Proof — four independent row relations

**Forced extreme columns.** At the lowest source ratio r_0, the column mass and weighted moment equations give

\[
\sum_i(r_i-r_0)E_{i0}=0.
\]

All summands are nonnegative, and the coefficients for i>0 are strictly positive; hence E_(i,0)=0 for i>0. At the highest source ratio r_(n-1), the same reasoning yields E_(i,n-1)=0 for i<n-1. This remains valid for zero endpoint source mass.

**Restricted matrix rank.** Restrict the linear system (1) to the allowed coordinates. There are 3n displayed rows but at least four linearly independent row dependencies: total row mass equals total column mass; weighted total row mass equals total column moment; and, on the restricted coordinates, the lowest and highest column-moment rows equal respectively r_0 and r_(n-1) times their own column-mass rows. Independence follows because the first two dependencies have row coefficients 1 and r_i (linearly independent since r_i are distinct), while the latter two independently involve the two endpoint column-moment coordinates. Hence

\[
\operatorname{rank}(A_{\mathrm{allowed}})\le 3n-4.
\]

**Existence and exact algorithm.** The nonempty nonnegative feasible set with prescribed finite total mass is a bounded polytope. At any extreme point the positive columns of its constraint matrix are independent (otherwise a small signed kernel perturbation would preserve feasibility in both directions). Thus at most 3n-4 entries are positive. Given an exact rational feasible E with more entries, select any 3n-3 positive allowed columns; they are linearly dependent. Exact Gaussian elimination produces a nonzero rational null vector d. This d has both positive and negative components since all row sums of its perturbation vanish. Advance along d until the first negative-direction coordinate reaches zero. All equations, nonnegativity and exact observer values persist. Each round removes at least one support edge; no new edge is created. The endpoint restriction leaves at most n(n-2)+2 positive positions initially, so at most (n-2)(n-3) elimination rounds suffice; n=7 gives **at most 20 rounds** from a maximally dense allowed support. For rational problem data, the nonempty rational polytope also admits a rational basic feasible point, ensuring rational existence without requiring an initially supplied rational E.

**Scope:** This is a provable universal upper bound for a common strictly ordered LR grid; optimality for the R5 lawful physical-flow subclass, bit complexity, and any stronger theorem about hidden branch histories remain separate questions.

## Reproducible exact experiments

The self-contained attached VERIFY_17.py uses Python standard-library Fraction only. Executed locally with python -S and exit code 0. Its exact rank computation finds rank 17 for all 37 permitted edge positions. Its independent synthetic seven-node martingale example has 37 positive edges; null-vector reduction reaches 17 edges after 20 rounds, preserving all 21 row/column/weighted-column equalities exactly. Read EXACT_OUTPUT.txt.

A separate expanded local Fraction checker also rechecked the **physical nonseedless-source/seedless-target 11-edge matrix already persisted in draft PR #1832** (source x=(1,1/6,1,0,31/240,0,1/60), previously published target and entries). It stays at 11 edges; no duplicate witness bytes are claimed as new. Exact grid regressions n=3,4,5,6,8 also passed. Those regressions test implementation; the all-real theorem rests on the exact rank and endpoint argument.

**BRC observation discipline:** The carrier is the full Q-mass transport graph, ordered LR labels and weighted column moments, not only a total count. Null-direction deletions preserve precisely the defined terminal observation class. There is no broad claim that nonobserved FULL_HIST branch provenance is reconstructed.

**Literature context:** Hobson and Norgilas, *The left-curtain martingale coupling in the presence of atoms*, Annals of Applied Probability 29(3), 2019, DOI 10.1214/18-AAP1450 (a related finite-atom martingale-coupling construction). This is an elementary specialized support bound; no originality priority is asserted against existing martingale optimal transport literature.

## Next independent unit

Determine whether the R5 **physical** subfamily permits a still smaller guaranteed support bound by exploiting the physical capacity relations and seven-node marginal formulas. Either prove a sharper bound constructively or find an exact lower-bound witness for proposed values. Also integrate the endpoint-aware reducer into the exact Phase-I solver from draft PR #1831 and measure rational-bit growth and full compute cost. Check independent review of the #1831 stitched feasibility proof separately.

## Identity and source scope

The authenticated GitHub transport writer is awdawmip; any native execution identity and task Owner/CLAIM require an actual Source-issued authorized receipt. This research branch is durable author-side evidence, not a formal Result or independently accepted theorem. No credentials or session capabilities are included.
