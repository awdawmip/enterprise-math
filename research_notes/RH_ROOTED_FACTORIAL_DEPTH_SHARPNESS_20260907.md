# RH rooted factorial-depth sharpness and populated critical corner

Status: `RESEARCH FRONTIER / TWO-SIDED POWER LAW + DEPTH-THRESHOLD SHARPNESS + GEOMETRIC IDENTIFICATION / NOT A PROOF OF RH`
Date: `2026-09-07`
Project: `Enterprise Math / 进取数论`
Scope: `RH / prime-rooted Volterra resolvent / Factor-BRC / critical arity / product-budget geometry`
Parent frontier:

- `RH_ROOTED_FACTORIAL_RESOLVENT_DEPTH_LAW_20260907.md`
- `RH_ROOTED_VOLTERRA_SOURCE_RESOLVENT_20260907.md`
- `RH_PRIME_ROOTED_ALLADI_ROUGH_PHASE_TRANSPORT_20260907.md`

Tool-reuse resolution: `EXTEND_EXISTING_TOOL`.

This note strengthens the parent factorial tail estimate by proving a matching power-scale lower bound for a positive test source. It therefore separates two claims:

1. the factorial upper bound is sufficient for square-root truncation;
2. the critical depth `~(1/2) log X/loglog X` is not merely an artifact of that upper bound—it is power-sharp for absolute/path-capacity control.

P000 is unchanged. Prime labels, ordered face depth, and product budget are arithmetic relation/provenance coordinates, not native spatial axes.

BRC discipline:

`PROVENANCE > MULTIPLICITY > BOOLEAN SUPPORT`.

The lower bound is a positive-capacity theorem. It does not imply signed Möbius cancellation and does not preclude a stronger estimate that uses the actual signed one-prime source.

---

## 1. Rooted path mass

Recall the increasing-prime Volterra operator

\[
(\mathcal K F)(N,y)
=
\sum_{y<q\le N}
\frac{\lfloor N/q\rfloor}{N}
F(\lfloor N/q\rfloor,q).
\]

For the constant source `1`, iterating and retaining the ordered prime provenance gives exactly

\[
\boxed{
S_r(N,y):=(\mathcal K^r\mathbf 1)(N,y)
=
\sum_{\substack{y<q_1<\cdots<q_r\\q_1\cdots q_r\le N}}
\frac{\lfloor N/(q_1\cdots q_r)\rfloor}{N}.
}
\]

The canonical increasing order removes permutation multiplicity. Each surviving term is one squarefree rooted face with full prime-label provenance.

The parent note proved

\[
S_r(N,y)
\le
\frac{\Lambda(N,y)^r}{r!},
\qquad
\Lambda(N,y)=\sum_{y<q\le N}\frac1q.
\]

The open question was whether this upper bound has the correct power exponent at the RH-critical depth.

---

## 2. Two-sided power law

### Theorem

Fix `0<alpha<1`, and let

\[
r=r_N
=
\alpha\frac{\log N}{\log\log N}
+o\left(\frac{\log N}{\log\log N}\right)
\]

be an integer sequence. Then

\[
\boxed{
S_r(N,1)=N^{-\alpha+o(1)}.
}
\]

The upper and lower bounds use different parts of the same BRC state:

- the upper bound forgets the product budget after retaining canonical prime order;
- the lower bound exhibits a concrete polylogarithmic prime shell whose every labeled `r`-face survives the product budget.

---

## 3. Upper bound

Let

\[
L=\log N,
\qquad
\ell=\log\log N.
\]

The prime-harmonic mass satisfies

\[
\Lambda(N,1)=\ell+O(1).
\]

Therefore

\[
S_r(N,1)
\le
\frac{(\ell+O(1))^r}{r!}.
\]

Stirling's formula gives

\[
\log(r!)=r\log r-r+O(\log r).
\]

Since

\[
\log r
=
\ell-\log\ell+O(1),
\]

we obtain

\[
\log S_r(N,1)
\le
r\log(\ell+O(1))-r\log r+r+O(\log r)
=
-\alpha L+o(L).
\]

