# ADDMUL Formal-Group Interpolation — Research Return

Task: `RS-ADDMUL-FORMAL-GROUP-INTERPOLATION`  
Publication: `TP2-07769644BE60D76159D9`  
Researcher-ID: `EM-AMFGRP-A3-6C4E91`  
Claim: `chatgpt-amfgrp-a3-20260830-1050-6c4e91`  
Execution record: `ER-11F4C3F65419AC089140`  
Status: `SUCCESS / FINITE_INTERPOLATING_LAW_INTERFACE_CLASSIFIED`

## 1. Executive disposition

Hard target:

`FORMAL_GROUP_ADD_MUL_INTERPOLATION_ENTERPRISE_TRANSLATION_CLASSIFIED_OR_OBSTRUCTED`

Disposition:

`CLASSIFIED_WITH_EXACT_FINITE_INTERFACE_AND_INTEGER_LINEARIZATION_BOUNDARY`.

The family

\[
F_c(x,y)=x+y+cxy
\]

is not merely a heuristic interpolation. Over every commutative unital ring it is an exact commutative associative monoid law with unit `0`, and

\[
T_c(x)=1+cx
\]

is an exact multiplicative transport:

\[
T_c(F_c(x,y))=T_c(x)T_c(y).
\]

The decisive distinction is not associativity but **information retention and inverse domain**.

- If `c` is a unit, `T_c` is an affine bijection onto the whole ring, so `F_c` is exactly multiplication written in shifted/scaled coordinates at the monoid level.
- If `c` is regular but not a unit, `T_c` is injective into the proper multiplicatively closed submonoid `1+cR`; this is an exact embedded multiplication model, not full multiplication on `R`.
- If `c` is a zero divisor, `T_c` loses exactly `Ann_R(c)`: `T_c(x)=T_c(y)` iff `c(x-y)=0`. The quotient by these fibers is the information-preserving multiplicative image.
- The whole carrier is generally a monoid, not a group. The exact group locus is `1+cx in R^×`, with inverse `-x/(1+cx)`.

For finite/integer Enterprise semantics there are two clean interfaces:

1. `INTERPOLATING_SCALAR_CELL_V1` on `Z/NZ`, with exact finite fibers and inverse locus;
2. `FORMAL_GROUP_JET_CELL_V1` on the nilpotent ideal of `(Z/MZ)[epsilon]/(epsilon^(d+1))`, where a true formal-group `d`-jet gives an **exact finite associative operation** because all omitted terms vanish in the declared cell.

The ordinary-polynomial truncation of a formal group is different: it is associative only modulo the discarded degree. A sharp exact counterexample is given below; a degree-3 truncation has first associativity defect in degree 4 equal to

\[
-16xyz(x-z).
\]

The formal logarithm/ exponential route is also sharply bounded over `Z`: through degree `d`, the coefficients are integral exactly when the primorial `prod_{p<=d}p` divides `c`. Thus the classical characteristic-zero linearization does not silently provide an all-depth integer operation-safe bridge.

## 2. Exact algebra of `F_c`

Let `R` be a commutative unital ring and `c,x,y,z in R`.

### 2.1 Commutativity, unit, associativity

Commutativity and the unit `0` are immediate. Direct expansion gives

\[
F_c(F_c(x,y),z)
=x+y+z+c(xy+xz+yz)+c^2xyz,
\]

and the same expression is obtained from `F_c(x,F_c(y,z))`. Therefore no localization, completeness, topology or limiting argument is required for the basic law.

### 2.2 Exact shifted multiplicative transport

\[
\begin{aligned}
1+cF_c(x,y)
&=1+cx+cy+c^2xy\\
&=(1+cx)(1+cy).
\end{aligned}
\]

Hence `T_c:R -> R`, `x -> 1+cx`, is a monoid homomorphism from `(R,F_c,0)` to `(R,multiplication,1)`.

Its image is exactly `1+cR`, which is multiplicatively closed because

\[
(1+ca)(1+cb)=1+c(a+b+cab).
\]

Its fibers are exact:

\[
T_c(x)=T_c(y)\iff c(x-y)=0.
\]

Therefore the information kernel is precisely `Ann_R(c)`.

Consequences:

