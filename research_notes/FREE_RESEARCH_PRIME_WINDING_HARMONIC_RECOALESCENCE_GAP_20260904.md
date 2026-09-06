# Free Research — Prime-Winding Harmonic Recoalescence and Quotient Gap

Status: `FREE_RESEARCH_FRONTIER / COEFFICIENT_TWO_CLOSED / EXACT_SUPPORT_GAP_CLOSED / PNT_TRANSFER_GATE_OPEN / NOT_WORKING_TRUTH / NOT_FOUNDATION / EXTERNAL_NOVELTY_UNVERIFIED`
Date: `2026-09-04`
Parent: `FREE_RESEARCH_PI_PRIME_GEOMETRY_FRONTIER_V3_20260904.md`

## 1. Executive advance

The V3 frontier left two successive gates:

1. prove the primitive-energy main term
   \[
   \Psi_2(N)=2N\log N+O(N);
   \]
2. exclude a persistent approximate `-1` mode of the prime-power quotient-return operator.

This checkpoint closes the first gate by an elementary finite harmonic-recoalescence argument and closes the **exact support-level** part of the second gate by a `2-2-4` odd triangle. It also proves that the normalized return kernel becomes uniform in logarithmic quotient scale against every fixed smooth test function.

The remaining problem is narrower:

> transfer the scalar Selberg residual, or a higher positive provenance energy, into quantitative control of the signless quotient-edge defects for the actual bounded but nonsmooth error profile.

No complex zero-free theorem, numerical PNT assumption, or primitive value of `pi` is used.

---

## 2. Ordered harmonic history volumes

For `r >= 0` and `N >= 1`, define the ordered `r`-history harmonic volume

\[
\mathcal H_0(N):=1,
\]

and

\[
\boxed{
\mathcal H_r(N)
:=\sum_{n_1\cdots n_r\le N}
\frac1{n_1\cdots n_r}.
}
\]

Thus

\[
\mathcal H_1(N)=\sum_{n\le N}\frac1n
\]

is the ordinary harmonic number and

\[
\mathcal H_2(N)=\sum_{ab\le N}\frac1{ab}
\]

is the ordered two-history volume under the multiplicative cutoff.

These are finite positive rational quantities before any logarithmic completion.

---

## PHR-T01 — Exact Möbius recoalescence hierarchy

For every `r >= 1` and `N >= 1`,

\[
\boxed{
\sum_{d\le N}\frac{\mu(d)}d
\mathcal H_r\!\left(\left\lfloor\frac Nd\right\rfloor\right)
=\mathcal H_{r-1}(N).
}
\]

### Proof

Expand the left side:

\[
\sum_{d n_1\cdots n_r\le N}
\frac{\mu(d)}{d n_1\cdots n_r}.
\]

Group the first two labels by `m=d n_1`. Their coefficient is

\[
\frac1m\sum_{d\mid m}\mu(d).
\]

The divisor sum is `1` for `m=1` and `0` otherwise. Therefore the first Möbius-labelled history and the first positive history recoalesce completely, leaving exactly the ordered `(r-1)`-history volume.

The first two instances are

\[
\boxed{
\sum_{d\le N}\frac{\mu(d)}d
\mathcal H_1\!\left(\left\lfloor\frac Nd\right\rfloor\right)=1
}
\]

and

\[
\boxed{
\sum_{d\le N}\frac{\mu(d)}d
\mathcal H_2\!\left(\left\lfloor\frac Nd\right\rfloor\right)
=\mathcal H_1(N).
}
\]

This is the finite arithmetic core that forces the coefficient `2` below.

---

## 3. Smoothed Möbius moments

Set

\[
M_j(N):=
\sum_{d\le N}\frac{\mu(d)}d
\log^j\!\left(\frac Nd\right).
\]

The exact floor identity

\[
\sum_{d\le N}\mu(d)\left\lfloor\frac Nd\right\rfloor=1
\]

implies

\[
M_0(N)=O(1),
\]

because replacing `floor(N/d)` by `N/d` has total error at most `N`.

Using

\[
\mathcal H_1(\lfloor y\rfloor)
=\log y+\gamma+O(1/y)
\]

inside PHR-T01 for `r=1` gives

\[
\boxed{M_1(N)=O(1).}
\]

The weighted remainder is bounded because

\[
\sum_{d\le N}\frac1d O(d/N)=O(1).
\]

---

## PHR-T02 — Exact hyperbola decomposition of the two-history volume

Let `m=floor(sqrt N)`. Then

