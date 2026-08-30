# Perfect Prime Beta–Bernstein Principal-Angle / Exterior-Power Closure — Research Return

Researcher-ID: `EM-PPTBBPA-6E863B`  
Task: `RS-PERFECT-PRIME-BETA-BERNSTEIN-PRINCIPAL-ANGLE-EXTERIOR-POWER`  
Publication: `TP2-10717029BFD72A8E1F76`  
Claim: `chatgpt-pptbbpa-20260830-1057-6e863b`  
Execution record: `ER-4E41ADAD5023F187ED93`

## 1. Terminal verdict

`SUCCESS / STRICT_TRANSVERSALITY_REDUCTION_PROVED`

The parent all-`m` theorem is **not** proved here. The exact frozen target

\[
\det(I_{m-1}-Q_m)\ne 0
\]

remains open for arbitrary `m`.

This execution does, however, strictly narrow the geometric route in three ways:

1. it constructs the exact positive cross-Gram matrix hidden behind the two Beta–Bernstein half maps and proves that the frozen operator is not its ordinary Hilbert Gram square but the **signature-twisted Krein square**
   \[
   Q^{1/2}KQ^{-1/2}=Z^T JZJ;
   \]
2. it gives an exact counterexample, using the **actual AP measure already at `m=2`**, to the naive identification of the nontrivial spectrum of `K` with ordinary principal-angle/canonical-correlation squares between the two Bernstein subspaces;
3. it proves an all-`m` adversarial theorem for the unweighted Cauchy model: keeping the same two subspaces, the same order map `u -> u^m`, the same Möbius weights, the same common positive-measure construction, and the same STP/Bernstein mechanism, but removing only the AP polynomial weight, one gets
   \[
   \boxed{K^{(0)}_m=I_m\quad\text{for every }m\ge2.}
   \]
   Hence common measure + STP + ordinary subspace transversality + `u -> u^m` do not contain the missing theorem. The specific factor
   \[
   \rho_m(u)=(1-u^{m^2})^{m-1}
   \]
   is the indispensable transversality carrier.

The surviving load-bearing lemma is therefore no longer “find some principal-angle argument.” It is the explicit **AP Christoffel `J`-transversality lemma**: the polynomial modification `rho_m` must break the Cauchy model's full `J`-isometry down to the one known positive-type direction.

No Working Truth, Foundation status, novelty, or canonical promotion is claimed.

---

## 2. Frozen input and notation

Set

\[
n=m-1,\qquad
h_m(q)=\frac1{\prod_{\ell=0}^{n}(1+q+\ell m^2)},
\]
\[
H_{ij}=h_m(i+mj),\qquad 0\le i,j\le n,
\]
\[
w_i=(-1)^i\binom ni,
\qquad
W=\operatorname{diag}(w_i).
\]

The accepted parent result defines

\[
e_i=\sum_jH_{ij}w_j>0,
\qquad
d_j=\sum_iw_iH_{ij}>0,
\]
\[
E=\operatorname{diag}(e_i),
\qquad D=\operatorname{diag}(d_j),
\]
\[
A=E^{-1}HW,
\qquad
B=D^{-1}H^TW,
\qquad
K=BA.
\]

The stochastic-type normalizations are exact:

\[
A\mathbf1=B\mathbf1=\mathbf1,
\qquad K\mathbf1=\mathbf1.
\]

Let the binomial Möbius involution be

\[
R_{jk}=(-1)^k\binom jk\quad(k\le j),
\qquad R^2=I.
\]

Then the accepted quotient operator is

\[
\mathcal T_m=RKR=\begin{pmatrix}1&*\\0&Q_m\end{pmatrix}.
\]

The task is to exploit the common positive measure

\[
d\mu_m(u)=\kappa_m(1-u^{m^2})^n\,du,
\qquad
\kappa_m=\frac1{n!m^{2n}},
\]

for which

\[
H_{ij}=\int_0^1u^{i+mj}\,d\mu_m(u).
\]

