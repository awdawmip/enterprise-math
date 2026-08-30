# Addition–Multiplication Bridge A1 — Integer Binomial Jet / Cross-Effect Calculus Research Return

Researcher-ID: `EM-AMBIN-A1-4C7F2D`  
Task: `RS-ADDMUL-BINOMIAL-CROSS-EFFECT-CALCULUS`  
Publication: `TP2-FFA35294B92DF03EDC0D`  
Claim: `chatgpt-ambin-a1-20260830-1047-4c7f2d`  
Execution record: `ER-72DC5FB53F1D1D2C29B6`

## 1. Terminal verdict

`SUCCESS / EXACT_CROSS_EFFECT_CALCULUS_CONSTRUCTED`

Hard target disposition:

`INTEGER_BINOMIAL_JET_ADDITIVE_CROSS_EFFECT_CALCULUS_CLASSIFIED = EXACT_CROSS_EFFECT_CALCULUS_CONSTRUCTED`.

The task does **not** discover Chu–Vandermonde, Newton interpolation, integer-valued polynomial theory, or the general notion of cross-effect. Those are classical. The task-local residue is the exact synthesis needed by `OBJ-ADDMUL-BRIDGE-STRUCTURE`:

1. a closed all-order integer formula for every reduced cross-effect of the binomial jet;
2. an exact classification of its vanishing depth and multilinearity boundary;
3. a precise minimal sense in which multiplication is reconstructed from addition plus the second binomial observable;
4. an integer-only dilation/detail formula that couples the cross-effect hierarchy to the existing Enterprise graded-precision carry calculus;
5. a strict boundary showing that lower cross-effects are **filtered-degree** objects, not homogeneous graded objects, so they cannot be silently fed into the existing homogeneous monomial precision API without a lower-filtration correction.

The resulting local interface is called below:

`BINOMIAL_FILTERED_CROSS_EFFECT_PRECISION_V1`.

It is a task-local derived interface, not a new global tool family and not a canonical promotion.

---

## 2. Definitions

For `k >= 0`, define the integer-valued binomial polynomial

\[
Q_k(n)=\binom nk
      =\frac{n(n-1)\cdots(n-k+1)}{k!},
\qquad n\in\mathbf Z,
\]

with `Q_0=1`.

For a truncation level `K` define the binomial jet

\[
J_K(n)=(Q_0(n),Q_1(n),\ldots,Q_K(n)).
\]

For a map `F: Z -> Z`, its reduced `r`-fold cross-effect is

\[
\operatorname{cr}_rF(x_1,\ldots,x_r)
=
\sum_{S\subseteq[r]}
(-1)^{r-|S|}
F\!\left(\sum_{i\in S}x_i\right).
\]

For `F(0)=0`, `cr_2 F(x,y)=F(x+y)-F(x)-F(y)` is the ordinary additive deviation.

---

## 3. Theorem A — all-`k` additive convolution and finite truncation closure

For every `k>=0` and all `x,y in Z`,

\[
Q_k(x+y)=\sum_{i=0}^k Q_i(x)Q_{k-i}(y).
\tag{A1}
\]

This is the classical Chu–Vandermonde identity, here used as frozen input / independently regression-checked rather than claimed as new mathematics.

Consequently, for every fixed `K`,

\[
J_K(x+y)=J_K(x)\star_K J_K(y),
\]

where the `k`th coordinate of `\star_K` is the truncated Cauchy convolution in (A1). No coordinate above `K` is needed. Thus the finite binomial jet is **exactly closed under addition**.

### Closure boundary

The same fixed truncation is not closed under arbitrary multiplication of jet observables. In the binomial basis,

\[
Q_a(n)Q_b(n)
=
\sum_{j=0}^{\min(a,b)}
\frac{(a+b-j)!}{j!(a-j)!(b-j)!}
Q_{a+b-j}(n).
\tag{A2}
\]

All structure constants are nonnegative integers, but the top term has degree `a+b`. Therefore multiplying two generic degree-`<=K` jet expressions requires the jet through degree `2K`.

This is the first important firewall:

`ADDITIVE_TRUNCATION_CLOSED != MULTIPLICATIVE_TRUNCATION_CLOSED`.

---

## 4. Theorem B — exact reduced cross-effect formula

