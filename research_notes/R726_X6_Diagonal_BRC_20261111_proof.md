# R726 — Sharp finite-length diagonal fibers and signed BRC orientation repair

Author-side exact mathematics, 2026-11-11. Parent scientific line: `RS-X6-TRIADIC-CLOSURE-DYNAMICS`, publication `TP2-8B7E13C5904A2D6F1142`. Scientific input remains pinned at `awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389`. Previous author-side frontier R725, PR #2100, commit `65ffaaeaad239af801be072a7795a54c387f504d`. No formal claim, Result, independent Driver review, or FORCE/V29/V39 promotion is asserted by this note.

## Question and typed carrier

For the signed X6 Cell torsor, let `U={+e_i,-e_i:0<=i<6}`. Set `W_L={sum of L ordered members of U}`, the possible **net signed Cell displacements after exactly L primitive coordinate steps**. Keep the full Path-formal/BRC branch trace when needed; a displacement is only its endpoint. The **joint complete relative observer** is `pi(v)=v mod Delta`, with `Delta=Z*(1,1,1,1,1,1)`. It can equivalently be represented by `can6(v)` or by all twenty complete three-axis `can3` coordinate readouts. This is *not* the coarser twenty-bit change mask `b(v)` of R725.

Source reuse: `definitions/ENTERPRISE_X6_NATIVE_SPATIAL_CELL_TORSOR_20260905.md` already fixes the X6 quotient, integer common-depth repair and exact signed N-BRC path-count formula. This note newly optimizes the **finite-length** common-depth index and identifies a signed/unsigned BRC contrast; it does not rename an existing foundational quotient as a new one.

## Theorem 1 — optimal length-L repair bits

For every integer L>=0, the largest fiber of `pi|W_L` has exactly

```
M(L) = floor(L/3) + 1.
```

Consequently, when L and the complete joint relative observer are known, the smallest possible **fixed-length worst-case auxiliary binary code** recovering the full signed X6 net displacement uses exactly

```
B(L) = ceil(log2(floor(L/3)+1)) bits.
```

For L=0, B(0)=0. This is information for *net displacement*; the number of bits recovering an ordered signed path is separately larger. The code is an index within the finite compatible diagonal fiber; it is not a fixed global yes/no observation.

**Proof.** First,

```
W_L = {v in Z^6 : ||v||_1 <= L and ||v||_1 = L (mod 2)}.
```

Necessity follows from L signed unit steps; sufficiency uses `||v||_1` directed steps followed by cancelling pairs. If v+t1 and v+s1 both belong to W_L, the triangle inequality gives

```
6|t-s| = ||(v+t1)-(v+s1)||_1
        <= ||v+t1||_1 + ||v+s1||_1 <= 2L,
```

hence the integer t-range spans at most `floor(L/3)`, so it contains at most M(L) points.

For sharpness put k=floor(L/3), and choose three coordinates equal to `-floor(k/2)` and three equal to `-ceil(k/2)`. At t=0 and t=k the 1-norm is `3k`; for each 0<=t<=k, convexity of the 1-norm bounds it by `3k`. If `L-3k=0 or 2`, the norm parity already agrees with L. If `L-3k=1`, increase one coordinate of the base vector by one: the 1-norm at every t increases by at most one, remains <=3k+1=L, and its parity flips. Translating all six coordinates by t changes the 1-norm by an even parity (`6t mod 2=0`), so every t=0,...,k is reachable by exactly L primitive steps. Hence M(L) is attained. Distinguishing M(L) possibilities requires at least ceil(log2 M(L)) bits; an index achieves the bound. QED.

The existing full integer repair can be written equivalently as `sigma(v)=sum_i v_i`; for `r=can6(v)` one has `v=r+h1` with `h=(sigma(v)-sum_i r_i)/6`. Thus `(r,sigma)` is lossless, and the finite-length index encodes the bounded set of admissible h values without changing native Cell identity.

## Theorem 2 — R725's 20 invisible pairs survive every unsigned N-BRC endpoint count

