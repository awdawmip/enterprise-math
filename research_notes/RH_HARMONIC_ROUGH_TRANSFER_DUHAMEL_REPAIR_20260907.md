# RH harmonic rough-state transfer and Duhamel repair

Status: `RESEARCH FRONTIER / EXACT RETYPING + UNIFORM HARMONIC TRANSFER + EXACT DUHAMEL REPAIR / NOT A PROOF OF RH`
Date: `2026-09-07`
Project: `Enterprise Math / 进取数论`
Researcher: `EM-RHHR-20260907`
Scope: `RH / Möbius / rough-divisor BRC / generalized Dickman carrier / quotient cells / observer preservation`
Parent frontier:

- `RH_CONTINUUM_DICKMAN_GAMMA_COUNTERTERM_20260907.md`
- `RH_HYPERBOLA_COUNTERTERM_TOWER_20260907.md`
- `RH_ROUGH_DIVISOR_DUHAMEL_QUOTIENT_CELL_BRC_20260907.md`

## 0. Executive correction

The generalized Dickman carrier

\[
R_t(u)
=
\sum_{m\ge 0}\frac{(-t)^m}{m!}
\int_{\substack{x_i\ge 1\\x_1+\cdots+x_m\le u}}
\frac{dx_1\cdots dx_m}{x_1\cdots x_m}
\]

is naturally the continuum model for the **harmonic** rough-divisor state

\[
H_{Y,t}(V)
=
\sum_{\substack{a\le V\\P^-(a)>Y}}
\frac{\mu(a)t^{\omega(a)}}{a},
\]

not for the unweighted cumulative state

\[
M_{Y,t}(V)
=
\sum_{\substack{a\le V\\P^-(a)>Y}}
\mu(a)t^{\omega(a)}
\]

that occurs in the first Abel form of the exact discrete Duhamel identity.

Therefore the direct identification

```text
R_t(u) = CONTINUUM_ANALOGUE_OF_UNWEIGHTED_M_rough
```

is retyped as

```text
R_t(u) = CONTINUUM_ANALOGUE_OF_HARMONIC_H_rough.
```

The Laplace transform, delay equation, Gamma coefficient and boundary-layer
profile in the parent continuum note remain valid for this harmonic carrier.
To use them in the exact discrete coupling, one must insert the harmonic
quotient-cell bridge and retain an explicit floor repair.

This is an observer/provenance correction, not a rejection of the Dickman-Gamma
profile.

P000 is unchanged. The variables `u`, `V`, rough arity and quotient index are
arithmetic relation coordinates, not native spatial axes.

BRC resolution:

```text
COMPOSE_APPLIED
EXTEND_EXISTING_TOOL
HARMONIC_ROUGH_STATE != UNWEIGHTED_ROUGH_STATE
CONTINUUM_TRANSFER_REQUIRES_OBSERVER_MATCH
```

---

## 1. Two exact rough cumulative states

Put

\[
w_t(a)
=
\mu(a)t^{\omega(a)}
\mathbf 1_{\{P^-(a)>Y\}},
\qquad
P^-(1)=\infty .
\]

Define

\[
M_{Y,t}(V)=\sum_{a\le V}w_t(a)
\]

and

\[
H_{Y,t}(V)=\sum_{a\le V}\frac{w_t(a)}a.
\]

They contain the same labeled rough branches, but they are different
observers. Exact partial summation gives

\[
\boxed{
H_{Y,t}(V)
=
\frac{M_{Y,t}(V)}V
+
\sum_{n=1}^{V-1}
\frac{M_{Y,t}(n)}{n(n+1)}.
}
\]

The inverse relation is

\[
\boxed{
M_{Y,t}(V)
=
V H_{Y,t}(V)
-
\sum_{n=1}^{V-1}H_{Y,t}(n).
}
\]

Thus the map `M -> H` is smoothing, while `H -> M` is a discrete derivative.

In particular, a uniform approximation

\[
H_{Y,t}(n)=H_0(n)+O(\varepsilon)
\]

alone only implies the generic bound

\[
M_{Y,t}(V)-M_0(V)=O(V\varepsilon).
\]

The factor `V` is not an artifact: the inverse operator has linear
`ell_infinity` norm, and alternating perturbations realize this scale.