For integers `k>=1` and `r>=1`,

\[
\boxed{
\operatorname{cr}_rQ_k(x_1,\ldots,x_r)
=
\sum_{\substack{a_1+\cdots+a_r=k\\a_i\ge1}}
\prod_{i=1}^r Q_{a_i}(x_i)
}
\tag{B1}
\]

with the empty sum interpreted as zero.

### Proof

Apply the multivariable form of Vandermonde to every subset term:

\[
Q_k\!\left(\sum_{i\in S}x_i\right)
=
\sum_{\substack{a_i\ge0,\ i\in S\\\sum a_i=k}}
\prod_{i\in S}Q_{a_i}(x_i).
\]

Fix one exponent vector `(a_1,...,a_r)` and let `T={i:a_i>0}`. Its coefficient after inclusion–exclusion is

\[
\sum_{S\supseteq T}(-1)^{r-|S|}
=
(1-1)^{r-|T|}.
\]

This is zero unless `T=[r]`, and equals one when every `a_i>0`. That leaves exactly (B1). No division occurs in the cross-effect coefficients.

### Immediate classification

From (B1):

1. **Vanishing depth**
   \[
   \operatorname{cr}_rQ_k=0
   \quad\text{for }r>k.
   \]

2. **Exact nonvanishing depth**  
   for every `1<=r<=k`, the cross-effect is nonzero as a polynomial map.

3. **Symmetry**  
   `cr_r Q_k` is symmetric in its `r` arguments.

4. **Top cross-effect**
   \[
   \boxed{
   \operatorname{cr}_kQ_k(x_1,\ldots,x_k)=x_1x_2\cdots x_k.
   }
   \tag{B2}
   \]

5. **Binary cross-effect**
   \[
   \operatorname{cr}_2Q_k(x,y)
   =
   \sum_{i=1}^{k-1}Q_i(x)Q_{k-i}(y).
   \tag{B3}
   \]

6. For `k=2`,
   \[
   \boxed{
   Q_2(x+y)-Q_2(x)-Q_2(y)=xy.
   }
   \tag{B4}
   \]

This gives an exact integer cross-effect ladder: the `k`th binomial observable contains the `k`-fold product as its highest additive interaction kernel.

---

## 5. Theorem C — multilinearity occurs exactly at top arity

For `1<=r<=k`, `cr_r Q_k` is symmetric. It is additive in every argument for all inputs exactly when `r=k` (apart from the trivial zero case `r>k`).

The positive statement is (B2): a product of one copy of each variable is multilinear.

For the negative statement, assume `r<k` and put

\[
m=k-r+1\ge2.
\]

Set the other `r-1` arguments equal to `1`. Since `Q_a(1)=0` for `a>=2`, formula (B1) collapses to

\[
\operatorname{cr}_rQ_k(x,1,\ldots,1)=Q_m(x).
\tag{C1}
\]

Now

\[
Q_m(1)=0,\qquad
Q_m(m-1)=0,\qquad
Q_m(m)=1.
\]

Hence

\[
Q_m(1)+Q_m(m-1)\ne Q_m(m),
\]

so the first slot is not additive. By symmetry, no slot is generally additive.

Therefore the exact boundary is

\[
\boxed{
r=k:\ \text{multilinear};
\qquad
r<k:\ \text{generally non-multilinear};
\qquad
r>k:\ 0.
}
\tag{C2}
\]

This prevents a common overreach: the existence of higher cross-effects does not turn every lower interaction layer into a multilinear tensor.

---

## 6. Theorem D — multiplication recovery and the exact semantic boundary

Since `Q_0=1` is constant and `Q_1(n)=n` is additive, their higher additive deviations vanish. `Q_2` is the **first coordinate in the binomial-jet hierarchy** with a nonzero binary cross-effect, and (B4) yields multiplication exactly:

\[
xy
=
Q_2(x+y)-Q_2(x)-Q_2(y).
\tag{D1}
\]

Thus in the structure whose primitives include the additive group of `Z` and one unary observable `q=Q_2`, multiplication is definable by polarization.

### Normalized refinement uniqueness

Suppose an arbitrary function `q:Z->Z` satisfies

\[
q(x+y)-q(x)-q(y)=xy
\tag{D2}
\]

