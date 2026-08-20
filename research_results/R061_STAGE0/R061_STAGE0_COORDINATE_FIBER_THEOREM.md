# R061 Stage 0 — Coordinate Fiber Theorem

Task: `RS-R061-STAGE0-ENTERPRISE-LINE-FORMULA-ALGEBRAIC-PATH-LIFT-VALIDATION`  
Source: `0936ade269bcdc3a58b3d8b4c2148c6197dc1a63`

## Status

`COORDINATE_FIBER_COMPLETE = true`

`ALGEBRAIC_FACTOR_EXTRACTION_COMPLETE = true`

This theorem is sector-local and algebraic. It uses the current native law
`L_E(a,b,0)^2=a^2+b^2`; it does not import a carrier Euclidean metric.

## 1. Ground-truth fiber

For `N in N_0` define

`D_N={(a,b) in N_0^2 : a^2+b^2=N}`.

For `N=0`, `D_0={(0,0)}`.

For `N>0`, direct exact enumeration is obtained by looping
`0<=a<=floor(sqrt(N))`, testing whether `N-a^2` is an integer square, and
including the ordered leg swap. This is only checker semantics.

## 2. Factor/norm extraction in A_E

Let

`A_E = Z[J]/(J^2+1)`

and

`Norm_E(a+bJ)=(a+bJ)(a-bJ)=a^2+b^2`.

As a ring, `A_E` is the Gaussian-integer Euclidean domain. Write the ordinary
integer factorization

`N = 2^e0 * product_i p_i^e_i * product_j q_j^f_j`

with `p_i == 1 (mod 4)` and `q_j == 3 (mod 4)`.

The rational primes behave as follows in `A_E`:

- `2` ramifies, associated to `(1+J)^2`;
- every `p_i == 1 (mod 4)` splits as `p_i=pi_i * conjugate(pi_i)` with
  `Norm_E(pi_i)=p_i`;
- every `q_j == 3 (mod 4)` remains prime.

Hence `D_N` is empty exactly when some `f_j` is odd. Otherwise every signed
Gaussian integer of norm `N` is, up to a unit `epsilon in {+1,-1,+J,-J}`,

`epsilon * (1+J)^e0
 * product_i pi_i^t_i conjugate(pi_i)^(e_i-t_i)
 * product_j q_j^(f_j/2)`

for independent choices `0<=t_i<=e_i`.

Taking the coefficient pair, then absolute values, then deduplicating produces
exactly all ordered nonnegative pairs in `D_N`.

### Completeness

Unique factorization in `A_E` forces every factor of an element `z` with
`Norm_E(z)=N` to occur in exactly one of the three prime behaviors above.
A `q_j==3 mod 4` factor must occur symmetrically in `z` and its conjugate, so
`f_j` is even. For a split prime, choosing how many copies of `pi_i` lie in `z`
and how many conjugate copies lie in `z` is exactly the integer `t_i`. Units
account for sign/order rotations. Therefore no norm solution is omitted.

### Deduplication

Different factor choices may become associates or conjugates. The exact
sector fiber is the set of resulting ordered nonnegative coefficient pairs,
not the raw factor-choice multiset. Set-deduplication after units/conjugation
is therefore required and sufficient.

## 3. Euclid cross-check for N=r^2

For a nondegenerate integer solution

`a^2+b^2=r^2`, `a,b>0`,

let `d=gcd(a,b)` and divide by `d`. The resulting primitive integer
Pythagorean triple has, up to leg swap,

`a'=m^2-n^2`,
`b'=2mn`,
`r'=m^2+n^2`

for unique admissible parameters with

- `m>n>0`;
- `gcd(m,n)=1`;
- `m` and `n` of opposite parity.

Multiplying by `k=d` gives every nonprimitive triple:

`a=k(m^2-n^2)`,
`b=2kmn`,
`r=k(m^2+n^2)`.

This is used only as an integer theorem. It does not reinterpret the carrier
120-degree presentation as a classical 90-degree angle.

## 4. Deterministic validation

The committed checker validates:

- every `N=0..100000`;
- direct enumeration versus factor/norm extraction;
- every square `N=r^2` with `0<=r<=4096`;
- direct nondegenerate solutions versus complete Euclid generation.

Results:

- factor/norm mismatches: `0`;
- Euclid square-case mismatches: `0`;
- canonical fiber digest:
  `0f4bccc2ff3fd7e7ae22ccd9e4abf248cf215bffea7bdd02aabca9b8c2bb8338`.

Aggregate `N=0..100000` classes:

- empty fiber: `75972`;
- axis-degenerate present: `317`;
- exactly one nondegenerate branch up to swap: `13034`;
- at least two nondegenerate branches up to swap: `10840`;
- has primitive nondegenerate branch: `14581`;
- has nonprimitive nondegenerate branch: `10242`;
- square `N`: `317`;
- nonsquare `N`: `99684`.

Selected exact fibers:

- `D_3 = empty`;
- `D_25={(0,5),(3,4),(4,3),(5,0)}`;
- `D_65={(1,8),(4,7),(7,4),(8,1)}`;
- `D_4225` contains axis branches and four inequivalent nondegenerate
  branches up to swap:
  `(16,63),(25,60),(33,56),(39,52)`.

The full mandatory-case census is in
`R061_STAGE0_COORDINATE_FIBER_CENSUS.json`.
