# BRC multiplier square-content reduction

Status: `PROVED STATE-DEPENDENT REDUCTION / EXACT GENERALIZATION OF 2-ADIC CASE / NO FACTORIZATION COMPLEXITY CLAIM`
Date: `2026-09-06`
Parent: `t0.brc_multiplier_basin`, `t0.brc_multiplier_priority_jump`

## Question

The dynamic 2-adic rule strips a factor 4 from a multiplier when the known BRC ceiling root is even. Is this phenomenon specific to p=2?

No. It is the p=2 case of an exact square-content reduction valid for every prime square dividing the multiplier.

## Theorem

Let n,m be positive integers with

`gcd(n,m)=1`,

and suppose the already-known BRC ceiling root is

`x=ceil(sqrt(mn))`.

Write the canonical squarefree decomposition

`m=a^2*d`,

with d squarefree, and set

`g=gcd(a,x)`.

If the completion gap is a square

`y^2=x^2-mn`,

then g divides y. Therefore

`m' = m/g^2`,
`x' = x/g`,
`y' = y/g`

satisfy

`m'n = x'^2-y'^2`.

Moreover

`x' = ceil(sqrt(m'n))`.

Finally, because `gcd(g,n)=1`,

`gcd(x-y,n)=gcd(x'-y',n)`.

Thus every square factor of m whose root is already visible in x is exact scan redundancy.

## Proof

Since `g|a`, `g^2|m`; since `g|x`, both `x^2` and `mn` are divisible by `g^2`. Hence `g^2|y^2`, so `g|y`.

The divided difference-of-squares identity is immediate.

For the ceiling statement, put `z=m'n`. The original root condition is

`gx' = ceil(g*sqrt(z))`.

Therefore

`gx'-1 < g*sqrt(z) <= gx'`.

After division by g,

`x'-1/g < sqrt(z) <= x'`,

which implies `x'=ceil(sqrt(z))`.

The gcd identity follows because g is coprime to n.

## One-shot normalization

Because `g=gcd(a,x)` contains every compatible prime power at once, dividing by `g^2` removes all square-content that can be stripped from the current ceiling root. If

`m=a^2*d`,

then after reduction

`m'=(a/g)^2*d`

and

`gcd(a/g,x/g)=1`.

So no second odd-prime square-content pass is needed. The existing 2-adic state representative is then applied only to detect an impossible residual 2-adic class.

## Examples

- `n=35, m=9`: `9*35=18^2-3^2`; square content a=3 and g=3. Reduction gives `35=6^2-1^2`, same factor 5.
- `n=203, m=45`: `45*203=96^2-9^2`; a=3, g=3. Reduction gives `5*203=32^2-3^2`, same factor 29.
- `n=15, m=16`: a=4, x=16, g=4. One-shot reduction gives m'=1 and x'=4. This subsumes two successive p=2 divisions.

## Squareful multipliers cannot be statically deleted

The reduction is state-dependent. A squareful multiplier can still be a genuine irredundant first hit when its ceiling root is coprime to the multiplier's square-content root.

Example:

`n=111=3*37`, `m=9`.

Then

`9*111=32^2-5^2`,

and `gcd(32,3)=1`. In the exact mod-8 representative scan, m=9 is the first successful multiplier. Hence no rule of the form "discard all squareful multipliers" is valid.

Additional bounded examples occur at m=25,27,45,49,63,75,81 with ceiling roots coprime to their square-content roots.

## Finite effect

For the static 62-candidate m<=100 representative set, random odd 64..2048-bit inputs showed:

- static mod-8 set: 62 candidate states;
- dynamic 2-adic gap-test irredundancy: about 56 states on average;
- full square-content gap-test irredundancy: about 53.2 states on average.

So the odd-prime square-content extension removes roughly another 2.7 gap tests per N beyond the 2-adic state reduction in this bounded setting.

This is a finite diagnostic. It does not claim a universal probability law.

## Coprimality boundary

The executable API requires `gcd(n,m)=1`. This is natural for multiplier factoring: if the gcd is nontrivial, the multiplier has already exposed a factor of n and the square-gap scan is unnecessary. The reduction theorem's same-gcd statement should not silently cross that boundary.

## Toolization

`src/enterprise_math/brc_multiplier_square_content.py` provides:

- `SquareContentReduction`;
- `odd_n_square_content_scan_reduction(n,m,x)`;
- `jump_state_square_content_reduction(state)`.

The module reuses the canonical `squarefree_decomposition` from the multiplier-basin tool and the exact odd-N 2-adic state representative from the priority/jump tool.

## Boundary / prior art

Scaling a difference-of-squares witness by a common factor is elementary classical arithmetic. The Enterprise value here is the typed BRC state criterion: the already-retained ceiling root tells exactly which part of the multiplier's square content can be quotiented before gap squarehood testing.

No novelty priority, asymptotic factorization speedup, or RSA-breaking claim is made.