\[
\boxed{
\mathcal H_2(N)
=2\sum_{a\le m}\frac1a
\mathcal H_1\!\left(\left\lfloor\frac Na\right\rfloor\right)
-\mathcal H_1(m)^2.
}
\]

Indeed every pair `(a,b)` with `ab<=N` has `a<=m` or `b<=m`; the intersection is the full square `a,b<=m`.

Insertion of the elementary harmonic estimate yields

\[
\boxed{
\mathcal H_2(\lfloor y\rfloor)
=\frac12\log^2y+2\gamma\log y+C_2
+O\!\left(\frac{1+\log y}{\sqrt y}\right)
}
\]

for a constant `C_2` whose value is irrelevant here.

The important geometric term is

\[
\frac12\log^2 y.
\]

It is the volume of the ordered logarithmic simplex

\[
\{(u,v)\in\mathbb R_{\ge0}^2:u+v\le\log y\}.
\]

---

## PHR-T03 — The Möbius second moment has coefficient `2`

Insert PHR-T02 into the exact `r=2` recoalescence identity. The remainder contributes only `O(1)` because

\[
\frac1{\sqrt N}
\sum_{d\le N}
\frac{1+\log(N/d)}{\sqrt d}
=O(1).
\]

Consequently

\[
\mathcal H_1(N)
=\frac12M_2(N)+2\gamma M_1(N)+C_2M_0(N)+O(1).
\]

Since

\[
\mathcal H_1(N)=\log N+O(1),
\qquad M_0(N)=O(1),
\qquad M_1(N)=O(1),
\]

we obtain

\[
\boxed{
M_2(N)=2\log N+O(1).
}
\]

### Geometric meaning of `2`

The factor is not inserted from an analytic target. It is forced by the inverse of the simplex coefficient `1/2`:

\[
\text{ordered two-history area }
\frac12(\log N)^2
\xrightarrow{\text{one Möbius recoalescence}}
\text{one-history length }\log N.
\]

Thus the coefficient `2` is the normalization required for a two-dimensional logarithmic history volume to collapse to a one-dimensional history length.

---

## PHR-T04 — Primitive Selberg energy main term

Recall

\[
\Lambda_2:=\mu*\log^2
=\Lambda\log+\Lambda*\Lambda
\]

and

\[
\Psi_2(N):=\sum_{n\le N}\Lambda_2(n).
\]

Finite convolution rearrangement gives

\[
\Psi_2(N)
=\sum_{d\le N}\mu(d)
Q_2\!\left(\left\lfloor\frac Nd\right\rfloor\right),
\]

where

\[
Q_2(Y):=\sum_{m\le Y}(\log m)^2.
\]

Elementary sum-integral comparison gives

\[
Q_2(\lfloor y\rfloor)
=y\bigl(\log^2y-2\log y+2\bigr)
+O(1+\log^2y).
\]

The total contribution of the remainder is `O(N)`, because

\[
\sum_{d\le N}\bigl(1+\log^2(N/d)\bigr)=O(N).
\]

The main term is

\[
N\bigl(M_2(N)-2M_1(N)+2M_0(N)\bigr).
\]

Using PHR-T03 therefore proves

\[
\boxed{
\Psi_2(N)=2N\log N+O(N).
}
\]

Equivalently,

\[
\boxed{
\sum_{n\le N}\Lambda(n)\log n
+
\sum_{ab\le N}\Lambda(a)\Lambda(b)
=2N\log N+O(N).
}
\]

This closes the first open gate in the V3 return-operator frontier.

### Prior-art boundary

The resulting asymptotic is Selberg's classical symmetry formula. The claim here is not external novelty for that formula. The project-specific contribution is the exact carrier identification:

- `Lambda` is the prime-winding layer birth current;
- `Lambda*Lambda` is ordered two-history recoalescence energy;
- the coefficient `2` is forced by finite harmonic history-volume collapse.

---

## PHR-T05 — Higher primitive-energy recurrence

Let `D` be logarithmic differentiation on arithmetic functions,

\[
(Df)(n)=f(n)\log n,
\]

and define

\[
\Lambda_r:=\mu*\log^r.
\]

The derivation rule for Dirichlet convolution and `mu*1=delta` give

\[
\boxed{
\Lambda_{r+1}=D\Lambda_r+\Lambda*\Lambda_r.
}
\]

Since `Lambda_1=Lambda>=0`, this proves inductively

\[
\boxed{\Lambda_r(n)\ge0\quad(r\ge1).}
\]

The first cases are