Freeze:

```text
HARMONIC_TRANSFER != UNWEIGHTED_TRANSFER
SMOOTHING_OBSERVER_INVERSION_REQUIRES_REPAIR
UNIFORM_H_ERROR_ALONE -> POSSIBLE_V_AMPLIFICATION_IN_M
```

This is the precise reason that the Dickman-Gamma carrier cannot simply be
substituted for `M_rough` inside the earlier Abel formula.

---

## 2. Exact harmonic quotient-cell bridge

Let

\[
z=t-1,
\qquad
D_U(z)=G_U(z)-G_X(z),
\]

where `G_U` is the suffix average from the parent rough-divisor Duhamel
identity.

The exact centered coupling is

\[
C_X(t)
=
\sum_{\substack{a\le X\\P^-(a)>Y}}
w_t(a)\frac{\lfloor X/a\rfloor}{X}
D_{\lfloor X/a\rfloor}(t-1).
\]

For the quotient cell

\[
I_U(X)
=
\left\{
a:\frac{X}{U+1}<a\le\frac XU
\right\},
\]

all branches have the same residual population `U`.

Define

\[
\Delta H_U
=
H_{Y,t}\!\left(\left\lfloor\frac XU\right\rfloor\right)
-
H_{Y,t}\!\left(\left\lfloor\frac X{U+1}\right\rfloor\right)
=
\sum_{a\in I_U(X)}\frac{w_t(a)}a.
\]

Since

\[
\frac UX
=
\frac1a+
\left(\frac UX-\frac1a\right)
\qquad(a\in I_U(X)),
\]

we obtain the exact decomposition

\[
\boxed{
C_X(t)=C_X^{\mathrm{harm}}(t)+E_X^{\mathrm{floor}}(t),
}
\]

where

\[
C_X^{\mathrm{harm}}(t)
=
\sum_{U=1}^{X}\Delta H_U\,D_U(t-1)
\]

and

\[
\boxed{
E_X^{\mathrm{floor}}(t)
=
\sum_{\substack{a\le X\\P^-(a)>Y}}
w_t(a)
\left(
\frac{\lfloor X/a\rfloor}{X}-\frac1a
\right)
D_{\lfloor X/a\rfloor}(t-1).
}
\]

The floor repair is exact and satisfies pointwise

\[
\left|
\frac{\lfloor X/a\rfloor}{X}-\frac1a
\right|<\frac1X.
\]

No absolute-value estimate is imposed at this stage; doing so would erase the
rough Möbius orientation.

---

## 3. Harmonic Abel form

Let

\[
V_U=\left\lfloor\frac XU\right\rfloor.
\]

Discrete Abel summation in the quotient variable gives

\[
C_X^{\mathrm{harm}}(t)
=
H_{Y,t}(X)D_1
+
\sum_{U=2}^{X}
H_{Y,t}(V_U)(D_U-D_{U-1}).
\]

Because `D_X=0`, a constant state may be subtracted exactly:

\[
\boxed{
C_X^{\mathrm{harm}}(t)
=
[H_{Y,t}(X)-1]D_1
+
\sum_{U=2}^{X}
[H_{Y,t}(V_U)-1](D_U-D_{U-1}).
}
\]

For `V_U<=Y`, the only admissible rough divisor is `1`, hence
`H_{Y,t}(V_U)=1`. Therefore the sum is supported on

\[
U\le U_0:=\left\lfloor\frac X{Y+1}\right\rfloor.
\]

This is the operation-safe entry point for the Dickman-Gamma carrier.

Freeze:

```text
UNWEIGHTED_ABEL_FORM = EXACT_BUT_WRONG_PORT_FOR_R_t
HARMONIC_CELL_FORM + FLOOR_REPAIR = EXACT_MATCHED_PORT
```

---

## 4. Prime-log measure carrier

Fix `u>=1` and put `V=Y^u`. Define the atomic prime-log measure

\[
\nu_{Y,u}
=
\sum_{Y<p\le Y^u}
\frac1p\,
\delta_{\log p/\log Y}
\]

on `[1,u]`, and the continuum measure

\[
\lambda_u(dx)
=
\mathbf 1_{[1,u]}(x)\frac{dx}{x}.
\]