for all integers `x,y`. Then `q(0)=0`, and

\[
g(n)=q(n)-Q_2(n)
\]

is additive. Every additive map `Z->Z` has the form `g(n)=cn`. Hence

\[
q(n)=Q_2(n)+cn.
\tag{D3}
\]

If the normalization `q(1)=0` is imposed, then `c=0`, so `q=Q_2`.

This is the exact minimal-data statement available at task scope: within the binomial-jet hierarchy, `Q_2` is the first unary observable whose additive deviation recovers multiplication, and a normalized quadratic refinement with that deviation is unique.

### Firewall: definability is not primitive elimination

The theorem does **not** prove that multiplication is globally unnecessary as a primitive.

- If `Q_2` is itself introduced by the formula `n(n-1)/2`, then multiplication was used to define the observable.
- If `Q_2` is independently supplied as a primitive unary observable satisfying (D2), then multiplication is definable from `(+ ,Q_2)`.
- These are different language/semantic claims.

Accordingly:

`MULTIPLICATION_RECOVERABLE_FROM_PLUS_AND_Q2`

is proved, while

`MULTIPLICATION_CEASES_TO_BE_AN_INDEPENDENT_PRIMITIVE_IN_ALL_PRESENTATIONS`

is **not** claimed.

---

## 7. Theorem E — general iterated finite-difference calculus

Let

\[
\Delta_hF(n)=F(n+h)-F(n).
\]

For `r>=1`,

\[
\boxed{
\Delta_{h_1}\cdots\Delta_{h_r}Q_k(n)
=
\sum_{\substack{a_1,\ldots,a_r\ge1,\ b\ge0\\
a_1+\cdots+a_r+b=k}}
Q_b(n)\prod_{i=1}^rQ_{a_i}(h_i).
}
\tag{E1}
\]

At `n=0`, only `b=0` survives and this becomes the cross-effect formula (B1).

For unit steps,

\[
\Delta_1Q_k=Q_{k-1},
\qquad
\Delta_1^rQ_k=Q_{k-r},
\tag{E2}
\]

with `Q_j=0` for `j<0`.

Therefore the binomial basis converts repeated unit finite difference into a literal shift of the degree index—no rational coefficient recovery and no denominator bookkeeping.

---

## 8. Theorem F — integer-valued polynomial reconstruction

Let

\[
\operatorname{Int}(\mathbf Z)
=
\{p\in\mathbf Q[n]: p(\mathbf Z)\subseteq\mathbf Z\}.
\]

Every `p in Int(Z)` of degree at most `K` has a unique expansion

\[
\boxed{
p(n)=\sum_{k=0}^K a_k Q_k(n),
\qquad
a_k=\Delta_1^kp(0)\in\mathbf Z.
}
\tag{F1}
\]

This is the classical Newton/binomial basis theorem. It gives the reconstruction strength of the jet: the first `K+1` integer finite-difference coefficients are exactly the integral coordinates of every integer-valued polynomial of degree `<=K`.

### Power basis comparison

The ordinary integral power ring `Z[n]` is itself closed under finite differences; no contrary claim is made.

The distinction is instead:

- `Z[n]` is a strict subring of `Int(Z)`;
- for `k>=2`, `Q_k` has leading coefficient `1/k!`, so generally `Q_k notin Z[n]`;
- the binomial basis is an integral `Z`-basis for `Int(Z)`;
- in that basis `Delta_1` is the integral shift `Q_k -> Q_(k-1)`;
- converting the entire integer-valued polynomial class back to the ordinary power basis necessarily introduces factorial/Stirling denominator structure.

So the precise benefit is **integral closure for integer-valued polynomial observables**, not the false statement that power polynomials fail to survive finite differences.

---

## 9. Theorem G — exact integer dilation/detail expansion

This is the task-local bridge to finite precision.

Let the refinement ratio be `rho>=1`, and write a natural fine state as

\[
x=\rho a+u,
\qquad
a\in\mathbf N,\quad 0\le u<\rho.
\]

Define the nonnegative integer coefficient

\[
D_\rho(j,t)
=
[z^j]\big((1+z)^\rho-1\big)^t.
\tag{G1}
\]

