# Native odd-curvature filament: complete universal-breaker phase diagram modulo 60

Status: `FREE_RESEARCH_EXACT_PHASE_CLASSIFICATION / EXTERNAL_NOVELTY_UNRESOLVED / NOT_CANONICAL_FOUNDATION`

Date: `2026-08-25`

Researcher-ID: `EM-FREE-NEPS-239A6D`

Parent: `NATIVE_FILAMENT_ODD_CURVATURE_DEFORMATION_MASTER_THEOREM_20260825.md`.

## 1. Problem

For the odd-curvature filament

`F_B(H,r)=H+(B*r^2+eps(r))/2`,

with positive odd `B`, call a prime `q` a **universal breaker** if every transverse class `H mod q` contains at least one `q`-divisible filament value.

Equivalently, there is no q-transparent transverse class.

This note classifies all universal breaker primes for every odd `B`.

## 2. Channel 2

Because `B` is odd:

- if `B=3 mod4`, then `(B*r^2+eps(r))/2` is even for both parities, so the filament is constant mod2 and `H=1` is transparent;
- if `B=1 mod4`, the two shell parities differ by1 mod2, so every `H` is hit.

Therefore

`2 is a universal breaker iff B=1 mod4`.

In the breaker case the mod2 word alternates zero/nonzero, so the sharp maximum nonzero run length is1.

## 3. Channel 3

If `3|B`, the two parity branches reduce to two distinct constants in `H`, leaving exactly one transparent class.

If `3` does not divide `B`, direct quadratic-character counting gives no transparent class.

Therefore

`3 is a universal breaker iff 3 does not divide B`.

In that breaker phase the shell sequence has period6 and every transverse class is hit. A tangency class has exactly one zero per period, so the sharp maximum nonzero run length is

`2*3-1=5`.

For `B=1 mod3`, `H=0` is such a one-zero class; for `B=2 mod3`, `H=1` is such a class.

## 4. Channel 5

The master transparency theorem gives:

- `T_B(5)=3` if `5|B`;
- `T_B(5)=1` if `B` is a nonzero quadratic residue mod5;
- `T_B(5)=0` if `B` is a quadratic nonresidue mod5.

Thus

`5 is a universal breaker iff Legendre(B/5)=-1`,

or equivalently

`B=2 or3 mod5`.

In this phase the exact sharp maximum nonzero run length is

`2*5-1=9`,

attained at the two tangency classes `H=0` and `H=2 mod5`.

## 5. No breaker above5

For every prime `q>=7`:

- if `q|B`, there are `q-2>0` transparent classes;
- if `q` does not divide `B`,
  `T_B(q)=[q-3+(B/q)+(-B/q)]/4 >= (q-5)/4 >0`.

Hence

`NO PRIME q>=7 IS A UNIVERSAL BREAKER`.

So the complete single-prime breaker set is

`Break(B)`

`= ({2} if B=1 mod4 else empty)`

`union ({3} if 3 does not divide B else empty)`

`union ({5} if Legendre(B/5)=-1 else empty)`.

## 6. First-breaker phase diagram modulo60

Classify the 30 positive odd residue classes modulo60 by the smallest breaker prime.

### First breaker 2

`B mod60 in`

`{1,5,9,13,17,21,25,29,33,37,41,45,49,53,57}`.

There are15 classes.

### First breaker 3

`B mod60 in`

`{7,11,19,23,31,35,43,47,55,59}`.

There are10 classes.

### First breaker 5

`B mod60 in {3,27}`.

There are exactly2 classes.

### No universal breaker at any prime

`B mod60 in {15,39,51}`.

There are exactly3 classes.

## 7. Finite-wheel iff classification

Let `S` be any finite set of prime channels.

If `S` contains a universal breaker, then that channel alone hits every transverse class, so every filament is cut.

If `S` contains no universal breaker, choose one transparent class modulo every `q in S`. By CRT there is an integer `H` realizing all choices simultaneously. The corresponding filament survives every channel in `S`.

Therefore

`EVERY FILAMENT IS CUT BY A FINITE WHEEL S`

iff

`S intersects Break(B)`.

For the three no-breaker residue classes `{15,39,51} mod60`, no finite set of prime channels can destroy all infinite filaments.

## 8. Native B=3 extremality

The Enterprise filament has `B=3`.

It satisfies simultaneously

`B=3 mod4`,

`3|B`,

`Legendre(B/5)=-1`.

Thus channels2 and3 both leave a transparent long filament, but channel5 cuts every one.

Moreover `B=3` is the smallest positive odd coefficient with this property.

So among odd-curvature deformations that possess a universal breaker, the native coefficient realizes the latest possible first-breaker prime and does so at the smallest curvature magnitude:

`B=3 -> FIRST UNIVERSAL BREAKER = 5 -> SHARP RUN CAP = 9`.

This gives an extremal parameter-selection interpretation of the native constants `3,5,9`.

## 9. Boundary

The congruence and quadratic-character computations are elementary. The research-specific object is the complete breaker phase diagram of the geometry-motivated odd-curvature deformation family and the fact that the native tri-sector coefficient `B=3` occupies the minimal first-breaker-5 class.

External novelty remains unresolved; no claim is made that residue-class classification itself is a new classical number-theory theorem.