For a positive finite measure `alpha` on `[1,u]`, define the cumulative
Poissonized simplex functional

\[
Z_\alpha(u;t)
=
\sum_{m\ge0}
\frac{(-t)^m}{m!}
\alpha^{*m}([0,u]).
\]

Because every atom lies at least at `1`, only `m<=floor(u)` contributes.

For the continuum measure,

\[
\boxed{Z_{\lambda_u}(u;t)=R_t(u).}
\]

For the prime measure, `Z_nu` permits repeated use of the same prime label.
The exact harmonic rough state instead permits each prime label at most once.
The difference is therefore a diagonal/repeated-label repair.

---

## 5. Convolution discrepancy lemma

Let `alpha` and `beta` be positive measures on `[1,u]`. Put

\[
\Delta
=
\sup_{0\le v\le u}
|\alpha([0,v])-\beta([0,v])|
\]

and assume both total masses are at most `L`.

For every integer `m>=1`,

\[
\boxed{
\frac{
|\alpha^{*m}([0,u])-\beta^{*m}([0,u])|
}{m!}
\le
\frac{2\Delta L^{m-1}}{(m-1)!}.
}
\]

### Proof

Use the exact telescoping identity

\[
\alpha^{*m}-\beta^{*m}
=
\sum_{j=0}^{m-1}
\alpha^{*j}*(\alpha-\beta)*\beta^{*(m-1-j)}.
\]

For each term, integrate the signed measure `alpha-beta` against the
monotone tail-cumulative function supplied by the remaining `m-1`
convolution factors. Its variation is at most `L^{m-1}`. Stieltjes
integration by parts and the cumulative discrepancy bound give at most

\[
2\Delta L^{m-1}
\]

per term. Summing the `m` terms and dividing by `m!` proves the claim.

Consequently,

\[
\boxed{
|Z_\alpha(u;t)-Z_\beta(u;t)|
\le
2\Delta |t|e^{|t|L}.
}
\]

This is a cumulative-observer estimate. It does not require the total
variation of `alpha-beta` to be small.

---

## 6. Repeated-prime collision repair

Put

\[
Q_{Y,u}
=
\sum_{Y<p\le Y^u}\frac1{p^2}
\]

and

\[
L_{Y,u}
=
\sum_{Y<p\le Y^u}\frac1p.
\]

In the `m`-fold ordered prime tuple expansion, the total mass of tuples with
at least one repeated prime label is bounded by the union bound

\[
\binom m2 Q_{Y,u}L_{Y,u}^{m-2}.
\]

After division by `m!` and summation over `m`, this gives

\[
\boxed{
|H_{Y,t}(Y^u)-Z_{\nu_{Y,u}}(u;t)|
\le
\frac{|t|^2}{2}Q_{Y,u}
e^{|t|L_{Y,u}}.
}
\]

This is the exact BRC price of replacing distinct labeled prime branches by a
Poissonized measure convolution.

Freeze:

```text
POISSONIZED_CONVOLUTION_REUSES_LABELS
SQUAREFREE_FACTOR_BRC_REQUIRES_DIAGONAL_COLLISION_REPAIR
```

---

## 7. Uniform harmonic discrete-to-continuum theorem

Define the prime-harmonic cumulative discrepancy

\[
\delta_Y(u)
=
\sup_{1\le v\le u}
\left|
\sum_{Y<p\le Y^v}\frac1p-\log v
\right|
\]

and

\[
L_Y(u)
=
\max\left(
\sum_{Y<p\le Y^u}\frac1p,\,
\log u
\right).
\]

Combining Sections 5 and 6 gives the exact finite-scale bound

\[
\boxed{
|H_{Y,t}(Y^u)-R_t(u)|
\le
e^{|t|L_Y(u)}
\left(
2|t|\delta_Y(u)
+
\frac{|t|^2}{2}Q_{Y,u}
\right).
}
\]

Classical prime-harmonic Mertens estimates yield, uniformly in `u>=1`,

\[
\delta_Y(u)\ll\frac1{\log Y},
\]

while trivially

\[
Q_{Y,u}\le\sum_{n>Y}\frac1{n^2}\ll\frac1Y
\]

and