Hence

\[
S_r(N,1)\le N^{-\alpha+o(1)}.
\]

This recovers the power exponent implicit in the parent factorial tail law.

---

## 4. Polylogarithmic shell lower bound

Put

\[
Z=N^{1/r}.
\]

Then

\[
\log Z=\frac{\log N}{r}
=
\frac{\ell}{\alpha}+o(\ell),
\]

so

\[
Z=(\log N)^{1/\alpha+o(1)}.
\]

Let

\[
\mathcal P_Z=\{q\text{ prime}:Z/2<q\le Z\},
\qquad
M_Z=\#\mathcal P_Z.
\]

The prime number theorem on the fixed-ratio interval gives

\[
M_Z
=
\frac{Z}{2\log Z}(1+o(1)).
\]

Because `alpha<1`,

\[
\frac{M_Z}{r}
=(\log N)^{1/\alpha-1+o(1)}
\longrightarrow\infty.
\]

Every `r`-element subset of `P_Z` is an admissible rooted path, because

\[
q_1\cdots q_r\le Z^r=N.
\]

For each such subset,

\[
\frac{\lfloor N/(q_1\cdots q_r)\rfloor}{N}
\ge\frac1N.
\]

Therefore

\[
\boxed{
S_r(N,1)
\ge
\frac1N\binom{M_Z}{r}.
}
\]

Since `r=o(M_Z)`, Stirling gives

\[
\log\binom{M_Z}{r}
=r\log\frac{M_Z}{r}+r+o(r).
\]

Moreover

\[
\log\frac{M_Z}{r}
=\left(\frac1\alpha-1\right)\ell+o(\ell).
\]

Thus

\[
\log\binom{M_Z}{r}
=(1-\alpha)L+o(L),
\]

and consequently

\[
S_r(N,1)
\ge
N^{-1}N^{1-\alpha+o(1)}
=N^{-\alpha+o(1)}.
\]

Together with the upper bound, this proves the theorem.

---

## 5. Boundary-layer resolvent term

Let

\[
t=\frac{\tau}{\log\log N},
\]

where `tau` is any fixed nonzero complex number. For the same depth `r`,

\[
|t|^r
=
\exp\left(
-r\log\frac{\log\log N}{|\tau|}
\right)
=N^{-o(1)}.
\]

Therefore

\[
\boxed{
|t|^r S_r(N,1)
=N^{-\alpha+o(1)}.
}
\]

The boundary-layer factor changes only subpower terms. It does not alter the power exponent of the critical face capacity.

Hence an absolute/path-capacity truncation after depth `R` has the following sharp threshold:

- if `R=(alpha+o(1)) log N/loglog N`, a positive test source can leave a term of size `N^(-alpha+o(1))`;
- obtaining `N^(-1/2+o(1))` by absolute truncation requires and is achieved at

\[
\boxed{
R=\left(\frac12+o(1)\right)
\frac{\log N}{\log\log N}.
}
\]

This makes the parent depth law power-sharp within its declared positive-capacity/absolute-control class.

Freeze:

`ROOTED_FACTORIAL_DEPTH_EXPONENT = SHARP_FOR_POSITIVE_PATH_CAPACITY`.

`ABSOLUTE_TRUNCATION_BEFORE_HALF_DEPTH != RH_SCALE_UNIFORMLY`.

---

## 6. The RH critical corner is actually populated

At the square-root exponent `alpha=1/2`,

\[
r
\sim
\frac{\log N}{2\log\log N}.
\]

The shell scale becomes

\[
Z=N^{1/r}
=(\log N)^{2+o(1)}.
\]

This is exactly the RH cutoff

\[
Y=(\log N)^2
\]

up to a subpower factor.

Thus the lower-bound paths are not abstract extreme configurations. They are squarefree integers of the form

\[
a=q_1\cdots q_r,
\qquad
q_i\in(Y/2,Y],
\]

with

\[
\omega(a)=r,
\qquad
a\le N.
\]

The number of available prime labels in the shell is

