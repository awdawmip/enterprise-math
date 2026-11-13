# R749T — Exact four-step positive source transport and uniform all-p mixing

**2026-11-12.** Independent author-side continuation of R749S/R749N. TASK `RS-X6-TRIADIC-CLOSURE-DYNAMICS` remains held by its other active owner; no CLAIM/Result/native event license is asserted. Frozen science: `awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389`; R749N exact input at `e8c5c874aca5b7098acfdbaf8fadb8ad64a1506f`; R749S source at `34ba2817b9b45bd301804030931b2f484fae75d7`.

## Exact carrier and proposition

Reuse the 60 signed-Port pair vertices `V` and 16-regular undirected adjacency graph `G`, with 960 directed-edge states `D={(u,v):u~v}` from R749N. Each directed source `e=(u,v)` moves to `(v,w)` for one of the 16 neighbors `w` of `v`. The distinguished forced XOR neighbor `w=u△v` has probability `q=(1+15p)/16` and each of 15 alternatives has `r=(1-p)/16`. R749N proved that the stationary edge distribution `U_D` is uniform for every `p∈[0,1]`.

**Theorem 1 (full 960×960 four-step path count and primitive exponent).** Write `A` for the unweighted `60×60` adjacency matrix of `G`, and `M` for the **unweighted** `960×960` directed-edge transition adjacency (all 16 options count once). For every `n≥1` and `e=(u,v), f=(x,y)` in `D`,
```
M^n(e,f) = A^(n−1)(v,x).
```
Consequently `M^3(e,·)` vanishes at exactly 16 endpoints, while every entry of `M^4` is at least 16, and 16 is attained. The **minimal strictly positive power of M is exactly 4**.

**Proof of factorization:** A length-`n` path of directed-edge states is uniquely an adjacent vertex word `z0=u,z1=v,...,z_n=x,z_(n+1)=y`. For fixed starting and ending edges, the intermediate `z2,...,z_(n−1)` range over the `n−1`-step vertex walks from `v` to `x`. The final step `x→y` is fixed and legal by `f∈D`. Thus the counts agree, including `n=1` via `A^0`.

The precise classification of `A²(v,x)` and `A³(v,x)` depends only on the signed-axis incidence relation of the source vertex and target vertex, as follows. Fix `v={+E1,+E2}` by signed-axis transitivity, and enumerate `x` over the exact 60 admissible two-Port vertices:

| Target relation to v | Count of x | A²(v,x) | A³(v,x) |
|---|---:|---:|---:|
| Same signed pair | 1 | 16 | 112 |
| Same two axes, one sign reversed | 2 | 8 | 64 |
| Exactly one identical signed Port, other axis different | 16 | 7 | 98 |
| Same two axes, both signs reversed | 1 | 0 | 16 |
| Exactly one common axis but opposite signed Port on that axis | 16 | 1 | 46 |
| Two axes disjoint | 24 | 4 | 64 |

Each table entry is an exact integer neighbor-intersection calculation: `A²(v,x)=|N(v)∩N(x)|` and `A³(v,x)=Σ_(t∈N(x)) A²(v,t)`. The companion checker constructs every of the 60 vertex rows and verifies the displayed table for each of the 3600 pairs, giving a complete finite proof by exhaustive enumeration of this specifically finite carrier. Because the entries of `A³` are all positive and one entry of `A²` vanishes, the primitive exponent statement follows. This argument is also a direct all-960-edge proof through the factorization, rather than a few random-source samples.

At each directed source, the histogram of the 960 target path counts in `M^4` is:
```
M^4 path count:   16    46    64    98    112
target frequency: 16   256   416   256     16
```
The sum of all counted four-step words is exactly `16^4=65536`, confirming complete 16-way branching at every step.

## Theorem 2 — all-p Doeblin lower bound and ergodicity

For every `p∈[0,1)`, every pair `e,f∈D`, and `r=(1-p)/16>0`, each legal one-step branch has probability at least `r`. There are at least 16 distinct four-step branch words connecting `e` to `f`. Therefore

```
P_p^4(e,f) ≥ 16 r^4
          = (1-p)^4 / 4096
          = ε(p) U_D(f),
ε(p) = (15/64)(1-p)^4 > 0.
```

Since `U_D` is stationary, this is an exact **uniform Doeblin minorization**. For every initial probability measure `μ` and integer `n≥0`,
```
|| μ P_p^n − U_D ||_TV
 ≤ [1 − (15/64)(1-p)^4]^floor(n/4) · ||μ−U_D||_TV.
```

The proof is the standard elementary splitting: `P_p^4=ε 1 U_D+(1−ε)Q` for a stochastic `Q`; Markov operators contract total variation. Convergence is uniform over all 960 initial signed-source states for any fixed `p<1`. In the endpoint `p=1`, `P_1=F` has period-three deterministic source orbits, and the uniform distribution is stationary but not attractive from a point mass. This identifies the exact qualitative loss-of-mixing boundary in this finite candidate model.

## Theorem 3 — sharpened p=0 edge mixing and exact four-step TV

At `p=0`, all 16 legal next-source choices have probability `1/16`. Theorem 1 becomes

```
P_0^n((u,v),(x,y))
  = [A^(n−1)(v,x)] / 16^n
  = [T^(n−1)(v,x)] /16,
T=A/16,  n≥1.
```

Thus the 960-edge observer has exactly the same total variation from uniform after `n` steps as the 60-vertex random walk started from `v` after `n−1` steps:

```
||δ_(u,v) P_0^n−U_D||_TV
 = ||δ_v T^(n−1)−U_V||_TV   (n≥1).
```

By R749S's full 60-state spectral theorem, for `n≥2` the exact chi-square distance is

```
χ²(δ_(u,v)P_0^n || U_D)
 = 6 / 4^(n−1) + 14 / 16^(n−1) + 24 / 64^(n−1).
```

At four steps the displayed target histogram gives the exact total variation
```
||δ_e P_0^4−U_D||_TV
 = (1/2) Σ_(c∈{16,46,64,98,112}) mult(c) · |c/65536−1/960|
 = 487/3840.
```

At one edge step the exact chi-square is 59 (the `A` zero-eigenvalue sector contributes at initial vertex time zero), so `n≥2` is the correct scope of the spectral chi-square formula above.

## Evidence, representation boundaries, next question

The stdlib checker `R749T_FOUR_STEP_MINORISATION_CHECK.py` reconstructs exactly 60 vertex states, the 3600 pairs of `A²,A³`, the complete 960 target histogram, 16 unreachable three-step targets, positive four-step kernel, explicit 960-state four-step recursion for five diverse source edges, and four exact rational `p` cases. It emits `R749T_FOUR_STEP_MINORISATION_RESULTS.json`, uses integers and `fractions.Fraction`, and reports PASS. The complete finite 60×60 domain and bijection to 960×960 powers justify the global finite statement. The all-`p` theorem then follows algebraically without approximations.

The distinction remains typed: a signed Port here is a **signed axis/identity label**, not a signed force amplitude. The positive BRC path counts describe a candidate stochastic source observer; native Cell/Link/Port event permissions, actual `TRIADIC_CLOSURE_E` witnesses and physical time interpretation require separate source-certified bridge evidence. No existing X6 Task CLAIM or Foundation meaning is altered.

**Next scientific question:** exploit R749S's signed-axis character blocks, together with this all-`p` minorization, to derive sharper `p∈(0,1)` spectral/entropy mixing bounds, ideally reducing the 960×960 characteristic problem to lower-dimensional invariant blocks, while preserving the carried signed-source identity.
