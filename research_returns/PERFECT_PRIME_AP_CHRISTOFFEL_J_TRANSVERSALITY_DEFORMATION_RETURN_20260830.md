# Perfect Prime AP Christoffel J-transversality deformation flow — Research Return

Task: `RS-PERFECT-PRIME-AP-CHRISTOFFEL-J-TRANSVERSALITY-DEFORMATION`  
Publication: `TP2-7A1C9E54B2306D8F41AA`  
Researcher-ID: `EM-PPTAPCHR1-0FF8B7`  
Claim: `chatgpt-pptapchr1-20260830-0ff8b7`  
Execution record: `ER-4A59F13A39780D3D2FF5`  
Reserved Result-ID: `RR-4857CC9B4B0CBF4EA6AD`

## Terminal verdict

`SUCCESS / EXACT_FIRST_ORDER_REAL_INERTIA_OBSTRUCTION_AT_M10 / PARENT_SURVIVES`

Hard-target disposition:

`AP_CHRISTOFFEL_J_TRANSVERSALITY_NO_ZERO_FLOW_PROVED_OR_EXACTLY_OBSTRUCTED` is closed at the **exact-obstruction** terminal class for the proposed crossing/inertia engines, not by a counterexample to the parent theorem.

The deformation
\[
\rho_{m,t}(u)=(1-tu^{m^2})^{m-1},\qquad 0\le t\le1,
\]
does exactly leave the Cauchy identity endpoint, and the quotient determinant has a nonzero first-order splitting coefficient in every exactly checked dimension `m=2,...,10`.  However two natural global transversality invariants fail exactly:

1. the symmetric Schur crossing form is already **indefinite at `m=3`** on the quotient of the known fixed direction;
2. more decisively, at the smallest dimension `m=10` the first quotient derivative `Q'_{10}(0)` is invertible and squarefree but has only seven real eigenvalues and one non-real conjugate pair.

Therefore a proof based on tracking `m-1` **real** crossing eigenvalues, their order, or a real spectral inertia from `t=0` cannot be an all-`m` proof engine.  This obstruction is AP-Christoffel-specific: it is extracted from the first derivative of the AP weight insertion itself.

