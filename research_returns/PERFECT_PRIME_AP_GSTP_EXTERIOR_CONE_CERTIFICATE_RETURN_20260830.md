# Perfect Prime AP GSTP exterior-cone certificate — Research Return

Task: `RS-PERFECT-PRIME-AP-GSTP-EXTERIOR-CONE-CERTIFICATE`  
Publication: `TP2-C5D08271E39A4B6F215C`  
Researcher-ID: `EM-PPTAPGSTP1-B540D3`  
Claim: `chatgpt-pptapgstp1-20260830-1613-b540d3`  
Execution record: `ER-98170DF2D49D4F82FA91`  
Reserved Result-ID: `RR-8C7AF805D30FEA04C67B`

## Terminal verdict

`SUCCESS / EXACT_GSTP_CERTIFICATE_BOUNDARY`

Hard-target disposition:

`EXISTENTIAL_GSTP_ROUTE_IS_NONREDUCTIVE_AND_CANONICAL_HALF_PASCAL_SIGNED_ORTHANT_CONES_ARE_EXACTLY_REFUTED_AT_M2; ACTUAL_AP_GSTP_STATUS_REMAINS_OPEN`.

This task did **not** prove that the actual AP operator is not generalized strictly totally positive.  It did something narrower and exact:

1. it pinned the external GSTP theorem interface and showed that a merely existential cone invocation is logically non-reductive here: existence of *some* all-exterior-power proper-cone structure is equivalent, under the cited Kushel result, to positive simple spectrum, which is stronger than the parent fixed-point-simplicity target;
2. it retained the mandatory all-`m` Cauchy identity endpoint, which proves that no cone proof based only on the broad common-measure / `u -> u^m` / factorwise-STP architecture can work;
3. it found an exact AP-specific midpoint-Pascal conjugacy `S^{-1} R S=J`, reducing the full operator to a clean generalized matrix pencil;
4. it then refuted, on the **actual AP operator at `m=2`**, every signed-orthant cone transported by that canonical midpoint-Pascal coordinate system;
5. it froze a new exact finite discovery packet (`m=2..6`) suggesting a much sharper successor: a singular total-positivity boundary for the transformed pencil difference `C_* - A_*`.

The correct conclusion is therefore an exact **certificate-route obstruction / negative boundary**, not a counterexample to the AP parent theorem and not a proof that no exotic proper-cone family exists.

---

## 1. Frozen AP operator

Let `n=m-1`,

\[
w_j=(-1)^j\binom nj,
\qquad
R_{ij}=(-1)^j\binom ij,
\qquad R^2=I.
\]

For the actual AP Christoffel weight

\[
\rho_m(u)=(1-u^{m^2})^n,
\]

the exact moment matrix is

\[
H_{ij}
=\int_0^1 u^{i+mj}(1-u^{m^2})^n\,du
=\sum_{\ell=0}^{n}
\frac{(-1)^\ell\binom n\ell}
{i+mj+m^2\ell+1}.
\]

Set

\[
e=Hw,\qquad d=H^T w,
\qquad E=\operatorname{diag}(e),\qquad D=\operatorname{diag}(d),
\]

\[
A=E^{-1}HW,
\qquad
B=D^{-1}H^T W,
\qquad W=\operatorname{diag}(w),
\]

\[
\widehat A=AR,
\qquad
\widehat B=BR,
\qquad
T_m=R\widehat B R\widehat A.
\]

The frozen parent already supplies

\[
T_m e_0=e_0.
\]

The target is to exclude a second fixed direction, equivalently

\[
\det(I_{m-1}-Q_m)\ne0.
\]

Factorwise strict total positivity of `Ahat,Bhat` is accepted input and is not reproved here.

---

## 2. Exact external theorem interface: what GSTP would give, and why existence alone is circular

The pinned external source is:

O. Y. Kushel, *Cone-theoretic generalization of total positivity*, Linear Algebra and its Applications 436(3) (2012), 537–560, DOI `10.1016/j.laa.2011.07.003`.

At the interface used by this task:

- GSTP is formulated by strict preservation of proper cones by all exterior powers / compound operators;
- Theorem 22 gives the forward spectral implication: GSTP with respect to a total-positive structure implies a positive, simple spectrum;
- Proposition 19 gives the converse existence statement used here: a matrix with positive simple spectrum is GSTP with respect to a suitable total-positive structure.

Consequently, at pure **existence** level,

\[
\boxed{
\text{there exists a Kushel GSTP cone structure for }T_m
\iff
T_m\text{ has positive simple spectrum}
}
\]

in the finite-dimensional setting of the task.

This matters logically.  The parent theorem asks only that the already-known eigenvalue `1` be simple.  Proving positive simplicity of the *whole* spectrum merely in order to invoke Proposition 19 is stronger than the target and does not provide an independent theorem engine.  Therefore a successful GSTP route must exhibit a cone family from AP data **without first knowing the desired spectral conclusion**.

