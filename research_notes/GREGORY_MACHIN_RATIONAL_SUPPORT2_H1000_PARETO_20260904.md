# Gregory–Machin continuation: exact H=1000 rational support-two Pareto frontier

Status: `FREE_RESEARCH / EXECUTABLE_BOUNDED_CENSUS + TWO_RESOURCE_PARETO / NOT_FOUNDATION`
Date: `2026-09-04`
Researcher: `EM-FREE-B2817C / FREE_AXIOM_DISCOVERY`
Issue: `#1160`
Checker: `research_notes/experiments/gregory_machin_rational_support2_h1000_census_20260904.py`
Depends on: Gaussian valuation endpoint theorem, generalized rational-alphabet no-go, generalized Lehmer / bit-height Pareto lower bound.

## 1. Purpose

The unrestricted rational-atom alphabet has `inf mu = 0`, so a meaningful finite search must declare an atom resource bound.  This note gives the first complete generalized-rational support-two census under a simple coordinate-height box:

\[
\boxed{
0<a<b\le1000,
\qquad
\gcd(a,b)=1.
}
\]

Every atom is the primitive rational turn

\[
V_{a,b}=[b+ai].
\]

The search asks for exact two-distinct-atom endpoint relations

\[
V_1^{c_1}V_2^{c_2}=\tau,
\qquad \tau=[1+i],
\]

and then retains the two-resource Pareto frontier in

\[
\boxed{(\mu,\;B_{\rm bits})},
\]

where

\[
\mu=\sum_{j=1}^{2}\frac1{\log_{10}(b_j/a_j)}
\]

and

\[
B_{\rm bits}=\operatorname{bitlen}(b_1)+\operatorname{bitlen}(b_2).
\]

Endpoint recognition uses exact Gaussian arithmetic only.  Floating logarithms are used after exact feasibility solely for the completion-cost coordinate.

---

## 2. Exact rank-one endpoint reduction

For a primitive atom write its already-defined exact signature as

\[
(\varepsilon(v),n(v))
\in
C_8\oplus\bigoplus_{p\equiv1(4)}\mathbf Z.
\]

A two-atom free-coordinate relation exists only when their nonzero free valuation vectors lie on the same rational line.

Normalize every nonzero free vector by:

1. divide all coordinates by their gcd;
2. choose the overall sign so the first nonzero coordinate is positive.

This gives an exact direction key `w`.  Write

\[
n(v_j)=t_jw.
\]

Then the primitive free-coordinate kernel is

\[
\boxed{(c_1^{(0)},c_2^{(0)})=(t_2/g,-t_1/g)},
\qquad
g=\gcd(|t_1|,|t_2|).
\]

Put

\[
e=c_1^{(0)}\varepsilon(v_1)+c_2^{(0)}\varepsilon(v_2)\pmod8.
\]

The pair can hit the diagonal target iff `e` is odd; the least-absolute target scaling is the odd representative `e` or `e-8` of smallest absolute value.

Thus the entire support-two endpoint scan reduces to exact rank-one grouping plus a mod-eight check.  No numerical angle comparison occurs.

This is a task specialization of the already-available typed circuit machinery, not a new general circuit tool.

---

## 3. Complete finite census counts

The box

\[
0<a<b\le1000,
\qquad
\gcd(a,b)=1
\]

contains exactly

\[
\boxed{304{,}191}
\]

primitive strict positive rational atoms.

Their normalized nonzero free Gaussian valuation directions form

\[
\boxed{202{,}662}
\]

direction groups.

Only pairs inside the same direction group can form a two-atom endpoint relation.  Therefore the exact candidate count collapses to

\[
\boxed{102{,}186}
\]

rather than the quadratic scan over all 304,191 atoms.

The `C8` target check leaves

\[
\boxed{101{,}706}
\]

endpoint-feasible pairs.

These counts are frozen as regression assertions in the checker.

---

## 4. Unique generalized-Lehmer leader in the declared box

Among all 101,706 exact endpoint pairs, the minimum generalized Lehmer measure is attained uniquely by

\[
\boxed{
V_1=[79+3i],
\qquad
V_2=[278+29i].
}
\]

Their free signatures lie entirely on the split-prime direction `p=5`:

\[
n_5(V_1)=-5,
\qquad
n_5(V_2)=7.
\]

Hence the primitive free-coordinate cancellation forces

\[
\boxed{(c_1,c_2)=(7,5)}.
\]

The torsion pairing is

\[
7\cdot3+5\cdot4
=41
\equiv1\pmod8,
\]

