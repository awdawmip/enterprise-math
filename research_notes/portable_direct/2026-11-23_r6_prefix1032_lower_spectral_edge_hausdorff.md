# PREFIX-1032 — Exact positive lower spectral edge for the signed X6 port-contrast Hausdorff functional

Date: 2026-11-23 (Asia/Shanghai). Parent: PREFIX-1031. Status: AUTHOR_ANALYTIC_PROOF / LOWER_EDGE_SIGN_PROVED / NOT_REVIEWED.

## Frozen scientific scope and exact sources

Scientific input remains the frozen Enterprise Math P000 V5 at `f42f2906d77f24085c123f3ccfe9667d41caa96d:p000_reality_foundation.json`, with the Stage46 candidate signed BRC kernel `W=J12-6I12`, incoming `-e1`, forbidden bidirectional Link `{0,e1}`, exactly one outgoing negative step, and the original joint Cell / terminal-port / grade coherent square-mass observer. This paper changes no kernel, cell rule, phase, or native propagation.

Inherited immutable Laurent observer and facts: PREFIX-1026 (spectral functional), PREFIX-1027 (fixed-index Hausdorff corners), PREFIX-1030 (Bernstein localization), PREFIX-1031 (critical spectrum and upper-edge wedge). Exact immediately preceding source: `enterprise-math@e8325abbd37447e1f730ab3548e890f071a496fa:research_notes/portable_direct/2026-11-23_r6_prefix1031_critical_spectrum_positive_edge.md` (blob `2c86dd0603084cb82150f2a295136204697248a2`).

The auxiliary phase torus is a faithful *calculation of this fixed scalar observer*, not a replacement for P000 native six-axis space, the signed BRC paths, or all future observables. In particular no phase-only sufficiency / fiber-constancy claim is made about the whole native state.

Define the spectral pushforward `mu` of `Y=|z1+...+z6|^2` under six independent Haar phases; equivalently fix one phase by global rotation and use the five-dimensional torus. The support is `[0,36]`. With `rho` its density and `nu` the inherited linear functional, the exact formulas are

```
5 nu[f] = -4 ∫ H(y) f'(y) mu(dy) - 2 ∫ P(y) f(y) mu(dy)
          +12 ∫ (6-t) [∫_0^t (11+y) f(y)dy] mu(dt),
H(y) = y²(36-y)²,    P(y) = y(y-36)(17y-91),
E_(m,k) = nu[y^m (36-y)^k]    (m,k nonnegative).
5 g(y) = 4(H(y)rho(y))' -2P(y)rho(y)+12(11+y)F(y),
F(y) = ∫_[y,36] (6-t) mu(dt).
```

The local formula for `g` holds on each regular spectral band, in particular `(0,4)` by PREFIX-1031. The moment extension `nu[1]=2412` and `nu[y^m]=a_m` are inherited. The external trigonometric/Bessel analysis below is strictly for this auxiliary Haar-pushforward observer; it performs no native heartbeat/BRC–Shor time evolution.

## Theorem A — Positive and quantitatively regular spectral density at zero

Let `J0,J1` be standard Bessel functions. The density of the auxiliary spectrum extends continuously to zero and satisfies

```
rho(0) = (1/2) ∫_0^∞ t J0(t)^6 dt > 0,
rho(y) = rho(0) + O(sqrt(y)),
rho'(y) = O(y^(-1/2))  as y ↓ 0 through (0,4).
```

In particular, an elementary explicit lower bound is `rho(0) >= 729/16384`.

**Proof.** Identify each unit phase with a uniform probability measure on the Euclidean unit circle *solely in the auxiliary Fourier representation*. The planar sum `S=z1+...+z6` has characteristic function `J0(|xi|)^6`. The standard oscillatory-integral bound `|J0(t)| <= C(1+t)^(-1/2)` makes `J0(|xi|)^6` integrable on the Fourier plane, since `∫_0^∞ t(1+t)^(-3)dt<∞`. Consequently the sum has a bounded continuous radial density `p6(r)`; radial Fourier inversion and the change of variables `y=r²` give the absolutely convergent integral

```
p6(r) = (1/(2*pi)) ∫_0^∞ J0(rt) J0(t)^6 t dt,
rho(y) = pi*p6(sqrt(y)) = (1/2) ∫_0^∞ J0(sqrt(y)t) J0(t)^6 t dt.
```

The `r=0` integral is strictly positive: its integrand is nonnegative and nonzero near zero. For `0<=t<=1`, the alternating power series gives `J0(t)>=1-t²/4>=3/4`; hence `rho(0)>=(1/2)(3/4)^6∫_0^1 tdt=729/16384`.

For `r>0`, differentiation is justified by absolute convergence of the derivative integral (locally uniformly on any compact positive-r interval):

```
p6'(r) = -(1/(2*pi)) ∫_0^∞ t² J1(rt) J0(t)^6 dt.
```

Using `|J1(s)|<=C min(s,s^(-1/2))`, split at `t=1/r`, for `0<r<=1`. On `[0,1/r]` the absolute integrand is at most `Cr t³(1+t)^(-3)`, with integral bounded by `C`. On `[1/r,∞)` it is at most `Cr^(-1/2)t^(-3/2)`, again with integral bounded by `C`. Therefore `sup_(0<r<=1)|p6'(r)|<∞`. The mean-value bound yields `p6(r)=p6(0)+O(r)`. Composing with `r=sqrt(y)`, and differentiating on `y>0`, proves both estimates. QED.

