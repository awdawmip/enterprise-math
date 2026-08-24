# Quadratic Packet Grothendieck Rank-Two Rigidity — Withheld Source Proof

Status: `WITHHELD UNTIL RAW AUDIT FREEZE / ORIGINATING SOURCE ARGUMENT / NOT INDEPENDENT VALIDATION`

Date: `2026-08-24`

Originating research context: `EM-FREE-5K7N2Q`

This file records the source-side proof that motivated the independent audit. It must not be used before the blind-forward raw verdict required by the audit packet is frozen.

## 1. Claim

Let `A` be a commutative unital `Z`-algebra whose additive group is free of rank `n >= 2`. Let `e in A` be nonzero nilpotent. Assume there is a prime `ell` such that:

1. `A / (ell + e)A` is cyclic as an additive abelian group;
2. there exist `k in Z` and `u in A^x` with

   `(ell + e)^2 = u (ell^2 + k e)`.

Then `n = 2`.

## 2. Phase-neutral index is automatic from nilpotence

Let `M_e` denote multiplication by `e` on the free abelian group underlying `A`.

Because `e` is nilpotent, `M_e` is nilpotent. Hence over `Q` its characteristic polynomial is `X^n`, so

`det(ell I + M_e) = ell^n`.

Therefore multiplication by `ell + e` has finite-index image of index `ell^n`, and

`|A / (ell + e)A| = ell^n`.

Since the quotient is assumed cyclic, it is therefore isomorphic as an abelian group to `Z / ell^n Z`.

## 3. The phase cannot vanish modulo ell

Suppose for contradiction that `e in ell A`, say `e = ell a`.

Since the additive group of `A` is torsion-free and `e` is nilpotent, `a` is nilpotent as well. Thus `1 + a` is a unit.

Then

`ell + e = ell(1 + a)`,

so `(ell + e)A = ell A`. Consequently

`A / (ell + e)A = A / ell A ≅ (Z/ell Z)^n`,

which is not cyclic for `n >= 2`.

Hence the image `e_bar` of `e` in

`V := A / ell A`

is nonzero.

## 4. Self-closure forces square-zero phase modulo ell

Reduce

`(ell + e)^2 = u(ell^2 + k e)`

modulo `ell`. This gives

`e_bar^2 = u_bar k_bar e_bar`.

If `k_bar != 0`, then `v := u_bar k_bar` is a unit of `A/ell A`, and

`e_bar^2 = v e_bar`.

Equivalently,

`e_bar(e_bar - v) = 0`.

Because `e_bar` is nilpotent and `v` is a unit, `e_bar - v = -v(1 - v^{-1}e_bar)` is a unit. Therefore `e_bar = 0`, contradicting the previous step.

Hence `k_bar = 0`, and therefore

`e_bar^2 = 0`.

Let

`E: V -> V`

be multiplication by `e_bar`. Then

`E^2 = 0`.

Thus

`im(E) subset ker(E)`,

so

`rank(E) <= n/2`.

## 5. Cyclic primitive quotient forces corank one

Tensor the cyclic quotient with `F_ell`. Since its order is `ell^n`,

`(A / (ell + e)A) tensor F_ell ≅ F_ell`.

On the other hand,

`(A / (ell + e)A) tensor F_ell`

is canonically

`A / (ell A + eA) ≅ V / e_bar V = coker(E)`.

Therefore

`dim_Fell coker(E) = 1`,

so

`rank(E) = n - 1`.

Combining with the square-zero bound gives

`n - 1 <= n/2`.

Hence `n <= 2`. Since `n >= 2`,

`n = 2`.

This also gives

`|A / (ell + e)A| = ell^2`.

## 6. Positive rank-two model

Take

`A = Z[eps] / (eps^2)`,

`e = eps`.

For every prime `ell`,

`A / (ell + eps)A ≅ Z / ell^2 Z`,

and

`(ell + eps)^2 = ell^2 + 2 ell eps`,

so both hypotheses hold and rank `2` is attained.

## 7. Source-side premise pressure already found

These examples were found in the originating research context and are recorded only for post-freeze comparison.

### Drop the one-chain quotient

Let

`A = Z[eps,delta] / (eps^2, eps delta, delta^2)`

with `e = eps`. This is free of rank `3`; `e^2 = 0`; one-clock self-composition holds. But

`A / (ell + eps)A ≅ Z/ell^2 Z ⊕ Z/ell Z`,

so the quotient is not cyclic.

### Drop self-composition closure

Let

`A = Z[eps] / (eps^3)`,

`e = eps`.

Then

`A / (ell + eps)A ≅ Z/ell^3 Z`

is cyclic, but

`(ell + eps)^2`

cannot be associate to any `ell^2 + k eps`: modulo `ell`, the left side has exact `eps`-adic contact order `2`, while a one-clock right side is either zero or has contact order `1`.

### Nilpotence premise

The originating run did not establish a clean rank-greater-than-two countermodel showing full logical independence of nilpotence while preserving the other two hypotheses. This remains an explicit audit target rather than a source-side result.

## 8. Scope guard

This argument proves only a conditional algebraic rigidity statement.

It does not prove that Enterprise Math Foundation must model packet phase by a nilpotent element, must impose one-clock composition closure, or must require primitive packet quotients to be single cyclic chains.

Those are separate semantic premises and require separate Foundation justification.
