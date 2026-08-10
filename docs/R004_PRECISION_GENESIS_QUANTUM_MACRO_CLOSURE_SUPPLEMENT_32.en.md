# R004 precision genesis — Supplement 32: fractionless COUNT coupling basis and Smith birth spectrum

Status: `PROVED_WIP + EXECUTABLE_REFERENCE + COUNT-COUPLING SPECIALIZATION`
Parent: `R004_PRECISION_GENESIS_QUANTUM_MACRO_CLOSURE_SUPPLEMENT_31.en.md`
Owner branch: `research/r004-precision-genesis-closure-20260810`

Supplement 31 gave typed liveness gates for joint couplings. This supplement specializes exact COUNT semantics and constructs an integer basis for the information left after one-way marginals.

## 1. Marginal-star / coupling-cell split

Let the joint COUNT tensor have shape `(n_1,...,n_m)` and choose one base value on each axis. A **star cell** is the base cell or differs from the base on exactly one coordinate. A **coupling cell** differs on at least two coordinates.

The number of star cells is

`1 + sum_i (n_i-1) = sum_i n_i-(m-1)`,

and the number of coupling cells is

`d_coup = prod_i n_i - sum_i n_i + (m-1)`.

The one-way marginal incidence map has integer rank `sum_i n_i-(m-1)`. The quotient of the free joint-cell lattice by the marginal row lattice is therefore free of rank `d_coup`.

## 2. Fractionless reconstruction

Retain all one-way marginals plus the counts on all coupling cells. Every single-change star cell is recovered by integer subtraction from its one-way marginal; the base cell is recovered by subtracting every non-base cell from the total count.

Thus the exact joint COUNT table is reconstructed with integer additions/subtractions only. No probability, ratio, normalization or division is primitive.

## 3. Integer coupling residual

For an integer query coefficient tensor `c`, define its marginal-separable interpolation from the base/star cells by

`c_hat(y)=c(base)+sum_i(c(star_i(y_i))-c(base))`.

The residual `r_c=c-c_hat` vanishes on all star cells. Restricting `r_c` to the coupling cells gives an integer quotient coordinate whose kernel is exactly the marginal row lattice.

Therefore coupled COUNT queries modulo the information already carried by marginals are represented by an integer residual matrix on `d_coup` coupling coordinates.

## 4. Smith birth spectrum

Let the nonzero integer Smith invariants of a residual query matrix be `d_1,...,d_r`. At p-adic cap K the active depth of direction j is

`e_j(K)=max(0,K-nu_p(d_j))`.

It first becomes visible at `K_birth(j)=nu_p(d_j)+1`. The total coupling mass is

`mu_K=sum_j max(0,K-nu_p(d_j))`.

Hence `mu_(K+1)-mu_K = #{j: nu_p(d_j)<=K}`, and the second finite difference counts directions born at the new precision layer.

For the 2x2 equality-count query the residual is the single coefficient `2`. It is invisible modulo 2, has depth 1 modulo 4, depth 2 modulo 8, and has full depth at odd primes.

## 5. Coordinate nonuniqueness, structural invariance

Changing the base tuple changes the explicit coupling-cell coordinates, but every base gives an integral splitting of the same quotient lattice. The change of primitive coupling coordinates is unimodular. Smith invariants and therefore the p-adic birth spectrum are base-independent.

## 6. Validation

Independent exact checks from the research session include exact marginal reconstruction for small 2D/3D shapes, exhaustive COUNT-query liveness checks from Supplement 31, Smith-invariant agreement across every base choice for 400 random query families, and the explicit 2x2 equality residual equal to 2.

This is a compiler specialization of integer marginal lattices and Smith normal form, not a novelty claim for contingency-table algebra.

## 7. Consequence

Joint COUNT coupling has a primitive fractionless instruction surface:

`one-way marginals + d_coup coupling counters`.

For a declared query family, the residual Smith profile can be strictly smaller than the full `d_coup` surface. Coupling distinctions therefore have precision-dependent birth layers rather than existing as one all-or-nothing correlation object.
