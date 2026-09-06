# TASK #1162 — cyclotomic floor-Hall / factorial-ratio certificate for LCM

Status: `RESEARCH_FRONTIER / THEOREM CANDIDATE / NOT PROMOTED`
Researcher-ID: `EM-DIRECT-B62D`
At: `2026-09-06T21:23:00+08:00`

## Setup

Suppose a normalized even-character rotation kernel admits the finite cyclotomic/hyperbolic factorization

`h(z)=prod_d [sinh(d sqrt(z)/2)/(d sqrt(z)/2)]^(c_d)`, with integer exponents c_d.

Normalization in the quadratic-character examples gives `sum_d c_d=1` and `sum_d d*c_d=-2`.

Define the exact integer floor deficit

`H(x) = - sum_d c_d floor(d x)`.

## LCM via frequency matching

The logarithmic derivative of the hyperbolic product is a difference of Gaussian heat traces. Negative c_d contribute pole/supply frequency lattices and positive c_d contribute zero/demand lattices. If

`H(x)>=0 for every x>=0`,

then after sorting all frequencies, every demand frequency admits a supply frequency no larger than it. Hence each Gaussian supply weight is at least the matched demand weight for every heat time t>0. Therefore the pole heat trace dominates the zero heat trace, so `-d/dz log h(z)` is completely monotone and h is logarithmically completely monotone / infinitely divisible.

Because `sum d*c_d=-2`,

`H(x+1)=H(x)+2`.

Thus it is enough to check finitely many rational jump points on `0<=x<1`.

## Exact examples checked

The following fully cyclotomic positive fundamental quadratic examples all pass the exact integer floor test with minimum H=0 on the fundamental interval and period surplus 2:

- D=5: `{1:+1,2:+1,5:-1}`
- D=8: `{2:+1,4:+1,8:-1}`
- D=12: `{4:+1,6:+1,12:-1}`
- D=24: `{4:-1,6:+1,8:+1,12:+1,24:-1}`
- D=28: `{2:-1,4:+2,6:-1,12:+1,14:+1,28:-1}`
- D=60: `{6:-1,10:-1,12:+2,20:+1,30:+1,60:-1}`.

## p-adic / factorial-ratio bridge

Define

`Q_c(n) = prod_{c_d<0} (d n)!^(-c_d) / prod_{c_d>0} (d n)!^(c_d)`.

Legendre's formula gives exactly

`v_p(Q_c(n)) = sum_{k>=1} H(n/p^k)`.

Hence the same floor-Hall certificate implies `v_p(Q_c(n))>=0` for every prime p and n, so `Q_c(n)` is an integer for every n. This is the same floor mechanism as Landau-type factorial-ratio integrality.

Example D=24:

`(4n)!(24n)! / [(6n)!(8n)!(12n)!]` is integral for every n, and the same H certifies LCM of the associated rotation kernel.

## BRC significance

This route preserves exact integer exponent counts, floor histograms, and p-adic valuations before any transcendental heat/Laplace readout. It is therefore an exact integer-valued BRC certificate for a transcendental infinite-divisibility property.

## Boundary

Cyclotomic factorization of generalized Fekete polynomials is prior-art territory. No novelty is claimed for those factor tables or Landau's general factorial-ratio criterion. The project candidate is the precise bridge from the cyclotomic exponent carrier through floor-Hall matching / valuation nonnegativity to Gaussian heat domination and LCM of the finite-rotation kernel.

## Next

Decide whether every fully cyclotomic primitive quadratic Fekete kernel automatically satisfies H>=0, or construct a fully cyclotomic counterexample. If automatic, identify the structural reason in the exponent table rather than relying on case enumeration.
