# #1162 — structural roughness bridge for finite cycle inverse-spectrum readouts

Status: RESEARCH_NOTE / FINITE PERTURBATION BRIDGE / NOT_PROMOTED
Researcher-ID: EM-DIRECT-B62D
Research-Mode: TASK_RESEARCH
Progress-Event-ID: 1162-structural-roughness-bridge-20260908-b62d
Date: 2026-09-08

## 1. Why a second stability layer is needed

The refinement projector stability theorem controls errors in the retained scalar samples once those errors are honestly bounded. It does not by itself control how much the scalar inverse-spectrum readout changes when the underlying finite operator is changed by the rough relation.

Keep distinct:

1. readout/sample/model-residual error on a fixed declared operator family;
2. structural roughness of the operator itself.

The second layer needs its own typed bridge.

## 2. Relative quadratic-form roughness for weighted cycles

Let `L_N` be the unit-edge cycle Laplacian and let `L_N(w)` be the weighted cycle Laplacian with edge conductances `w_e>0`.

Assume the finite local roughness condition

`1-eta <= w_e <= 1+eta`,  `0<=eta<1`,

for every edge.

Then on the constant-vector orthogonal complement,

`(1-eta)L_N <= L_N(w) <= (1+eta)L_N`

in quadratic-form order, because both energies are sums of the same squared edge differences with conductance weights in that interval.

By the min-max principle, every positive eigenvalue satisfies

`(1-eta) lambda_i(L_N) <= lambda_i(L_N(w)) <= (1+eta) lambda_i(L_N)`.

Hence for every integer m>=1,

`(1+eta)^(-m) Tr[(L_N^+)^m]
 <= Tr[(L_N(w)^+)^m]
 <= (1-eta)^(-m) Tr[(L_N^+)^m]`.

For the normalized readouts

`b_m(N)=2^(2m-1)N^(-2m)Tr[(L_N^+)^m]`,

and the weighted versions `b_m^w`, the same relative bounds hold.

This is an entirely finite spectral perturbation bridge; no derivative with respect to edge weight or resolution is used.

## 3. Composition with the stable refinement projector

If the same relative roughness envelope eta holds at every sample scale in a q-refinement orbit, then

`|b_m^w(q^jN)-b_m(q^jN)|
 <= [(1-eta)^(-m)-1] b_m(q^jN)`.

Feeding these honest sample envelopes into the derivative-free projector gives

`|Pi_(m,q)b_m^w - C_m|
 <= kappa_(m,q) max_j |b_m^w(q^jN)-b_m(q^jN)|`,

with `kappa_(m,q)<2` for every integer q>=2.

Thus the projection/cancellation step itself remains uniformly well conditioned; any growth with m coming from `(1-eta)^(-m)` is physical sensitivity of the inverse-moment observable to structural spectral changes, not instability of the projector. These two mechanisms must not be conflated.

## 4. Explicit Basel roughness bound

For m=1 the exact cycle readout satisfies

`0<b_1(N)<1/6`.

Therefore

`|b_1^w(N)-b_1(N)| < eta/[6(1-eta)]`.

Using the dyadic two-scale estimator

`C_hat=(4 b_1^w(2N)-b_1^w(N))/3`,

we obtain the finite robust interval

`|C_hat-1/6| < 5 eta/[18(1-eta)]`.

No continuum limit and no infinitesimal perturbation are involved.

This bound is deliberately conservative; correlations between the two scales or additional gauge normalization can improve it, but must be proved rather than assumed.

## 5. Why an absolute operator-norm roughness bound is not enough uniformly in N

The positive spectral gap of the unit cycle behaves as

`lambda_2(L_N)=4 sin^2(pi/N)=O(N^(-2))`

in the classical compatibility readout. Equivalently, finite graph spectral gaps tend to zero with increasing cycle size.

Therefore a fixed additive operator error bound `||Delta_N||<=epsilon` independent of N is not a uniform inverse-spectrum stability hypothesis: eventually epsilon is not small relative to the lowest positive mode. In a general PSD operator class, a perturbation of size comparable to that lowest mode can close it and destroy invertibility on the previously retained subspace.

Hence a native roughness bridge must be relative to a retained energy/form/gap structure, or otherwise carry an explicit N-dependent error scale. Absolute arithmetic precision is not a substitute.

## 6. BRC typing

REUSE_APPLIED: keep structural operator roughness distinct from sample/readout uncertainty. The relative edge-conductance interval is retained as a repair coordinate until it has been propagated through the finite quadratic form and spectral readout.

The positive form inequality is not a claim that all signed/projector coefficients are positive BRC mass. Projection remains a signed linear quotient; rough operator energy is a separate finite positive carrier.

## 7. Next

1. Test whether a more native gauge-normalized edge-roughness relation yields an N-uniform sharper Basel interval.
2. Extend the form-order bridge to allowed non-cycle local perturbations while preserving the one-dimensional refinement topology.
3. Use cross-q projector redundancy to distinguish structural roughness from mere sample noise.