Combinatorially, after partitioning `rho*a` labelled points into `a` blocks of size `rho`, `D_rho(j,t)` counts the ways to choose `j` points from exactly `t` already-selected nonempty blocks.

Then

\[
\boxed{
Q_j(\rho a)
=
\sum_{t=0}^jD_\rho(j,t)Q_t(a),
}
\tag{G2}
\]

and by Vandermonde,

\[
\boxed{
Q_k(\rho a+u)
=
\sum_{j=0}^k
\sum_{t=0}^j
D_\rho(j,t)Q_t(a)Q_{k-j}(u).
}
\tag{G3}
\]

All coefficients are integers and no continuous limit or rational projection is introduced.

The top diagonal coefficient is

\[
D_\rho(j,j)=\rho^j.
\tag{G4}
\]

Thus the dilation is triangular with respect to binomial degree: the degree-`j` top component scales by `rho^j`, while lower binomial degrees leak into the same fine observable.

This is the exact reason the binomial jet is naturally **filtered**, not purely graded, under precision scaling.

---

## 10. Theorem H — cross-effect precision carry/detail decomposition

Fix `1<=r<=k`, a refinement ratio `rho>=1`, and natural fine inputs

\[
x_i=\rho a_i+u_i,\qquad 0\le u_i<\rho.
\]

Write

\[
C_{r,k}(\mathbf x)
=
\operatorname{cr}_rQ_k(x_1,\ldots,x_r).
\]

Substitute (G3) into the positive-composition formula (B1). In each composition
`alpha_1+...+alpha_r=k`, there is a distinguished top choice

\[
j_i=t_i=\alpha_i,\qquad Q_0(u_i)=1,
\]

whose coefficient is

\[
\prod_i D_\rho(\alpha_i,\alpha_i)
=
\rho^k.
\]

All other terms are nonnegative on natural inputs. Therefore there is an exact integer remainder

\[
\boxed{
C_{r,k}(\rho\mathbf a+\mathbf u)
=
\rho^k C_{r,k}(\mathbf a)
+
R_{r,k,\rho}(\mathbf a,\mathbf u),
\qquad
R_{r,k,\rho}\ge0.
}
\tag{H1}
\]

Define

\[
\kappa_{r,k,\rho}
=
\left\lfloor\frac{R_{r,k,\rho}}{\rho^k}\right\rfloor,
\qquad
\delta_{r,k,\rho}
=
R_{r,k,\rho}\bmod\rho^k.
\tag{H2}
\]

Then

\[
\boxed{
\left\lfloor
\frac{C_{r,k}(\rho\mathbf a+\mathbf u)}{\rho^k}
\right\rfloor
=
C_{r,k}(\mathbf a)+\kappa_{r,k,\rho},
}
\tag{H3}
\]

and

\[
C_{r,k}(\rho\mathbf a+\mathbf u)
=
\rho^k
\left(C_{r,k}(\mathbf a)+\kappa_{r,k,\rho}\right)
+
\delta_{r,k,\rho},
\quad
0\le\delta<\rho^k.
\tag{H4}
\]

This is an exact degree-`k` projection/carry/detail decomposition.

### Tight finite-cell carry bound

Because every `Q_m(n)` is nondecreasing for `n>=0`, the positive formula (B1) makes `C_(r,k)` coordinatewise nondecreasing. Hence, for fixed coarse cell `a`, the carry is maximized at

\[
u_1=\cdots=u_r=\rho-1.
\]

Therefore

\[
0\le\kappa(\mathbf a,\mathbf u)
\le
\left\lfloor
\frac{
C_{r,k}(\rho\mathbf a+(\rho-1)\mathbf1)
-\rho^k C_{r,k}(\mathbf a)
}{\rho^k}
\right\rfloor,
\tag{H5}
\]

and the upper bound is attained at the upper detail corner.

### Existing-tool exact reuse at top arity

When `r=k`, theorem (B2) gives

\[
C_{k,k}(\mathbf x)=x_1\cdots x_k.
\]

Then (H1)–(H4) are exactly the existing degree-`k` homogeneous monomial projection defect in `src/enterprise_math/graded_precision.py`.

For `k=r=2`, with

\[
x=\rho a+u,\qquad y=\rho b+v,
\]

the carry is exactly

