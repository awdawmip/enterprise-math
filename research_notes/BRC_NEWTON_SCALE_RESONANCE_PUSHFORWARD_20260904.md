# BRC Newton scale resonance and exact pushforward law

Date: 2026-09-04
Mode: TASK_RESEARCH
Status: research candidate; no Foundation promotion in this note
Parent: WBRC-T51, WBRC-T52/T53, main-backed PR #1191

## 1. Motivation

The first failed validation of PR #1191 exposed an exact phenomenon that is more general than that one handoff family.

With eta=1/2, tau_1=1/3 and the original trial tau_2=1/4, the third Newton stage had

(tau_2/tau_1) = (eta^2/tau_1) = 3/4.

A newly declared common-shift contribution and an intrinsic nonlinear contribution therefore reached the **same Newton scale**.  They had to be combined in the same edge polynomial before the next root could be selected.  Replacing tau_2 by 3/10 separated the scales and restored the clean translated root -1.

This note extracts the exact general law behind that collision.

Newton polygons, valuations and Puiseux transformations are classical prior art.  The Enterprise/BRC content is the typed finite-scale pushforward law and its role as the correct information-loss boundary between explicit source provenance and the residual Newton jet.

## 2. Newton atoms

Let the current exact jet be

J_s(x)=sum_sigma sigma^s P_sigma(x),

where the scale support is finite and lies in the rational-valuation group

S_rad = Q_{>0}^x tensor_Z Q.

Fix a selected root x_0 of multiplicity r in the scale-one polynomial and a chosen Newton scale theta.

Write the Taylor expansion

P_sigma(x_0+theta^s y)
=
 sum_k a_{sigma,k} theta^{ks} y^k,

with

a_{sigma,k}=P_sigma^(k)(x_0)/k!.

After division by theta^{rs}, one Taylor atom

(sigma,k,a_{sigma,k})

has residual scale

boxed:
    rho = sigma theta^{k-r}.

Thus define the affine Newton scale map

Phi_{theta,r}(sigma,k)=sigma theta^{k-r}.

## 3. Exact pushforward law

For every residual scale rho define

Q_rho(y)=
 sum_{sigma,k : Phi_{theta,r}(sigma,k)=rho}
 a_{sigma,k} y^k.

Then exactly

boxed:
    theta^{-rs} J_s(x_0+theta^s y)
    = sum_rho rho^s Q_rho(y).

This is a finite identity, not an asymptotic statement.

The residual Newton jet forgets which old scale/source produced a Taylor atom once those atoms have the same residual scale and Taylor degree.  The coefficient polynomial at one residual scale is the sum over the whole scale fiber.

## 4. Resonance criterion

Two Taylor sources (sigma_1,k_1) and (sigma_2,k_2) lie on the same residual scale iff

sigma_1 theta^{k_1-r}
=
sigma_2 theta^{k_2-r},

or equivalently

boxed:
    sigma_1/sigma_2 = theta^{k_2-k_1}.

In finite prime-valuation coordinates this becomes

boxed:
    v_p(sigma_1)-v_p(sigma_2)
    = (k_2-k_1) v_p(theta)

for every prime p.

Hence Newton-scale resonance is an exact rational-linear relation in the finite valuation support.  No radical materialization is needed.

## 5. Edge polynomial is the scale-one fiber

The next Newton edge polynomial is exactly

boxed:
    E(y)=Q_1(y).

Therefore the correct order of operations is:

1. Taylor expand all source layers;
2. push every atom through Phi_{theta,r};
3. aggregate every equal residual scale;
4. apply semantic-zero reduction inside the coefficient algebra;
5. only then inspect the scale-one edge and select its root.

This order is mandatory even when the original branch carrier is positive, because determinant/characteristic compression has signed polynomial coefficients.

## 6. Resonance versus cancellation

Different Taylor orders that land on the same residual scale generally contribute different powers of y, so resonance changes the **shape** of the edge polynomial rather than simply adding scalar masses.

Exact cancellation can occur only after coefficient aggregation at the same residual scale and polynomial degree, or semantically in a selected-root evaluation algebra.  Thus source-level nonzero terms must not be treated as independently root-active after aggregation.

This refines the semantic-zero-first law of WBRC-T53:

boxed:
    SAME_SCALE AGGREGATION -> SEMANTIC ZERO -> ROOT/CONTACT ANALYSIS.

## 7. Composition / one-shot identity

For two successive Newton transformations

x=x_0+theta_1^s(y_0+theta_2^s z),

the source-atom valuation map is the affine composition of the two one-step maps.  Therefore:

- staged pushforward and one-shot binomial substitution produce the same residual scale-polynomial jet;
- aggregation is associative and independent of the order in which source provenance is enumerated.

This gives a provenance-level explanation of the recursive-vs-direct identities already verified in WBRC-T52.

## 8. PR #1191 resonance witness

Use the repeated-block irrational-root handoff family with

eta=1/2,
tau_1=1/3.

After the first two Newton translations, compare two choices.

### Resonant choice

For tau_2=1/4,

new common-shift ratio = tau_2/tau_1 = 3/4,
intrinsic second-order ratio = eta^2/tau_1 = 3/4.

These two sources occupy the same valuation scale and both enter the third edge polynomial.  The edge is not the pure translated `(x+1)^2` edge.

### Separated choice

For tau_2=3/10,

new common-shift ratio = 9/10,
intrinsic second-order ratio = 3/4.

The new common-shift scale is strictly larger, so it alone controls the next edge and the selected translated root is again -1 with multiplicity two.

This is an exact demonstration that a change in scale ordering, not a change in the algebraic root carrier, caused the first failed #1191 check.

## 9. Observer boundary

The pushforward law gives a precise representation boundary:

- explicit source provenance: remembers original sigma and origin of every Taylor atom;
- residual Newton jet: remembers only residual scale rho, Taylor degree k and aggregated coefficient;
- edge observer: sees only the rho=1 fiber after semantic-zero reduction.

Do not infer source provenance from a residual edge polynomial.

## 10. Validation requirements

The exact checker must:

- generate finite rational Newton jets and compare an independent atom-pushforward implementation with production `rational_newton_step`;
- verify the valuation resonance criterion for every detected scale collision;
- verify aggregation is invariant under reversing source enumeration;
- identify the scale-one edge as the exact pushforward fiber;
- verify staged vs one-shot two-step pushforward on selected examples;
- reproduce the PR #1191 tau_2=1/4 resonance and tau_2=3/10 separation with exact rational-valuation comparisons;
- verify the resonant third edge differs semantically from the separated pure translated edge.

## 11. Hard boundaries

- NEWTON_SCALE_RESONANCE != SIGNED_BRANCH_INTERFERENCE; signed coefficients here arise from algebraic/characteristic compression.
- SAME_RESIDUAL_SCALE != SAME_SOURCE_PROVENANCE.
- SOURCE_NONZERO != AGGREGATED_SEMANTIC_NONZERO.
- EDGE_POLYNOMIAL != COMPLETE_RESIDUAL_JET.
- RESONANCE_PUSHFORWARD != COMPLETE_NEWTON_PUISEUX_SOLVER.
- No generic novelty for Newton polygons/valuations is claimed.
