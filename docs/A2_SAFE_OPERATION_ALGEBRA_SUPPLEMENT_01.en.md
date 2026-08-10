# A2 — Safe-Operation Algebra, Supplement 01: Polynomial Unary Spectrum

Status: `PROVED_WIP / EXECUTABLE_CHECKED / NOT CANONICAL_MAIN`  
Parent: `docs/A2_SAFE_OPERATION_ALGEBRA.en.md`  
Scope: ordinary integer-valued polynomial self-maps of `N_0` acting on P008 complete-growth interval quotients

## 1. Question

The parent note separates the classical absolute safe clone

\[
\operatorname{Pol}(\ker q)
\]

from the project-specific natural operation spectrum

\[
\operatorname{Spec}_{\mathcal A}(q)
=
\mathcal A\cap\operatorname{Pol}(\ker q).
\]

A first nontrivial ambient family is the family of ordinary polynomial self-maps

\[
f:\mathbb N_0\to\mathbb N_0.
\]

This supplement gives a complete classification for polynomial complete-growth laws.

The result is much more rigid than the translation theorem:

> fixed-block linear growth retains a periodic translation family, whereas every polynomial complete-growth law of degree at least two retains only constants and the identity among ordinary polynomial unary dynamics.

## 2. Setup

Let

\[
V(0)=0<V(1)<V(2)<\cdots
\]

be an integer-valued polynomial on `N_0`, and define the P008 level quotient by

\[
q_V(n)=k
\iff
V(k)\le n<V(k+1).
\]

Write

\[
w_k=V(k+1)-V(k).
\]

A unary map `f:N_0->N_0` is safe exactly when each source basin is sent wholly into one target basin:

\[
\boxed{
q_V(x)=q_V(y)
\Longrightarrow
q_V(f(x))=q_V(f(y)).
}
\]

For a monotone `f`, it is already necessary that the image span of every basin fit inside one target basin.

## 3. A2-SOA-S1-T01 — asymptotic source-span versus target-width law

Assume

\[
V(k)=c k^p+O(k^{p-1}),
\qquad
c>0,
\qquad
p\ge2,
\]

and let

\[
f(n)=a n^m+O(n^{m-1}),
\qquad
a>0,
\qquad m\ge1,
\]

be a nonconstant polynomial self-map of `N_0`.

Set

\[
x_k=V(k),
\qquad
y_k=V(k+1)-1.
\]

Then

\[
w_k
=cpk^{p-1}+O(k^{p-2}),
\]

and `w_k/x_k -> 0`.

For `m>=2`, polynomial expansion over the basin width gives

\[
\boxed{
f(y_k)-f(x_k)
\sim
ampc^m k^{pm-1}.}
\]

For `m=1`, if `f(n)=an+b`, then

\[
\boxed{
f(y_k)-f(x_k)
\sim
acp k^{p-1}.}
\]

Now let

\[
\ell_k=q_V(f(x_k)).
\]

Since

\[
f(x_k)
\sim
ac^m k^{pm},
\]

we have

\[
\boxed{
\ell_k
\sim
A k^m,
\qquad
A=(ac^{m-1})^{1/p}.}
\]

Therefore the width of the target basin containing `f(x_k)` satisfies

\[
\boxed{
w_{\ell_k}
\sim
cpA^{p-1}k^{m(p-1)}.}
\]

Safety requires

\[
f(y_k)-f(x_k)<w_{\ell_k}
\]

for every sufficiently large `k`, because both endpoint images must lie in the same target basin.

This one comparison drives the classification below.

## 4. A2-SOA-S1-T02 — every polynomial map of degree at least two is unsafe

Assume `p>=2` and `m>=2`.

The source-basin image span has growth degree

\[
pm-1,
\]

whereas the relevant target-basin width has growth degree

\[
m(p-1)=pm-m.
\]

Their degree difference is

\[
(pm-1)-(pm-m)=m-1>0.
\]

Hence

\[
\frac{f(y_k)-f(x_k)}{w_{\ell_k}}
\to\infty.
\]

For all sufficiently large `k`, the image of one source basin is wider than the entire target basin containing its left endpoint. Thus the source basin must cross a target boundary.

Therefore

\[
\boxed{
\deg V\ge2,\ \deg f\ge2
\Longrightarrow
f\notin\operatorname{Safe}_1(q_V).}
\]

This is stronger than the stage-3 fixed-translation no-go: nonlinear polynomial dynamics fail because their within-basin expansion eventually outgrows the target basin geometry itself.

## 5. A2-SOA-S1-T03 — affine maps of slope at least two are unsafe

Let

\[
f(n)=an+b,
\qquad a\ge2.
\]

For `m=1`, the constant `A` in T01 is

\[
A=a^{1/p}.
\]

Hence

\[
\frac{f(y_k)-f(x_k)}{w_{\ell_k}}
\to
\frac{a}{a^{(p-1)/p}}
=a^{1/p}>1.
\]

So the image span is eventually strictly wider than the available target basin.

Therefore

\[
\boxed{
\deg V\ge2,\ a\ge2
\Longrightarrow
(n\mapsto an+b)\text{ is unsafe}.}
\]

## 6. A2-SOA-S1-T04 — slope one reduces exactly to translation rigidity

An integer-valued affine self-map of `N_0` with positive slope and slope less than two must have slope one:

