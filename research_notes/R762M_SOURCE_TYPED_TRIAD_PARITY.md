# R762M — Source-labeled X6 triads: exact pair-observer parity kernel

Research date: 2026-11-13 Asia/Shanghai. Status: author-side exact proof, computation corroborated; independent Driver review not performed. Parent Task: RS-X6-TRIADIC-CLOSURE-DYNAMICS, publication TP2-8B7E13C5904A2D6F1142. Frozen scientific input: a72226e2430ffa4786321ac86e7f0c599d5f0389. Prior work: R762K PR #2297 and R762L PR #2300.

## Typed native X6 candidate domain

Fix a Cell c of the signed X6 affine torsor. Three independently named sources α, β, γ occupy three distinct signed primitive native-axis ports of c; the full candidate datum is (i_α,i_β,i_γ ; s_α,s_β,s_γ), with injective axes i∈{0,...,5} and sign bits s∈{0,1}³ (1 = negative direction). The ordering of the *source labels* supplies a candidate cyclic orientation. The established S6 axis-name permutations act on axes, not source labels or signs; the source-typed chirality therefore transforms covariantly.

There are (6)_3 = 120 injective axis assignments for each of eight sign vectors: 960 typed candidates. Under S6 each sign vector forms a single orbit of size 120. Every invariant Boolean *candidate-incidence* law A is exactly an eight-bit function a:{0,1}³→{0,1}, and all 2^8 = 256 laws occur.

This candidate domain is an X6 port-star incidence model. P000 fixes the primitive stable arity three and the native equal-quantum PERP_E relation at its stipulated 120°; it does **not** say every distinct-axis candidate is an admitted TRIADIC_CLOSURE_E physical event. Signed force cancellation, actual rotation, and event update rules have not been assumed here.

## Theorem 1 — Pairwise counts have exactly one nontrivial ambiguity

Fix any two named, signed visible source ports on distinct axes, leaving source j hidden. There are four unused X6 axes and two choices of hidden sign. Retain each hidden-source completion as a positive unit N-BRC candidate branch. The total admitted count is

B_j(t) = 4 [a_(t,j=0) + a_(t,j=1)] = 4 M_j(a)(t),

where t is the two-source sign assignment. Across three missing-source names and four t choices each, M consists of 12 orbit-reduced readouts, representing 3×6×5×4 = 360 actual named visible-pair instances in the six-axis model.

**Claim.** Among all 256 Boolean laws a, the joint pair-count observer M has precisely 255 different signatures: 254 singleton fibers and one double fiber. The only colliding laws are

a_even(s) = 1 when s_α+s_β+s_γ is even; and
a_odd(s) = 1 when s_α+s_β+s_γ is odd.

The two laws admit disjoint sets of 480 typed candidate triples each, yet B_j(t)=4 for every one of the 360 visible-pair instances under both laws.

**Proof.** Let a and b have equal M and define d(s)=a(s)-b(s). For every coordinate j and fixed remaining two signs, d(s with j=0)+d(s with j=1)=0. Flipping one sign therefore negates d. From c=d(0,0,0) we obtain d(s)=c(-1)^(s_α+s_β+s_γ). Because a,b are Boolean, c is 0, +1, or -1. If c=0, a=b. If c=±1, |d(s)|=1 everywhere and the binary constraints uniquely force the two complementary parity predicates. Both indeed give M_j(t)=1 for all 12 choices, proving the single double fiber. Each accepts four of eight sign patterns, each pattern having 120 native axis assignments, hence 480 accepted candidates. QED.

All lower-order count-only marginals (one-source or no-source sums) are sums of the pairwise marginals, so they also fail to distinguish this pair. By contrast a single triple-sign query at s=(0,0,0) distinguishes them, or one hidden-sign-resolved count distinguishes them for any fixed visible pair. Thus **one bit of third-source relation information is both necessary and sufficient to distinguish the unique exceptional pair of laws**. The full identity of one hidden branch, history, V29 ledger and V39 transport would require their own typed state; this bit claim concerns law identification only.

## Theorem 2 — General binary source-cube marginal kernel

For any n≥1 source-labeled binary slots, consider all Boolean laws on {0,1}^n and all (n−1)-slot marginal sums M_j(a)(t)=a_(t,j=0)+a_(t,j=1).

**Claim.** Their simultaneous real-linear kernel is one-dimensional, spanned by the alternating parity character χ(s)=(-1)^(sum s_i). Within Boolean laws, only the two complementary parity laws collide. Consequently the number of distinct signatures is exactly

2^(2^n) − 1.

**Proof.** Every kernel element d satisfies d(s⊕e_j)=-d(s) for all j. Each vertex of the binary cube is connected to 0 by coordinate flips, hence d(s)=d(0)χ(s). Conversely χ has zero marginal along every coordinate. Differences of two Boolean laws take values in {-1,0,1}, so any nonzero difference of this form has coefficient ±1 and forces complementary parity values. There is exactly one unordered colliding pair. QED.

This n-slot theorem concerns an abstract incidence observer; the primitive stable event in P000 remains **three-force**.

## Provenance, observer safety, verification

The paired source identity and sign are essential to the preceding statement. The source labels resolve the old unlabelled chirality-stabilizer obstruction only at the candidate level. If actual physical source-exchange symmetry is imposed, it must be checked separately. The retained parity distinction is a three-way joint-relation residual invisible to the entire family of two-source positive N-BRC totals, directly illustrating the mandated observer-specific relation-preservation constraint.

Exact standard-library checker R762M_SOURCE_TYPED_TRIAD_OBSERVER.py enumerates all 960 typed triples and 720 axis permutations, all 256 laws, all 360 named visible-pair instances per law, and every one of their eight hidden completions. It confirms the 255 signatures, the unique parity pair and all integer counts. Companion JSON preserves deterministic output; the n-generalization is proved above, not inferred from finite n=3 testing.

Frozen scientific references: enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389:p000_reality_foundation.json and definitions/P000_DISCRETE_DIRECTION_TRIADIC_BALANCE_20260905.md. Exact taskbook: enterprise-math@e01d91db2ad6e45fbfbb8360837cbf78a2bc5e11:research_tasks/RS_X6_TRIADIC_CLOSURE_DYNAMICS_20260906.md. Current behavioral overlay was separately read from docs/RESEARCH_CONTINUATION_PROTOCOL.md#current-normative-context, the account mathematical evidence policy and current research_priorities/research_method.json. No P000 or ACTIVE worldview modification.

**Next discriminating unit:** give one fully typed native TRIADIC_CLOSURE_E Cell/Link/Port predicate with source order/phase and its actual update; verify S6 covariance, legal repeat dynamics, V29 PASS/TRANSFER and V39 frame effects. Recompute the pair observer over genuinely admitted (not merely candidate) events, and decide whether the exhibited parity residual survives its actual state and source restrictions. Formal Result/CLAIM/independent Driver review retain their own Source authorization.