\[
\boxed{
\kappa
=
\left\lfloor
\frac{\rho av+\rho bu+uv}{\rho^2}
\right\rfloor,
}
\tag{H6}
\]

which is the existing `multiplication_precision_carry`.

Thus the multiplication recovered as `cr_2 Q_2` is not merely algebraically identical to `xy`; it lands on the project's already-existing precision carry API without translation loss.

---

## 11. Theorem I — minimal failure of homogeneous precision reuse

For `r<k`, `C_(r,k)` is generally not homogeneous of degree `k` under ordinary scaling. Formula (G2) has strict lower-binomial-degree terms `D_rho(j,t)` with `t<j`, and they survive in lower cross-effects.

Therefore even with **zero local details** `u_i=0`, the remainder in (H1) can be nonzero.

Exact example:

- `k=3`, `r=2`, `rho=2`;
- coarse inputs `(a,b)=(1,2)`;
- fine inputs `(2,4)` with zero details.

Then

\[
\operatorname{cr}_2Q_3(1,2)=1,
\]

while

\[
\operatorname{cr}_2Q_3(2,4)=16.
\]

The nominal degree-3 transport of the coarse value is `2^3*1=8`, leaving

\[
R=8,\qquad \kappa=1,\qquad \delta=0.
\]

So a nonzero precision carry appears **without any local projection detail at the inputs**. It is generated purely by lower filtration leakage of the binomial observable.

This proves the exact reuse boundary:

- `r=k`: `REUSE_EXISTING_GRADED_MONOMIAL_PRECISION` is exact.
- `r<k`: `GRADED_MONOMIAL_PRECISION_ALONE` is insufficient; one must add the integral triangular dilation correction (G1)–(G3).

This is the smallest genuinely new precision-side residue of A1.

---

## 12. Tool/method reuse resolution

### A. `recent.fq008.mixed_difference_separability`

- coverage verdict: `REUSE_EXISTING_TOOL`
- reuse state: `REUSE_APPLIED`
- use: retained the project's accepted mixed-finite-difference interpretation of interaction versus separability.
- task-local extension: A1 supplies the exact positive-composition coefficient formula (B1), vanishing depth, and the top/lower multilinearity classification. It does not replace the general mixed-difference diagnostic.

### B. `precision.integer_projection_calculus`

- coverage verdict: `REUSE_EXISTING_TOOL`
- reuse state: `REUSE_APPLIED`
- use: coarse/detail decomposition `x=rho*a+u`, exact carry/detail semantics, integer-only projection.
- hard boundary: precision inputs in this part remain natural-number states, matching the current implementation.

### C. `src/enterprise_math/graded_precision.py`

- coverage verdict: `REUSE_EXISTING_TOOL_WITH_EXACT_SCOPE_BOUNDARY`
- reuse state: `REUSE_APPLIED_AT_TOP_CROSS_EFFECT`
- use: `cr_k Q_k=prod x_i` is a homogeneous degree-`k` monomial, so the existing degree transport and monomial defect apply exactly.
- gap: `cr_r Q_k` for `r<k` is filtered rather than homogeneous, so the existing monomial API is not silently generalized.

### D. New general tool family?

`NO`.

Method-harvest classification: `RESULT_ONLY`.

The new formula package `BINOMIAL_FILTERED_CROSS_EFFECT_PRECISION_V1` is frozen as a task-local mathematical interface. Promotion to executable global tooling should occur only if a downstream task demonstrates repeated cross-lane reuse.

---

## 13. Exact checker

Checker:

`research_checks/ADDMUL_BINOMIAL_CROSS_EFFECT_CALCULUS_CHECK_20260830.py`

Certificate:

`research_artifacts/ADDMUL_BINOMIAL_CROSS_EFFECT_CALCULUS/exact_regression_certificate.json`

Executed result:

`PASS`.

Deterministic regression envelope:

- `K_MAX = 8`;
- integer-valuedness includes negative arguments;
- all `k<=8` Vandermonde checks on a signed box;
- all `1<=r<=k<=8` cross-effect positive-composition checks on `{-1,0,1}^r`;
- explicit `r=k+1` vanishing probes;
- top cross-effect/product checks;
- `28` exact lower-arity non-multilinearity witnesses;
- unit and general iterated-difference checks;
- Newton coefficient reconstruction checks;
- binomial-basis product structure constants;
- exact dilation/detail checks for ratios `2..5`;
- filtered cross-effect precision carry/detail checks across ratios `2,3,4`;
- exact `k=r=2` equality with the existing multiplication carry formula.

