# BRC Energy-Jet Bilinear Rank Optimality — Round 15

Status: `PROVED LINEAR-COORDINATE PRODUCT LOWER BOUND / CURRENT C-COORDINATE ACHIEVES BOUND / MICRO-OPTIMIZATION NEGATIVES`
Date: `2026-09-07`
Parent: `t0.brc_square_increment_scaled_cross_coordinate`

## 1. Question

After the scaled cross coordinate C was merged, several smaller execution ideas
were tested:

- remove the orbit return tuple and add allocation-minimizing slots;
- replace the bounded quotient/root repair loops by fixed comparison trees;
- special-case the frequent `e=nabla^3 q=0` event;
- transport square-gap cascade residues instead of using native `%`.

All are exact.  None produced a stable cross-bit-size full-pipeline improvement
large enough to justify another production path.  This raises the structural
question: is the remaining bounded-coefficient multiplication count already
minimal under ordinary linear coordinate changes?

Yes, in a precise bilinear model.

## 2. Variables and outputs

On one stride-8 source orbit, put

`e = nabla^3 q_new`,
`w = nabla^3 J_new`,
`a = nabla^2 q_new`.

These are bounded innovations.  Their inherited exact ranges are

`e in [-4,4]`,
`w in [-3,387]`,
`a in [-2,98]`.

For the N-sized state part use

`x=(J_new,q_new,s,t,u_new)`,

where

`s=nabla q`,
`t=nabla J`.

The scaled cross implementation computes two exact outputs.  Ignoring only
terms involving bounded innovations alone, their bilinear N-sized parts are:

### Energy third difference

`B_E = 2e J_new + 2e q_new + 2w q_new`.

### Scaled cross-coordinate increment

From

`C_new-C = 6s w + 6e(s+t) + 6a(2u_new+a)`,

the N-sized bilinear part is

`B_C = 6e s + 6e t + 6w s + 12a u_new`.

The discarded terms here are only bounded-by-bounded products such as `e^2` or
`a^2`; they are not the operations whose cost grows with N.

## 3. Flattening matrix

Order output/innovation rows as

`(E,e),(E,w),(E,a),(C,e),(C,w),(C,a)`

and N-sized columns as

`J,q,s,t,u`.

The combined bilinear map has flattening

```
[2 2 0 0  0]
[0 2 0 0  0]
[0 0 0 0  0]
[0 0 6 6  0]
[0 0 6 0  0]
[0 0 0 0 12]
```

Its rational rank is exactly

`5`.

The energy block alone has rank 2 and the C-update block alone has rank 3.

## 4. Product lower bound

Consider the execution class in which:

1. the retained state may be changed by an invertible linear coordinate
   transformation using already-retained exact coordinates;
2. each N-growing multiplication has the form
   `(bounded innovation linear form) * (N-sized state linear form)`;
3. arbitrary additions, bounded-only arithmetic and output linear combinations
   are free for the purpose of counting these growing products.

One such multiplication contributes a rank-one matrix to the displayed
flattening.  A sum of r such products has flattening rank at most r.

Since the exact map has rank 5,

`r >= 5`.

Therefore **at least five bounded-coefficient/N-sized multiplications are
required** in this model to compute the energy third difference and scaled
cross-coordinate update together.

## 5. Current implementation achieves the lower bound

The merged C-coordinate formulas use exactly five such products:

1. `e * 2*(J_new+q_new)` for the energy output;
2. `2*w*q_new` for the energy output;
3. `6*e*(s+t)` for C transport;
4. `6*w*s` for C transport;
5. `12*a*u_new` inside `6*a*(2u_new+a)` for C transport.

Everything else in those two formulas is addition or bounded-only arithmetic.
Thus the current scaled cross formulation reaches the rank lower bound.

This explains why the post-Round-14 algebraic micro-optimizations only move
finite Python timings by a few percent: within this coordinate/operation model
there is no sixth-to-fifth product left to remove.

## 6. Important scope boundary

This is **not** an unconditional arithmetic-circuit lower bound for every
possible BRC implementation.

The proof does not exclude:

- retaining new nonlinear provenance coordinates that encode additional future
  cross-products;
- exploiting exact nonlinear relations among quotient/root innovations beyond
  the declared independent bilinear model;
- batching several multiplier transitions and sharing work across them;
- hardware fused operations, SIMD/vectorization or a different big-integer
  representation;
- replacing multiplication by architecture-specific shift/add operations.

It says something narrower and useful:

`SAME EXACT INFORMATION + INVERTIBLE LINEAR COORDINATE CHANGE`
`-> CANNOT REDUCE THE FIVE GROWING BILINEAR PRODUCTS BELOW FIVE`.

So another M/K/C-style linear recombination is not a promising research attack.

## 7. Post-merge negative execution probes

Several exact implementation variants were checked after the scaled coordinate
was derived.

### Allocation-free orbit/scanner path

Removing the six-element orbit return tuple and adding slots produced mixed
results: small gains in some cohorts and parity/slight regressions in others.
No stable production promotion.

### Fixed quotient/root comparison trees

The proved quotient repair `epsilon in [-4,4]` and root correction count <=2
allow fully unrolled comparison trees.  In CPython these saved a few percent at
smaller bit sizes but became neutral or slower for larger integers because the
extra thresholds and temporaries outweighed the tiny loop overhead.

### e=0 fast path

Finite random tails showed `e=0` on roughly one third to two fifths of visits.
The exact specialization removes the e-dependent terms, but branch overhead and
cohort variation prevented a stable full-range gain.  The theorem continues to
retain the full `[-4,4]` range.

### Cascade-residue / 2-adic front paths

These remain mathematically exact and zero-false-negative but filtering is no
longer the dominant cost after the energy jet.  They remain held back by
end-to-end timing.

## 8. Reproducible certificate

`experiments/brc_energy_bilinear_rank_check.py` performs exact rational Gaussian
elimination on the flattening, checks ranks 2, 3 and 5, and reconstructs the
matrix from the five rank-one products used by the current formulation.

No numerical fit or random-rank inference is used.

## 9. Decision / next frontier

Record the rank-five result as a **research boundary**, not a new executable
subtool or Foundation theorem.

Do not spend another cycle merely searching for an invertible linear
recombination of the current energy-jet coordinates to remove one more growing
multiplication.

The next credible directions must change one of the model assumptions:

1. batch multiple retained multiplier transitions and look for cross-step shared
   arithmetic;
2. add a genuinely nonlinear retained coordinate only if its update is cheaper
   than the product it removes;
3. move below Python-level arithmetic and test whether fixed bounded
   coefficients admit a specialized limb/shift-add implementation.

Any such direction must preserve the exact quotient remainder, root remainder,
finite-difference bounds and zero-false-negative square-gap semantics.