- `T_c` is injective iff multiplication by `c` is injective;
- if `c` is a unit, `T_c` is bijective `R -> R` and transports `F_c` to full multiplication;
- if `c` is regular nonunit, it embeds `F_c` into a proper multiplicatively closed affine ideal-coset;
- if `c` is a zero divisor, the exact quotient by the fiber congruence is isomorphic to `1+cR`.

This last statement is a direct application of the existing operation-safe quotient semantics: the preserved observable is explicitly `T_c`; no new general quotient machinery is introduced.

### 2.3 Exact inverse domain

Suppose `F_c(x,y)=0`. Applying `T_c` gives

\[
(1+cx)(1+cy)=1,
\]

so `1+cx` must be a unit. Conversely, if `1+cx` is a unit, then

\[
y=-x(1+cx)^{-1}
\]

satisfies `F_c(x,y)=0`. Because the coefficient of `y` in

\[
x+y+cxy=x+(1+cx)y
\]

is a unit, this inverse is unique.

Thus

\[
U_c=\{x\in R:1+cx\in R^\times\}
\]

is the exact group locus. The full carrier must not be called a group unless `U_c=R` has separately been proved.

## 3. Integer and finite-ring classification

### 3.1 Over `Z`

For `c=0`, `F_0=x+y` is the additive group.

For `c != 0`, multiplication by `c` is injective, so `T_c` is injective and the law is identified with the multiplicative submonoid `1+cZ`.

The only units of `Z` are `+/-1`. Therefore an integer `x` is invertible under `F_c` exactly when

\[
1+cx=\pm1.
\]

For nonzero `c`, this yields `x=0`, and possibly the second element `x=-2/c` when `c | 2`. Hence the nontrivial second group-locus element exists only for `c in {+/-1,+/-2}`.

Under a unit-linear coordinate change `phi_u(x)=ux`, `u in R^×`, one has

\[
\phi_u(F_c(x,y))=F_d(\phi_u(x),\phi_u(y))
\]

iff

\[
c=du.
\]

So parameters that differ by a unit are the same within this canonical linear coordinate class. Over `Z`, `c` and `-c` are therefore linearly isomorphic. This return does **not** claim a complete classification under arbitrary nonlinear abstract monoid isomorphisms.

### 3.2 Over `Z/NZ`

Let `g=gcd(c,N)` after choosing an integer representative of `c`. Then multiplication by `c` has kernel size `g` and image size `N/g`. Consequently

\[
|T_c(Z/NZ)|=N/g,
\]

and every shifted-readout fiber has exactly `g` elements.

Thus:

- `g=1` iff `c` is a unit iff `T_c` is a bijection and `F_c` is full multiplication in shifted coordinates;
- `g>1` gives a precisely quantified information loss;
- `x` is invertible under `F_c` iff `gcd(1+cx,N)=1`;
- on that locus,
  \[
  x^{-1_{F_c}}=-x(1+cx)^{-1}\pmod N.
  \]

This gives a finite exact `INTERPOLATING_SCALAR_CELL_V1` with no continuum semantics.

## 4. Formal logarithm: exact integer-depth obstruction

Over a coefficient ring where the denominators are legal, the classical formal coordinate is

\[
\log_c(x)=\frac{\log(1+cx)}{c}
=\sum_{n\ge1}(-1)^{n+1}\frac{c^{n-1}}{n}x^n,
\]

with inverse

\[
\exp_c(t)=\frac{e^{ct}-1}{c}
=\sum_{n\ge1}\frac{c^{n-1}}{n!}t^n.
\]

For `c=0` both are interpreted coefficientwise as the identity series.

The denominators cannot be hidden over `Z`. There is an exact finite-depth theorem.

### Theorem — primorial integrality criterion

For integer `c` and `d>=1`, all coefficients of both `log_c` and `exp_c` through degree `d` are integers iff

\[
P_d=\prod_{p\le d,\ p\ prime}p
\]

divides `c`.

**Necessity.** For each prime `p<=d`, the degree-`p` coefficient of `log_c` is `+/- c^{p-1}/p`. Its integrality forces `p|c`.

**Sufficiency for the logarithm.** If every prime divisor of `n<=d` divides `c`, then for every `p|n`,