This is the first exact boundary of the route:

`NONCONSTRUCTIVE_EXISTENTIAL_GSTP != REDUCTION_OF_PARENT_TARGET`.

---

## 3. Mandatory all-`m` negative control: the Cauchy endpoint kills generic cone arguments

The accepted oscillation result constructs the same broad architecture with constant measure `du` and the same order map `u -> u^m`, but obtains exactly

\[
T_m^{(0)}=I_m
\qquad(m\ge2).
\]

For any proper cone `K` in a space of dimension at least two, `K` has nonzero boundary points.  Since the identity fixes every boundary point,

\[
I_m(K\setminus\{0\})\not\subset \operatorname{int}K.
\]

Hence the identity is not strongly positive on **any** proper cone, already in exterior degree `j=1`.

Therefore no argument using only properties shared with that endpoint — common positive measure, the exact `u -> u^m` architecture, factorwise STP, or the previously frozen generic oscillation/sign-regularity package — can establish the required GSTP certificate.  A valid cone construction must use the nonconstant AP Christoffel factor essentially.

This is an all-`m` theorem, not finite evidence.

---

## 4. Exact AP-specific centering: the half-Pascal conjugacy

Define the one-parameter lower Pascal matrices

\[
P(t)_{ij}=\begin{cases}
\binom ij t^{i-j},&j\le i,\\
0,&j>i.
\end{cases}
\]

Binomial convolution gives

\[
P(s)P(t)=P(s+t).
\]

Let

\[
J=\operatorname{diag}(1,-1,1,-1,\ldots).
\]

Then

\[
J P(t)J=P(-t),
\qquad
R=P(1)J.
\]

Set the canonical midpoint

\[
S=P(1/2),
\qquad S^{-1}=P(-1/2).
\]

A direct calculation gives the all-`m` identity

\[
\boxed{S^{-1}RS=J.}
\]

Indeed,

\[
S^{-1}RS
=P(-1/2)P(1)JP(1/2)
=P(1/2)JP(1/2)
=J.
\]

Now define

\[
A_*=S^{-1}\widehat A S,
\qquad
B_*=S^{-1}\widehat B S,
\qquad
T_*=S^{-1}T_m S.
\]

Then

\[
\boxed{T_*=J B_*J A_*.}
\]

Introduce

\[
C_*:=J B_*^{-1}J.
\]

Because `J^2=I`,

\[
C_*^{-1}=J B_*J,
\]

and therefore the full AP problem has the exact pencil form

\[
\boxed{T_*=C_*^{-1}A_*.}
\]

Thus the fixed-point equation becomes

\[
A_*x=C_*x,
\qquad
(C_*-A_*)x=0.
\]

This centering is AP-task-specific algebra and does not assume the target spectrum.

---

## 5. Exact operator-specific obstruction: every midpoint-Pascal signed orthant fails at `m=2`

The most immediate explicit proper cones suggested by the centering are

\[
K_\sigma=S D_\sigma\,\mathbb R_+^m,
\]

where `D_sigma` ranges over diagonal sign matrices.  Strong positivity of `T_m` on such a cone would require

\[
D_\sigma T_*D_\sigma
\]

to map the nonzero standard orthant into its interior; in particular all entries must be strictly positive.

For the **actual AP operator at `m=2`**, exact rational calculation gives

\[
T_*
=
\begin{pmatrix}
59/56 & 3/28\\
-2187/6160 & 893/3080
\end{pmatrix}.
\]

Hence

\[
(T_*)_{01}(T_*)_{10}
=\frac{3}{28}\frac{-2187}{6160}<0.
\]

Diagonal sign conjugation multiplies the two off-diagonal entries by the same sign `sigma_0 sigma_1`, so their product is invariant.  Therefore one off-diagonal entry remains negative for **every** signed orthant choice:

\[
\boxed{
\forall D_\sigma,
\quad
D_\sigma T_*D_\sigma\not>0
\quad(m=2).
}
\]

Consequently no cone in the entire canonical family

\[
\boxed{K_\sigma=S D_\sigma\mathbb R_+^2}
\]

is even degree-one strongly invariant for the actual AP operator.  This is an exact, operator-specific obstruction, not a finite search over arbitrary cones.

The ordinary standard orthant is also impossible in the original coordinates because `T_m e_0=e_0` keeps the nonzero boundary ray `R_+e_0` on the boundary.

What this does **not** prove: it does not exclude nonlinear, non-simplicial, spectrally adapted, or otherwise exotic proper cones.

---

## 6. New finite exact discovery packet: a singular TP-boundary pencil

The exact checker evaluates the actual AP moments over `m=2,3,4,5,6` with rational arithmetic only.  In every tested dimension it finds:

1. `A_*` is strictly totally positive;
2. `B_*` is strictly totally positive;
3. `C_*=J B_*^{-1}J` is strictly totally positive;
4. for
   \[
   D_*:=C_*-A_*,
   \]
   every minor of order `1,...,m-1` is **strictly positive**;
