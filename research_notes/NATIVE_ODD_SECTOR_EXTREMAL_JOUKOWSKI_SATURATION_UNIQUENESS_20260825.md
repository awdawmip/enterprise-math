# Odd-sector extremal Joukowski saturation uniqueness theorem

Status: `FREE_RESEARCH_EXACT_UNIQUENESS_THEOREM / NOT_CANONICAL_ENTERPRISE_GEOMETRY`

Date: `2026-08-25`

Researcher-ID: `EM-FREE-NEPS-239A6D`

Depends on:
`NATIVE_ODD_SECTOR_LANE_LABEL_JOUKOWSKI_IMAGE_THEOREM_20260825.md`.

Only `s=3` is native Enterprise geometry. General odd `s` is the controlled shell allocator.

## 1. Setup

Let `s>=3` be odd and consider the central s-slot packet with lane-label Joukowski map

`Lambda_s(a)=-s*a-1/(2a)`

on `F_q^*`.

The native lane set is

`J_s={-(s-1)/2,...,(s-1)/2}`.

For `q>s`, complete transverse saturation is equivalent to

`Im Lambda_s subseteq J_s`.

At the extremal image-size bounds, both sets have size exactly `s`, so saturation means equality.

## 2. Upper extremal characteristic q=2s+1

Assume

`q=2s+1`

is prime and the packet saturates every nonzero residue modulo `q`.

Since `s` is odd,

`q=3 mod4`.

Moreover

`1/(2s)=-1 mod q`

is a nonresidue.

Therefore the Joukowski involution has no fixed points and every fiber of `Lambda_s` has size2.

Thus

`Im Lambda_s=J_s`

and

`2 * sum_(j in J_s) j^2`

`= sum_(a in F_q^*) Lambda_s(a)^2`.

Modulo q, because `s=-1/2`,

`Lambda_s(a)=(a-a^(-1))/2`.

For `q>3`,

`sum a^2=sum a^(-2)=0`,

so

`sum Lambda_s(a)^2=-(q-1)/2=-s`.

Hence

`sum_(j in J_s) j^2=-s/2`.

But

`sum_(j in J_s) j^2=s(s^2-1)/12`.

Cancel nonzero `s`:

`(s^2-1)/12=-1/2 mod q`,

so

`s^2+5=0 mod q`.

Since `s=-1/2 mod q`,

`1/4+5=21/4=0 mod q`.

Therefore

`q|21`.

As `q=2s+1>=7` is prime,

`q=7`,

hence

`s=3`.

Freeze:

`q=2s+1 EXTREMAL SATURATION => (s,q)=(3,7)`.

## 3. Lower extremal characteristic q=2s-1

Assume

`q=2s-1`

is prime and the packet saturates every nonzero residue modulo `q`.

Now

`q=1 mod4`,

and

`1/(2s)=1 mod q`

is a square.

The Joukowski involution

`a->1/a`

has exactly two fixed points `a=+/-1`.

The corresponding `Lambda_s` image values are `-1,+1`, each with singleton fiber. Every other image fiber has size2.

Again saturation gives

`Im Lambda_s=J_s`.

Counting the two singleton fibers correctly:

`sum_(a in F_q^*) Lambda_s(a)^2`

`=2 * sum_(j in J_s) j^2 - [(-1)^2+(+1)^2]`.

Modulo q, since `s=1/2`,

`Lambda_s(a)=-(a+a^(-1))/2`.

For `q>3`,

`sum Lambda_s(a)^2=(q-1)/2`.

Thus

`2 * sum_(j in J_s) j^2 -2=(q-1)/2`.

Since `q=2s-1`, this gives

`sum_(j in J_s) j^2=(s+1)/2`.

Using

`sum_(j in J_s) j^2=s(s^2-1)/12`,

we obtain

`s(s^2-1)=6(s+1) mod q`,

or

`s^3-7s-6=0 mod q`.

Since `s=1/2 mod q`,

`1/8-7/2-6=-75/8=0 mod q`.

Therefore

`q|75`.

As `q=2s-1>=5` is prime,

`q=5`,

hence

`s=3`.

Freeze:

`q=2s-1 EXTREMAL SATURATION => (s,q)=(3,5)`.

## 4. Dual-boundary uniqueness

Combining the two directions:

For every nontrivial odd sector count `s>=3`, the only possible exact saturation at either Joukowski image-size boundary is the native value `s=3`:

- lower boundary: `q=2s-1=5`;
- upper boundary: `q=2s+1=7`.

Therefore

`TRI-SECTOR s=3 IS THE UNIQUE NONTRIVIAL ODD-SECTOR MODEL`

`WHOSE CENTRAL PACKET SATURATES BOTH EXTREMAL JOUKOWSKI CHARACTERISTICS`.

## 5. Native 105 consequence

At `s=3` the coefficient-degenerate channel is

`s=3` itself,

while the two unique extremal Joukowski saturation channels are

`2s-1=5`,

`2s+1=7`.

Hence the complete small saturation gate is

`s(2s-1)(2s+1)`

`=3*5*7`

`=105`.

This is not a generic identity for odd `s`; it is the exact consequence of the dual-boundary uniqueness at `s=3`.

## 6. Relation to earlier selection theorems

The native value `s=3` now satisfies three independent exact selection properties inside the controlled odd-sector family:

1. it lies in the minimum-gate class `G_s=105`;
2. among that class, it has the latest finite longitudinal breaker `5`;
3. it is the unique nontrivial sector count saturating both extremal Joukowski boundaries `2s-1` and `2s+1`.

The third property uses a second-moment obstruction and is logically stronger than a bounded numerical scan.

## 7. Prior-art boundary

Joukowski maps, power sums over finite fields and second-moment arguments are classical ingredients.

The research-specific candidate is the exact odd-sector lane-label map and the resulting uniqueness of the tri-sector parameter under dual extremal saturation.