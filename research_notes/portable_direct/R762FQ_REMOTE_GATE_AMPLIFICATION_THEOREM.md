# R762FQ — Arbitrarily many one-step provenance bits leaked by disconnected triad-incidence gates

Date: 2026-11-19 (Asia/Shanghai). Status: AUTHOR_PROVED / EXACT_ENUMERATION_PASS / NOT_REVIEWED.
Mother Task: RS-X6-TRIADIC-CLOSURE-DYNAMICS, publication TP2-8B7E13C5904A2D6F1142.
Frozen taskbook: awdawmip/enterprise-math@857280d1012943290d141d1317179c40ec3cbdf8:research_tasks/RS_X6_TRIADIC_CLOSURE_DYNAMICS_20260906.md.
Frozen P000 V5: awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389:p000_reality_foundation.json.
Direct antecedent: R762FP, PR #2787@709d171c2529534bba2ebb4dc664e0f78f171674; R762FO #2785 and R762FN #2782. This is a strict amplification of R762FP's k=3 remote-gate counterexample, not its duplication.

## Typed setup and scope

Choose three distinct signed native X6 axes within a three-axis research slice. On each axis put k *named* positive source tokens A_i, B_j, C_l. A history is a pair of bijections (sigma,tau) in S_k x S_k, with triples (A_i,B_{sigma(i)},C_{tau(i)}). A binary *candidate* incidence tensor M(i,j,l) defines the legal history set L_M: every chosen triple must have M=1.

A proposed edge action e={u,v} exchanges **both** B/C partners of rows u and v. It is enabled exactly when the resulting history lies in L_M; otherwise it produces an observable terminal BLOCK. Successful operations are involutions. The fixed port reads Q_1=(sigma(1),tau(1)). Every known-word experiment starts from a fresh copy of its initial history, as in R762FP. The horizon h counts attempted edge actions, **not** physical time.

These are candidate typed combinatorial gates, not an assertion of the native TRIADIC_CLOSURE_E Cell/Link/Port permission. Signed cancellation, Euclidean force-vector balance and a second primitive force equilibrium are not assumed.

## Theorem: unbounded one-step remote-gate information

For every integer m>=1 there exists an explicit candidate M_m with k=2m+1, a graph of m disjoint exchange edges and isolated visible root A_1 such that:

1. Exactly 3^m histories are legal; all display the same present Q_1=(1,1).
2. The number N_h of distinguishable histories under all resettable known-word experiments of length <=h is N_0=1 and N_h=2^m **for every h>=1**.
3. For the m-bit BLOCK vector b, writing z for the number of blocked gates, the corresponding class fiber contains 2^(m-z) complete histories. There are binomial(m,z) such classes. The provenance-weighted gate polynomial is
   F_m(u_1,v_1,...,u_m,v_m)=product_(r=1)^m (2u_r+v_r),
   where u_r marks enabled and v_r blocked. Evaluating all markers at 1 yields 3^m.
4. The minimal additional *fixed-length* storage preserving all these horizon-h experiments, for every h>=1, is **exactly m bits**, despite the complete disconnection of all gate edges from the observation port. Distinguishing every complete history would instead require ceil(m log_2 3) bits.
5. For a single fixed-point-free involutive remote gate with differing BLOCK outcomes and identical present root output, at least **three legal histories** are necessary. This construction attains three at m=1.

Hence the gate-disclosure effect is arbitrarily large with increasing k. R762FO's graph-distance-only count is not a safe quotient without the total-operation hypothesis or a replacement permission certificate.

### Explicit construction

Take k=2m+1. Row A_1 allows only partners (B_1,C_1). For each r=1,...,m let a=2r and b=2r+1. The **only** allowed local partners are:

| Row | Allowed ordered (B,C) partners |
| --- | --- |
| A_a | (a,a), (a,b), (b,b) |
| A_b | (b,b), (b,a), (a,a) |

