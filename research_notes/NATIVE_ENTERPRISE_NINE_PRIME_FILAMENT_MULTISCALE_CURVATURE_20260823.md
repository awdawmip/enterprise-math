# Native Enterprise sharp nine-prime filament：multiscale square-curvature ladder

Status: `FREE_RESEARCH_EXACT_MULTI_SCALE_PRIME_VALUED_READOUT / NOT_CANONICAL_FOUNDATION`

Date: `2026-08-23`

Researcher-ID: `EM-FREE-NEPS-239A6D`

Parent: `NATIVE_ENTERPRISE_MAXIMAL_PRIME_FILAMENT_SHARP_LENGTH_FIVE_20260823.md`

## 1. Sharp filament packet

A sharp length-five maximal-prime filament contains exactly nine distinct primes

`p1 < p2 < ... < p9`.

The five maximal flowers are the rolling windows

`p1..p5`, `p2..p6`, `p3..p7`, `p4..p8`, `p5..p9`.

The middle prime `p5` is the center of the middle flower at shell `r0+2`.

## 2. Multiscale symmetric curvature

For `j=1,2,3,4`, define

`C_j = p_{5-j} - 2*p5 + p_{5+j}`.

Using the exact rolling gap law

`2d(s)=6s-9+(-1)^s`,

a direct finite-sum calculation gives

`C_j = 3*j^2` for even `j`,

`C_j = 3*j^2 + (-1)^r0` for odd `j`.

Equivalently

`C_j = 3*j^2 + ((1-(-1)^j)/2)*(-1)^r0`.

Thus after removing one parity chirality term on odd scales, the curvature ladder is exactly

`3*(1^2,2^2,3^2,4^2)`.

## 3. Two exact chiral packets

### Even-start packet

The first explicit sharp filament found has

`r0=10688`, `h=-2474`.

Its nine primes are

`171283421, 171315481, 171347543, 171379609, 171411677, 171443749, 171475823, 171507901, 171539981`.

Its multiscale curvature vector is

`(4,12,28,48)`.

### Odd-start packet

A second exact sharp filament was found at

`r0=107813`, `h=7624`.

Its nine primes are

`17434825207, 17435148641, 17435472079, 17435795519, 17436118963, 17436442409, 17436765859, 17437089311, 17437412767`.

Its gap word is

`323434, 323438, 323440, 323444, 323446, 323450, 323452, 323456`.

Its multiscale curvature vector is

`(2,12,26,48)`.

All nine values in both packets were independently checked by direct trial division through their square roots.

## 4. Chiral decomposition

The two realizable sharp packets therefore have curvature vectors

`(3+chi, 12, 27+chi, 48)`,

where

`chi=(-1)^r0 in {+1,-1}`.

The even scales are chirality-blind:

`C_2=12=3*2^2`,

`C_4=48=3*4^2`.

The odd scales carry the same one-bit chirality:

`C_1=3+chi`,

`C_3=27+chi`.

Hence

`C_3-C_1=24`

is itself chirality-independent.

## 5. Interpretation

The sharp maximal filament is not only a longest rolling prime cluster. Its prime values carry a four-scale discrete curvature hierarchy selected by the native incidence geometry.

The hierarchy separates into

- a universal quadratic backbone `3j^2`;
- one parity/chirality bit visible only on odd scales.

This is a genuinely prime-valued multi-Cell readout: the Boolean fact that nine cells are prime does not contain the four actual curvature values or the recovered shell scale.

No novelty claim is made for finite differences or prime k-tuples as classical objects. The research-specific object is the emergence of this exact square-curvature ladder from the sharp native maximal-flower filament.