\[
v_p(c^{n-1})\ge n-1\ge v_p(n),
\]

hence `n|c^{n-1}`.

**Sufficiency for the exponential.** For every prime `p<=n<=d`, `p|c`, and

\[
v_p(c^{n-1})\ge n-1\ge v_p(n!),
\]

so `n!|c^{n-1}`.

Therefore the maximum all-coefficient integer-safe depth is

\[
D(c)=\min\{p\text{ prime}:p\nmid c\}-1,
\]

with `D(0)=infinity`.

Examples:

- `c=1`: depth `1`;
- `c=2`: depth `2`;
- `c=6`: depth `4`;
- `c=30`: depth `6`.

This is a finite coefficient statement only. It does not turn the rational formal logarithm into a global integer isomorphism.

## 5. General finite truncation and the associativity defect

Let a true one-dimensional formal group law be

\[
F(X,Y)=X+Y+\text{higher terms}
\]

and let `G_d=J_dF` be its total-degree-`<=d` truncation.

There are two semantically distinct operations.

### 5.1 Correct finite jet cell

Work in

\[
A_{M,d}=(Z/MZ)[\epsilon]/(\epsilon^{d+1}),\qquad I=(\epsilon).
\]

For `x,y in I`, every monomial of total degree `>d` vanishes. Hence `F(x,y)` is determined exactly by `J_dF`, and the induced operation

\[
x\star y=J_dF(x,y)
\]

is exactly associative, has unit `0`, and inherits its inverse jet. The state set is finite, with cardinality `M^d`.

This is the recommended `FORMAL_GROUP_JET_CELL_V1` Enterprise interface.

### 5.2 Naive ordinary-polynomial truncation

If instead `G_d` is evaluated in an ordinary untruncated polynomial/ring carrier, its associator need not vanish.

Let the first omitted homogeneous layer be `H_{d+1}`:

\[
F=G_d+H_{d+1}+O(d+2).
\]

Define

\[
A_d=G_d(G_d(X,Y),Z)-G_d(X,G_d(Y,Z)).
\]

Exact associativity of `F` implies

\[
\operatorname{ord}(A_d)\ge d+1,
\]

and the degree-`d+1` layer is

\[
[A_d]_{d+1}
=-\bigl(
H(X,Y)+H(X+Y,Z)-H(Y,Z)-H(X,Y+Z)
\bigr).
\]

So the first external defect is the negative additive 2-coboundary of the first omitted layer. It can vanish, in which case the first defect occurs later. For example, the degree-1 truncation of `F_c` is ordinary addition and remains exactly associative because the omitted `cXY` layer has zero additive coboundary.

### 5.3 Sharp explicit counterexample

Take the strict integral coordinate

\[
h(t)=t+t^2.
\]

Its compositional inverse begins

\[
h^{-1}(s)=s-s^2+2s^3-5s^4+\cdots,
\]

so

\[
F=h^{-1}(h(X)+h(Y))
\]

is an exact associative integral formal group law. Through degree 4,

\[
F=X+Y-2XY+4X^2Y+4XY^2
-8X^3Y-20X^2Y^2-8XY^3+O(5).
\]

Its degree-3 ordinary polynomial truncation is

\[
G_3=X+Y-2XY+4X^2Y+4XY^2.
\]

Exact symbolic composition gives

\[
[G_3(G_3(X,Y),Z)-G_3(X,G_3(Y,Z))]_4
=-16XYZ(X-Z),
\]

which is nonzero. Thus the lower bound `d+1` is sharp already at `d=3`.

## 6. Tool reuse resolution

The current toolbox/method inventory was checked before introducing any reusable mechanism.

### T5 — Integer Precision / Refinement Calculus

- Coverage verdict: `REUSE_EXISTING_TOOL`.
- Reuse state: `REUSE_APPLIED`.
- Application: retained the existing finite-resolution discipline. High-order loss is explicit as a truncation/fiber defect; no real-number completion or continuum limit is smuggled into the project interface.
- Boundary preserved: finite integer precision only.

### T6 — Operation-Safe Quotient