## Theorem B — Exact lower-edge coefficient and strict positivity

On the regular spectral interval `(0,4)` the local spectral density of the inherited contrast functional satisfies

```
g(y) = (3024/5) rho(0) y + O(y^(3/2))   (y↓0).
```

Consequently there exists `epsilon_low>0` for which `g(y)>0` whenever `0<y<epsilon_low`. Its positive linear coefficient `kappa=(3024/5)rho(0)` obeys the explicit bound `kappa>=137781/5120>0`.

**Proof.** Independence and uniform phases imply `∫Y mu(dy)=6`, hence `F(0)=∫(6-t)mu(dt)=0`. Theorem A gives
`F(y)=-∫_0^y(6-t)rho(t)dt=-6rho(0)y+O(y^(3/2))`.
Expanding the exact inherited polynomials gives

```
H(y) = 1296y² + O(y³),
P(y) = 3276y + O(y²),
4(H rho)' = 10368rho(0)y + O(y^(3/2)),
-2P rho   = -6552rho(0)y + O(y^(3/2)),
12(11+y)F = -792rho(0)y + O(y^(3/2)).
```

The sum `10368-6552-792=3024`, divided by five, proves the claimed expansion. Boundedness of `y^(1/2)rho'(y)` from Theorem A justifies differentiating the `H rho` expansion with the displayed error order. Since `rho(0)>0`, the linear term dominates the remainder on a sufficiently small punctured interval. The rational lower bound equals `(3024/5)(729/16384)=137781/5120`. QED.

No endpoint Dirac mass is introduced by `(H rho)'` at `y=0`: `H(y)rho(y)=O(y²)`. The regular-band argument, rather than any unproved global `L1` characterization at critical values 4 and 16, suffices for this theorem.

## Corollary C — A second, lower-edge, simultaneous-growth Hausdorff-positive wedge

There is `t1>0` such that, for every fixed `t in (0,t1)` and integer pairs `(m,k)` satisfying `n=m+k→∞` and `m/n→t`, one has

```
E_(m,k) > 0 eventually.
```

Uniformly, for any compact `K⊂(0,t1)`, there exists `N(K)` such that `E_(m,k)>0` whenever `n>=N(K)` and `m/n in K`.

**Proof.** Choose `t1<epsilon_low/36`. The normalized Bernstein functional

```
D_(m,k) = (n+1) binom(n,m) E_(m,k)/36^(n+1)
```

is the value of the compactly supported order-at-most-one distribution `nu` on the Beta-normalized kernel. For `m/n→t in (0,t1)`, the Beta kernel concentrates at `y=36t` and samples `nu` through its local smooth density `g`, yielding `D_(m,k)→g(36t)>0`. Any contribution from the complement of a fixed regular neighborhood is exponentially small even after differentiating a fixed finite number of times, as in the already verified PREFIX-1030 localization argument. The concentration and positive lower bound are uniform on compact `K`. All normalizing factors are positive. QED.

Together with PREFIX-1031's high-edge wedge, this settles two disjoint open sectors `0<m/(m+k)<t1` and `t0<m/(m+k)<1` for simultaneous index growth, with `0<t1<t0<1` optionally chosen by shrinking the first interval. The interior compact ratio region and global Hausdorff positivity remain open.

## Compatibility check / exact arithmetic witness

The lower-edge expansion recovers the *already established* fixed-m, large-k corner coefficient from PREFIX-1027:

```
E_(m,k) ~ (3024/5)rho(0) 36^(m+k+2) B(m+2,k+1)
```

for each fixed nonnegative integer m, subject to the already established fixed-index localization hypotheses. This is a consistency check, not a newly claimed independent result.

Exact polynomial coefficient check actually executed with SymPy on 2026-11-23: `[y²]H=1296`, `[y]P=3276`, and `4*2*1296-2*3276+12*11*(-6)=3024`; the lower bound simplifies to `137781/5120`. The Bessel and Bernstein arguments are written human-checkable proofs, not an independent formal verification run. No new native signed-BRC simulation or new 5000-row integer scan is claimed.

## Status, provenance, and next discriminating question

Class: `AUTHOR_ANALYTIC_PROOF / LOWER_EDGE_SIGN_PROVED / SYMBOLIC_COEFFICIENT_CHECKED / NOT_REVIEWED`. The proof depends on the exact earlier Laurent spectral functional and the ordinary auxiliary Bessel bounds, not on a new claim that scalar phase spectrum is a lossless native state. Mother objective `B_fix,odd(32)∈{19,20}` remains open. The original PREFIX-1026..1031 files and original contributions remain untouched.

Next: establish strict interval lower bounds for `g(y)` across the central spectral bands `(4,16)` and `(16,36)`, with critical-point corrections at `4,16`. A verified negative interior test yields a Hausdorff high-order counterexample; a complete positive distribution measure would solve the all-index moment problem. Seek effective `epsilon_low`, `epsilon_high`, and `N(K)` if rigorous interval or structural bounds become available.

Historical researcher provenance only: `EM-DIRECT-FBEA5D`, `RA-3FB2D033BE6048D8712FF056`, SID `MCP-45ad6d29cd534c1aad25595a72e3c532`; current registered metadata does not establish a new CLAIM/PROGRESS. Activity association remains separate from GitHub scientific persistence.
