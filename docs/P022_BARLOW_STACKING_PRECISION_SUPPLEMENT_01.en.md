# P022 Barlow Stacking Precision Supplement 01 — Exact Shell Formula and Drift-Controlled Geodesic Growth

Status: `ACTIVE RESEARCH NOTE / EXACT INTEGER FINITE FORMULA + ASYMPTOTIC THEOREM / NOVELTY UNVERIFIED`  
Owner: `program/p022-geometry-v2`  
Depends on: `P022_BARLOW_STACKING_PRECISION.*`  
Boundary: the exact combinatorics are proved here; historical priority for this Barlow-specific geodesic-growth formula has not yet been audited

## 1. From target-layer precision to whole-shell geometry

The main Barlow note proved that the complete root-to-one-target-layer distance+count language depends only on the target layer length

\[
q=|k|
\]

and the prefix imbalance

\[
\delta_k.
\]

Write

\[
d_k=|\delta_k|,
\qquad
c_k=\frac{q-d_k}{2}.
\]

Then the minimal vertical witness polynomial has normal form

\[
P_k=(A+3)^{c_k}B_{\pm}^{d_k}.
\]

A whole graph shell of radius `n`, however, queries every target layer

\[
-n\le k\le n.
\]

The correct state is therefore not one final imbalance but the finite trajectory

\[
(d_{-n},\ldots,d_0,\ldots,d_n).
\]

The first result below gives the exact contribution of each coordinate of that trajectory.

## 2. Exposed-face counting on the triangular norm

The triangular graph norm is

\[
h(q,r)=\max(|q|,|r|,|q+r|).
\]

Its radius shell has six facets and six corners.

For a non-negative Laurent polynomial `P`, consider

\[
P A^t,
\qquad t>0,
\]

where

\[
A=x+x^{-1}+y+y^{-1}+xy^{-1}+x^{-1}y.
\]

The coefficients lying at triangular distance exactly `t` outside `supp(P)` form the outer boundary of the Minkowski expansion by the radius-`t` hexagon.

Fix one facet normal. To land on that exposed facet:

- the chosen exponent from `P` must lie on the corresponding exposed face of `P`;
- every one of the `t` factors of `A` must choose one of the two triangular primitive steps maximizing that normal.

Hence the coefficient mass on that facet is

\[
F(P)\,2^t,
\]

where `F(P)` is the coefficient mass of the exposed face of `P`.

Adjacent facets overlap at one corner. At a fixed corner, each `A` factor has exactly one maximizing primitive step, so the overlap mass is just the corresponding corner mass `C(P)`.

Every boundary point belongs to one facet or to the intersection of two adjacent facets. Therefore inclusion-exclusion gives

\[
\boxed{
\operatorname{Bd}_t(P)
=2^t\sum_{f=1}^{6}F_f(P)
-\sum_{v=1}^{6}C_v(P).
}
\]

This is an exact coefficient identity, not an asymptotic approximation.

## 3. Face and corner masses of the Barlow normal form

For `A+3`, the constant term is interior to every nonzero exposed direction. Thus it has the same exposed faces as `A`:

- every facet mass is `2`;
- every corner mass is `1`.

For either `B_+` or `B_-`:

- three of the six facet masses are `1`;
- the other three are `2`;
- all six corner masses are `1`.

Exposed faces of products multiply because maximizing exponents add. Hence for

\[
P_k=(A+3)^cB_\pm^d
\]

we obtain

\[
\sum_fF_f(P_k)
=3\cdot2^c(1+2^d),
\]

and

\[
\sum_vC_v(P_k)=6.
\]

Therefore, for every `t>0`,

\[
\boxed{
\operatorname{Bd}_t(P_k)
=3\cdot2^{c+t}(1+2^d)-6.
}
\]

The formula depends on the stacking prefix only through `c` and `d`, equivalently through `(q,|delta_k|)`.

## 4. P022-BG01 — exact target-layer contribution to shell `n`

Let shell radius be `n`, target layer `k`, and

\[
q=|k|\le n,
\qquad
d=|\delta_k|,
\qquad
c=(q-d)/2.
\]

### Extreme target layer `q=n`

No in-layer step can appear in a geodesic of length `n`. Every monotone vertical word has length `n`, and there are three choices at each interface. Thus

\[
\boxed{
L_n(k)=3^n
\qquad(q=n).
}
\]

### Non-extreme target layer `q<n`

Put

\[
t=n-q>0.
\]