No cross-block partners are permitted. The graph has only the m edges {a,b}, and the root 1 is isolated.

Each block admits precisely three bijective assignments:
- H0: (a,a);(b,b), gate ENABLED and leads to H2.
- H1: (a,b);(b,a), gate BLOCKED, since the target (b,a);(a,b) violates M_m.
- H2: (b,b);(a,a), gate ENABLED and leads to H0.

The fourth abstract pairing (b,a);(a,b) is illegal. Blocks use disjoint B/C token sets, so every legal history is exactly one choice from {H0,H1,H2} per block. There are 3^m.

### Proof

All histories agree at the untouched root, giving N_0=1. At horizon 1, probing edge r yields BLOCK precisely in H1. Every one of 2^m BLOCK vectors occurs, and each has 2 choices (H0,H2) in every enabled block, yielding fiber 2^(m-z). Thus N_1=2^m and its exact fixed-length code is m bits.

Every successful edge action merely interchanges H0 with H2 within its own block, so it preserves the enabled/blocked status. Different blocks commute. Thus in *any* longer experiment a word is blocked exactly when it tries a gate initially marked blocked; otherwise it returns the unchanged root output. The initial bit vector determines the entire future experiment family. Since one-step experiments already recover it, N_h=2^m for all h>=1, proving the sharp bit bound and polynomial.

For the one-gate minimality, let an enabled state s and blocked state t share root output. Applying the involutive fixed-point-free gate to s yields a distinct legal state s'. The gate is enabled at s' (it returns s), hence t differs from both s and s'. At least three histories are necessary. H0,H1,H2 attains the bound. QED.

## BRC algebra and safe state reductions

Introduce independent named source-event variables e_{i,j,l} and partner markers x_j,y_l. The coefficient
  [x_1...x_k y_1...y_k] product_(i=1)^k (sum_(j,l:M_m(i,j,l)=1) x_j y_l e_{i,j,l})
in the positive polynomial semiring N[e] is the sum of distinct monomials representing all legal named triad histories. Substituting e=1 yields the total 3^m but loses incidence information required by subsequent BLOCK observations. For the declared gate-only observer, the m-bit status vector is an exact future-safe quotient; for full BRC named-event reconstruction it is not. This explicitly preserves the P000 and joint-relation observer/provenance boundary.

## Exact validation

The companion Python verifier uses direct backtracking with separate uniqueness constraints on B and C partner tokens to enumerate **all** legal tensor histories, rather than assuming a product formula. It tests m=1..6 (k=3,5,7,9,11,13), obtaining respectively 3,9,27,81,243,729 legal histories. For all of them it verifies exact status-vector fibers and agreement of the observation partitions at horizons 0,1,2,3; for m<=3 it additionally compares each ordered pair of histories with an independent enumeration of every actual operation word up to horizon 3. All tests PASS. The attached JSON records the full class and fiber table.

The universal theorem is an exact combinatorial proof for all m>=1 and all finite h>=1. The computation tests only m<=6, h<=3. This is author-proved / author-checked, independent mathematical review NOT_REVIEWED.

## Next problems and control provenance

1. Extract actual native signed Cell/Link/Port permission and decide whether a remote-provenance gate can occur under genuine TRIADIC_CLOSURE_E and S6 covariance. Candidate M_m alone grants no native event permission.
2. Model irreversible, non-resettable operation traces and silent failures; calculate exact policy-dependent observation partitions under those changed observation semantics.
3. Compare precomputation, update, state recovery and verification costs for m-bit gates versus full provenance and BRC formal paths; no algorithmic speed claim is made here.

GitHub research publication does not grant a protected CLAIM, PROGRESS, Result or independent Review. Original R762FL Source PROGRESS request emr3-20261119-0702-r762fl-native-progress-v1 was read back FAILED / SOURCE_TARGET_CHANGED_DURING_REBASE; it is retained without replay.
