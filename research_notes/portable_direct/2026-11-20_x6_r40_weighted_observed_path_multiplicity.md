# X6 R40 — 路径重数未来观察的线性证书与 Boolean-BRC 边界

Date: 2026-11-20 (Asia/Shanghai). Task context: RS-X6-NATIVE-TIME-DYNAMICS.
Status: CONDITIONAL_AUTHOR_PROOF / EXACT_FINITE_CHECK_PASS / NOT_INDEPENDENTLY_REVIEWED.
Portable scientific research. This file does not assert a live native CLAIM, PROGRESS, Result, or Review.

## Exact frozen scientific source and continuation
- P000 V5: awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389:p000_reality_foundation.json, Git blob dc84bdae6595b5e237a2ad50d8b21916adb2e447.
- Joint observer preservation: same frozen commit at definitions/ENTERPRISE_JOINT_RELATION_OBSERVER_PRESERVATION_20260905.json, blob 3923890d77a02d84b772f789e6912dd14f220d14.
- R37 concerns Boolean successful-word language; R38 future deterministic readout; R39 nondeterministic observed Boolean trace support. This R40 treats the number of internal paths realizing each named, observed word as a different, stronger observation. It does not assume a concrete native TRIADIC_CLOSURE_E whole-triad successor law, or a physical path-count meter.

## R40.1 — Exact path-multiplicity model

Let A and B be finite directed multi-event graphs with n_A,n_B >= 1 states, common finite named event alphabet Sigma and public destination-readout alphabet O. Parallel microscopic paths are counted by integer weights w_a(i,j) >= 0. Source and signed Port must be included in event names if observed. Each state has current public readout o(i) in O.

For observed letter gamma=(a,v) in Gamma=Sigma x O define the integer matrix

  M_gamma(i,j) = w_a(i,j) [o(j)=v].

From state s the exact number of microscopic paths yielding the publicly observed word u=gamma_1 ... gamma_k is

  C_s(u) = e_s^T M_(gamma_1) ... M_(gamma_k) 1,  C_s(empty)=1.         (R40.1)

The initial public readout o(s) is compared separately. This is an integer path-count observer, not a physical amplitude model. With nonnegative weights, the R39 Boolean support predicate is exactly C_s(u)>0.

## R40.2 — Linear exact future certificate

**Theorem.** Let p in A and q in B. Their current outputs and complete future observed path-multiplicity series agree if and only if

  o_A(p)=o_B(q) AND C_p(u)=C_q(u) for every |u| <= n_A+n_B-1.         (R40.2)

If initial outputs agree but future counts differ, the first distinguishable event/readout word has length at most n_A+n_B-1. The result allows nondeterminism, parallel edges and any finite named Gamma. Unlike Boolean-support determinization, it requires no exponential powerset construction for this exact additive observer.

**Proof.** Put N=n_A+n_B. Over Q form the block diagonal matrices T_gamma=diag(M^A_gamma,M^B_gamma), row r=(e_p^T,-e_q^T), and terminal vector v=(1_A,1_B)^T. For every word u,

  C_p(u)-C_q(u) = r T_u v.

Let V_k = span_Q {r T_u: |u| <= k}. Its dimension starts at 1 and is bounded above by N. If V_k=V_(k+1), then V_k T_gamma is contained in V_k for every gamma, so the sequence is permanently stable. Otherwise its dimension increases by at least one. Therefore V_(N-1) spans all reachable rows r T_u. The finite equalities in (R40.2) say that the linear functional x -> x v annihilates every generator of V_(N-1), hence every reachable row. This proves all-word equality; the reverse direction is immediate. The current output comparison is a separate depth-zero condition. QED.

The proof also works for exact weights embedded in a common field, with the interpretation of the observer adapted accordingly. A signed sum of zero cannot be interpreted as absence of paths when cancellation is possible. Under Boolean support, the linear difference proof does not apply; R39's reachable-subset certificate remains the matching statement.

## R40.3 — Six-state strict counterexample

Take six states p,q,u,v,t1,t2, all with public output 0, and the only arrows

  p -a-> u;   q -a-> v;
  u -b-> t1;  u -b-> t2;  v -b-> t1.

p and q have *identical entire Boolean observed trace-support languages* {empty,a,ab}. Their path counts for empty and one-event words agree, but

  C_p((a,0)(b,0))=2,    C_q((a,0)(b,0))=1.

Thus they first separate at depth 2 under exact path-multiplicity observation. Erasing their difference using only R39 Boolean support would lose a declared joint/path observable. This is a fully specified finite model, not an admission claim about native P000 triadic events.

## R40.4 — Exhaustive declared finite check

The companion self-contained Python checker enumerates all 324 two-state, one-event, binary-destination-output machines with each ordered edge weight in {0,1,2}. Each of the 324 machines has both initial states, giving 648 rooted machines and 419,904 ordered rooted-machine comparisons.

It computes exact integer multiplicity for every observed word through depth 6. The n_A+n_B-1=3 certificate and depth-6 equality agree on every pair (PASS). First differences: current-output depth 0 = 209,952 pairs; depth 1 = 184,032; depth 2 = 14,128; depth 3 = 448; equal through both depths = 11,344. The six-state example has identical Boolean support for all event lengths but counts 2 versus 1 at (a,0)(b,0).

The exhaustive check applies to that finite universe; the theorem for arbitrary finite state counts is established by the symbolic proof, not by extrapolating the test.

Artifacts:
- research_notes/portable_direct/2026-11-20_x6_r40_weighted_observed_path_multiplicity.md
- research_notes/portable_direct/x6_r40_multiplicity_future_verify.py
- research_notes/portable_direct/x6_r40_multiplicity_future_results.json

Reproduce with Python 3: python3 x6_r40_multiplicity_future_verify.py > x6_r40_multiplicity_future_results.json.

## R40.5 — Native transfer boundary and next discriminating problem

R39 supports erasing distinctions that have identical *existential* named observation languages. R40 supports exact erasure when the stronger path-count series agrees; path-count equality implies Boolean-support equality for nonnegative weights, but not conversely.

To apply either certificate to frozen P000, first derive or verify a **legally admitted complete TRIADIC_CLOSURE_E event subsystem** with six-dimensional Cell, three nonzero forces, exact Link and signed Port changes, source/branch identities, rotation/frame, and actual observation contract. Decide whether two distinct microscopic realizations of an observed event are counted, identified, signed, or measured through another operator. If joint-source information or signed interference is an observable, preserve its type and obtain a corresponding certificate instead of assuming unweighted Boolean equivalence.

The unresolved mother-objective dependency remains the genuine native whole-triad successor/observation bridge. Existing R21–R39 provenance and all contributor ownership remain unchanged. No independent scientific Review or promotion is asserted.
