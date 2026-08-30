# Perfect Prime AP Christoffel J-transversality deformation — Research Return

Task: `RS-PERFECT-PRIME-AP-CHRISTOFFEL-J-TRANSVERSALITY-DEFORMATION`  
Publication: `TP2-7A1C9E54B2306D8F41AA`  
Researcher-ID: `EM-PPTAPCHR1-7C8D5B`  
Claim: `chatgpt-pptapchr1-20260830-1609-7c8d5b`  
Execution record: `ER-0A657A17DB33F4511E63`

## Terminal verdict

`SUCCESS / FIRST_ORDER_GLOBAL_NO_RECROSSING_ROUTE_EXACTLY_OBSTRUCTED`

Hard-target disposition:

`AP_CHRISTOFFEL_J_TRANSVERSALITY_NO_ZERO_FLOW_PROVED_OR_EXACTLY_OBSTRUCTED` is satisfied at the **exact-obstruction** branch, not at the parent-theorem branch.

This execution does **not** prove or disprove the actual all-`m` AP theorem

\[
\det(I_{m-1}-Q_m)\ne0.
\]

It freezes three exact facts that materially narrow the surviving proof route:

1. the full Christoffel flow is exactly self-adjoint in a signed diagonal metric, so there is a canonical symmetric crossing form at the Cauchy endpoint;
2. that crossing form is already indefinite at `m=3`, ruling out the naive positive/negative-definite crossing-form inertia route;
3. the most natural scalar continuation of the first nonzero quotient determinant coefficient is **not monotone even on the genuine positive Christoffel path at `m=2`**, and the first-order tangent Christoffel path has an exact secondary fixed-space recrossing at `m=4`, `t=49/51`.

Therefore the local first-order splitting data at `t=0` cannot by itself be promoted to a global no-recrossing theorem. The nonlinear higher-order terms of

\[
(1-tu^{m^2})^{m-1}
\]

are load-bearing for any successful global proof.

## 1. Exact deformation and preserved parent equivalence

Put `n=m-1`, `M=m^2`,

\[
w_i=(-1)^i\binom ni,\qquad W=\operatorname{diag}(w_i),
\]

and use the scalar-free moments

\[
H_{ij}(t)
=\int_0^1 u^{i+mj}(1-tu^M)^n\,du
=\sum_{r=0}^{n}(-1)^r\binom nr
\frac{t^r}{i+mj+1+rM}.
\]

The omitted AP scalar is positive and cancels from the normalized half maps. Define

\[
e_i(t)=\sum_j H_{ij}(t)w_j,\qquad
 d_j(t)=\sum_i H_{ij}(t)w_i,
\]

\[
E_t=\operatorname{diag}(e_i(t)),\qquad
D_t=\operatorname{diag}(d_j(t)),
\]

\[
A_t=E_t^{-1}H_tW,\qquad
B_t=D_t^{-1}H_t^TW,\qquad
K_t=B_tA_t.
\]

Let

\[
R_{ij}=(-1)^j\binom ij\quad(j\le i),\qquad R^2=I,
\]

and

\[
\mathcal T_t=RK_tR.
\]

Since `A_t 1=B_t 1=1`, `K_t 1=1`, hence `\mathcal T_t e_0=e_0`. In the frozen splitting

\[
\mathbb R^m=\langle e_0\rangle\oplus\mathbb R^{m-1},
\qquad
\mathcal T_t=
\begin{pmatrix}
1&*\\
0&Q_m(t)
\end{pmatrix}.
\]

Thus the actual AP target is still exactly

\[
D_m(1):=\det(I_{m-1}-Q_m(1))\ne0,
\]

and the flow target would be `D_m(t) != 0` for every `0<t<=1`.

At `t=0`, the accepted Cauchy endpoint gives

\[
K_0=I_m,\qquad Q_m(0)=I_{m-1},\qquad D_m(0)=0.
\]

For every `0<=t<=1`, the weight is nonnegative and positive almost everywhere, and

\[
e_i(t)=\int_0^1 u^i(1-u^m)^n(1-tu^M)^n\,du>0,
\]

\[
d_j(t)=\int_0^1 u^{mj}(1-u)^n(1-tu^M)^n\,du>0.
\]

So no normalizer pole occurs on the genuine path.

## 2. All-m theorem: exact signed self-adjointness