The boundary mass from Section 3 counts the ordered horizontal/vertical internal choices before interleaving. Choose the positions of the `t` in-layer moves among the full `n`-step geodesic word:

\[
\binom nt=\binom nq.
\]

Therefore

\[
\boxed{
L_n(k)
=\binom nq
\left(
3\cdot2^{c+n-q}(1+2^d)-6
\right),
\qquad q<n.
}
\]

Equivalently,

\[
\boxed{
L_n(k)=\binom nq
\left[
3\cdot2^n
\left(
2^{-(q+d)/2}+2^{-(q-d)/2}
\right)-6
\right].
}
\]

No shell endpoint enumeration remains.

## 5. P022-BG02 — exact whole-shell formula for arbitrary periodic or aperiodic prefixes

For any Barlow stacking for which the finite prefix imbalances through layers `[-n,n]` are known,

\[
\boxed{
T(n)=\sum_{k=-n}^{n}L_n(k).
}
\]

Thus the complete shell-total shortest-path multiplicity is a function only of the finite absolute prefix-imbalance trajectory

\[
\boxed{
(|\delta_{-n}|,\ldots,|\delta_n|).
}
\]

The signs of the imbalances have disappeared because the whole horizontal layer is summed and the triangular lattice is reflection symmetric.

This is a stronger task-relative compression than the target-endpoint theorem:

- a fixed endpoint layer needs signed `delta_k` to retain coordinate-sensitive coefficients;
- the **shell-total** contribution of that layer needs only `|delta_k|`;
- the whole radius-`n` shell needs only the absolute imbalance trajectory through the queried layers.

The executable reference checks BG01 layer by layer—not only after whole-shell summation—for every periodic ± pattern of period at most four through radius five.

## 6. Periodic drift

Now let the stacking be periodic with period length

\[
L\ge1
\]

and signed period drift

\[
D=\sum_{j=0}^{L-1}\sigma_j.
\]

Define the rational absolute drift density

\[
\boxed{
\mu=\frac{|D|}{L}\in[0,1].
}
\]

No floating-point approximation is needed; the exact data are the integers `(|D|,L)`.

For an upward target layer `q=mL+r`, periodicity gives

\[
\delta_q=mD+\delta_r.
\]

The finite remainder `delta_r` is bounded. Downward prefixes have the same property with the corresponding reversed phase. Therefore there is a stacking-dependent finite constant `C` such that for all signed target layers `k`,

\[
\boxed{
\left|
|\delta_k|-\mu|k|
\right|\le C.
}
\]

So the absolute imbalance is a linear drift plus bounded periodic phase.

## 7. P022-BG03 — periodic shell-total growth depends only on drift density

For `q<n`, BG01 can be written

\[
L_n(k)=\binom nq
\left[
3\cdot2^n
\left(
2^{-(q+d_k)/2}+2^{-(q-d_k)/2}
\right)-6
\right].
\]

Since `d_k>=0`, the second exponential inside the parentheses is the larger one. Periodicity gives

\[
d_k=\mu q+O(1).
\]

Hence there are positive constants `c_1,c_2`, depending only on the finite stacking period, such that for every non-extreme layer and all sufficiently large shells,

\[
 c_1\binom nq2^n
 2^{-q(1-\mu)/2}
\le
L_n(k)
\le
 c_2\binom nq2^n
 2^{-q(1-\mu)/2}.
\]

The `-6` term does not spoil the lower bound: for `q<n`, the uncorrected boundary factor is at least `4`, so

\[
3F-6\ge\frac32F.
\]

Let

\[
a=2^{-(1-\mu)/2}.
\]

Summing over target-layer heights gives, up to fixed multiplicative constants,

\[
2^n\sum_{q=0}^{n-1}\binom nqa^q.
\]

But

\[
\sum_{q=0}^{n-1}\binom nqa^q
=(1+a)^n-a^n.
\]

The two extreme layers contribute only

\[
2\cdot3^n,
\]

and

\[
2(1+a)\ge2+\sqrt2>3,
\]

so they are exponentially smaller than the non-extreme sum.

Therefore

\[
\boxed{
T(n)=\Theta\!\left(\lambda(\mu)^n\right)
}
\]

with

\[
\boxed{
\lambda(\mu)
=2(1+a)
=2+2^{(1+\mu)/2}.}
\]

Equivalently,

\[
\boxed{
\lim_{n\to\infty}T(n)^{1/n}
=2+2^{(1+\mu)/2}.}
\]

