# R038 Addendum — Point-Group-Symmetrized Native L2 Witness

Researcher-ID: `EM-R038-6A7D21`

Status: `EXACT_THEOREM_ADDENDUM / SEMANTIC_CHECKPOINT / NOT_CANONICAL`

This strengthens `R038_NATIVE_L2_TRANSCENDENCE_WITNESS.md` by removing dependence on one arbitrarily selected translation axis.

## 1. Axis observable

For a bi-infinite nearest-neighbor translation axis `ell` through a root `o`, define

\[
S(\ell)=\sum_{x\in\ell\setminus\{o\}}\frac{1}{d_G(o,x)^2}.
\]

The previous addendum proves, using integer 1-Lipschitz graph heights, that every axis in the relevant FCC/HCP translation-axis orbit satisfies

\[
S(\ell)=2\sum_{n=1}^{\infty}\frac1{n^2}=\frac{\pi^2}{3}.
\]

## 2. FCC point-group symmetrization

The FCC root has 12 NN directions, paired into 6 undirected straight NN translation axes. The FCC crystallographic point group permutes these 6 axes transitively.

Let `A_FCC(o)` be this 6-element orbit and define

\[
S_{FCC}^{PG}(o)=\sum_{\ell\in A_{FCC}(o)}S(\ell).
\]

Then

\[
\boxed{S_{FCC}^{PG}(o)=6\cdot\frac{\pi^2}{3}=2\pi^2}.
\]

This rooted observable is invariant under the FCC point group. Because `2pi^2` is transcendental, point-group symmetrization does not remove the L2 transcendence gateway.

## 3. Ideal-HCP point-group symmetrization

In ideal HCP, the six in-layer triangular NN directions form 3 undirected basal NN translation axes. The HCP crystallographic point group preserves the basal plane and permutes these 3 axes transitively.

Let `A_HCP,basal(o)` be this 3-element orbit and define

\[
S_{HCP}^{PG}(o)=\sum_{\ell\in A_{HCP,basal}(o)}S(\ell).
\]

Then

\[
\boxed{S_{HCP}^{PG}(o)=3\cdot\frac{\pi^2}{3}=\pi^2}.
\]

This rooted observable is invariant under the HCP crystallographic point group and is transcendental.

## 4. Interpretation

The first native L2 witness could be challenged as depending on a marked axis. The symmetrized version shows that this is not merely a single-axis accident:

- FCC admits a rooted point-group-invariant exact L2 observable equal to `2*pi^2`;
- ideal HCP admits a rooted point-group-invariant exact L2 observable equal to `pi^2`.

No continuum geometry, Euclidean circle area, Gaussian limit, or Fourier integral is part of the observable definition. Only the discrete contact graph, its crystallographic translation/point-group action, graph distance, rational finite-stage weights, and the infinite completion are used.

The remaining naturalness frontier is therefore narrower:

`POINT_GROUP_INVARIANT_L2_TRANSCENDENCE` is established;

what remains open in R038 is whether a comparably elementary **fully unmarked / full-automorphism-invariant bulk observable** is forced to a provably transcendental exact value.

## 5. Layer audit

For finite cutoff `N`, each symmetrized partial sum is rational:

FCC:
\[
S_{FCC,N}^{PG}=12\sum_{n=1}^{N}\frac1{n^2}\in\mathbb Q.
\]

HCP:
\[
S_{HCP,N}^{PG}=6\sum_{n=1}^{N}\frac1{n^2}\in\mathbb Q.
\]

Only the `N->infinity` L2 completion produces `2*pi^2` and `pi^2`, respectively.

Classification:

`POINT_GROUP_INVARIANT_FCC_HCP_L2_PROVABLY_TRANSCENDENTAL_WITNESS`.