---

## 3. Theorem A — exact Hilbert adjointization exists only after stripping the Möbius signature

Write

\[
\lambda_i=\binom ni>0,
\qquad
\Lambda=\operatorname{diag}(\lambda_i),
\qquad
J=\operatorname{diag}((-1)^i),
\]

so that

\[
W=J\Lambda=\Lambda J.
\]

Define the positive diagonal metrics

\[
P=E\Lambda,
\qquad
Q=D\Lambda,
\]

and strip the alternating signature from the two half maps:

\[
X:=AJ=E^{-1}H\Lambda,
\qquad
Y:=BJ=D^{-1}H^T\Lambda.
\]

Then

\[
QY
=D\Lambda D^{-1}H^T\Lambda
=\Lambda H^T\Lambda,
\]

while

\[
X^TP
=\Lambda H^TE^{-1}E\Lambda
=\Lambda H^T\Lambda.
\]

Therefore

\[
\boxed{QY=X^TP.}
\]

So `X` and `Y` really are adjoints for **positive** diagonal Hilbert metrics.

Now put

\[
Z=P^{1/2}XQ^{-1/2}.
\]

Its entries are explicitly

\[
\boxed{
Z_{ij}=H_{ij}
\sqrt{\frac{\lambda_i\lambda_j}{e_i d_j}}
}.
\]

Thus `Z` is obtained from `H` by positive row and column scaling. Since the accepted parent theorem proves `H` STP, `Z` is STP as well.

Moreover, if

\[
\phi_i(u)=\sqrt{\frac{\lambda_i}{e_i}}u^i,
\qquad
\psi_j(u)=\sqrt{\frac{\lambda_j}{d_j}}u^{mj},
\]

then

\[
Z_{ij}=\langle\phi_i,\psi_j\rangle_{L^2(\mu_m)}.
\]

So `Z` is a genuine positive common-Hilbert-space **cross-Gram matrix**.

### The crucial obstruction

The frozen operator is not `YX`. It is

\[
K=BA=(YJ)(XJ)=YJXJ.
\]

Consequently

\[
\boxed{
Q^{1/2}KQ^{-1/2}=Z^TJZJ.
}
\]

The ordinary positive Gram square would be `Z^T Z`. The project operator has two interposed signature matrices `J`.

This pinpoints the exact geometric obstruction: **the common Beta measure does give Hilbert adjointness, but Möbius orientation converts the fixed-point problem into indefinite/Krein geometry before the two halves are composed.**

A second exact form avoids square roots entirely. Since

\[
DWK=A^TEWA,
\]

the matrix `DWK` is symmetric, and hence

\[
\boxed{K^T(DW)=(DW)K.}
\]

Thus `K` is self-adjoint for the nondegenerate signed form `DW=JQ`, whose inertia is the alternating signature of `J`.

This identity is all-`m`; it is not a finite regression.

---

## 4. Distinguished positive-type fixed direction

Let

\[
u=P^{1/2}\mathbf1,
\qquad
v=Q^{1/2}\mathbf1.
\]

Using `A 1 = B 1 = 1` and `A=XJ`, `B=YJ` gives

\[
ZJv=u,
\qquad
Z^TJu=v.
\]

Therefore

\[
Z^TJZJv=v.
\]

So `v` is the exact `J`-singular/fixed direction corresponding to the distinguished eigenvalue `1`.

Its signed norm is not isotropic:

\[
\begin{aligned}
v^TJv
&=\mathbf1^TQJ\mathbf1\\
&=\sum_jd_jw_j\\
&=w^THw\\
&=\int_0^1
(1-u)^n(1-u^m)^n\,d\mu_m(u)\\
&>0.
\end{aligned}
\]

Hence the known fixed direction is of **positive type** in the Krein metric.

Define the symmetric `J`-Gram defect

\[
\Delta_m:=J-Z^TJZ.
\]