Total exact checks:

`381181`.

No mismatch was observed.

The checker is a regression certificate only. The all-integer/all-order result is supplied by the symbolic proofs above.

---

## 14. Prior-art / novelty boundary

The following are standard mathematics and are not claimed as project-original:

1. Chu–Vandermonde for binomial coefficients;
2. the binomial basis of `Int(Z)` and Newton finite-difference coordinates;
3. cross-effects/deviations as a classical way to measure non-additivity and polynomial degree;
4. binomial rings / integer-valued polynomial structure.

Relevant prior-art anchors inspected during this task include:

- J. Elliott, *Binomial rings, integer-valued polynomials, and lambda-rings*, Journal of Pure and Applied Algebra 207 (2006), 165–185, DOI `10.1016/j.jpaa.2005.09.003`.
- I. B. S. Passi, *Polynomial Maps*, Lecture Notes in Mathematics 372 (1974), 550–561, DOI `10.1007/978-3-662-21571-5_58`.
- Mathlib `RingTheory.Binomial`, which exposes a formal Chu–Vandermonde `add_choose_eq` API.
- Sage's integer-valued polynomial ring documentation, which uses the binomial basis and positive integral product structure constants.

The project-specific value is the exact synthesis and scope control needed for the add–multiply bridge objective, especially theorem H/I's coupling to Enterprise finite precision.

No literature novelty claim is made for the positive-composition formula itself; it is treated as an exact derived specialization unless separately audited.

---

## 15. What A1 establishes for the add–multiply bridge

The useful hierarchy is now precise:

\[
Q_k
\ \xrightarrow{\text{additive }r\text{-cross-effect}}
\sum_{a_1+\cdots+a_r=k,\ a_i>0}
\prod_i Q_{a_i}
\ \xrightarrow{r=k}
x_1\cdots x_k.
\]

At `k=2` this yields the ordinary binary product.

So addition plus nonlinear integer-valued observables can encode multiplicative interaction **without introducing multiplication at the cross-effect evaluation step**. But the source of the nonlinear observable remains semantically significant; the bridge is a definability/reconstruction theorem, not a universal ontology claim.

The strongest task-local statement is:

`BINOMIAL_JET_ADDITION_HAS_AN_EXACT_FINITE_INTERACTION_TOWER_WHOSE_TOP_CROSS_EFFECTS_ARE_PRODUCTS`.

---

## 16. Smallest follow-up interface

Do **not** open a successor merely to reprove binomial identities.

The smallest useful downstream interface is:

`BINOMIAL_FILTERED_CROSS_EFFECT_PRECISION_V1`

with the following fields:

- `k`: binomial degree;
- `r`: cross-effect arity;
- positive-composition expansion `(B1)`;
- `rho`: precision ratio;
- coarse vector `a`;
- detail vector `u`;
- dilation coefficients `D_rho(j,t)`;
- filtered remainder `R_(r,k,rho)`;
- carry `kappa=floor(R/rho^k)`;
- detail `delta=R mod rho^k`;
- reuse flag:
  - `HOMOGENEOUS_REUSE` iff `r=k`;
  - `FILTERED_CORRECTION_REQUIRED` iff `r<k`.

A valuable successor would ask whether this filtered correction composes coherently along a precision chain and whether its staged/direct defect is already captured by the existing precision-holonomy/cocycle tools.

That question should **reuse** the current `precision_holonomy` machinery rather than creating another transport formalism.

---

## 17. Scope firewall

This return proves/classifies the exact integer binomial-jet cross-effect calculus. It does not establish:

- that multiplication is dispensable from every foundational language;
- that `Q_2` is available without semantic cost in every model;
- that all nonlinear observables have binomial-type cross-effects;
- that lower cross-effects are multilinear;
- that fixed finite jets are closed under arbitrary multiplication;
- that the filtered precision correction is already canonical/global tooling;
- any Foundation, Working Truth, or canonical theorem promotion.

The task terminates successfully at the requested research scope and awaits independent Driver review.