\[
f(n)=n+b,
\qquad b\ge0.
\]

If `b=0`, this is the identity and is safe.

If `b>0`, polynomial complete growth of degree at least two has unbounded basin widths. Choose a basin with

\[
w_k>b.
\]

Then `V(k)` and `V(k+1)-b` lie in the same basin, but after adding `b` the second point reaches the next boundary while the first remains inside the old basin. Thus fixed `+b` is unsafe.

Therefore

\[
\boxed{
\deg V\ge2,\ f(n)=n+b
\Longrightarrow
f\text{ safe}\iff b=0.}
\]

## 7. A2-SOA-S1-T05 — complete polynomial unary spectrum for nonlinear complete growth

Every polynomial self-map `f:N_0->N_0` has either degree zero or positive leading coefficient.

- Degree zero maps are constants and are always safe.
- Degree at least two maps are excluded by T02.
- Degree one maps have integer slope `a>=1`; slopes `a>=2` are excluded by T03, and slope one is classified by T04.

Hence for every strictly increasing integer-valued polynomial complete-growth law with

\[
\deg V\ge2,
\]

the complete ordinary-polynomial unary spectrum is

\[
\boxed{
\operatorname{Spec}_{\mathrm{Poly}}(q_V)
=
\{\text{constant maps }\mathbb N_0\to\mathbb N_0\}
\cup
\{\operatorname{id}\}.}
\]

So the entire polynomial growth degree `p>=2` regime has the same polynomial unary safe spectrum, even though its basin geometries differ.

This gives another important reverse-identifiability boundary:

\[
\boxed{
\operatorname{Spec}_{\mathrm{Poly}}(q_V)
\text{ does not determine }p
\text{ once }p\ge2.}
\]

A richer operation language or additional causal observations are required to recover the growth degree.

## 8. A2-SOA-S1-T06 — complete polynomial unary spectrum for a nontrivial fixed block

Now take the linear fixed-block law

\[
V_d(k)=dk,
\qquad d>1,
\]

so every basin has width `d`.

Let `f:N_0->N_0` be polynomial.

If `deg f>=2`, then on the block

\[
[dq,dq+d-1]
\]

the endpoint span

\[
f(dq+d-1)-f(dq)
\]

grows without bound as `q->infinity`, while a target block has fixed width `d`. Thus `f` is unsafe.

If `f(n)=an+b` with `a>=1`, safety forces

\[
a(d-1)\le d-1,
\]

so `a=1`. The remaining translation

\[
f(n)=n+b
\]

preserves every fixed block exactly when

\[
d\mid b.
\]

Constants are safe.

Therefore

\[
\boxed{
\operatorname{Spec}_{\mathrm{Poly}}(q_d)
=
\{\text{constant maps}\}
\cup
\{n\mapsto n+jd:j\in\mathbb N_0\},
\qquad d>1.}
\]

For `d=1`, the quotient is equality and every polynomial self-map is safe.

## 9. A2-SOA-S1-C01 — polynomial-operation phase transition

Combining T05 and T06 gives a sharp operation-spectrum change:

\[
\boxed{
\begin{array}{ll}
V(k)=dk,\ d>1:
&\text{constants plus the period translations }n\mapsto n+jd,\\[4pt]
\deg V\ge2:
&\text{constants plus identity only.}
\end{array}}
\]

Thus stage-3's translation rigidity is not an isolated additive fact. It is the degree-one edge of a broader polynomial-operation collapse.

The interpretation is causal rather than metric:

> nonlinear complete-growth basins do not merely make a fixed step inconvenient; they forbid every nontrivial ordinary polynomial unary dynamics from being exact on level-only state.

Any richer exact dynamics in that regime must therefore use at least one of:

- retained basin/detail state;
- a non-polynomial operation adapted to the quotient geometry;
- a typed operation whose domain is not the anonymous coarse level alone;
- a future-safe refinement generated by the actual action language.

## 10. Relation to the parent no-go theorems

The parent note proves that ordinary internal binary addition and multiplication force the identity P008 quotient. This supplement is complementary:

- the parent theorems constrain **multi-input ordinary arithmetic**;
- T05 constrains the entire family of **unary ordinary polynomial self-maps** under nonlinear complete growth;
- T06 shows exactly what survives in the linear fixed-block exception.

The common source is the same: a safe operation must transport each collapsed fiber into one collapsed fiber. The operation's image variation cannot exceed the geometry available in the target fiber.

## 11. Prior-art discipline

The proof uses only elementary polynomial asymptotics and the classical quotient-congruence criterion. No generic universal-algebra or transformation-semigroup theorem is claimed as new.

The Enterprise Math contribution under pressure test is the specific P008 complete-growth classification and its causal interpretation as a natural-operation-spectrum phase transition.

## 12. Executable evidence

`src/enterprise_math/safe_operation_algebra.py` now includes

- `finite_growth_unary_witness(...)`, an exact finite-prefix descent oracle.

`tests/test_safe_operation_algebra.py` pressure-tests the classification on:

- square complete growth;
- cubic complete growth;
- fixed blocks of width five;
- identity and constants as surviving controls;
- positive translations, dilation, and squaring as failing controls where the theorem predicts failure.

The bounded oracle is executable evidence only; T02–T06 are the mathematical proofs.
