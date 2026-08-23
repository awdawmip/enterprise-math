# Native Enterprise 7-Cell star：Poisson invariant and local coordinate self-localization

Status: `FREE_RESEARCH_EXACT_PRIME_FREE_LOCALIZATION / NOT_CANONICAL_FOUNDATION`

Date: `2026-08-23`

Researcher-ID: `EM-FREE-NEPS-239A6D`

## 1. Local star

Fix one internal Enterprise Cell under the tri-sector integer allocation. Let its integer label be `n` and let the six nearest incident-neighbor Cell labels, cyclically ordered, be

`E, NE, N, W, SW, S`.

In shell-fiber presentation `(r,t,sigma)`, the exact offsets are

- `E-n = 3r+sigma`;
- `NE-n = 6r+4+2sigma`;
- `N-n = 3r+1+sigma`;
- `W-n = -3r+3-sigma`;
- `SW-n = -6r+8-2sigma`;
- `S-n = -3r+2-sigma`.

These formulas are prime-free.

## 2. Constant graph Laplacian

Summing the six offsets gives exactly `18`. Hence

`E+NE+N+W+SW+S - 6n = 18`.

Equivalently the local six-neighbor average is always

`n+3`.

Thus the integer allocation satisfies a constant-source discrete Poisson law on the triangular Cell adjacency graph:

`Delta_triangle N = 18`.

This scalar is independent of `r,t,sigma`.

A direct reverse-traversal ablation gives the same value, so the scalar star Laplacian survives the allowed global side-orientation reversal.

## 3. Opposite-pair Hessian spectrum

Pair the six neighbors by geometric opposition:

- `(E,W)`;
- `(NE,SW)`;
- `(N,S)`.

Define

`H(pair)=u+v-2n`.

Then identically

- `H(E,W)=3`;
- `H(NE,SW)=12`;
- `H(N,S)=3`.

Therefore the unordered local directional-curvature spectrum is

`{3,3,12}`.

It is independent of `r,t,sigma`; reverse traversal leaves the same unordered spectrum. In particular, the star itself identifies one unique high-curvature opposite pair without requiring a globally named axis.

The elementary symmetric invariants are

- trace `18`;
- pair sum `81`;
- product `108`.

## 4. Opposite-pair gap spectrum

Let the absolute label gaps of the same three opposite pairs be sorted as

`g1 < g2 < g3`.

Writing `u=3r+sigma`, the exact values are

`g1=2u-3`,

`g2=2u-1`,

`g3=4u-4`.

Hence

`g2=g1+2`,

`g3=g1+g2`.

The unique curvature-12 pair is exactly the pair carrying `g3`.

## 5. Local recovery of shell and slot

From `g3` alone,

`g3 = 12r + 4sigma - 4`.

Therefore

`r = floor((g3+4)/12)`

and

`sigma = ((g3+4) mod 12)/4`.

Once `r` and `sigma` are recovered, the center label gives

`B_r = 1 + 3r(r-1)/2`,

`t = n - B_r - sigma*r`.

Thus the full exact presentation coordinate is locally reconstructible:

`CENTER + SIX NEIGHBOR LABELS -> (r,t,sigma)`.

No search over shells and no prior global coordinate tag is required.

The geometric shell index `r` is recovered from an unordered local star spectrum. The slot `sigma` remains a presentation coordinate and transforms with cyclic choice of start sector as expected.

## 6. Coordinate reconstruction consequence

Using the standard inverse chart:

- `sigma=0 -> (a,b,c)=(r-t,t,0)`;
- `sigma=1 -> (a,b,c)=(0,r-t,t)`;
- `sigma=2 -> (a,b,c)=(t,0,r-t)`,

the same seven labels recover the canonical Enterprise address of the center Cell.

So the integer allocation is locally self-describing with respect to the native Cell-incidence graph.

## 7. Relation to the prime-allocation program

This invariant does not use primality and therefore cannot be dismissed as a fit to the prime set. It gives a prime-independent geometric coordinate readout on which prime statistics may subsequently be conditioned.

The earlier 13-state prime loop code is Boolean. The star Poisson/Hessian readout is strictly richer: two stars with identical prime/composite bits can have different shell coordinates, while their integer star spectra recover `r` exactly.

Current classification:

`SEVEN_CELL_STAR_POISSON_SELF_LOCALIZATION = STRONGEST PRIME_FREE MULTI-CELL COORDINATE READOUT SO FAR`.

## 8. Boundary

Constant discrete Laplacians and finite-difference Hessians are classical constructions. No novelty claim is made for those general notions.

The research-specific object is the exact derivation from the native Enterprise tri-sector integer allocation and the resulting local recovery of the shell-fiber coordinate from one seven-Cell incidence neighborhood.