For any vector `y`,

\[
Z^TJZJy=y
\iff
\Delta_m(Jy)=0.
\]

Therefore the parent target is equivalent to

\[
\ker\Delta_m=\operatorname{span}\{Jv\}.
\]

This is the exact exterior-power/transversality object generated by the common measure. In particular,

\[
\bigwedge^{m-1}\Delta_m\ne0
\]

is the natural compound-matrix witness once the known kernel direction is removed.

What makes the reduction useful rather than merely notational is the exact control model in Sections 6–7: the same construction without the AP weight has `Delta_m=0` identically. Thus `Delta_m` measures precisely the transversality created by the AP polynomial modification.

---

## 5. Exact actual-weight counterexample to the naive ordinary-principal-angle identification

Let

\[
V_m=\operatorname{span}\{1,u,\dots,u^n\},
\qquad
W_m=\operatorname{span}\{1,u^m,\dots,u^{mn}\}
\]

inside the **actual** Hilbert space `L^2(mu_m)`.

Their Gram matrices are

\[
(G_V)_{ij}=h_m(i+j),
\qquad
(G_W)_{ij}=h_m(m(i+j)),
\]

and the cross Gram is `H`. The standard squared-principal-angle / canonical-correlation operator on `W_m` is

\[
C_m=G_W^{-1}H^TG_V^{-1}H.
\]

Since the two spaces share constants, `C_m` has a unit eigenvalue.

At `m=2`, exact rational arithmetic gives

\[
\operatorname{spec}(K_2)
=\left\{1,\frac{529}{1540}\right\},
\]

while

\[
\operatorname{spec}(C_2)
=\left\{1,\frac{18515}{19968}\right\}.
\]

The two nontrivial eigenvalues are unequal. Equivalently,

\[
1-\frac{529}{1540}=\frac{1011}{1540},
\]

whereas the ordinary principal-angle factor is

\[
1-\frac{18515}{19968}=\frac{1453}{19968}.
\]

Thus even with the **exact accepted AP measure**, ordinary principal angles between the two Bernstein/monomial subspaces do not directly encode `Q_m` or its determinant.

This is an exact adversarial certificate against the simplest proposed geometric closure. It does not prove that Hilbert-space ideas are useless; it proves that any successful use must incorporate the Möbius signature/oblique normalization rather than identify `K` with a product of orthogonal projections.

---

## 6. Theorem B — all-`m` unweighted Cauchy model has perfect duality `K=I`

This is the decisive control model.

Keep all of the following unchanged:

- `m`, `n=m-1`;
- the two exponent sets `{0,1,...,n}` and `{0,m,...,mn}`;
- the order map `u -> u^m`;
- the Möbius weights `w_i=(-1)^i binom(n,i)`;
- the definitions of `e,d,A,B,K`;
- a common positive one-dimensional measure;
- the same binomial/Bernstein transform mechanism.

Change only the AP weight by taking the common measure `d mu_0(u)=du`. Then

\[
H^{(0)}_{ij}=\int_0^1u^{i+mj}\,du
=\frac1{1+i+mj}.
\]

Set

\[
x_i=1+i,
\qquad y_j=mj.
\]

Then

\[
H^{(0)}_{ij}=\frac1{x_i+y_j}
\]

is a classical Cauchy matrix.

### 6.1 Exact normalizers

The elementary finite-difference identity

\[
\sum_{j=0}^n
\frac{(-1)^j\binom nj}{a+mj}
=
\frac{n!m^n}{\prod_{r=0}^n(a+mr)}
\]

gives

\[
e_i^{(0)}
=\frac{n!m^n}{\prod_{r=0}^n(x_i+mr)}.
\]

Similarly,

\[
d_j^{(0)}
=\frac{n!}{\prod_{r=0}^n(y_j+1+r)}.
\]

Both are strictly positive.

### 6.2 `A` is an exact Lagrange evaluation map

Let `L_j(t)` be the Lagrange basis for the nodes