\[
L_Y(u)=\log u+O(1/\log Y).
\]

Let

\[
u_X=\frac{\log X}{\log Y},
\qquad
L_X=\log u_X,
\]

and assume `u_X>1`. Uniformly for `Y<=V<=X` and

\[
|t|\le\frac c{L_X},
\]

we obtain

\[
\boxed{
H_{Y,t}(V)
=
R_t\!\left(\frac{\log V}{\log Y}\right)
+
O_c\left(
\frac1{\log Y\,L_X}
+
\frac1{Y L_X^2}
\right).
}
\]

At the RH-critical cutoff

\[
Y=(\log X)^2,
\qquad
u_X=\frac{\log X}{2\log\log X},
\]

this becomes

\[
\boxed{
\sup_{\substack{Y\le V\le X\\|t|\le c/L_X}}
\left|
H_{Y,t}(V)
-
R_t\!\left(\frac{\log V}{\log Y}\right)
\right|
\ll_c
\frac1{(\log\log X)^2}.
}
\]

This closes the previously open discrete-to-continuum transfer at the
**harmonic rough-state level** on the full shrinking boundary-layer window.

It does not transfer the unweighted state `M_rough`, and it does not prove RH.

---

## 8. Exact measure-valued Duhamel source

Define the signed exponential convolution measure

\[
\mathfrak E_t(\alpha)
=
\sum_{m\ge0}\frac{(-t)^m}{m!}\alpha^{*m}.
\]

Let

\[
\eta=\nu_{Y,u}-\lambda_u,
\qquad
\alpha_\theta=\lambda_u+\theta\eta.
\]

Differentiating the finite convolution series on `[0,u]` gives

\[
\frac{d}{d\theta}\mathfrak E_t(\alpha_\theta)
=
-t\,\eta*\mathfrak E_t(\alpha_\theta).
\]

Hence

\[
\boxed{
Z_{\nu_{Y,u}}(u;t)-R_t(u)
=
-t\int_0^1
[\eta*\mathfrak E_t(\alpha_\theta)]([0,u])
\,d\theta.
}
\]

Therefore the harmonic transfer defect has exactly two sources:

1. the prime-harmonic intensity measure `eta`;
2. the repeated-prime diagonal collision repair.

No third hidden continuum source is present.

This is the measure-level analogue of the rough-divisor Duhamel formula and
makes the first-line BRC provenance explicit.

---

## 9. Corrected continuum Duhamel carrier

For every quotient index set

\[
u_U=\frac{\log V_U}{\log Y},
\qquad
V_U=\left\lfloor\frac XU\right\rfloor.
\]

Define

\[
\mathcal B_X^{\mathrm{harm}}(t)
=
[R_t(u_1)-1]D_1
+
\sum_{U=2}^{U_0}
[R_t(u_U)-1](D_U-D_{U-1}),
\]

where

\[
U_0=\left\lfloor\frac X{Y+1}\right\rfloor.
\]

Put

\[
e_{Y,t}(V)
=
H_{Y,t}(V)
-
R_t\!\left(\frac{\log V}{\log Y}\right).
\]

Then the original exact centered coupling satisfies

\[
\boxed{
C_X(t)-\mathcal B_X^{\mathrm{harm}}(t)
=
E_X^{\mathrm{floor}}(t)
+
e_{Y,t}(X)D_1
+
\sum_{U=2}^{U_0}
e_{Y,t}(V_U)(D_U-D_{U-1}).
}
\]

This is the required discrete-minus-continuum residual with all repair
coordinates retained.

The previous continuum counterterm can now be interpreted correctly:

```text
DICKMAN_GAMMA_PROFILE
-> HARMONIC_ROUGH_PROPAGATOR
-> QUOTIENT-CELL PAIRING
+ FLOOR_REPAIR
+ PRIME-MEASURE_TRANSFER_REPAIR
```

---

## 10. Why the uniform theorem still does not close the coupling

Define the unsigned response-variation seminorm

\[
\mathcal V_X(D)
=
|D_1|
+
\sum_{U=2}^{U_0}|D_U-D_{U-1}|.
\]

The uniform transfer theorem gives only

