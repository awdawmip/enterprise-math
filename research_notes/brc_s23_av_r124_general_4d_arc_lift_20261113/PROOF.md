# R124 — Four-integer lift for arbitrary directed half-open S23 multi-time signatures

Date: 2026-11-13 (Asia/Shanghai). Scope: auxiliary S23 ranked Boolean observer, author-side result. Predecessor R123 frozen proof commit `c5e7cb5aaa31be2d12f261c9efd6db9e5563fc9c`. Frozen scientific input is unchanged: `43ec6098b1330ae86d0a7863be336c5d97f6ef34`.

## 1. Statement

Fix integers `j,a,c,N,d`, with `d != 0`, rational `x`, an open rational parameter interval `J=(l,h)`, and `m>=2`. For each `i=0,...,m-1` put

```
Y_i(theta) = x + (N+i*d-j)*theta
M_i(theta) = 1_{ frac(Y_i) in [frac(a*theta),frac(c*theta))_directed }
```

The directed positive circle arc includes its start and excludes its end; **coincident endpoints yield the empty arc**. Given any prescribed bit word `b in {0,1}^m`, exact existence of a *single* `theta in J` satisfying all bits reduces to at most `3*2^m*|P_m|` rational integer-linear feasibility systems in **four integer variables**, where `P_m` is the finite mechanical-word vocabulary

```
P_m = { (floor(alpha+i*beta))_{i=0}^{m-1} : 0<=alpha,beta<1 }.
```

Its known size is `|P_m| = 1 + sum_{r=1}^{m-1}(m-r)*phi(r) = Theta(m^3)` (R121, classical finite Sturmian factor count). Each resulting system is exactly decidable by fixed-dimension integer programming in bit complexity polynomial in the binary input length, including the magnitudes of `a,c,j,N,d`. A feasible system yields a **rational theta witness**. In particular, for fixed `m`, no enumeration proportional to `|a|, |c|, |d|, |N|` is required. The statement concerns *attained Boolean signatures*, not their possibly numerous connected components.

If `J` is a singleton rational point, evaluate the original fractional-circle predicate there directly. For old histories, apply this oracle separately on each already-certified old-signature open atom and retain the exact old provenance and rank-history identity. This does not assert an operation in native X6 Cell/Link/Port dynamics.

## 2. Four integer variables and the mechanical word

Write the four integer variables

```
n = floor(x+(N-j)*theta),    k = floor(d*theta),
r = floor(a*theta),          s = floor(c*theta).
```

Set `alpha=Y_0-n`, `beta=d*theta-k`, `u=a*theta-r`, `v=c*theta-s`. All four fractional quantities lie in `[0,1)`. Since `Y_i=Y_0+i*d*theta`,

```
q_i = floor(alpha+i*beta),
z_i = Y_i - n - i*k - q_i = frac(Y_i).
```

For each candidate word `q in P_m`, its realization is equivalent to the following **linear** inequalities in the real unknown `theta` and four integer unknowns `n,k,r,s`:

```
l < theta < h;
0 <= d*theta-k < 1,      0 <= a*theta-r < 1,
0 <= c*theta-s < 1,      0 <= z_i < 1 for all i.
```

Here `q_0=0`, so the `i=0` inequality also enforces `n=floor(Y_0)`. A candidate word not actually realizable with the selected data is automatically rejected by these constraints.

## 3. Directed-arc disjunction, including equality and half-open boundaries

All symbols `u,v,z_i` in this section are rational-affine in the continuous variable and integer variables. Split into one of three exact cases.

- `u<v`: bit 1 iff `u<=z_i<v`; bit 0 iff `z_i<u` OR `z_i>=v`.
- `u>v`: bit 1 iff `z_i>=u` OR `z_i<v`; bit 0 iff `v<=z_i<u`.
- `u=v`: the arc is empty, so every bit is 0.

For a fixed bit pattern, each of the `m` bits chooses at most two affine conjunctive branches; the endpoint-order case has at most three possibilities. Therefore there are at most `3*2^m` systems per mechanical word. **Every inequality retains its strict or weak sense**. Empty endpoint segments are eliminated by ordinary feasibility rather than by assumptions about positive width. This also handles isolated theta values where the two arc endpoints coincide.

