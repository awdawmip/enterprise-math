# BRC_RADIAL_ANCHOR_MAJORANT — positive anchor domination for the signed pair network

Task: `RS-RHR-CLAUDE-RH-RERUN-20260811`  
Researcher-ID: `RHR-9Q6M2K`  
Driver: `EM-DVR-7Q4K2C`

Status:

`RADIAL_ANCHOR_MAJORANT_PROVED / SIGNED_SUBSET_BRANCHES_COMPRESSED / FINITE_DEPTH_TODA_INTERFACE / RH_NOT_CLOSED`

## 1. Motivation

`BRC_WEIGHTED_PAIR_TODA_BRIDGE.md` shows that at the first locally unsafe rank a conjugate
pair has exactly one negative Littlewood--Richardson mode, the full-row mode `(r)`. The remaining
problem is to control the positive part of several active pairs without enumerating every signed
subset path.

The natural positive comparison is the **radial anchor**

`barY={R,R}`

for an actual conjugate pair

`Y={R exp(i theta), R exp(-i theta)}`.

The radial anchor has only positive real variables and hence is PF-infinity by construction.

## 2. Pair-local coefficient domination

For a two-row partition `nu=(a,b)`, `a>=b>=0`, put `m=a-b+1`. Then

`S_nu(Y)=R^(a+b) sin(m theta)/sin(theta)`

and

`S_nu(barY)=m R^(a+b)`.

Assume the actual pair is in its first locally unsafe layer for width `r`:

`pi/(r+1)<theta<=pi/r`.

For every `nu` of width at most `r`, except `nu=(r)`, the actual coefficient is nonnegative.
Moreover

`|sin(m theta)|<=m sin(theta)`

for `0<theta<pi`, equivalently the Chebyshev bound
`|U_(m-1)(cos theta)|<=m`. Therefore

`0<=S_nu(Y)<=S_nu(barY)`

for every nonnegative pair mode. For the unique negative mode `(r)`, the positive part has
coefficient zero while `S_(r)(barY)>0`.

If

`T_Y=P_Y-eta_Y U_(r)`

is the signed transfer from the previous checkpoint, and `T_barY` is the full radial transfer,
then coefficientwise on the partition carrier

`boxed: 0<=P_Y<=T_barY.`

This is an exact RCC majorant, not a numerical approximation.

## 3. Multi-pair radial-majorant theorem

Let `Y_1,...,Y_M` be first-layer active pairs, with

`T_i=P_i-eta_i U_(r)`.

Let `f_X>=0` be a rank-r-safe background partition-state vector. Define

`F=P_1...P_M f_X`

and the radial anchor state

`barF=T_barY1...T_barYM f_X`.

By Section 2,

`f_X<=F<=barF`

coefficientwise.

The weighted-pair theorem already gives at the rectangular target

`D_actual(r,k)>=F_k-sum_(j odd) e_j(eta) F_(k-j)`.

Using `F_k>=D_X(r,k)` and `F_(k-j)<=barD_(r,k-j)`, where

`barD_(r,n)=barF(r^n)`, gives the sharper externalized lower bound

`boxed:
 D_actual(r,k)
 >=D_X(r,k)-sum_(j odd) e_j(eta_1,...,eta_M) barD_(r,k-j).`

Hence the finite domination criterion

`boxed:
 sum_(j odd) e_j(eta) barD_(r,k-j)/D_X(r,k)<1`

implies `D_actual(r,k)>0`.

At the first sharpened spectral boundary the previous checkpoint proved `M<=12`, so only

`j in {1,3,5,7,9,11}`

can occur.

## 4. Finite-depth Toda form

Define the radial-anchor adjacent ratios

`barP_(r,n)=barD_(r,n-1)/barD_(r,n)`

and the anchor inflation

`kappa_(r,k)=barD_(r,k)/D_X(r,k)`.

Then exactly

`barD_(r,k-j)/D_X(r,k)
 =kappa_(r,k) product_(t=k-j+1)^k barP_(r,t)`.

Therefore the sufficient criterion becomes

`boxed:
 kappa_(r,k)
 sum_(j odd) e_j(eta)
 product_(t=k-j+1)^k barP_(r,t)<1.`

The ratio sequence is itself a Toda carrier:

`barP_(r,n)/barP_(r,n+1)=barq_(r,n)`.

Thus the multi-pair signed problem has been reduced to:

- at most six elementary defect weights;
- at most eleven adjacent radial-Toda ratios;
- one scalar anchor-inflation factor.

No exponential branch enumeration remains at this layer.

## 5. Exact factor residual

At the generating-function level

`B_Y(z)=1+2R cos(theta) z+R^2 z^2`,

while

`B_barY(z)=(1+Rz)^2`.

Their difference is the one-coordinate negative residual

`boxed:
 B_Y(z)-B_barY(z)=-2R(1-cos theta)z.`

Using `1-cos theta<=theta^2/2` and the zeta-pair bounds

`R<=1/(4 gamma^2)`, `theta<=1/gamma`,

the scalar factor defect obeys

`2R(1-cos theta)<=R theta^2<=1/(4 gamma^4)`.

This absolute smallness does not by itself control high-order Toeplitz signs, because the
minor can be ill-conditioned near the sector boundary. It does, however, show that the
anchor-to-actual correction is sparse in coefficient space as well as sparse in the partition
carrier.

## 6. Current hard bridge

The remaining theorem is no longer a generic cluster-count problem. It is:

`RADIAL_ANCHOR_STABILITY`:

> control `kappa_(r,k)` and the finite set of radial adjacent ratios strongly enough that the
> six-term defect criterion remains below one until another certified positivity region takes
> over.

The radial anchor itself is positive-real/PF-infinity. The unresolved difficulty is the
conditioning of the rectangular observable relative to the safe background, not the sign of
the anchor model.

## 7. Classification

Proved here:

- coefficientwise positive-part domination `P_Y<=T_barY`;
- multi-pair radial majorant;
- finite-depth Toda reformulation;
- sparse anchor-factor residual.

Not proved:

- a uniform bound on `kappa`;
- closure of the RH critical cone.

Final status: `RH_NOT_CLOSED`.