\[
y_0,y_1,\dots,y_n.
\]

Using

\[
\prod_{r\ne j}(y_j-y_r)
=m^n(-1)^{n-j}j!(n-j)!,
\]

one obtains

\[
A^{(0)}_{ij}
=\frac{w_j/(x_i+y_j)}{e_i^{(0)}}
=L_j(-x_i).
\]

Therefore `A^(0)` takes the values of a polynomial `p` of degree at most `n` on the `y`-grid and returns its values on the grid

\[
-x_0,-x_1,\dots,-x_n.
\]

### 6.3 `B` is the inverse evaluation map

Let `N_i(t)` be the Lagrange basis for the nodes

\[
-x_0,-x_1,\dots,-x_n.
\]

Since

\[
\prod_{r\ne i}((-x_i)-(-x_r))
=\prod_{r\ne i}(x_r-x_i)
=(-1)^i i!(n-i)!,
\]

we get

\[
B^{(0)}_{ji}
=\frac{w_i/(x_i+y_j)}{d_j^{(0)}}
=N_i(y_j).
\]

Thus `B^(0)` reconstructs the same degree-`n` polynomial from its values at `-x_i` and evaluates it back at `y_j`.

Consequently

\[
\boxed{B^{(0)}A^{(0)}=I_m}
\]

for every `m>=2`.

Hence

\[
\boxed{K^{(0)}_m=I_m\quad(m\ge2).}
\]

This is an analytic all-`m` theorem. The checker only replays it for finite `m` as regression.

### 6.4 Why this model is a serious adversarial control

The two function spaces still satisfy

\[
V_m\cap W_m=\operatorname{span}\{1\},
\]

because every nonzero exponent in `V_m` lies in `{1,...,m-1}`, whereas every nonzero exponent in `W_m` is at least `m`.

So the geometric intersection is still exactly one-dimensional, yet `K^(0)=I` has an `m`-dimensional fixed space.

The same Andreief/generalized-Vandermonde argument used in the parent return also applies to the unweighted positive measure; after Möbius/Bernstein conversion the two positive half matrices remain STP. Therefore the following package is still insufficient:

`COMMON_POSITIVE_MEASURE + TWO_BERNSTEIN_FLAGS + u->u^m + STP + ONE_DIMENSIONAL_SUBSPACE_INTERSECTION`.

The missing information is not “more generic total positivity” and not “ordinary principal angles.”

---

## 7. Theorem C — the AP matrix is an exact polynomial/Christoffel deformation of the Cauchy control

The only ingredient removed in the Cauchy control is

\[
\rho_m(u)=(1-u^{m^2})^n.
\]

Expand it:

\[
\rho_m(u)
=\sum_{\ell=0}^n(-1)^\ell\binom n\ell u^{m^2\ell}.
\]

For any integer `q>=0`,

\[
\begin{aligned}
\int_0^1u^q\rho_m(u)\,du
&=\sum_{\ell=0}^n
\frac{(-1)^\ell\binom n\ell}{q+1+m^2\ell}\\
&=\frac{n!(m^2)^n}
{\prod_{\ell=0}^n(q+1+m^2\ell)}.
\end{aligned}
\]

Since

\[
\kappa_m=\frac1{n!m^{2n}},
\]

this becomes exactly

\[
\kappa_m\int_0^1u^q\rho_m(u)\,du
=h_m(q).
\]

Thus the actual AP moment matrix is the normalized polynomial modification of the one-pole Cauchy moment kernel:

\[
H_{ij}
=\kappa_m\sum_{\ell=0}^n
(-1)^\ell\binom n\ell
\frac1{1+i+mj+m^2\ell}.
\]

Equivalently, the AP kernel is an exact `n`-th finite difference, in a shift of size `m^2`, of the Cauchy kernel.

This isolates the only feature that distinguishes the fully degenerate exact model `K^(0)=I` from the actual frozen problem.

---