- Coverage verdict: `REUSE_EXISTING_TOOL`.
- Reuse state: `REUSE_APPLIED`.
- Application: `T_c` is the declared observable; its fibers are an exact operation congruence. Over a general ring the lost fiber is `Ann(c)`; over `Z/NZ` every fiber has `gcd(c,N)` elements.
- Boundary preserved: the tool does not choose which distinctions are disposable; this task explicitly chooses shifted multiplicative readout.

### T9 — Holonomy / Cocycle / Gluing obstruction

- Coverage verdict: `NOT_APPLICABLE` to the ordinary-polynomial associator calculation.
- Reuse state: `NOT_APPLICABLE`.
- Reason: no transport graph or loop is declared here. The associator is kept as a typed polynomial coherence defect instead of inventing a renamed holonomy mechanism.

Executable-source search found no current formal-group-specific callable covering this exact input/output contract. The task-specific checker is therefore a certificate, not a proposed new global tool family.

Method harvest classification: `RESULT_ONLY`.

## 7. Deduplication against A1 and A2

### A1 — binomial cross-effect calculus

A1 asks how multiplication is recovered from additive observables such as

\[
Q_2(x+y)-Q_2(x)-Q_2(y)=xy.
\]

Its primitive carrier remains addition plus higher observable data. A3 instead changes the **binary law itself** to `F_c` and studies exact transport, inverse domains, parameter classes, and finite formal-group jets. Therefore A3 is not a repackaging of the A1 cross-effect route.

### A2 — delta/Frobenius defect tower

A2 studies prime-indexed additive defects

\[
D_p(x,y)=\delta_p(x+y)-\delta_p(x)-\delta_p(y),
\]

with `p=2` recovering `-xy` and odd primes carrying higher mixed terms. A3 has no prime-indexed Frobenius primitive: multiplication appears through the structural identity `1+cF_c=(1+cx)(1+cy)`. The A2 cocycle/valuation problem and the A3 law/coordinate/integrality problem are therefore distinct.

Possible future synthesis should compare the information cost of three typed bridges only after A1 and A2 have frozen their own results; this task does not pre-empt those independent returns.

## 8. Exact checker

Checker:

`research_checks/ADDMUL_FORMAL_GROUP_INTERPOLATION_CHECK_20260830.py`

A standalone standard-library replay in the execution environment returned:

```text
PASS ADDMUL_FORMAL_GROUP_INTERPOLATION
integer_assoc_transport=66759
integer_inverse_domain=3025
finite_ring_states=33579
integral_log_exp_jets=3368
truncation_associator_terms=16
```

The checker covers exact integer associativity/transport, integer inverse domains, `Z/NZ` image/fiber/inverse classification, the primorial log/exp criterion, and the degree-4 associator certificate for the strict-coordinate counterexample.

## 9. Frozen outputs and limitations

Frozen positive results:

1. exact `F_c` monoid law and shifted multiplicative transport;
2. exact information kernel `Ann(c)`;
3. exact group locus and inverse formula;
4. exact `Z/NZ` finite-cell classification;
5. exact primorial finite-depth integrality criterion;
6. exact nilpotent finite-jet interface;
7. exact general lowest-order associator-defect formula;
8. explicit sharp degree-3 truncation counterexample.

Frozen boundaries:

- no claim that arbitrary `F_c` carriers are groups;
- no hidden rational division in integer semantics;
- no claim that finite coefficient-integral log/exp jets are global integer linearizations;
- no claim of a complete arbitrary-coordinate classification of all parameters `c`;
- no claim that ordinary polynomial truncation is associative outside the declared nilpotent quotient;
- no claim that these classical formal-group identities are novel mathematics.

## 10. Terminal recommendation

Terminal state:

`FINITE_INTERPOLATING_LAW_INTERFACE_CLASSIFIED`.

The valuable residue is not a new generic formal-group toolkit. It is the exact separation of three regimes:

`EXACT_SHIFTED_MULTIPLICATIVE_MONOID`  
`FINITE_NILPOTENT_JET_EXACT`  
`ORDINARY_TRUNCATION_HAS_TYPED_COHERENCE_DEFECT`.

Driver review should preserve that three-way distinction and the primorial integer-safety boundary. Any later synthesis with A1/A2 should compare required auxiliary information and finite operation-safety rather than merging the routes by vocabulary alone.
