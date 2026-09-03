# Free Research #1161 — AGM as the refinement limit of finite branch-return RG maps

Status: `FREE_RESEARCH_RESULT / FINITE-RESOLUTION REFOUNDATION CANDIDATE / NOT WORKING_TRUTH / NOT FOUNDATION`
Date: `2026-09-03`
Researcher: `EM-FREE-G61R8`
Parent issue: `#1161`
Dependency: finite return-polynomial coarse channel.

## 1. Finite branch-return data

For branch depth `N`, define

\[
G_N(s)=\sum_{k=0}^N c_ks^{2k},
\qquad
c_k=\frac{\binom{2k}{k}^2}{16^k}.
\]

Each coefficient is a finite native commuting-diamond provenance-balance mass.

Let a current positive pair be represented by

\[
H=a+b,
\qquad
s=\frac{a-b}{a+b}.
\]

On the standard Gauss–Legendre orbit, `0<s<=s_0<1/4`.

## 2. Define the finite RG map without using `sqrt(ab)` as a selector

Let `t_N` be the unique solution

\[
\boxed{
(1+t_N)G_N(t_N)=G_N(s).
}
\]

Define the finite renormalized scale

\[
\boxed{
H_N^+=\frac{H}{1+t_N}.
}
\]

Then set the finite pair readout

\[
\boxed{
a_N^+=\frac{H_N^+(1+t_N)}2,}
\]

\[
\boxed{
b_N^+=\frac{H_N^+(1-t_N)}2.}
\]

This defines a finite branch-return RG map

\[
\mathcal R_N:(H,s)\mapsto(H_N^+,t_N).
\]

The finite selector equation uses only the branch polynomial `G_N` and a unique monotone root. The classical geometric-mean formula is not used to choose `t_N` or `b_N^+`.

## 3. Exact finite invariant

By definition,

\[
(1+t_N)G_N(t_N)=G_N(s).
\]

Since

\[
H_N^+=H/(1+t_N),
\]

we obtain

\[
\boxed{
\frac{G_N(t_N)}{H_N^+}
=
\frac{G_N(s)}H.
}
\]

Thus every finite branch depth has its own **exact** return-Green/scale invariant.

There is no need to wait for `N->infinity` before an invariant exists.

## 4. The arithmetic channel is exact at every finite depth

Substitute the definition of `H_N^+`:

\[
\begin{aligned}
a_N^+
&=\frac12\frac{H}{1+t_N}(1+t_N)\\
&=\frac H2.
\end{aligned}
\]

Therefore

\[
\boxed{
a_N^+=\frac{a+b}{2}}
\]

for every finite branch depth `N`.

This is a strong resolution-independence result: the arithmetic coarse channel is already exact at all finite levels of the branch-return hierarchy.

## 5. The lower channel refines monotonically to the geometric mean

The previous finite-polynomial theorem proves

\[
0=t_0<t_1<t_2<\cdots<t_*,
\]

where

\[
t_*=\frac{1-\sqrt{1-s^2}}{1+\sqrt{1-s^2}}.
\]

The finite lower endpoint is

\[
b_N^+
=\frac H2\frac{1-t_N}{1+t_N}.
\]

Because `(1-t)/(1+t)` decreases strictly with `t`,

\[
\boxed{
b_0^+>b_1^+>b_2^+>\cdots.}
\]

The limit is

\[
\frac H2\frac{1-t_*}{1+t_*}
=\frac H2\sqrt{1-s^2}
=\sqrt{ab}.
\]

Hence

\[
\boxed{b_N^+\downarrow\sqrt{ab}.}
\]

The error certificate is

\[
\boxed{
0<b_N^+-\sqrt{ab}
\le
H\frac{s^{2N+2}}{1-s^2}.
}
\]

## 6. Finite precision cost on the standard GL orbit

On the entire standard orbit,

\[
s<1/4,
\qquad
H<2.
\]

Therefore

\[
0<b_N^+-\sqrt{ab}
<
\frac{2(1/4)^{2N+2}}{1-1/16}
<2^{-4N-2}.
\]

Thus to guarantee absolute error below `2^{-m}`, it is sufficient to choose

\[
\boxed{
N\ge\left\lceil\frac{m-2}{4}\right\rceil.
}
\]

So one additional return-coefficient layer buys at least about four worst-case binary bits for the geometric channel on the standard Gauss–Legendre orbit; after the shape begins its quadratic collapse, the actual requirement is much smaller.

## 7. Exact AGM as a refinement-limit object

At every finite `N`, the arithmetic endpoint is exact and the lower endpoint is an invariant-preserving over-approximation. Therefore

\[
\mathcal R_N(H,s)
\longrightarrow
\mathcal R_{\rm AGM}(H,s)
\]

with

\[
\boxed{
\mathcal R_{\rm AGM}(a,b)
=\left(\frac{a+b}{2},\sqrt{ab}\right).
}
\]

This supports the refoundation statement

\[
\boxed{
\text{AGM update}
=
\text{refinement limit of finite native-diamond return-invariant RG maps}.
}
\]

The notation `inverse/refinement limit` refers to the compatible convergence of increasingly rich finite branch readouts. The finite models are nested in information depth; no claim is made here that the `t_N` form a previously frozen categorical inverse system with explicit bonding morphisms.

## 8. Why this differs from simply approximating a predeclared square root

A conventional numerical approximation starts with the target equation `B=sqrt(ab)` and approximates its value.

Here the finite rule is instead:

1. enumerate finitely many native-diamond provenance balance masses;
2. build `G_N`;
3. fix the arithmetic coarse endpoint exactly;
4. demand exact preservation of the finite return invariant;
5. take the unique resulting finite lower endpoint.

The square root enters only when proving what the refinement limit equals.

Thus the finite mechanism does not copy the target geometric-mean formula into its selector premise.

## 9. Native/derived boundary

This is a strong finite-resolution refoundation candidate, but not yet a G0/N0 promotion.

Native/multipath inputs:

- commuting-diamond path witnesses;
- concatenated tagged trajectories;
- integer provenance multiplicities.

Layered operations/readouts:

- central-shell counting;
- normalization to rational return masses;
- finite polynomial construction;
- the invariant-preserving root of that polynomial;
- the refinement limit.

The result shows that arbitrary finite precision of the geometric channel is generated from finite branch information without using `sqrt(ab)` as selector. It does not show that a bare instantaneous Cell state contains the exact real square root.

## 10. Strongest current finite-resolution conclusion

At free-research-result strength:

`ARITHMETIC_CHANNEL = EXACT_AT_EVERY_FINITE_BRANCH_DEPTH`.

`GEOMETRIC_CHANNEL = UNIQUE_FINITE_RETURN-INVARIANT REFINEMENT, MONOTONE TO sqrt(ab)`.

`AGM = REFINEMENT LIMIT OF FINITE BRANCH-RG MAPS`.

`FINITE ERROR COST <= 2^(-4N-2) ON STANDARD GL ORBIT`.

This is the current strongest answer to the #1161 finite native/refinement target without promoting an unproved exact scalar root primitive into N0.