\[
M_Y
\sim
\frac{Y}{2\log Y},
\]

whereas

\[
r\sim\frac{\log N}{2\log\log N}.
\]

Since `M_Y/r -> infinity`, there are

\[
\binom{M_Y}{r}
=N^{1/2+o(1)}
\]

such labeled faces. Each contributes at least `1/N` to the rooted path mass, giving the matching `N^(-1/2+o(1))` capacity.

Therefore the Alladi light-cone corner

\[
p^k\approx N,
\qquad
p\approx(\log N)^2,
\qquad
k\approx\frac{\log N}{2\log\log N}
\]

is not only a support boundary. It contains a square-root-sized family of distinct Factor-BRC provenance states.

This is the geometric meaning of the critical depth:

> the RH cutoff and the RH arity meet at a densely populated product-budget face, not at an isolated exceptional Cell.

---

## 7. Consequences for X6 and Factor-BRC

The theorem strengthens the fixed-width/growing-depth interpretation.

1. X6 remains the fixed local port. No new spatial dimension is introduced.
2. The depth `r` is serial provenance depth: each additional prime factor opens another labeled arithmetic branch.
3. At the critical corner, the set of labels in one local shell is far larger than six, so a one-shot six-axis endpoint cannot retain identity.
4. The square-root residual is carried by `N^(1/2+o(1))` distinct high-arity faces. Collapsing them to arity alone or to a fixed endpoint destroys the exact state that saturates the bound.
5. Canonical ordering removes the artificial `r!` path multiplicity, but the remaining subset multiplicity is still power-scale significant.

In BRC terms:

`PERMUTATION_QUOTIENT` is safe,

but

`PRIME_LABEL_SUBSET -> ARITY_ONLY`

is not safe at the RH critical face.

---

## 8. What the sharpness theorem does not say

The lower bound uses the constant positive source `1`. The actual rooted discrepancy source `Q_N(y;t)` is signed and may exhibit additional cancellation.

Therefore the theorem does not prove that the actual resolvent tail is as large as `N^(-alpha)`, and it does not rule out a signed argument that truncates earlier.

It proves the narrower but important no-go:

\[
\boxed{
\text{factorial suppression + absolute values alone cannot beat the half-depth threshold.}
}
\]

Any improvement must use information absent from the positive capacity estimate, such as:

- sign of the one-prime discrepancy;
- root-label location;
- adjacency in the ordered-prime edge carrier;
- cancellation between neighboring quotient Cells;
- a weighted Hilbert/dual norm adapted to the final square-root observer.

This exactly matches the unresolved front block in the parent frontier.

---

## 9. Exact finite checker

Task-local checker:

`experiments/rh_rooted_factorial_depth_sharpness_check.py`.

It verifies with exact rational arithmetic:

- the explicit increasing-prime path sum for `(K^r 1)(N,1)`;
- the factorial upper bound;
- the interval-shell lower bound `binom(M_Z,r)/N`;
- finite critical tables for `alpha=1/2`.

The checker is diagnostic only. The asymptotic theorem is proved by the preceding upper/lower argument.

---

## 10. New smallest research unit

The depth/tail question is now closed at the positive-capacity power scale:

\[
\text{high-depth tail} = N^{-R\log\log N/\log N+o(1)}
\]

is both an upper and lower exponent for suitable positive data.

The only admissible route to a shallower RH-scale estimate is therefore signed. The next research unit is to pass the actual one-prime source through the adjoint rooted resolvent and retain the final square-root root-label observer:

\[
\langle L_{\sqrt p},(I+t\mathcal K)^{-1}Q\rangle
=
\langle (I+t\mathcal K^*)^{-1}L_{\sqrt p},Q\rangle.
\]

The concrete targets are:

1. derive the exact adjoint path weight on a root prime;
2. identify whether neighboring root labels enter through a discrete derivative rather than raw intensity;
3. test a weighted Hilbert norm in which the adjoint observer is subpolynomial at depth `K`;
4. prove any cancellation that is genuinely source-specific and unavailable to the positive constant witness above.

No RH proof is claimed.
