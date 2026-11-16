# RH Weil L5 — post-handoff fixed-window prior-art and exact conditional coverage
Date: 2026-11-16
Task: RS-RH-WEIL-L5-SCHUR-CERT; immutable publication TP2-836A025740E28C349B4D
Status: AUTHOR-SIDE SOURCE/TRIAGE NOTE. External theorem claims inspected; no independent end-to-end certificate verification or mathematical acceptance is asserted.

## Frozen task and previously audited boundary
The 2026-09-09 task asks for rigorous classical Weil quadratic-form positivity for both parity sectors, for every L in [4/5, (log 5)/2], or a theorem-quality obstruction to the Schur/response approach. Its finite inverse-free Schur residual square, polynomial Bernstein interval checker, boundary-jump counterexample and conditional common-form-space estimate are already verified in the project audit. The genuine Weil form normalization, domain, tail coercivity and full residual enclosure were outstanding as of that handoff.
Primary taskbook: awdawmip/enterprise-math@bae50d8a34ca9bea2d8095d777b7a2be0a159014:research_tasks/RH_WEIL_L5_SCHUR_CERT_20260909.md
Author-side prior task handoff: research_notes/RH_WEIL_SCHUR_L5_HANDOFF_20260909.md.

## Subsequent primary literature — all claims attributed, not independently adopted
1. Vincent Liu, *Certified Weil Positivity Beyond the Unit Window: Source-Exact Block-Schur and Tail-Compensation Bounds for the Riemann Zeta Function*, submitted September 2026:
   https://www.alphaxiv.org/abs/2609.weil-positivity-riemann-zeta-bounds
   Its abstract claims classical Weil-form coercivity for arbitrary complex smooth tests supported in half-width 1, with lower bound 2^(-151), and half-width 17/16 with bound 2^(-49162). The public frozen research repository is
   https://github.com/luciferyu666/certified-weil-positivity/tree/b6cd2183c1e79c6c27a34267812a7b2d73ed1b59
   Connector read verified at that commit: README.md blob SHA1 564f1b6fdc6cce922700afafbd5a9acfce2786f3; REPRODUCIBILITY.md blob SHA1 4d1b1d8093587e86a51ce40dec368da029b0052a.
   The archive release is https://github.com/luciferyu666/certified-weil-positivity/releases/tag/v1.0-mcom-submission ; README records 634659625 bytes, 292 frozen archive members, SHA256 7f8e47d265326cbfa4da95197c98bc226fe6cbfd8a22e6896955c18d8cdb376d. The author explicitly reports that a third-party external complete reproduction was not yet performed. This author-side audit has read the pinned source descriptions and NOT downloaded, executed or verified the large frozen computation; hash values are source claims not independently recomputed.
2. Hongmin Li, *Cutoff-free positivity of localized Weil forms through the (log 11)/2 threshold*, cited in the following Oct-26 paper:
   https://rstation.ai/problems/riemann_hypothesis/papers/45/v1
   This earlier independent construction claims positivity on a larger interval than the L5 question, subject to exact definition comparison and its actual original proof.
3. *Full-source Schur certificates for Weil positivity at support radius two*, rStation, 2026-10-26:
   https://rstation.ai/problems/riemann_hypothesis/papers/60
   Theorem 1.1 claims full form strict positivity for both parity sectors at half-width 2, then at all 0<a<=2. The posted automatic reviewer reports reproducing both 512-mode core congruences and transfer solves, but not rerunning the large M=524288 source construction or 130560-dimensional factorization. Site review is not the Enterprise Math independent Driver acceptance and not end-to-end reproduction. Compare its normalization (2.1), test-function domain and two complete Schur completions before using it.

## Exact mathematical coverage reduction, conditional on verified theorem identity
Define X_L=C_c^infinity((-L,L),C) and let Q be ONE fixed Weil quadratic form on the union of these spaces, under the same support parametrization, normalization, parity decomposition, Fourier/Mellin convention and boundary-extension rule as the external theorem. For every 4/5 <= L <= (log 5)/2, L<1 because e^2>1+2+2=5. Therefore X_L is a subspace of X_1. If the external bound Q(f)>=2^(-151)||f||_2^2 is valid for all f in X_1 with identical normalization, restriction proves the same uniform positive bound for every nonzero f in each even/odd X_L. The argument is a restriction of test space, not an extra numerical certificate and not a result for all-support Weil positivity or RH.
The key unverified premise is equality of the actual forms and their norm conventions, plus independent validity of the source theorem. If an L-dependent rescaling changes the form, derive the explicit isometry and norm constants before transferring the inequality. Strict positivity at one larger window does not by itself prove a bound for a differently normalized L-dependent form.

## Distinct next scientific unit / deduplication
(1) Pin the original Weil-source formula, support convention, Fourier-Mellin normalization, parity subspaces and domain in the project and in Liu, Li and rStation; construct explicit change-of-variables and coercivity constant transfer (or a counterexample).
(2) Audit the cited primary analytic lemmas and actual interval/Schur certificate manifests; independently reproduce small mathematical source and hash checks, then a selected full numerical branch under the specified environment before promotion.
(3) If the stronger external source fails an indispensable step, state the exact failed implication and return to the smallest unproved infinite-tail/coercivity unit. Preserve 2026-09-07 finite Schur/Bernstein results; do not rebuild their synthetic regression or infer RH.
This note is the post-September-09 research state correction and can be used as a handoff to a qualified independent reviewer. It does not change any current task/result/review/Foundation state.