Define the signed metric

\[
G_t:=D_tW=\operatorname{diag}(d_j(t)w_j).
\]

Because `D_t`, `E_t`, and `W` are diagonal,

\[
\begin{aligned}
G_tK_t
&=D_tW D_t^{-1}H_t^TW E_t^{-1}H_tW\\
&=W H_t^T W E_t^{-1}H_tW.
\end{aligned}
\]

Taking transpose and commuting `W` with `E_t^{-1}` gives the same matrix. Hence

\[
\boxed{K_t^TG_t=G_tK_t}
\]

for every admissible `m` and every `t` for which the normalizers are nonzero; in particular for the full genuine path `0<=t<=1`.

Since every `d_j(t)>0`, the signature of `G_t` is exactly the alternating signature of `W`. This is an exact Krein/J-self-adjoint structure, not an ordinary Hilbert-space self-adjointness statement.

At `t=0`, `K_0=I`. Differentiating the symmetric matrix `G_tK_t` gives

\[
G'_0+G_0K'_0
\]

symmetric. As `G'_0` is diagonal, the crossing matrix

\[
\boxed{\mathcal C_m:=-G_0K'_0}
\]

is symmetric. Also `K'_0\mathbf1=0`, so the known fixed direction lies in its kernel and the form descends to the quotient.

This supplies the exact crossing form requested by the taskbook.

## 3. Exact obstruction 1: the crossing form is not definite

For `m=3`, exact differentiation of the moment/normalizer formulas gives

\[
K'_0=
\begin{pmatrix}
\frac{141}{15470}&\frac{519}{30940}&-\frac{801}{30940}\\
-\frac{519}{3094}&\frac{53637}{68068}&-\frac{42219}{68068}\\
-\frac{2403}{1105}&\frac{126657}{24310}&-\frac{73791}{24310}
\end{pmatrix}.
\]

At the Cauchy endpoint,

\[
G_0=\operatorname{diag}\left(\frac13,-\frac1{30},\frac1{252}\right).
\]

Therefore the symmetric crossing form `\mathcal C_3=-G_0K'_0` has diagonal entries

\[
(\mathcal C_3)_{00}=-\frac{47}{15470}<0,
\qquad
(\mathcal C_3)_{11}=\frac{17879}{680680}>0.
\]

Hence

\[
\boxed{\mathcal C_3\ \text{is indefinite}.}
\]

Because the fixed direction is in the kernel, this sign conflict survives on the nontrivial quotient. Consequently a proof of global no-recrossing based on a uniformly positive- or negative-definite ordinary crossing form is impossible already at `m=3`.

This does **not** say that the quotient fails to split locally; it says only that ordinary definiteness/inertia is the wrong invariant.

## 4. Exact obstruction 2 on the genuine path: normalized determinant is not monotone

For `m=2`, `n=1`, so the full Christoffel deformation itself is exactly linear:

\[
\rho_{2,t}(u)=1-tu^4.
\]

Direct exact elimination of the `2x2` normalized route gives

\[
\boxed{
D_2(t)
=
\frac{6t(5t-13)(13t-350)}
{(t-15)(t-6)(3t-35)(3t-14)}.
}
\]

For `0<t<=1`, both numerator factors besides `t` are negative and all four denominator factors are negative, so

\[
D_2(t)>0.
\]

Thus the genuine `m=2` Christoffel path has immediate splitting and no recrossing.

The natural normalization by the exact Cauchy vanishing order is

\[
F_2(t):=\frac{D_2(t)}t
=
\frac{6(5t-13)(13t-350)}
{(t-15)(t-6)(3t-35)(3t-14)}.
\]

Its exact endpoint data are

\[
F_2(0)=\frac{13}{21},\qquad
F_2(1)=\frac{1011}{1540},
\]

and, crucially,

\[
\boxed{F_2'(0)=\frac{1523}{22050}>0,}
\]

while

\[
\boxed{F_2'(1)=-\frac{319731}{18972800}<0.}
\]

Therefore `F_2` is not monotone on `[0,1]`.

This is an exact obstruction **inside the actual positive deformation**, not a comparison-model artifact. It kills the most direct strategy “divide by the first nonzero `t`-order and prove the normalized scalar has one monotone sign flow”.

For completeness, the unnormalized determinant itself has

\[
D_2'(t)=
-\frac{6(t^2-70)(3t^2-121t+210)(195t^2-3649t+13650)}
{(t-15)^2(t-6)^2(3t-35)^2(3t-14)^2},
\]

which is positive on `[0,1]`. So the obstruction is specifically to the normalized-coefficient monotonicity route, not to `m=2` no-recrossing.

## 5. All-m tangent structure: only one possible secondary root

The first-order Taylor deformation at `t=0` is

\[
\rho^{\mathrm{lin}}_{m,t}(u)=1-nt u^M,
\]

with moment kernel

\[
h^{\mathrm{lin}}_t(q)
=\frac1{q+1}-\frac{nt}{q+1+M}.
\]

Let `C_t=W H_t^{lin} W` and let `L_t` be its signed complete-bipartite Laplacian. Write `\tau_m^{lin}(t)` for any spanning-tree cofactor.

First note a shifted Cauchy identity. For every `a>0`,

\[
H^{(a)}_{ij}=\frac1{a+i+mj}
\]

with the same binomial `w` has normalized composite `K^{(a)}=I_m`. The accepted Cauchy Lagrange proof carries over verbatim after replacing `x_i=i+1` by `x_i=a+i`: the formulas

\[
e_i^{(a)}=\frac{n!m^n}{\prod_{r=0}^n(a+i+mr)},
\qquad
 d_j^{(a)}=\frac{n!}{\prod_{r=0}^n(a+mj+r)}
\]

and the same leading-coefficient interpolation identity make all off-diagonal entries of the normalized composite vanish, while row sums force the diagonal to be `1`.

Consequently the full signed Laplacian of either pure Cauchy endpoint has nullity exactly `m`. If one deletes a right-side vertex, the `(2m-1)x(2m-1)` cofactor matrix has nullity exactly `m-1` because its left diagonal block is invertible.

Now `L_t=L_0+tL_1`. Therefore its cofactor determinant is divisible by `t^{m-1}`. Applying the same argument to the leading matrix `L_1` after reversing the polynomial bounds the total degree by

\[
(2m-1)-(m-1)=m.
\]

Hence for every `m>=2`,

\[
\boxed{
\tau_m^{\mathrm{lin}}(t)=t^{m-1}(\alpha_m+\beta_m t).
}
\]

Thus the entire first-order tangent model has at most one nonzero recrossing parameter. The question is whether that one root lies in the physical interval.

## 6. Exact obstruction 3: tangent recrossing at m=4

The deterministic exact checker evaluates the preceding polynomial without floating point and gives

\[
\tau_2^{\mathrm{lin}}(t)
=-\frac{t(5t-13)}{1260},
\]

\[
\tau_3^{\mathrm{lin}}(t)
=-\frac{243t^2(5t-7)}{476476000},
\]

and

\[
\boxed{
\tau_4^{\mathrm{lin}}(t)
=-\frac{3145728\,t^3(51t-49)}
{25617946563506171875}.
}
\]

Therefore the `m=4` first-order tangent model has the exact secondary zero

\[
\boxed{t_*=\frac{49}{51}\in(0,1).}
\]

This zero is not caused by a normalizer pole. At `t=49/51`, the exact left normalizers are

\[
\left(
\frac{5328896}{8171475},
\frac{172288}{765765},
\frac{86020096}{797986035},
\frac{163}{2720}
\right),
\]

and the right normalizers are

\[
\left(
\frac{20579}{82365},
\frac{6329}{1806420},
\frac{257}{546975},
\frac{26107}{222520480}
\right),
\]

all nonzero. Exact Gaussian elimination gives

\[
\operatorname{rank} L_{4,t_*}^{\mathrm{lin}}=6,
\]

so its nullity is exactly `2`: the universal gauge direction plus exactly one extra fixed direction.

Hence the first-order Taylor path genuinely recrosses.

The tangent weight is not positive on all of `[0,1]` for `m=4`, so this is **not** a counterexample to the actual Christoffel flow. Its force is different and precise:

> Any attempted global proof that uses only the first derivative/crossing data of the Christoffel factor at `t=0` cannot establish no-recrossing. The nonlinear `t^2,...,t^{m-1}` terms of the genuine factor are necessary to distinguish the true flow from an exact tangent flow that recrosses.

## 7. What is proved, what is killed, and what remains

### Proved exactly

1. `K_t` is self-adjoint for the signed metric `G_t=D_tW` on the full genuine deformation.
2. The endpoint crossing form `-G_0K'_0` is symmetric.
3. The `m=3` crossing form is indefinite.
4. The actual `m=2` quotient determinant has the displayed closed formula and is nonzero for every `0<t<=1`.
5. The normalized actual `m=2` determinant `D_2(t)/t` is nonmonotone.
6. Every tangent-model tree cofactor has the all-m shape `t^{m-1}(alpha_m+beta_m t)`.
7. The tangent `m=4` model has an exact non-pole secondary fixed-space recrossing at `49/51`.

### Routes now closed

- positive- or negative-definite ordinary crossing form / ordinary inertia flow;
- “first nonzero coefficient divided by `t^{m-1}` is monotone” as a general Christoffel no-zero theorem;
- extrapolating the `t=0` first derivative or tangent deformation to global no-recrossing;
- any proof whose decisive step is unchanged after discarding the nonlinear Christoffel terms.

### Parent theorem still open

No exact zero of the **genuine** full Christoffel flow was found. No all-m no-zero theorem was proved. Therefore

\[
\boxed{\det(I_{m-1}-Q_m(1))\ne0}
\]

remains open for general `m`.

The smallest surviving residue is now sharper:

> Find an exact invariant that sees the nonlinear higher Christoffel coefficients and prevents the tangent-model recrossing mechanism from surviving in the full positive flow. Equivalently, compare the genuine compound/tree cofactor to its tangent polynomial by an exact higher-order sign, interlacing, or Krein-collision exclusion theorem.

A continuation that merely recomputes the first crossing form, proves local splitting for finitely many `m`, or assumes monotonicity of the normalized determinant would repeat a route closed here.

## 8. Deterministic exact checker

The exact checker is

`research_checks/PERFECT_PRIME_AP_CHRISTOFFEL_J_TRANSVERSALITY_DEFORMATION_CHECK_20260830.py`.

It uses only Python standard-library rational arithmetic. It verifies:

- the exact genuine `m=2` determinant formula by rational-function polynomial identity;
- the exact endpoint values and opposite derivative signs of `D_2(t)/t`;
- signed-metric self-adjointness for exact regression points `m=2..5`, `t in {0,1/3,1}`;
- crossing-form symmetry through `m=6` and the exact `m=3` indefinite diagonal certificate;
- exact tangent tree-cofactor polynomial factorizations at `m=2,3,4` by polynomial determinant expansion;
- at `m=4,t=49/51`, nonzero normalizers and exact Laplacian rank `6`.

The bounded-`m` checks are regression/certificates for the finite claims. The all-m signed-self-adjointness and tangent-degree statements are proved algebraically in this return.

Expected terminal line:

`AP_CHRISTOFFEL_J_TRANSVERSALITY_DEFORMATION_EXACT_CHECK_PASS`.

## 9. Previously closed shortcuts respected

This execution does not use finite-`m` evidence as an all-m theorem; does not reopen generic STP, generic common-measure oscillation, entrywise Perron, ordinary norm contraction, normalized complete monotonicity, raw SSR/TN, or the falsified sign-regular core shortcut. The AP Christoffel deformation enters essentially in the genuine `m=2` nonmonotonicity certificate and in the exact comparison between the full nonlinear factor and its first-order tangent.

No Working Truth, Foundation, L4, novelty, or canonical theorem promotion is claimed.

## 10. Recommended Driver disposition

Accept the task at terminal class

`FIRST_ORDER_GLOBAL_NO_RECROSSING_ROUTE_EXACTLY_OBSTRUCTED`.

Freeze the following as reusable exact boundaries:

- `SIGNED_METRIC_SELF_ADJOINTNESS` is valid;
- `ORDINARY_DEFINITE_CROSSING_FORM` is false;
- `NORMALIZED_DETERMINANT_MONOTONICITY` is false already on the genuine `m=2` path;
- `FIRST_ORDER_TANGENT_NO_RECROSSING` is false exactly at `m=4,t=49/51`;
- `NONLINEAR_HIGHER_CHRISTOFFEL_TERMS_REQUIRED` is the new route condition.

If a successor is published, it should target the nonlinear residue directly rather than restarting the local crossing calculation.