This proves that **the exponential shell-total geodesic growth rate of every periodic Barlow stacking depends only on the absolute period drift density `|D|/L`, not on literal interface order inside the period.**

Finite shells can still differ because the bounded prefix phase remains visible before the exponential limit.

## 8. Integer-first algebraic form of the growth constant

The growth constant need not be stored as a floating-point real number.

With

\[
\mu=|D|/L,
\]

write

\[
\lambda-2=2^{(L+|D|)/(2L)}.
\]

Raise to the integer power `2L`:

\[
\boxed{
(\lambda-2)^{2L}=2^{L+|D|}.}
\]

Thus the exact growth descriptor is the pair of integers

\[
\boxed{(2L,\ 2^{L+|D|})}
\]

together with the instruction to select the positive real root greater than `2`.

This algebraic encoding is fully compatible with Enterprise Math's integer-first state discipline.

## 9. Special cases

### FCC-type constant drift

`L=1`, `|D|=1`, so

\[
\mu=1,
\qquad
\lambda=2+2=4.
\]

The exact integer equation is

\[
(\lambda-2)^2=4.
\]

This matches the earlier closed form

\[
T_{FCC}(n)
=6\cdot4^n+8\cdot3^n-24\cdot2^n+12.
\]

### HCP alternating stacking

`L=2`, `D=0`, so

\[
\mu=0,
\qquad
\lambda=2+\sqrt2.
\]

The integer equation is

\[
(\lambda-2)^4=4.
\]

This matches the HCP recurrence from the preceding supplement.

### Every zero-drift periodic Barlow stacking

If

\[
D=0,
\]

then regardless of period length or internal order,

\[
\boxed{
\lambda=2+\sqrt2.}
\]

So HCP is not unique at the level of asymptotic geodesic-growth exponent. Its finite multiplicity spectrum and prefix phase still distinguish it from other zero-drift stackings.

### Intermediate drift

For period `(-,-,+)`,

\[
L=3,\quad |D|=1,\quad\mu=1/3,
\]

so

\[
\lambda=2+2^{2/3},
\]

encoded by

\[
(\lambda-2)^6=16.
\]

For `(-,-,-,+)`,

\[
L=4,\quad |D|=2,\quad\mu=1/2,
\]

so

\[
\lambda=2+2^{3/4},
\]

encoded by

\[
(\lambda-2)^8=64.
\]

Hence the close-packed family fills a strict geodesic-growth continuum of algebraic rates between the zero-drift and constant-drift extremes, indexed by rational drift density.

## 10. Precision interpretation

The results expose three different query languages and therefore three different exact states.

### One selected target layer

State:

\[
\delta_k.
\]

### Whole horizontal shell contribution at one selected layer

State:

\[
|\delta_k|.
\]

The sign is erased by horizontal reflection after summing the layer.

### Whole finite graph shell radius `n`

State:

\[
(|\delta_{-n}|,\ldots,|\delta_n|).
\]

### Exponential growth rate of a periodic stacking

State collapses further to only

\[
\boxed{(|D|,L)}
\]

or equivalently the rational drift density `|D|/L`.

Thus the same literal stacking history has a hierarchy of legal finite compressions:

\[
\text{word}
\to
\text{prefix imbalance trajectory}
\to
\text{selected imbalances}
\to
\text{absolute imbalance trajectory}
\to
\text{period drift density},
\]

but **only as the declared future language weakens accordingly**.

This is one of the clearest concrete examples so far of the P023/P024 future-language precision principle inside an intrinsic geometry.

## 11. What is and is not proved

Proved here:

- exact target-layer shell contribution BG01;
- exact whole-shell sum BG02;
- exact periodic drift bound;
- exact exponential rate BG03;
- drift-density dependence of that rate.

Not proved or claimed:

- two stackings with the same drift density have identical finite shells;
- they have identical full multiplicity spectra;
- one growth rate is physically preferable;
- Barlow geodesic growth is historically novel.

Indeed, finite-shell equality is false in general. Different zero-drift periods can share the same asymptotic rate while having different shell totals and spectra at finite radius.

## 12. Executable assets

Added:

- `src/enterprise_math/p022_barlow_growth.py`;
- `tests/test_p022_barlow_growth.py`.

The tests verify BG01 separately on every target layer for every ± pattern of period at most four through radius five, then verify the whole-shell formula through radius six, plus FCC/HCP specializations and equal-drift/different-finite-shell counterexamples.
