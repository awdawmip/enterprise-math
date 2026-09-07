# Divisor-Layer Lift Probe — Local tau Spectrum and Factor-Forcing Targets

Status: `PROVED ELEMENTARY LIFT OBSTRUCTION + SQUAREFREE PRIME-LAYER ENCODER / FINITE SMALL-N DIAGNOSTIC / NO LARGE-N FACTORING CLAIM`
Date: `2026-09-08`

## 1. User idea and operationalization

For an integer n, let tau(n) be the divisor-count function.  To make the idea
"raise primes and semiprimes to the divisor-count level of nearby composites"
exact, define for a target divisor layer T

`L_T(n)={a>=1 : tau(a*n)=T}`

and, when the set is nonempty,

`lambda_T(n)=min L_T(n)`.

For the neighborhood itself, do **not** collapse immediately to a single mode.
Retain the labeled/multiset spectrum

`{(n+j, tau(n+j)) : 0<|j|<=r, n+j composite}`.

The mode is retained only as a comparison observer.

## 2. Multiplicative obstruction theorem

If `gcd(a,n)=1`, multiplicativity of tau gives

`tau(a*n)=tau(a) tau(n)`.

Therefore:

`tau(n) does not divide T  =>  every a in L_T(n) has gcd(a,n)>1`.

Call such a target a **factor-forcing divisor layer**.

For a squarefree semiprime `n=pq`, `tau(n)=4`, hence every neighboring target
with `4 not dividing T` is factor-forcing.

For a prime n, tau(n)=2, hence every odd target T is factor-forcing.

This theorem is elementary but useful as a classification boundary: a target
layer can be declared factor-forcing before any lift multiplier is searched.

## 3. Strong squarefree prime-layer encoder theorem

Let

`n=p_1...p_k`

be squarefree with distinct primes, and let r be an odd prime.  Set

`T=2^(k-1) r`.

Every source prime already occurs in `a*n` with exponent at least one, so its
factor `(e_i+1)` in tau(a*n) is at least two.  The integer T has exactly k prime
factors counted with multiplicity: k-1 copies of 2 and one copy of r.
Consequently there is no room for an additional prime divisor of `a*n`, and the
only exponent pattern is

`(r-1,1,...,1)`

up to permutation.  Thus any lift changes exactly one source-prime exponent,
and the minimal lift uses the smallest source prime:

`lambda_T(n)=p_min^(r-2)`.

For a squarefree semiprime `n=pq`, p<q, this specializes to

- `T=6  -> lambda_6(n)=p`,
- `T=10 -> lambda_10(n)=p^3`,
- `T=14 -> lambda_14(n)=p^5`,
- `T=22 -> lambda_22(n)=p^9`.

Thus the target family `T=2r`, r odd prime, is a **strong factor-encoding
layer**.  If lambda_T were available, the smaller factor is its exact
`(r-2)`-th root.

## 4. Other target layers behave differently

This experiment immediately separates target types.

For squarefree semiprime n=pq:

- T=4: no lift is needed;
- T=8: a coprime lift is normally possible by adjoining a new prime, so it need
  not reveal a source factor;
- T=9: both source exponents must become 2, so the minimal lift is n itself in
  the generic squarefree case and gcd(lambda,n)=n rather than a proper factor;
- T divisible by 4: coprime lifts are not obstructed by multiplicativity;
- T not divisible by 4: every exact lift overlaps n, but only special target
  shapes such as 2r give the clean one-factor power encoder above.

So "raise to the same divisor count" is not one mechanism.  The arithmetic
factorization of the target layer T determines which exponent changes are
allowed.

## 5. Finite neighborhood experiment

The committed finite probe scans squarefree semiprimes in `[20,L)` and all
composite neighbors within radius r.  A strong opportunity means at least one
neighbor has

`tau(m)=2r_prime` with r_prime an odd prime.

Selected results:

| L | radius | semiprimes | any factor-forcing | strong 2r layer | tau=6 neighbor | strong after mode compression |
|---:|---:|---:|---:|---:|---:|---:|
| 1,000 | 2 | 284 | 181 (63.73%) | 146 (51.41%) | 118 (41.55%) | 47 (16.55%) |
| 5,000 | 2 | 1,342 | 697 (51.94%) | 531 (39.57%) | 427 (31.82%) | 146 (10.88%) |
| 10,000 | 2 | 2,596 | 1,246 (48.00%) | 936 (36.06%) | 749 (28.85%) | 266 (10.25%) |
| 20,000 | 2 | 5,043 | 2,193 (43.49%) | 1,629 (32.30%) | 1,319 (26.15%) | 483 (9.58%) |

The fixed small targets become less frequent as the range grows, so these
percentages must not be extrapolated to RSA scale.  The finite experiment is a
structure probe, not an asymptotic density theorem.

## 6. Provenance / no-early-compression finding

At L=10,000 and radius 2:

- retaining all nearby composite tau layers gives strong opportunities for
  `936/2596 = 36.055%` of squarefree semiprimes;
- collapsing first to the modal local tau layer gives only
  `266/2596 = 10.247%`;
- the full local layer spectrum therefore exposes about `3.519x` as many strong
  opportunities.

Equivalently, modal compression discards about 71.6% of these strong
opportunities.

This is directly consistent with the BRC observer/provenance discipline:
compression is safe only after the future operation is declared.  Here the
future operation asks whether **any** neighboring layer has a factor-encoding
shape, so the modal tau value is not an adequate quotient.

## 7. Algorithmic boundary

The factor-encoding theorem does **not** by itself factor a large unknown n.
Two costs remain potentially factorization-hard:

1. obtaining exact tau values of arbitrary large neighbors;
2. materializing `lambda_T(n)` by generic search.

For T=6 the statement `lambda_6(pq)=p` is structurally exact but does not give p
from N for free.  Brute-force search for lambda would merely repackage factor
search.

The route is therefore currently an opportunistic observer:

- if nearby numbers happen to factor cheaply/smoothly, their exact tau layers
  are cheap metadata;
- factor-forcing and strong-encoder layers can then be flagged at negligible
  additional cost;
- downstream BRC/multiplier experiments may use the flag, but must preserve an
  exact fallback and must not claim a factor unless an N-visible operation
  actually recovers it.

## 8. Connection to current BRC boundary work

A tau=6 neighbor usually has exponent shape `r^2 s`, while the source
squarefree semiprime has shape `pq`.  A close pair therefore satisfies a local
Diophantine relation of the form

`pq - r^2 s = d`, with small d.

This is not the same object as the hidden multiplier-boundary collision spectrum
already studied in T0_BRC, but both are examples where preserving a structured
boundary/layer spectrum matters more than a coarse count.  Any future bridge
must be N-visible; hidden factor-shape information is not itself an algorithm.

## 9. Decision

Retain as a research probe and candidate opportunistic observer:

`LOCAL COMPOSITE TAU SPECTRUM`
`-> FACTOR-FORCING TARGET TEST`
`-> STRONG 2^(k-1) r PRIME-LAYER ENCODER FLAG`.

Do not yet promote it as a factoring shortcut.  The next discriminating task is
to search for a cheap N-visible observable that predicts or certifies one of
these target layers without fully factoring the neighbor or the source.