5. `det(D_*)=0`.

Items 4–5 imply, in each checked dimension,

\[
\operatorname{rank}D_*=m-1.
\]

Equivalently, the generalized eigenvalue `1` of the pencil `(A_*,C_*)` is simple throughout the checked range.  This is consistent with the parent target, but it is **not** an all-`m` proof.

The important new pattern is stronger than merely observing finite simple spectra: `D_*` lies on a very rigid singular boundary of total positivity — every proper minor is strictly positive while the full determinant vanishes.

This suggests a successor theorem of the form:

`AP_CHRISTOFFEL_WEIGHT => ALL_PROPER_MINORS(C_*-A_*)>0 AND det(C_*-A_*)=0`

proved directly from the moment structure, or an exact counterexample to that pattern.  Such a theorem would be AP-specific and noncircular.  It is more promising than an unconstrained search for arbitrary Kushel cones.

Guard: the finite `m=2..6` pattern is regression evidence only.  The present task does not promote it to an all-`m` theorem.

---

## 7. What is proved, what is not

### Proved exactly

- the external logical boundary: existential GSTP is not an independent reduction because Kushel's converse reconstructs a GSTP structure from positive simple spectrum;
- the Cauchy identity endpoint cannot be strongly positive on any proper cone for `m>=2`;
- the all-`m` half-Pascal conjugacy `S^{-1}RS=J`;
- the exact transformed pencil identity `T_*=C_*^{-1}A_*`;
- on the actual AP operator at `m=2`, every signed midpoint-Pascal orthant cone `S D_sigma R_+^2` fails degree-one strong positivity;
- exact finite rational regression `m=2..6` for the transformed STP / singular-proper-minor pattern.

### Not proved

- `T_m` is not GSTP in some other proper-cone system;
- `T_m` has positive simple spectrum for all `m`;
- the `D_*` proper-minor pattern holds for all `m`;
- the parent theorem `det(I-Q_m) != 0` for all admissible `m`.

Accordingly:

`ACTUAL_AP_GSTP_NOT_REFUTED`  
`PARENT_PERFECT_PRIME_TARGET_REMAINS_OPEN`.

---

## 8. Toolbox coverage

The current Enterprise toolbox registry was checked before introducing any global mechanism.  No registered tool exactly covers the present GSTP / exterior-power proper-cone certificate problem.  This execution therefore uses a task-local exact-rational checker and does **not** promote the midpoint-Pascal centering or the singular TP-boundary pattern to a global tool.

Tool disposition: `NOT_APPLICABLE / NO_MATCHING_REGISTERED_TOOL`.

---

## 9. Exact verification

Checker:

`research_checks/PERFECT_PRIME_AP_GSTP_EXTERIOR_CONE_CERTIFICATE_CHECK_20260830.py`

It uses Python standard-library `Fraction` arithmetic and verifies:

- the finite midpoint identity `S^{-1}RS=J` as a regression of the all-`m` proof;
- exact construction of actual AP `H,Ahat,Bhat,T`;
- `T_*=C_*^{-1}A_*`;
- strict positivity of every minor of `A_*,B_*,C_*` for `m=2..6`;
- strict positivity of every proper minor of `D_*=C_*-A_*` and `det(D_*)=0` for `m=2..6`;
- the exact `m=2` opposite-sign off-diagonal obstruction.

The bounded run is evidence only; all claims labeled all-`m` above are proved algebraically in this return.

---

## 10. Recommended Driver action

Accept this task at the exact obstruction / negative-boundary terminal class.

Freeze the following nonproductive inference:

`FACTORWISE_STP + ABSTRACT_EXISTENCE_OF_SOME_CONES => PARENT_TARGET`.

Do **not** interpret this return as a proof that actual AP is non-GSTP.

If a successor is opened, prefer the AP-specific half-Pascal pencil frontier:

1. derive closed integral / determinant formulae for minors of `A_*`, `C_*`, and especially `C_*-A_*`;
2. prove or refute all-`m` strict positivity of every proper minor of `C_*-A_*`;
3. if the pattern survives, connect it to the exact one-dimensional kernel forced by `T_m e_0=e_0` without assuming spectral simplicity;
4. alternatively use the already-published Christoffel deformation lane, which attacks the same indispensable AP weight by an independent transversality route.

Do not reopen generic common-measure positivity, unconstrained existential-cone search, or finite-spectrum-as-proof.

## External source boundary

- O. Y. Kushel, *Cone-theoretic generalization of total positivity*, Linear Algebra Appl. 436(3) (2012), 537–560, DOI `10.1016/j.laa.2011.07.003`.
- Internal mandatory negative control: `RR-33B5E1F81BCD9EEF1BD1`.
- Internal actionable prior-art map: `RR-4B168EE0BCE14D5C058A`.

No novelty, Working Truth, Foundation, or canonical-promotion authority is asserted by this return.
