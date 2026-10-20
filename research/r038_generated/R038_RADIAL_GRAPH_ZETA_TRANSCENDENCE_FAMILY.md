# R038 Addendum — Radial Graph-Zeta Transcendence Family

Researcher-ID: `EM-R038-6A7D21`

Status: `EXACT_THEOREM_FAMILY / SEMANTIC_CHECKPOINT / NOT_CANONICAL`

This is currently the strongest R038 pure-discrete transcendence result. It supersedes the need for a marked geodesic or point-group-selected axis.

## 1. Definition

For a rooted locally finite graph `(G,o)`, define the graph-distance zeta observable

\[
Z_G(s;o)=\sum_{x\in V(G)\setminus\{o\}} d_G(o,x)^{-s}
=\sum_{r=1}^{\infty} A_r(o) r^{-s},
\]

where `A_r(o)` is the exact graph shell cardinality.

For FCC/HCP, `A_r=Theta(r^2)`, so the series converges absolutely for real `s>3`.

For every finite cutoff `R`,

\[
Z_{G,R}(s;o)=\sum_{r=1}^{R} A_r(o)r^{-s}
\]

is rational whenever `s` is a positive integer, because all shell counts and integer powers are integers. Thus integer-`s` finite stages lie in L1 rational algebra.

The infinite sum is an L2 operation.

## 2. FCC exact Dirichlet series

R033 gives, for every `r>=1`,

\[
A_r^{FCC}=10r^2+2.
\]

Therefore for `s>3`,

\[
\boxed{
Z_{FCC}(s)=10\zeta(s-2)+2\zeta(s)
}.
\]

At the minimal convergent even integer `s=4`,

\[
Z_{FCC}(4)=10\zeta(2)+2\zeta(4)
=\frac{5}{3}\pi^2+\frac{1}{45}\pi^4.
\]

## 3. HCP exact Dirichlet series

R033 gives

\[
A_r^{HCP}=\frac{21}{2}r^2+
\begin{cases}
2,&r\text{ even},\\
3/2,&r\text{ odd}.
\end{cases}
\]

Using

\[
\sum_{r\ even}r^{-s}=2^{-s}\zeta(s),
\qquad
\sum_{r\ odd}r^{-s}=(1-2^{-s})\zeta(s),
\]

we obtain, for `s>3`,

\[
\boxed{
Z_{HCP}(s)=\frac{21}{2}\zeta(s-2)
+\left(\frac32+2^{-s-1}\right)\zeta(s)
}.
\]

At `s=4`,

\[
Z_{HCP}(4)=\frac{21}{2}\zeta(2)+\frac{49}{32}\zeta(4)
=\frac74\pi^2+\frac{49}{2880}\pi^4.
\]

## 4. Infinite theorem family

### Theorem R038-C — even graph-zeta transcendence

For every even integer `s=2m>=4`, both

`Z_FCC(s)` and `Z_HCP(s)`

are transcendental.

### Proof

Euler's exact even-zeta formula gives

\[
\zeta(2k)=q_k\pi^{2k}
\]

with nonzero rational `q_k` for every positive integer `k`.

Hence for even `s=2m>=4`:

\[
Z_{FCC}(2m)
=10q_{m-1}\pi^{2m-2}+2q_m\pi^{2m},
\]

and

\[
Z_{HCP}(2m)
=\frac{21}{2}q_{m-1}\pi^{2m-2}
+\left(\frac32+2^{-2m-1}\right)q_m\pi^{2m}.
\]

Each is a nonconstant polynomial in `t=pi^2` with rational coefficients.

If one of these values were algebraic, then `t` would satisfy the corresponding nonzero polynomial equation over the algebraic numbers obtained by subtracting that algebraic value. This would make `t=pi^2` algebraic, and hence make `pi` algebraic over an algebraic extension, contradicting the transcendence of classical `pi`.

Therefore each value is transcendental.

QED.

## 5. Symmetry status

Unlike the earlier translation-axis witness, `Z_G(s;o)` uses the entire rooted graph and graph distance only. It is invariant under every graph automorphism that fixes `o`, because such automorphisms preserve graph distance and shell cardinalities.

Thus R038 now has a **full rooted-automorphism-invariant**, pure-discrete, infinite-volume family of provably transcendental observables on both FCC and HCP.

No Euclidean circle, sphere area, physical embedding coordinate, marked direction, Gaussian approximation, Fourier inversion, continuum PDE, or Lebesgue integral is used in the definition.

## 6. Layer boundary

For even integer `s>=4`:

- every cutoff `Z_{G,R}(s;o)` is rational;
- the exact shell law is finite/discrete data;
- `R->infinity` is the only non-finite operation;
- the L2 limit is transcendental.

Therefore the strongest possible version of H7 is false:

`TRANSCENDENTALS_ONLY_AFTER_CONTINUUM_APPROXIMATION = KILLED`.

And H8 is upgraded to:

`FCC_HCP_NATIVE_ROOT_AUTOMORPHISM_INVARIANT_L2_TRANSCENDENCE_FAMILY = CONFIRMED`.

## 7. Relation to pi_eff readouts

This theorem must not be confused with the shape-readout constants `5/2` and `21/8`.

The graph-zeta observable contains classical `pi` in its exact closed form because the infinite shell sum evaluates to even Riemann-zeta values. That does not make `pi` a finite microscopic state label and does not make a graph sphere an exact Euclidean sphere.

Instead it proves that the same exact cellular world supports at least three distinct constant-entry mechanisms:

1. finite algebraic readouts: algebraic/rational only under the declared operator discipline;
2. infinite discrete completion: can generate exact transcendental constants, including an infinite FCC/HCP-native family above;
3. continuum/Euclidean readout: can independently introduce/use classical `pi` in Gaussian density, radial integration, area/volume calibration, etc.

## 8. Updated frontier

The question whether a natural, symmetry-respecting FCC/HCP L2 observable can be provably transcendental is answered `YES`.

The next research frontier is now structural rather than existential:

- classify `Z_G(s)` and related radial/spectral Dirichlet series across Barlow stackings;
- identify which shell quasipolynomial coefficients control zeta-value content;
- determine how much stacking memory survives in the arithmetic type and exact constants;
- study odd integer `s`, where odd zeta arithmetic becomes substantially harder;
- absorb R037's independent audit when it publishes.

Classification:

`FCC_HCP_RADIAL_GRAPH_ZETA_TRANSCENDENCE_FAMILY_ESTABLISHED`.