Crucially, the obstruction does **not** produce a zero of the parent determinant.  At `m=10`,
\[
\det(-Q'_{10}(0))>0,
\]
so the fixed-space multiplicity collapses locally for sufficiently small `t>0`; and at the actual AP endpoint `t=1`,
\[
\det(I_9-Q_{10}(1))>0
\]
exactly.  Thus the parent Perfect-Prime cofactor target remains open and alive.

The best surviving route is spectrum-free: in midpoint half-Pascal coordinates the fixed-point equation is
\[
D_*(t)x=(C_*(t)-A_*(t))x=0.
\]
The known fixed vector is explicit for all `t`, and any nonzero maximal proper minor of `D_*(t)` closes fixed-point simplicity.  Exact finite discovery (`m=2..6`, derivative at `0` and `t=1/4,1/2,3/4,1`) finds **every proper minor positive** while `det D_*=0`.  This is evidence only, not an all-`m` theorem, but it survives the non-real spectral obstruction and is the sharply reduced successor frontier.

---

## 1. Exact deformation and the adversarial endpoint

Put `n=m-1`,
\[
w_i=(-1)^i\binom ni,\qquad W=\operatorname{diag}(w),
\]
and retain the frozen Möbius involution
\[
R_{ri}=(-1)^i\binom ri,\qquad R^2=I.
\]

The deformed moments are
\[
h_t(q)
=\int_0^1u^q(1-tu^{m^2})^n\,du
=\sum_{r=0}^{n}
\frac{(-1)^r\binom nr t^r}{q+1+r m^2},
\]
hence
\[
H(t)_{ij}=h_t(i+mj).
\]
Define
\[
e(t)=H(t)w,\qquad d(t)=H(t)^Tw,
\]
\[
A(t)=E(t)^{-1}H(t)W,\qquad
B(t)=D(t)^{-1}H(t)^TW,
\]
and
\[
T(t)=R\,B(t)A(t)\,R.
\]

The normalizers are positive throughout `0<=t<=1` because
\[
e_i(t)=\int_0^1u^i(1-u^m)^n\rho_{m,t}(u)\,du>0,
\]
\[
d_j(t)=\int_0^1u^{mj}(1-u)^n\rho_{m,t}(u)\,du>0.
\]
Thus the normalized operator is real-analytic in `t` on the entire interval.

At `t=0`,
\[
h_0(q)=\frac1{q+1},
\]
so the mandatory Cauchy negative control is reproduced exactly:
\[
T(0)=I_m.
\]
The known fixed vector is `e_0` in the frozen `T` coordinates for every `t`, so
\[
T(t)=
\begin{pmatrix}
1 & *\\
0 & Q_m(t)
\end{pmatrix},
\qquad
Q_m(0)=I_{m-1}.
\]
The target is
\[
\det(I_{m-1}-Q_m(1))\ne0.
\]

---

## 2. First Christoffel insertion

Differentiating the exact moments at `t=0` gives
\[
H_1{}_{ij}:=H'(0)_{ij}
=-\frac{m-1}{i+mj+1+m^2}.
\]
This is the first place where the AP-specific exponent `m^2` enters; replacing the weight by the constant Cauchy measure deletes this term.

Write
\[
T(t)=I+tT_1+O(t^2),
\qquad
Q_m(t)=I+tQ_{1,m}+O(t^2).
\]
The checker differentiates the row normalizers and both half maps exactly over `Fraction`, with
\[
A_1=E_0^{-1}H_1W-E_0^{-1}E_1A_0,
\]
\[
B_1=D_0^{-1}H_1^TW-D_0^{-1}D_1B_0,
\]
\[
T_1=R(B_1A_0+B_0A_1)R.
\]
The first column of `T_1` is zero, as required by persistence of the known fixed vector.

If `Q_{1,m}` is invertible then
\[
\det(I-Q_m(t))
=t^{m-1}\det(-Q_{1,m})+O(t^m).
\]
So the first-order quotient operator simultaneously measures immediate collapse of the degenerate fixed space and tests whether a real crossing/inertia law is even available.

---

## 3. Exact first-order census and the smallest real-spectrum obstruction

Pure rational Faddeev–LeVerrier plus Sturm sequences give:

| m | degree | negative real roots of `Q'_(m)(0)` | positive real roots | non-real roots | squarefree |
|---:|---:|---:|---:|---:|:---:|
| 2 | 1 | 1 | 0 | 0 | yes |
| 3 | 2 | 2 | 0 | 0 | yes |
| 4 | 3 | 3 | 0 | 0 | yes |
| 5 | 4 | 4 | 0 | 0 | yes |
| 6 | 5 | 5 | 0 | 0 | yes |
| 7 | 6 | 6 | 0 | 0 | yes |
| 8 | 7 | 7 | 0 | 0 | yes |
| 9 | 8 | 8 | 0 | 0 | yes |
| 10 | 9 | 7 | 0 | 2 | yes |

For every row above,
\[
\det(-Q_{1,m})>0.
\]

Thus `m=10` is the **smallest exact obstruction** to the tempting all-`m` statement

`FIRST_CHRISTOFFEL_SPLITTING_HAS_M_MINUS_1_SIMPLE_REAL_NEGATIVE_DIRECTIONS`.

At `m=10`, the degree-nine characteristic polynomial of `Q'_{10}(0)` has exactly seven real roots, all negative, and the remaining two roots form one simple non-real conjugate pair.  The canonical fraction-coefficient hash is

`sha256:0cf9c194b264d2e22123f3faeaf86ab4f63e1c08026201a1bdd159ffd61f1377`.

Moreover
\[
\det(-Q'_{10}(0))
=
\frac{
8597734096516157311064924037801994131870670312500000000000000000000
}{
13352633520989266022942994590924134927743000288908965291282138125853573914280323033879713
}>0.
\]

### Consequence 1: exact local splitting at `m=10`

Because the leading coefficient is nonzero,
\[
\det(I-Q_{10}(t))
=t^9\det(-Q'_{10}(0))+O(t^{10}),
\]
hence it is nonzero for all sufficiently small positive `t`.

The non-real pair is therefore **not** a failure of local transversality.  It is a failure of the idea that local transversality can be encoded by real ordered crossing eigenvalues.

### Consequence 2: real spectral inertia cannot be the all-m invariant

The scaled analytic family
\[
\frac{Q_{10}(t)-I}{t}
\]
extends to `Q'_{10}(0)` at `t=0`.  Since the latter has a simple non-real conjugate pair, continuity of polynomial roots implies that the deformed quotient has a non-real pair for all sufficiently small positive `t`.

Hence any proof requiring the quotient spectrum to leave `1` along `m-1` real branches, or requiring a real spectral order/inertia throughout the deformation, is obstructed at the starting boundary itself.

This does not say `det(I-Q)` vanishes.

---

## 4. Independent exact obstruction to a definite symmetric crossing form

There is a natural symmetric Schur quantity
\[
\Sigma(t)
=
D(t)W^{-1}
-
H(t)^T W E(t)^{-1}H(t).
\]
A direct identity gives
\[
I-B(t)A(t)
=
D(t)^{-1}\Sigma(t)W.
\]
At the Cauchy endpoint, `Sigma(0)=0`, and the known fixed vector gives
\[
\Sigma'(0)w=0.
\]

At `m=3`, exact differentiation gives
\[
\Sigma'(0)=
\begin{pmatrix}
-47/15470 & 173/61880 & 267/30940\\
173/61880 & 17879/2722720 & 14073/1361360\\
267/30940 & 14073/1361360 & 8199/680680
\end{pmatrix},
\]
with kernel vector
\[
w=(1,-2,1)^T.
\]

Choose a basis of the Euclidean complement of `w`,
\[
v_1=(2,1,0)^T,\qquad
v_2=(-1,0,1)^T.
\]
The restricted Gram matrix is
\[
G=
\begin{pmatrix}
2177/388960 & 1201/38896\\
1201/38896 & -5617/680680
\end{pmatrix},
\]
and
\[
\boxed{\det G=-243/243100<0.}
\]

So the quotient crossing form is indefinite already at `m=3`.  A uniform positive- or negative-definite Schur crossing theorem is exactly false.

This obstruction is logically independent of the `m=10` non-real first-order spectrum.

---

## 5. Exact positive anchor: the full `m=2` deformation has no zero

The failure of the two proposed invariants is not evidence that the determinant flow itself is false.  In the smallest case the full rational function can be closed exactly:
\[
\det(I-Q_2(t))
=
\frac{
6t(5t-13)(13t-350)
}{
(t-15)(t-6)(3t-35)(3t-14)
}.
\]
For `0<t<=1`, both numerator factors after `t` are negative and all four denominator factors are negative.  Therefore
\[
\boxed{\det(I-Q_2(t))>0\quad(0<t\le1).}
\]

So the deformation is genuinely capable of leaving the identity endpoint without a recrossing in at least the first nontrivial dimension; what fails is the attempted universal invariant.

---

## 6. Parent guard at the first obstruction dimension

The exact checker independently reconstructs the actual AP endpoint `t=1` at `m=10` and verifies
\[
\det(I_9-Q_{10}(1))>0.
\]
Its exact fraction hash is

`sha256:a8dd130f9c473546c667b5215d6ef291d35dde20b1ec8912e20d3ea8b3ea6f5b`.

This agrees with the claim-authorized sibling Result `RR-0BCEB5E65D4B34FB3462`, which separately found the actual AP `m=10` quotient to have seven real roots in `(0,1)` plus one non-real conjugate pair.

Therefore:

`M10_FIRST_ORDER_REAL_INERTIA_OBSTRUCTION != PARENT_COUNTEREXAMPLE`.

The Perfect-Prime parent theorem remains open for general `m`.

---

## 7. Spectrum-free half-Pascal rank frontier

Define the Pascal one-parameter group
\[
P(s)_{ij}=\binom ij s^{i-j}\quad(j\le i),
\]
let
\[
S=P(1/2),\qquad J=\operatorname{diag}(1,-1,1,-1,\ldots).
\]
The elementary convolution identity `P(a)P(b)=P(a+b)` gives
\[
S^{-1}RS=J.
\]

With
\[
\widehat A=AR,\qquad
\widehat B=BR,
\]
put
\[
A_*=S^{-1}\widehat AS,\qquad
B_*=S^{-1}\widehat BS,
\]
\[
C_*=J B_*^{-1}J.
\]
Then
\[
T_*=S^{-1}TS
=J B_*J A_*
=C_*^{-1}A_*.
\]
Hence the fixed-point equation is
\[
D_*(t)x=0,
\qquad
D_*(t):=C_*(t)-A_*(t).
\]

The known fixed vector becomes explicit:
\[
z=S^{-1}e_0
=
(1,-1/2,1/4,-1/8,\ldots)^T,
\]
so
\[
\boxed{D_*(t)z=0}
\]
for every `m,t`.  Thus `det D_*(t)=0` identically.

But this singularity is exactly the right one.  Since a fixed vector is already known,
\[
\operatorname{rank}D_*(t)=m-1
\]
is equivalent to simplicity of the fixed eigenvalue.  In particular **one nonzero maximal proper minor** of `D_*(t)` suffices to prove
\[
\det(I_{m-1}-Q_m(t))\ne0.
\]

This route does not require the remaining spectrum to be real.

---

## 8. Exact finite discovery packet for `D_*(t)`

The checker tests the first derivative `D_*'(0)` and the rational grid
\[
t\in\{1/4,1/2,3/4,1\}
\]
for `m=2,...,6`, entirely over exact fractions.

For every tested matrix:

- `det D_*=0` exactly;
- the explicit vector `z` is in the kernel exactly;
- **every proper minor is strictly positive**.

The exhaustive proper-minor counts per matrix are:

| m | proper minors checked |
|---:|---:|
| 2 | 4 |
| 3 | 18 |
| 4 | 68 |
| 5 | 250 |
| 6 | 922 |

The same counts are passed for `D_*'(0)` and separately at each of the four positive rational parameters.

This is **finite discovery/regression only**.  It is not promoted to the all-`m`, all-`t` statement.

The important structural reduction is narrower than the sibling finite observation:

> A successor does not need to control the quotient eigenvalues.  It needs only an AP-Christoffel determinant formula proving that one `(m-1)x(m-1)` minor of `D_*(t)` never vanishes for `0<t<=1`.

If all proper minors can be shown positive, that is stronger; but a single canonical maximal minor is enough for the parent theorem.

---

## 9. What is proved, refuted, and left open

### Proved exactly

- the exact polynomial/rational deformation and positivity of the normalizers on `0<=t<=1`;
- the Cauchy endpoint `T(0)=I`;
- the first Christoffel insertion formula;
- exact first-order quotient spectra for every `m=2,...,10`;
- `m=10` is the smallest obstruction to all-real simple negative first-order quotient spectrum;
- `det(-Q'_{10}(0))>0`, hence exact local splitting at the obstruction dimension;
- the natural symmetric Schur crossing is indefinite at `m=3`;
- the full `m=2` deformation has `det(I-Q_2(t))>0` for every `0<t<=1`;
- the actual AP `m=10` endpoint still has `det(I-Q_10)>0` exactly;
- the all-`m` half-Pascal pencil identities and explicit fixed kernel vector;
- finite exact `D_*` proper-minor discovery packet for `m=2..6`.

### Refuted exactly

- `UNIFORM_DEFINITE_SYMMETRIC_CROSSING_FORM`;
- `ALL_M_FIRST_ORDER_REAL_SIMPLE_NEGATIVE_SPECTRAL_SPLITTING`;
- therefore any no-recrossing proof whose invariant requires either of those properties.

### Not proved or refuted

- the actual all-`m` no-zero theorem
  \[
  \det(I-Q_m(t))\ne0\quad(0<t\le1);
  \]
- all-`m` positivity of maximal/proper minors of `D_*(t)`;
- a global no-recrossing theorem independent of real spectrum.

So the correct terminal classification is an **exact obstruction to the proposed deformation invariants with a sharper surviving rank frontier**, not a parent counterexample.

---

## 10. Checker and certificate

Checker:

`research_checks/PERFECT_PRIME_AP_CHRISTOFFEL_J_TRANSVERSALITY_DEFORMATION_CHECK_20260830.py`

Certificate:

`research_artifacts/PERFECT_PRIME_AP_CHRISTOFFEL_J_TRANSVERSALITY_DEFORMATION/exact_certificate_20260830.json`

The checker is Python standard library only and uses exact `Fraction` arithmetic.  It verifies:

1. first-order quotient construction for `m=2..10`;
2. exact Faddeev–LeVerrier characteristic polynomials and Sturm root counts;
3. the `m=10` first-order polynomial/determinant hashes;
4. the actual AP `m=10` quotient determinant;
5. the exact `m=3` indefinite symmetric crossing certificate;
6. the half-Pascal conjugacy and transformed pencil;
7. exhaustive positivity of all proper minors in the declared finite discovery packet.

Finite checks are used as exact counterexamples and regression/discovery evidence only.  No finite positive pattern is silently upgraded to an all-`m` theorem.

---

## 11. Toolbox and source-exposure boundary

A bounded lookup found no registered Enterprise toolbox entry that directly covers this AP-Christoffel deformation / exact first-order Sturm / half-Pascal rank-certificate task.  The execution therefore uses a task-local exact checker and does not promote a new global tool.

This execution is **nonblind**.  It read the accepted parent `RR-33B5E1F81BCD9EEF1BD1` and, after CLAIM, the claim-authorized sibling `RR-0BCEB5E65D4B34FB3462` / PR `#931`.

A server-later duplicate execution PR `#932` was also inspected after CLAIM.  Its midpoint-Pascal algebra overlaps the surviving `D_*` frontier.  This return makes no independence or novelty claim for that algebra: the identities and finite deformation packet used here were independently rederived and replayed by this task's checker, but the source exposure is explicitly recorded.

The new terminal contribution of this execution is the **deformation first-order classification**:
- exact `m=3` crossing indefiniteness;
- exact `m=10` non-real first-order quotient pair with nonzero local determinant coefficient;
- and the consequent elimination of real-inertia/no-recrossing as a universal proof engine.

---

## 12. Recommended Driver action

Accept this Result at the exact-obstruction terminal class.

Freeze the following killed routes:

`DEFINITE_SYMMETRIC_CROSSING_FORM -> ALL_M_NO_ZERO`

and

`REAL_SIMPLE_FIRST_ORDER_QUOTIENT_SPECTRUM + INERTIA_TRACKING -> ALL_M_NO_ZERO`.

Do **not** infer an AP counterexample: the obstruction dimension `m=10` has local splitting and the actual endpoint determinant is positive.

If Driver opens a mathematical successor, the highest-leverage target is:

`AP_CHRISTOFFEL_MAXIMAL_MINOR_OF_DSTAR_POSITIVE_FOR_ALL_M_AND_T_IN_0_1`.

The first proof attempt should seek a direct Christoffel-insertion / Andreief / Cauchy–Binet formula for one canonical `(m-1)x(m-1)` minor of
\[
D_*(t)=C_*(t)-A_*(t).
\]
A nonzero formula for that single minor already forces rank `m-1` and closes the parent quotient determinant, while remaining compatible with non-real quotient spectrum.

No Working Truth, Foundation, canonical promotion, or novelty certificate is requested from this research return.