\[
\Lambda_2=\Lambda\log+\Lambda*\Lambda,
\]

and

\[
\Lambda_3
=\Lambda\log^2
+3\Lambda*(\Lambda\log)
+\Lambda*\Lambda*\Lambda.
\]

This extends the factorial provenance hierarchy: degree `r` is a positive sum of ordered collision channels involving at most `r` prime-winding histories.

---

## 4. Cleaner real-scale return equation

Let `psi(x)` be defined for real `x>=1` by the usual prime-power cutoff and set

\[
r(x):=\frac{\psi(x)}x-1.
\]

PHR-T04 and the already proved boundary estimate `H(x)=O(x)` yield

\[
\psi(x)\log x
+
\sum_{a\le x}\Lambda(a)\psi(x/a)
=2x\log x+O(x).
\]

The factorial-mass identity together with `psi(x)=O(x)` gives

\[
\boxed{
A(x):=\sum_{a\le x}\frac{\Lambda(a)}a
=\log x+O(1).
}
\]

Substitution of `psi(y)=y(1+r(y))` now gives the floor-free normalized return law

\[
\boxed{
r(x)
+
\frac1{\log x}
\sum_{a\le x}\frac{\Lambda(a)}a r(x/a)
=O(1/\log x).
}
\]

This is equivalent in asymptotic strength to the V3 floor-normalized kernel but is better adapted to logarithmic-scale analysis.

---

## PHR-T06 — Uniform logarithmic-scale distribution of return mass

For `T>0`, define the positive measure on `[0,1]`

\[
\nu_T
:=\frac1T
\sum_{a\le e^T}\frac{\Lambda(a)}a
\delta_{\log a/T}.
\]

The preceding estimate for `A(x)` gives the uniform discrepancy bound

\[
\boxed{
\nu_T([0,u])=u+O(1/T)
\qquad(0\le u\le1).
}
\]

Hence for every fixed continuously differentiable test function `phi` on `[0,1]`,

\[
\boxed{
\int\phi\,d\nu_T
=
\int_0^1\phi(u)\,du
+O_\phi(1/T).
}
\]

Equivalently, the prime-power return current is asymptotically uniform in **logarithmic scale**, despite being singular and supported only on prime powers.

For the actual quotient variable this says

\[
\boxed{
\frac1{\log x}
\sum_{a\le x}\frac{\Lambda(a)}a
\phi\!\left(\frac{\log(x/a)}{\log x}\right)
=
\int_0^1\phi(v)\,dv
+O_\phi(1/\log x).
}
\]

Thus the limiting smooth return operator is the Hardy averaging operator

\[
(\mathcal Hf)(t)
=\frac1t\int_0^t f(v)\,dv.
\]

The formal limiting homogeneous equation

\[
f+\mathcal Hf=0
\]

has only the bounded solution `f=0`: if `F(t)=integral_0^t f`, then `F'=-F/t`, hence `(tF)'=0`; boundedness at the origin forces `F=0`.

This is a strong indication that the remaining obstruction is not a genuine macroscopic eigenmode, but a possible nonsmooth concentration effect in passing from the finite atomic kernels to the Hardy limit.

---

## 5. Exact `2-2-4` odd triangle

Define quotient maps

\[
q_2(n)=\left\lfloor\frac n2\right\rfloor,
\qquad
q_4(n)=\left\lfloor\frac n4\right\rfloor.
\]

They satisfy exactly

\[
\boxed{q_2(q_2(n))=q_4(n).}
\]

For any real-valued function `f`, define signless edge defects

\[
\delta_2f(n):=f(n)+f(q_2(n)),
\]

\[
\delta_4f(n):=f(n)+f(q_4(n)).
\]

Then

\[
\boxed{
2f(n)
=\delta_2f(n)+\delta_4f(n)-\delta_2f(q_2(n)).
}
\]

This is the algebraic boundary of the odd triangle

\[
n\xrightarrow{2}q_2(n)\xrightarrow{2}q_4(n),
\qquad
n\xrightarrow{4}q_4(n).
\]

The two paths to the same endpoint have different edge parity. Therefore an exact sign reversal on every prime-power quotient edge is impossible.

---

## PHR-T07 — Exact support-level `-1` mode is absent

If

\[
\delta_2f(n)=0
\quad\text{and}\quad
\delta_4f(n)=0
\]

for every `n`, then the odd-triangle identity gives

\[
2f(n)=0
\]

for every `n`. Hence

\[
\boxed{f\equiv0.}
\]

