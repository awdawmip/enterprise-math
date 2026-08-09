# A3-to-A4 Support Precision Pressure Test — Locating Cancellation Inside the Guard Quotient Module

Status: `RESEARCH WIP / CROSS-ROUTE PRESSURE TEST / BRIDGE OWNERSHIP PRESERVED`

## 1. Purpose

The A3-to-A4 bridge already preserves a cancellation counterexample: coarse support may hold while universal fine support does not.

This note does not re-own the bridge theorem or redefine A4 support. It asks a narrower A3 future-precision question:

> What exactly is lost by that cancellation inside the hidden predicate quotient?

## 2. Four fine coordinates and one coarse partition

Take unit-capacity fine totals

\[
c=(c_0,c_1,c_2,c_3)
\]

and coarse groups

\[
A=\{0,1\},\qquad B=\{2,3\}.
\]

The partition retains only

\[
C_A=c_0+c_1,
\qquad C_B=c_2+c_3.
\]

Its kernel is

\[
K_A=\{(a,-a,b,-b):a,b\in\mathbb Z\},
\]

of rank two.

## 3. Four fine cross-relation guards

Define

\[
z_{02}=c_0-c_2,
\quad z_{03}=c_0-c_3,
\quad z_{12}=c_1-c_2,
\quad z_{13}=c_1-c_3.
\]

Let

\[
W(c)=(z_{02},z_{03},z_{12},z_{13})\in\mathbb Z^4.
\]

For hidden motion

\[
\eta=(a,-a,b,-b),
\]

we obtain

\[
\boxed{W(\eta)=(a-b,\ a+b,\ -a-b,\ -a+b).}
\]

Thus universal fine-support geometry has only two hidden integer degrees despite containing four relation coordinates.

## 4. A3-ABP01 — Smith profile of the hidden guard image

Use the kernel basis

\[
(1,-1,0,0),
\qquad(0,0,1,-1).
\]

Their guard images are

\[
g_1=(1,1,-1,-1),
\qquad g_2=(-1,1,-1,1).
\]

Therefore

\[
L_G=\langle g_1,g_2\rangle_{\mathbb Z}\le\mathbb Z^4.
\]

Exact integer minors give

\[
\Delta_1=1,
\qquad\Delta_2=2,
\]

so the Smith invariant factors are

\[
\boxed{(1,2).}
\]

Hence

\[
\boxed{\mathbb Z^4/L_G\cong\mathbb Z^2\oplus\mathbb Z/2\mathbb Z.}
\]

The cancellation failure therefore has a precise A3 location: the coarse partition removes a rank-two hidden guard lattice, while the remaining predicate quotient carries a nontrivial parity-type torsion class that cannot be summarized by one coarse relation scalar.

## 5. A3-ABP02 — One coarse state contains both universal-support truth values

Fix

\[
(C_A,C_B)=(10,10).
\]

The fine lift

\[
c^{(+)}=(5,5,5,5)
\]

has all four cross relations zero, so universal radius-zero fine support is true.

The lift

\[
c^{(-)}=(0,10,0,10)
\]

has

\[
\boxed{(z_{02},z_{03},z_{12},z_{13})=(0,-10,10,0),}
\]

so universal radius-zero fine support is false.

Both lifts have the same coarse totals `(10,10)`. Their coarse cross relation is also identical:

\[
Z'_{AB}=\sum_{i\in A,j\in B}(c_i-c_j)=2(C_A-C_B)=0.
\]

Thus

\[
\boxed{\text{coarse relation}=0\not\Rightarrow\text{universal fine radius-zero support}.}
\]

The same coarse fiber explicitly contains a true and a false fine witness.

## 6. A3-ABP03 — Even one fine-pair support query may be ambiguous

For example,

\[
z_{02}=c_0-c_2
\]

has coefficient vector `(1,0,-1,0)`. Under the coarse partition, the gcd of within-block coefficient differences is one, so the hidden scalar step is

\[
\boxed{q=1.}
\]

At base relation value zero, the hidden fiber is all integers. The radius-zero predicate `|z_{02}|<=0` therefore contains both supported and unsupported fine lifts.

All four fine cross-pair relations have the same hidden-step-one behavior in this example.

## 7. Why coarse support remains exact

The coarse relation coefficient vector is

\[
(2,2,-2,-2),
\]

which is constant inside each coarse block. Hence

\[
\boxed{w(K_A)=0.}
\]

and the coarse relation descends exactly.

So:

- coarse support is exact;
- universal fine support is not exact;
- the difference is not numerical error but the future language's guard map `W`.

This is exactly the A3 future-precision principle: required precision is controlled by `W(K_A)`, not by the underlying coarse state alone.

## 8. Downstream meaning for the A3-to-A4 bridge

The pressure test separates three query scopes:

- **single coarse pair support**: the coarse weighted relation is enough;
- **single fine pair support**: a rank-one scalar band, handled by the hidden-band / rank-one residue solver;
- **universal support across all fine cross pairs**: a rank-two hidden predicate lattice with a `Z/2` quotient torsion component.

Therefore

\[
\boxed{\text{support-query precision complexity depends on query scope}.}
\]

Coarse support, one fine-pair support, and universal fine support are distinct future languages and cannot share one coarse truth value by default.

## 9. Ownership boundary

A3 owns the generic chain

\[
K_A\to W(K_A)\to\text{quotient module}\to\text{required precision}.
\]

The A3-to-A4 bridge owns support-family cancellation/interpolation statements, and A4 owns admissible-support/correspondence mother theory. This file remains only an A3 pressure test and relays its corollary to the bridge owner rather than duplicating bridge implementation.

## 10. Implementation

Added `tests/test_a3_a4_support_precision_pressure.py`, which verifies:

1. hidden rank `2`, free rank `2`, Smith factors `(1,2)`, and `Z/2` torsion for the cross-relation guard quotient;
2. true/false universal-support lifts inside the same coarse state;
3. ambiguity of each individual fine-pair radius-zero query at zero base;
4. exact visibility of the coarse relation itself.

## 11. Next

1. relay this pressure test to `research/core/relation-support-bridge`;
2. let the bridge owner use universal fine support as a concrete A2/P023 future-sufficiency obligation;
3. map staged support / split-completeness endpoint and intermediate-witness predicates into A3 guard quotients and measure hidden rank/torsion;
4. let P018 choose scalar/rank-one/rank-two precision solvers according to query scope rather than defaulting to full refinement;
5. if P022 supplies a restricted finite lattice/admissible domain, re-check the full-integer-fiber assumptions there instead of importing this result mechanically.