For any 3-subset H of {0,...,5}, define

```
v_H = sum_{i in H} e_i,
w_H = -sum_{j not in H} e_j.
```

These are distinct W_3 states with `v_H-w_H=1`, so every joint min-zero coordinate observation, every R725 terminal-change mask and every future **coordinate** continuation sees the same relative class.

Let `N_M(x)` count ordered signed-axis paths of length exactly M with endpoint x, using the established unweighted signed N-BRC path semantics. For every **odd M>=3**,

```
N_M(v_H) = N_M(w_H).
```

Indeed a permutation interchanging H and its complement followed by global sign reversal is a bijection of the signed-step alphabet, of all ordered words and of their endpoints `v_H <-> w_H`; hence it gives a path-by-path cardinality-preserving bijection at every length M. The short examples are `N_3=6`, `N_5=540` for both endpoints. Thus even retaining the complete unweighted endpoint multiplicity as an extra scalar does not separate these 20 source aliases.

Define the **signed orientation character** of an individual path `P=(u_1,...,u_M)` by

```
sigma(P) = sum_{t=1}^M sum_{i=0}^5 (u_t)_i
         = number_of_positive_steps - number_of_negative_steps
         = sigma(endpoint(P)).
```

The formal signed BRC endpoint polynomial `C_M(x;q)=sum_{P:end(P)=x} q^{sigma(P)}` therefore equals `N_M(x) q^{sigma(x)}`. For the pairs,

```
C_M(v_H;q) = N_M(v_H) q^3,
C_M(w_H;q) = N_M(v_H) q^(-3).
```

These differ as Laurent monomials for an indeterminate q. On `W_3`, a **single orientation bit**, e.g. the sign of sigma when the diagonal fiber has two members, separates all 20 ambiguous classes; one bit is information-theoretically optimal because those classes have two members. This is the signed/provenance-preserving correction; positive total-mass collapse loses it. It is a mathematical observability construction, **not an assertion that V29 or V39 physically reads this bit**. QED.

## Exact validation

Companion stdlib script enumerates **every** W_L for L=0..7 by recursion in signed Z^6, groups by pi, checks the sharp maximum and emits complete fiber-size histograms. It checks each of the 20 ordered complementary-pair witnesses, exact N_3 and N_5 counts by finite rational-coefficient formula, and the +/-3 signed orientation. All arithmetic is exact. Expected marker: `R726_DIAGONAL_BRC_FIBERS_EXACT_PASS`.

| L | |W_L| | joint-relative classes | largest diagonal fiber | optimal repair bits |
|---:|---:|---:|---:|---:|
| 0 | 1 | 1 | 1 | 0 |
| 1 | 12 | 12 | 1 | 0 |
| 2 | 73 | 73 | 1 | 0 |
| 3 | 304 | 284 | 2 | 1 |
| 4 | 985 | 835 | 2 | 1 |
| 5 | 2668 | 2036 | 2 | 1 |
| 6 | 6321 | 4347 | 3 | 2 |
| 7 | 13504 | 8408 | 3 | 2 |

The general M(L)/B(L) statement is established by the algebraic proof, not inferred from these seven positive-L finite checks.

## Relation to native forces; precise next problem

The frozen P000 source distinguishes coordinate adjacency, Path-formal/BRC sources, channels and nonzero three-force closure. A signed coordinate-step word is not itself a legal `TRIADIC_CLOSURE_E` force event. This note makes two discriminating typed predictions on the twenty R725 pairs: (a) any observer factoring through the complete relative coordinate quotient **and** unsigned N-BRC endpoint counts will return equal values; (b) any observer retaining this specific signed orientation character will return different values. Extract an exact frozen V29 PASS/TRANSFER or V39 loop-flow j event, supply the actual Cell/Link/Port incidence and force relation, and test whether its readout factors through (a) or detects (b). Preserve all field/port/branch information until this is decided, with no automatic promotion to native dynamics or Foundation theorem.