## 8. Strict surviving all-`m` lemma — AP Christoffel `J`-transversality

Let `Z_m` be the actual normalized cross-Gram matrix in Theorem A and

\[
\Delta_m=J-Z_m^TJZ_m.
\]

The Cauchy control satisfies

\[
K_m^{(0)}=I
\quad\Longrightarrow\quad
(Z_m^{(0)})^TJZ_m^{(0)}=J
\quad\Longrightarrow\quad
\Delta_m^{(0)}=0.
\]

For the AP weight, the already-known fixed vector gives

\[
\Delta_m(Jv_m)=0.
\]

The original quotient theorem will follow if one proves the **strict rank creation**

\[
\boxed{
\operatorname{rank}\Delta_m=m-1
}
\]

or, equivalently, the exterior-power transversality statement

\[
\boxed{
\bigwedge^{m-1}\Delta_m\ne0.
}
\]

with the known kernel

\[
\ker\Delta_m=\operatorname{span}\{Jv_m\}.
\]

The gain over the previous frontier is conceptual and falsifiable:

- the zero-deformation endpoint is now exactly solved (`Delta=0`, all directions fixed);
- the common-measure/STP/principal-angle data that survive at that endpoint are proved insufficient;
- the only allowed source of rank is the explicit polynomial modification `rho_m`;
- the correct geometry is an indefinite `J`-Gram defect, not an ordinary positive Gram/projection product;
- the remaining proof must therefore quantify how this **specific** finite-difference/Christoffel deformation creates `m-1` transverse directions.

Any future argument that does not use `rho_m` beyond positivity can be rejected immediately by the all-`m` Cauchy control.

This is the terminal `STRICT_TRANSVERSALITY_REDUCTION_PROVED` delivered by this task.

---

## 9. Exact regression certificate

Checker:

`research_checks/PERFECT_PRIME_BETA_BERNSTEIN_PRINCIPAL_ANGLE_EXTERIOR_POWER_CHECK_20260830.py`

Certificate:

`research_artifacts/PERFECT_PRIME_BETA_BERNSTEIN_PRINCIPAL_ANGLE_EXTERIOR_POWER/exact_regression_certificate.json`

Executed with exact `fractions.Fraction` arithmetic:

`--max-m 6 --baseline-max-m 8`

Result: `PASS`.

The checker verifies:

1. the AP finite-difference moment identity on every matrix entry for `2<=m<=6`;
2. `QY=X^T P`, `K=Y J X J`, and `DWK=A^T EWA` exactly for `2<=m<=6`;
3. the known fixed vector and positive signed norm;
4. finite regression `rank(I-K)=m-1` and `det(I-Q_m)!=0` for `2<=m<=6`;
5. the actual-measure principal-angle mismatch at `m=2`:
   - `K` nontrivial eigenvalue `529/1540`;
   - ordinary squared principal angle `18515/19968`;
6. the exact Cauchy normalizer formulas, both Lagrange-evaluation identities, and `B^(0)A^(0)=I` for every tested `2<=m<=8`.

The bounded checks are **not** used as the all-`m` proof. The all-`m` claims are the symbolic derivations in Sections 3, 6, and 7.

---

## 10. Prior-art / duplication firewall

The Cauchy kernel, Cauchy matrices, barycentric/Lagrange interpolation, and total-positive Cauchy biorthogonal systems are classical. In particular, Bertola–Gekhtman–Szmigielski, *Cauchy biorthogonal polynomials*, Journal of Approximation Theory 162 (2010), 832–867, DOI `10.1016/j.jat.2009.09.008`, develops biorthogonal polynomials for totally positive kernels and specializes to the Cauchy kernel.

Accordingly:

- no novelty is claimed for Cauchy total positivity, Cauchy inversion, Lagrange evaluation, biorthogonality, Christoffel–Darboux theory, or Krein-space terminology;
- the task-local contribution is the exact placement of the frozen AP operator relative to those standard structures, plus the all-`m` Cauchy adversarial control and the resulting isolation of the AP polynomial weight as the only surviving transversality source;
- the separately published prior-art lane remains the authority for any stronger duplication/novelty disposition concerning the full Perfect Prime route.