Thus the quotient support graph generated by the prime powers `2` and `4` has no nonzero exact `-1` mode.

This closes the qualitative support question left open in V3. What remains is quantitative transfer from the scalar averaged return residual to these individual edge defects.

---

## PHR-T08 — Uniform signless Poincare inequality

Cauchy--Schwarz applied to the odd-triangle identity gives

\[
\boxed{
4|f(n)|^2
\le3\Bigl(
|\delta_2f(n)|^2
+|\delta_4f(n)|^2
+|\delta_2f(q_2(n))|^2
\Bigr).
}
\]

Summing and observing that every quotient `m` has at most two preimages under `q_2` yields

\[
\boxed{
\sum_{n=4}^{N}|f(n)|^2
\le
\frac94\sum_{n=2}^{N}|\delta_2f(n)|^2
+
\frac34\sum_{n=4}^{N}|\delta_4f(n)|^2.
}
\]

Hence the support graph has a finite, uniform signless Poincare gap. The remaining issue is not the existence of a gap; it is whether the arithmetic energy controls the correct edge-defect norm.

---

## PHR-T09 — Prime-tower phase gap

For every integer `p>=2` and every complex phase `|z|=1`,

\[
\boxed{
\sum_{a\ge1}p^{-a}|1+z^a|^2
\ge\frac4{p^2-1}.
}
\]

Indeed

\[
\sum_{a\ge1}p^{-a}|1+z^a|^2
=
\frac2{p-1}+2\operatorname{Re}\frac{z}{p-z},
\]

and the minimum on the unit circle occurs at `z=-1`.

For a finite tower of height `A`,

\[
\boxed{
\sum_{a=1}^{A}p^{-a}|1+z^a|^2
\ge
\frac4{p^2-1}-\frac{4p^{-A}}{p-1}.
}
\]

This is a quantitative local version of the odd-cycle obstruction. After normalization in the full return kernel its visible gap is of order `1/log x`, so by itself it does not yet close the PNT normalization; however, its cumulative strength over logarithmically many scales is potentially divergent.

---

## 6. Updated status of the PNT route

### Closed in this checkpoint

1. The coefficient-two primitive-energy estimate:
   \[
   \Psi_2(N)=2N\log N+O(N).
   \]
2. The forcing in the V3 centered return equation is therefore `O(N)`.
3. The return current is uniformly distributed in logarithmic scale against fixed smooth tests.
4. The limiting Hardy equation has no bounded `-1` mode.
5. The exact finite quotient support graph has no nonzero `-1` mode.
6. A uniform finite signless Poincare inequality is available from the `2-2-4` triangle.

### Still open

1. Upgrade the scalar return residual to an averaged square-defect estimate such as
   \[
   \sum w_{N,a}|r(N)+r(N/a)|^2=o(1).
   \]
2. Alternatively, obtain that estimate from the degree-three positive primitive energy or from an averaged family of exact binomial/multinomial carry projectors.
3. Control possible concentration of the nonsmooth error profile when passing from the atomic finite kernels to the Hardy limit.
4. Deduce `r(N)->0`, hence `psi(N)~N` and then `pi(N)~N/log N`.

---

## 7. Next discriminating theorem

The next target is now precise:

> **Energy-to-defect transfer.** Construct a finite positive Gram identity whose diagonal is the degree-two Selberg return residual and whose off-diagonal recoalescence terms dominate the signless quotient defects on a family containing the `2-2-4` odd triangles.

A sufficient result would be

\[
\boxed{
\frac1{\log N}
\sum_{a\le N}\frac{\Lambda(a)}a
\left|r(N)+r(N/a)\right|^2
\longrightarrow0.
}
\]

Combined with PHR-T08 or the logarithmic Hardy limit, this would force

\[
r(N)\to0.
\]

The degree-three recurrence

\[
\Lambda_3=D\Lambda_2+\Lambda*\Lambda_2
\]

is the most natural next carrier because it contains exactly the self-energy and ordered collision terms needed to polarize the degree-two residual.

---

## 8. Verification boundary

The companion exact checker verifies:

- the finite Möbius harmonic-recoalescence hierarchy;
- the exact hyperbola identity for `H_2`;
- the logarithmic-derivation recurrence for the first primitive tensors over formal prime labels;
- nonnegativity and the top-shell factorial coefficient;
- the `2-2-4` triangle identity;
- local and global signless coercivity.

Asymptotic estimates are proved in this note by explicit finite rearrangement and elementary sum-integral bounds. The checker is regression evidence for the exact kernels, not a replacement for those proofs.