\[
\left|
e_{Y,t}(X)D_1
+
\sum_{U=2}^{U_0}
e_{Y,t}(V_U)(D_U-D_{U-1})
\right|
\le
\|e_{Y,t}\|_\infty\mathcal V_X(D).
\]

This is mathematically valid but structurally too coarse.

For the RH source `f(p)=sqrt(p)1_(p<=Y)`, at `t=0` one has

\[
G_1(-1)=0
\]

and

\[
-G_X(-1)
=
\sum_{p\le Y}\sqrt p\,
\frac{\lfloor X/p\rfloor}{X}
\sim
\sum_{p\le Y}\frac1{\sqrt p}
\sim
\frac{2\sqrt Y}{\log Y}.
\]

The same scale persists throughout the real boundary layer
`0<=t<=c/L_X`. Indeed,

\[
-G_X(t-1)
=
\frac1X\sum_{n\le X}
\sum_j(1-t)^{j-1}\sqrt{Q_j(n)}.
\]

Using `1-(1-t)^k<=kt`, its difference from the endpoint is at most

\[
t\sum_{q<r\le Y}
\frac{\sqrt q}{X}\left\lfloor\frac X{qr}\right\rfloor
\le
t\sum_{q<r\le Y}\frac1{\sqrt q\,r}
\ll
t\frac{\sqrt Y}{(\log Y)^2}.
\]

Thus uniformly on that boundary layer,

\[
|D_1(t-1)|
=
(1+o(1))\frac{2\sqrt Y}{\log Y},
\]

and hence

\[
\mathcal V_X(D)\ge |D_1|
\asymp\frac{\sqrt Y}{\log Y}.
\]

At `Y=(log X)^2`, this is of order

\[
\frac{\log X}{\log\log X}.
\]

Consequently the direct product of the Section 7 sup error with the unsigned
variation norm is of order at best

\[
\frac{\log X}{(\log\log X)^3}
\]

at nonzero boundary-layer scale. It does not even tend to zero. This does
not show that the actual signed pairing is large; it proves that the
`sup x total-variation` route cannot certify the needed cancellation.

The boundary-layer factor `t` and the signed correlation with
`D_U-D_(U-1)` must be used before absolute values are taken.

Freeze:

```text
UNIFORM_HARMONIC_TRANSFER x UNSIGNED_RESPONSE_VARIATION
!= RH_CANCELLATION
```

The transfer theorem removes a typing gap and isolates the source. It does
not supply the required signed pairing estimate.

---

## 11. Exact checker

Task-local extension:

`experiments/rh_harmonic_rough_duhamel_bridge_check.py`

It verifies with exact rational arithmetic:

- original floor-weighted Duhamel coupling
  `= harmonic cell pairing + floor repair`;
- harmonic cell pairing `= harmonic Abel form`;
- exact `M <-> H` partial-summation inversion;
- the finite convolution-discrepancy inequality;
- the repeated-label collision repair bound.

The checker is a finite regression certificate, not an asymptotic proof.

---

## 12. New smallest unresolved unit

The continuum product-budget profile is now attached to the correct discrete
state. The remaining residual is no longer an undefined
“discrete Dickman error”; it is the sum of two explicit pairings:

\[
E_X^{\mathrm{floor}}(t)
\]

and

\[
\mathcal P_X(t)
=
e_{Y,t}(X)D_1
+
\sum_{U=2}^{U_0}
e_{Y,t}(V_U)(D_U-D_{U-1}).
\]

The next admissible target is a signed boundary-layer estimate for
`mathcal P_X(t)` that uses the measure-valued Duhamel source before taking
absolute values.

A useful first theorem would prove, for some fixed `delta>0` and
`|t|<=c/L_X`, a gain over the generic variation bound by exploiting one or
more of:

- cancellation of the prime-harmonic discrepancy measure against suffix
  innovations;
- quotient-cell oscillation;
- ordered-prime edge provenance;
- a mean-square rather than `ell_1` response norm;
- exact treatment of the floor sawtooth source.

The theorem must not:

- replace `M_rough` by `H_rough` without the inverse/floor repair;
- erase prime labels into an arity histogram;
- interpret the positive convolution bound as signed cancellation;
- assume an RH-strength prime discrepancy;
- infer a growing-scale theorem from the exact finite checker.

No RH proof is claimed.
