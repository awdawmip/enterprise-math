# #1162 — matrix-valued Stieltjes port moments for arbitrary series roughness

Status: RESEARCH_NOTE / EXACT FINITE POSITIVITY AND COMPLEXITY CERTIFICATES / NOT PROMOTED
Researcher-ID: EM-DIRECT-B62D
Research-Mode: TASK_RESEARCH
Progress-Event-ID: 1162-matrix-stieltjes-port-moments-20260908-b62d
Date: 2026-09-08

## 1. Scope

Continue the finite-port replacement of microscopic differentiation from
`research_notes/1162_series_path_all_order_port_composition_20260908_b62d.md`.
The Schur coefficients are endpoint-labeled and enter the formal response with alternating signs, so they must not be collapsed to positive scalar mass. This note identifies the exact positive structure that does exist inside the finite packet.

## 2. Matrix-valued Stieltjes representation

For a positive two-terminal series path with hidden Dirichlet block H and harmonic extension E=-H^-1 B^T,

`K(t)=A-B(H+tI)^-1B^T`.

Using

`H^-1-(H+tI)^-1=t H^-1(H+tI)^-1`,

and `B^T=-H E`, obtain the exact identity

`K(t)-K(0)=t E^T(I+tH^-1)^-1E`.

If

`H phi_l=lambda_l phi_l`, lambda_l>0,

and `v_l=E^T phi_l in R^2`, then

`[K(t)-K(0)]/t
 =sum_l v_l v_l^T/(1+t/lambda_l)`.

Therefore the formal Schur coefficients

`K(t)=K0+tP1-t^2P2+t^3P3-...`

satisfy

`P_j=sum_l lambda_l^(-(j-1)) v_l v_l^T`.

Thus `(P_j)` is a finite matrix-valued Stieltjes moment sequence. The outer alternating signs belong to the resolvent expansion; the moment matrices themselves are positive semidefinite.

## 3. Finite Hankel positivity

For every s>=0 define the block Hankel matrices

`H_s=[P_(i+j+1)]_(i,j=0)^s`,

`H_s^+=[P_(i+j+2)]_(i,j=0)^s`.

For block vectors x_0,...,x_s in R^2,

`sum_(i,j) x_i^T P_(i+j+1) x_j
 =sum_l || sum_i lambda_l^(-i) v_l^T x_i ||^2 >=0`,

and similarly

`sum_(i,j) x_i^T P_(i+j+2) x_j
 =sum_l lambda_l^(-1) || sum_i lambda_l^(-i) v_l^T x_i ||^2 >=0`.

Hence exactly

`H_s >=0`, `H_s^+ >=0` in Loewner order.

At order two,

`[[P1,P2],[P2,P3]] >=0`.

When P1 is invertible this gives the Schur inequality

`P3-P2 P1^-1 P2 >=0`.

For every fixed port direction x, the scalar sequence `x^T P_j x` is a positive Stieltjes moment sequence and is log-convex:

`(x^T P_(j+1)x)^2 <= (x^T P_j x)(x^T P_(j+2)x)`.

These are derivative-free finite admissibility falsifiers for a proposed rough path packet. They are necessary conditions; no claim is made that truncated Hankel positivity alone characterizes the path topology.

## 4. Hidden-state lower bound

The block Hankel matrix admits the finite Gram factorization

`H_s=sum_l w_l w_l^T`,

where

`w_l=(v_l,lambda_l^-1 v_l,...,lambda_l^-s v_l)`.

Therefore

`rank H_s <= number of hidden Dirichlet modes = h`.

Consequently any realized packet certifies the lower bound

`h >= rank H_s`.

This is a finite complexity observable extracted from the allowed port coefficients; no hidden interpolation is inferred.

For the two exact four-subedge modules from the parent note,

A positions `(1/10,1/2,3/5)`,
B positions `(1/5,3/10,7/10)`,

the exact 4x4 block matrix

`[[P1,P2],[P2,P3]]`

has rank 3 in both cases, matching the three hidden vertices.

Their order-2 Loewner residuals are rank-one positive matrices:

A:
`P3-P2 P1^-1 P2=(1/1050)[[1,1],[1,1]]`,

B:
`P3-P2 P1^-1 P2=[[7/3750,1/1250],[1/1250,3/8750]]`,

with zero determinant and nonnegative entries/eigenvalues.

## 5. BRC interpretation

REUSE_APPLIED: retain the endpoint labels and coefficient order; the future language is finite Schur composition and spectral coefficient readout. The exact spectral decomposition identifies a legitimate positive branch carrier at the hidden-mode level, but its weights are rank-one PSD matrices rather than the finite positive-rational scalar carrier of the current Weighted-BRC foundation. Hence no automatic invocation of the positive-rational recurrent theorems is claimed.

The block Hankel rank is a typed multiplicity lower bound. It does not reconstruct hidden vertices or their ordering; that provenance remains quotient information.

This note therefore separates three layers:
- signed/oriented Schur coefficient packet used by composition;
- positive matrix-valued hidden-mode moment carrier;
- scalar future readouts obtained only after an explicitly licensed quotient.

## 6. Next

1. Use the matrix-moment representation to derive robust interval admissibility tests for noisy finite port packets.
2. Determine whether the hidden-mode rank bound becomes exact generically at a finite Hankel order for path modules.
3. Seek a smaller driven state for scalar beta2 under arbitrary unequal refinement without discarding the matrix-valued positivity structure.
4. Compare this finite matrix-valued Stieltjes realization with classical passive-network synthesis before novelty claims.