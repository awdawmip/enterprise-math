# Correction: Möbius W1 transport is an RH consequence, not an RH equivalence

Status: `CORRECTION / EXACT`
Date: `2026-09-08`
Project: `Enterprise Math / 进取数论`
Scope: `RH / Möbius quantile transport / earthmover W1 / Mertens`

## 0. Purpose

A research discussion on 2026-09-06 over-stated the one-dimensional earthmover/W1 formulation by calling the dyadic bound

`int_X^(2X) |M(t)| dt <<_eps X^(3/2+eps)`

RH-equivalent.

The cut-flux/optimal-transport identity behind that formulation is correct, and RH implies the displayed bound. The converse is false: an L1 bound of this size permits pointwise Mertens spikes of order `X^(3/4+o(1))`.

This note freezes the corrected logical status so later research does not use the false equivalence.

---

## 1. Exact cut-flux identity

Let positive Möbius Cells and negative Möbius Cells carry unit masses. On a finite interval with balanced endpoint bookkeeping, any transport plan from `mu=+1` mass to `mu=-1` mass has net signed flux across the cut at location `t` equal to the cumulative charge to the left, namely a Mertens discrepancy (with the appropriate interval/basepoint normalization).

For the global prefix version the charge is

`M(t)=sum_{n<=t} mu(n)`.

Therefore the absolute transport cost satisfies

`Cost >= int |M(t)| dt`.

The monotone same-rank transport realizes equality in one dimension. Thus the one-dimensional W1/earthmover cost is exactly the L1 norm of the cumulative charge.

Freeze:

`1D_MONOTONE_MOBIUS_TRANSPORT_COST = L1_CUMULATIVE_MERTENS_FLUX`.

This is an exact optimal-transport identity.

---

## 2. RH implies the W1 bound

RH is equivalent to

`M(t)=O_eps(t^(1/2+eps))`

for every `eps>0`.

Hence on a dyadic interval

`int_X^(2X)|M(t)|dt`
`<<_eps X * X^(1/2+eps)`
`= X^(3/2+eps)`.

Therefore

`RH => DYADIC_W1_MOBIUS_COST << X^(3/2+eps)`.

---

## 3. The converse fails

The arithmetic function `M(n)` changes by

`M(n)-M(n-1)=mu(n) in {-1,0,1}`.

Hence it is 1-Lipschitz on the integer line.

Suppose `|M(n0)|=H`. Then for every integer `n` with `|n-n0|<=H/2`,

`|M(n)|>=H/2`

unless the dyadic boundary truncates the interval. Away from a boundary this forces L1 area `>>H^2`; at a boundary one obtains the same conclusion after using the adjacent dyadic interval, up to constants.

Thus a uniform family of dyadic bounds

`int_X^(2X)|M(t)|dt << X^(3/2+eps)`

can imply at best, by this spike argument,

`|M(X)| << X^(3/4+eps/2)`

(up to harmless epsilon renaming and boundary bookkeeping).

It does **not** imply

`M(X)=O_eps(X^(1/2+eps))`.

Freeze correction:

`DYADIC_W1_BOUND_AT_X^(3/2) != RH_EQUIVALENCE`.

Correct logical relation:

`RH => W1_X^(3/2+eps)`,

while the W1 bound plus only the intrinsic unit-increment property gives a `3/4`-type pointwise exponent, not `1/2`.

---

## 4. What remains RH-equivalent

The same-rank **L-infinity** interlacing formulation remains the relevant pointwise transport reformulation:

if `a_j` lists squarefree `mu=+1` Cells and `b_j` lists squarefree `mu=-1` Cells in increasing order, then square-root-scale control

`|a_j-b_j|=O_eps(j^(1/2+eps))`

is equivalent, after using squarefree counting asymptotics, to the usual Mertens RH bound.

Thus:

- `W_infinity / maximal rank displacement` is RH-strength;
- `W_1 / total displacement` at the natural averaged scale is strictly weaker.

Do not substitute one for the other.

---

## 5. Research implication

The earlier idea of proving RH by merely controlling the **total** monotone transport cost is insufficient.

Any transport-based RH route must control either:

1. the maximal same-rank displacement;
2. a sufficiently high moment of displacement whose moment-to-sup conversion loses only `X^o(1)`;
3. or an independent arithmetic regularity principle strong enough to prevent `X^(3/4)`-height localized flux spikes.

This correction strengthens the observer hierarchy:

`BOOLEAN LOCAL REACHABILITY < W1 MASS TRANSPORT < WINFINITY RANK INTERLACING (RH STRENGTH)`.

No claim is made here that intermediate Wp moments for finite p are RH-equivalent.