---

## 11. Tool/method reuse resolution

### Existing common-measure / total-positivity machinery

`REUSE_APPLIED`.

The accepted Beta representation and STP theorem were consumed as frozen inputs; they were not reproved as a new project theorem.

### Exterior-power / Gram interface

`TASK_LOCAL_DERIVATION`.

The reusable mathematical primitive is standard: positive cross-Gram matrices, signature adjoints, and compound rank. No new global software/tool family is justified.

### Current method inventory

No existing Enterprise Math tool already encodes this Beta–Bernstein `J`-Gram/Christoffel transversality interface. The present output is therefore classified `RESULT_ONLY`, not `GLOBAL_TOOL_FAMILY` or `GLOBAL_SUBTOOL`.

Method-harvest disposition: `RESULT_ONLY`.

---

## 12. What is now ruled out

The following cannot close the task by themselves:

1. **generic STP** of `Ahat,Bhat` or `H`;
2. **ordinary principal angles** between `V_m` and `W_m` in the common `L^2(mu_m)` space;
3. the fact that `V_m cap W_m` consists only of constants;
4. the existence of one common positive measure;
5. the order map `u -> u^m` without using the exact AP factor `rho_m`;
6. any argument invariant under replacing `rho_m` by `1`, because that replacement gives the exact countermodel `K=I`.

This is stricter than the parent negative boundary, which had already excluded generic STP, entrywise PF on `Q_m`, ordinary `l_infinity` contraction, and the falsified full sign-regularity shortcut.

---

## 13. Smallest next mathematical action

Attack only the AP deformation

\[
\rho_m(u)=(1-u^{m^2})^{m-1}
\]

inside

\[
\Delta_m=J-Z_m^TJZ_m.
\]

The preferred next exact moves are:

1. derive a Christoffel/finite-difference formula for the `(m-1)`-compound of `Delta_m` relative to the solved Cauchy endpoint;
2. seek an exact sign or nonvanishing formula for the coefficient multiplying the known rank-one adjugate direction `Jv_m`;
3. exploit that the actual moment kernel is an `n`-th step-`m^2` finite difference of one-pole Cauchy kernels, rather than treating it as an arbitrary positive weight;
4. if a sign theorem fails, produce an exact `m` or deformation-parameter counterexample before reopening any generic principal-angle route.

A useful deformation family for a subsequent execution is

\[
\rho_{m,t}(u)=(1-tu^{m^2})^n,
\qquad 0\le t\le1,
\]

with `t=0` giving the exactly solved `K=I` endpoint and `t=1` the AP target. Any monotonicity, inertia-flow, or compound-minor no-zero theorem along this exact path would be genuinely stronger than the routes already killed here.

This deformation proposal is a next-action suggestion only; no monotonicity theorem is asserted in this return.

---

## 14. Scope firewall

This return does **not** establish:

- `det(I-Q_m)!=0` for every `m`;
- that every nontrivial eigenvalue of `K_m` lies in `(0,1)` for all `m`;
- that `Delta_m` has a fixed inertia pattern for all `m`;
- that no sophisticated Hilbert-space argument can ever help;
- novelty of the Cauchy/Krein/Christoffel ingredients;
- Working Truth, Foundation, L4, or canonical status.

It establishes exactly:

- the positive-metric adjoint structure after stripping `J`;
- the signature-twisted cross-Gram representation of the frozen operator;
- an actual-measure exact principal-angle spectral mismatch;
- the all-`m` Cauchy perfect-duality control `K^(0)=I`;
- the exact finite-difference/Christoffel identity connecting that control to the AP kernel;
- the resulting narrowed `J`-transversality frontier in which the AP polynomial weight is indispensable.