Conversely, every feasible branch has `0<=z_i,u,v<1`, the exact mechanical-floor identities, and the directed-arc inequalities for the selected bits, so the original predicate holds for the recovered theta. Every original theta has a unique `n,k,r,s,q` and belongs to one of the three endpoint-order cases, so no original signature is missed.

## 4. Exact projection and bit complexity

A branch is a finite family of rational affine constraints

```
A*theta + B*n + C*k + D*r + E*s <= F
```

or the same with `<` or `=`. Eliminate `theta` by taking the maximum of all affine lower bounds and minimum of all upper bounds, and comparing every lower/upper pair. The comparison is strict iff at least one endpoint is excluded. Zero-theta-coefficient constraints are retained. This elementary Fourier–Motzkin step yields rational affine constraints on only `n,k,r,s`, with polynomially many inequalities and polynomial coefficient bit growth. Integer-scale each rational inequality; a strict inequality `L(z)<H` becomes `L_int(z)<=H_int-1` after clearing positive denominators, since the left and right sides are integers.

A fixed-dimensional integer-programming algorithm (e.g. Lenstra's theorem for dimension 4) decides feasibility in polynomial bit complexity. To construct the original theta, substitute a feasible integer tuple into the unprojected affine bounds: choose a rational midpoint when the lower bound is smaller than the upper, or their common rational value when they coincide and both are weak. This theta is checked against the original predicate.

This is a **polynomial-time reduction** and a theoretical fixed-dimension solver guarantee, not a claim that our Python checker implements Lenstra's algorithm. The computational cost includes word generation, all branch systems, integer-programming coefficient/bit costs, witness recovery, and any old-atom preparation. For one bit pattern the upper bound is `O(2^m*m^3*poly(m,B))`; deciding all patterns adds an output-related factor `2^m`. No uniform polynomial bound in `m` is asserted for exhaustive output.

## 5. Verified finite implementation cross-check

`check_r124.py` is a standard-library Python `fractions.Fraction` reference checker. For small signed inputs, it **exhaustively** enumerates `r,s,n,k,q`, generates the exact linear inequalities and tests rational interval feasibility. Independently it enumerates all original fractional-circle phase-cut atoms from

```
a*theta, c*theta, (a-c)*theta,
Y_i(theta), Y_i(theta)-a*theta, Y_i(theta)-c*theta
```

and checks both singleton cuts and open gaps. It compares every bit pattern `m=2,3` and two explicit `m=4` inputs. The checker thereby tests the lifting and endpoint semantics; the polynomial bit bound relies on the fixed-dimension theorem rather than on its small-range enumeration implementation.

Actual run: `R124_PASS` with 87 cases, 532 complete signature queries, 4,659 executed lift-disjunct tests and 2,469 direct phase-atom representative samples (seed 1242026). Two additionally evaluated **positive** exact certificates use signed 101/111-digit `N` and 91/106-digit `d` with `m=4`. Full counters and inputs are in `verification_r124.json`. These large cases do not test a generic ILP decision procedure or certify infeasibility.

## 6. Relation to existing frontier, provenance and next unit

R118 covered arbitrary one-time directed arcs; R119.2 handled two times with relative-cut enumeration, and R120–R123 developed two-integer lifts / exact floor-sum solving for the simpler `a=j=0,c=1` case. R124 instead retains the additional endpoint floors as **two more integer coordinates** and uses the established fixed-dimension integer-feasibility theorem. This gives a uniform arbitrary-endpoint reduction with logarithmic dependence on signed phase coefficients for fixed `m`, while R123's specialized two-integer floor-sum solver can remain faster in its applicable case.

Next R125: implement a genuinely constructive four-integer feasibility routine (or a rational-structure specialization), compare full bit-operation and memory costs against R123 in its common domain, and test whether some endpoint-floor coordinates can be eliminated by bounded-dimensional transformations. Preserve the distinct author proof, finite implementation tests and independent review status.

Status: author-side mathematical reduction with finite exact cross-check; independent project review and formal Task CLAIM not established.