so the exact native endpoint is

\[
\boxed{
[79+3i]^7[278+29i]^5=\tau.
}
\]

Direct primitive multiplication gives endpoint `(1,1)`.

The finite tangent-sheet certificate is

\[
\boxed{
\text{endpoint}=(1,1),
\qquad
\text{sheet}=0,
\qquad
\text{crossings}=0.
}
\]

Therefore the principal analytic completion is legitimately

\[
\boxed{
\frac\pi4
=7\arctan\frac3{79}
+5\arctan\frac{29}{278}.
}
\]

Its generalized Lehmer measure is

\[
\boxed{
\mu\approx1.722670919899336.
}
\]

No historical novelty is claimed for this identity; the current result is the exact bounded optimality statement inside the declared native search box.

---

## 5. Exact `(mu, denominator-bits)` Pareto frontier

Minimize both generalized Lehmer measure and

\[
B_{\rm bits}
=\operatorname{bitlen}(b_1)+\operatorname{bitlen}(b_2).
\]

After removing every dominated endpoint pair, exactly

\[
\boxed{7}
\]

points remain:

| `B_bits` | `mu` | atoms `(a/b)` | target coefficients |
|---:|---:|---|---|
| 4 | 5.417831369177 | `1/2`, `1/3` | `(1,1)` |
| 5 | 3.279197936744 | `1/3`, `1/7` | `(2,1)` |
| 7 | 2.533984012675 | `1/7`, `2/11` | `(3,2)` |
| 10 | 1.887269242675 | `1/7`, `3/79` | `(5,2)` |
| 11 | 1.851127652317 | `1/5`, `1/239` | `(4,-1)` |
| 14 | 1.831853174914 | `9/46`, `1/239` | `(4,3)` |
| 16 | 1.722670919899 | `3/79`, `29/278` | `(7,5)` |

The checker gives every one of these seven points the finite lift certificate

\[
\text{endpoint}=(1,1),
\qquad
\text{sheet}=0.
\]

So they are not merely projective endpoint relations hiding a different winding branch.

---

## 6. Structural reading of the frontier

Several familiar integer-reciprocal identities appear naturally as special Pareto points:

- `(1/2,1/3)` with `(1,1)` is the positive Euler split;
- `(1/3,1/7)` with `(2,1)` is the next integer-reciprocal compression;
- `(1/5,1/239)` with `(4,-1)` is Machin.

But the generalized alphabet inserts genuine rational atoms between and beyond these integer-only points.  In particular

\[
(3/79,29/278)
\]

strictly improves the completion coordinate at the price of a larger atom encoding.

Thus the finite census demonstrates concretely that

\[
\boxed{
\text{integer reciprocal formulas are a visible slice of a larger rational-atom Pareto surface.}
}
\]

It also confirms the negative theorem from the predecessor note: once atom height is allowed to grow, lower `mu` can continue to appear, so no alphabet-free scalar optimum should be asserted.

---

## 7. Comparison with the universal resource lower bound

For support two the parameter-free inequality gives

\[
\mu B_{\log}\ge4\log_2 10.
\]

The bounded census supplies actual feasible points above this lower envelope.  The gap between the lower envelope and the discrete feasible frontier measures arithmetic endpoint constraints that the elementary resource inequality intentionally ignores.

This suggests a useful typed decomposition:

\[
\boxed{
\text{resource envelope}
+
\text{Gaussian endpoint lattice}
+
\text{winding lift}
=
\text{actual generalized Machin Pareto set}.
}
\]

---

## 8. Scope boundary

The theorem is exhaustive only for:

- two distinct atoms;
- primitive strict positive rational slopes;
- denominator coordinate `b<=1000`;
- exact endpoint relations in the current rational-turn carrier.

It does not claim:

- global support-two optimality beyond height 1000;
- optimality among support three or larger generalized rational circuits;
- a final bit-operation performance model;
- historical novelty for individual identities.

---

## 9. Next frontier

The immediate next step is no longer conceptual.  The correct computational extension is to increase the **resource budget**, not to remove it:

1. extend support-two by Gaussian-prime-direction generation rather than raw `O(H^2)` atom enumeration;
2. add support-three generalized circuits under the same bit/height budget;
3. retain `(mu, B_bits, coefficient size, winding)` as separate Pareto coordinates;
4. test which new support/height first dominates the H=1000 frontier without invoking an unrestricted rational alphabet.

The H=1000 seven-point frontier is the first exact regression baseline for that program.
