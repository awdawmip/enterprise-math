# RH fixed-order hyperbola counterterm tower and boundary-layer profile

Status: `RESEARCH FRONTIER / FIXED-ORDER ASYMPTOTIC + FORMAL RESUMMATION + NO-GO / NOT A PROOF OF RH`
Date: `2026-09-07`
Project: `Enterprise Math / 进取数论`
Scope: `RH / Möbius / rough-smooth covariance / Alladi jets / hyperbola budget / BRC`
Parent frontier:

- `RH_ROUGH_SMOOTH_BUDGET_COVARIANCE_20260907.md`
- `RH_ROUGH_DIVISOR_DUHAMEL_QUOTIENT_CELL_BRC_20260907.md`

## 0. Question and typing guard

The parent result showed that the first derivative of the centered rough/small coupling has a universal nonzero main term. The next question is whether this is an isolated first-order defect or the first member of a structured tower.

P000 remains unchanged. The variables below are arithmetic-depth and product-budget coordinates, not new native X6 axes.

BRC discipline remains:

`PROVENANCE > MULTIPLICITY > BOOLEAN SUPPORT`.

The fixed-order asymptotics below do not justify exchanging the Taylor order with the scale `X`. The formal resummation is explicitly typed as a carrier prediction, not a proved uniform approximation.

---

## 1. Taylor decomposition of the centered coupling

Let

`H=H_Y(N_X)=#{p|N_X:p>Y}`

for uniform `N_X<=X`, and let

`A(t)=A^suf_(N_X,f)(t-1)=sum_(j>=0)A_j(N_X)t^j`.

Define

`C_X(t)=Cov_X((1-t)^H,A(t)).`

Since

`(1-t)^H=sum_(a>=0)(-1)^a C(H,a)t^a,`

the coefficient

`c_m(X)=[t^m]C_X(t)`

satisfies exactly

`c_m(X)`
`=sum_(a=1)^m (-1)^a`
`  Cov_X(C(H,a), A_(m-a)).`

The `a=0` term vanishes because covariance with the constant `1` is zero.

For the prime weight

`f_(beta,Y)(q)=q^beta 1_(q<=Y),`

the zeroth suffix jet is

`A_0=-S_(beta,Y),`

where

`S_(beta,Y)=sum_(q<=Y)q^beta 1_(q|N_X).`

Therefore the extremal rough-depth term is

`(-1)^(m+1) Cov_X(C(H,m),S_(beta,Y)).`

---

## 2. The m-rough-prime hyperbola shell

Fix an integer `m>=1`. For a small prime `q<=Y`, define the unordered rough-prime shell mass

`J_m(X,Y;q)`
`=sum_(Y<p_1<...<p_m, X/q<p_1...p_m<=X)`
`  1/(p_1...p_m).`

Put

`a_X=log Y/log X,`

`delta_q=log q/log X,`

`L_X=log(1/a_X)=log(log X/log Y).`

At the logarithmic-prime-density level, `J_m` is the thin simplex shell

`(1/m!) int_(v_i>=a_X, 1-delta_q<sum v_i<=1)`
`        dv_1...dv_m/(v_1...v_m).`

For fixed `m`, the boundary density at `sum v_i=1` has the asymptotic

`L_X^(m-1)/(m-1)!`.

Reason: the leading logarithmic divergence occurs when one of the `m` coordinates carries the macroscopic remainder and the other `m-1` coordinates range independently down to `a_X`. There are `m` choices for the macroscopic coordinate, cancelling the `m!` unordered normalization down to `(m-1)!`.

Since `0<=delta_q<=a_X`, the shell thickness is small enough that uniform partial summation gives

`J_m(X,Y;q)`
`= (log q/log X)`
`  L_X^(m-1)/(m-1)!`
`  (1+o(1))`

in the aggregate weighted range `q<=Y`.

This is the geometric source of the tower: each additional rough prime opens one more logarithmic simplex coordinate.

---

## 3. Fixed-order covariance asymptotic

### Theorem candidate with completed fixed-m derivation

Fix `kappa>0`, `beta>0`, and a positive integer `m`. Let

`Y=(log X)^kappa`.

Then

`Cov_X(C(H_Y,m),S_(beta,Y))`
`= -Y^beta/(beta log X)`
`  L_X^(m-1)/(m-1)!`
`  (1+o(1)),`

where

`L_X=log(log X/log Y).`

Consequently

`c_m(X)`
`= (-1)^m Y^beta/(beta log X)`
`  L_X^(m-1)/(m-1)!`
`  (1+o(1)).`

### Derivation

The joint divisibility main terms cancel when

`q p_1...p_m<=X`.

When

`X/q<p_1...p_m<=X,`

the rough m-tuple occurs in the marginal but cannot coexist with the small prime `q`. Thus the leading covariance is the negative forbidden-shell mass

`-sum_(q<=Y)q^(beta-1)J_m(X,Y;q).`

Using the shell formula and the prime number theorem,

`sum_(q<=Y)q^(beta-1)log q`
`=Y^beta/beta (1+o(1)),`

which gives the stated main term.

It remains to compare the other exact Taylor terms

`Cov(C(H,a),A_(m-a))`, `a<m`.

The suffix jet `A_j` contains `j+1` selected small primes. Its additional small-prime harmonic volume is at most a fixed power of

`loglog Y`.

The rough shell of arity `a` contributes at most `L_X^(a-1)`. Hence every `a<m` term is bounded, up to the common amplitude `Y^beta/log X`, by

`L_X^(a-1)(loglog Y)^(m-a).`

For `Y=(log X)^kappa`,

`loglog Y=O(logloglog X)=o(L_X).`

Therefore all `a<m` terms are lower order than

`L_X^(m-1)`.

The floor-function errors are also lower order for fixed `m`; after splitting at the hyperbola and repeated partial summation, they gain at least one factor `1/log Y` or lose one logarithmic simplex volume.

For `m=1`, this recovers the proved covariance law in the parent note. For `m=2`, the dominant term is the covariance of one small prime with two rough primes in the thin product shell `X/q<p_1p_2<=X`.

No uniformity in growing `m` is claimed.

---

## 4. Critical specialization

At the balance

`kappa beta=1,`

the common amplitude satisfies

`Y^beta/(beta log X)->1/beta=kappa.`

Thus for every fixed `m`,

`c_m(X)`
`~(-1)^m (1/beta)`
`  L_X^(m-1)/(m-1)!.`

For the RH choice

`kappa=2`, `beta=1/2`,

`L_X=log(log X/(2loglog X))`

and

`c_m(X)`
`~2(-1)^m L_X^(m-1)/(m-1)!.`

The first three leading terms are therefore

`c_1~-2,`

`c_2~2L_X,`

`c_3~-L_X^2.`

This explains the finite sign pattern

`negative, positive, negative, ...`

and the slow growth of the second and higher derivatives.

---

## 5. Formal counterterm generating function

Define

`A_X=Y^beta/(beta log X).`

The fixed-order main terms are exactly the Taylor coefficients of

`B_X(t)=-A_X t exp(-L_X t).`

Indeed,

`-A_X t exp(-L_Xt)`
`=sum_(m>=1)(-1)^m A_X`
`  L_X^(m-1)/(m-1)! t^m.`

Thus `B_X(t)` is the canonical **hyperbola-budget counterterm tower**.

At the RH specialization,

`B_X(t)`
`=-2t (2loglog X/log X)^t`

up to the immaterial floor in `Y`.

This profile has a striking nonuniformity:

- `B_X'(0)->-2`;
- every fixed derivative of order `m>=2` grows like a power of `L_X`;
- for every fixed real `t>0`, `B_X(t)->0`.

There is no contradiction. The variation is concentrated in a shrinking boundary layer of width

`t~1/L_X.`

Freeze:

`FIXED_T_SMALLNESS != FIXED_JET_SMALLNESS`.

`GROWING_JET_TOWER = BOUNDARY_LAYER_PROVENANCE`.

---

## 6. Why the exponential factor is natural

The rough-prime harmonic mass between `Y` and `X` is

`sum_(Y<p<=X)1/p`
`=loglog X-loglog Y+o(1)`
`=L_X+o(1).`

In the independent/continuum carrier, the rough-prefix generating factor is therefore

`prod_(Y<p<=X)(1-t/p)`
`~exp(-tL_X)`
`=(log Y/log X)^t.`

The extra factor `-A_Xt` is the first-order loss from the thin forbidden shell created by inserting one weighted small prime.

Hence the formal resummation has a direct BRC meaning:

`SMALL_PRIME_INSERTION`
` x ROUGH_PREFIX_SURVIVAL_GENERATING_FACTOR.`

This does not prove that the actual coupling is uniformly asymptotic to `B_X(t)` for fixed `t`. It explains why all fixed Taylor layers share one exponential counterterm family.

---

## 7. A second depth scale appears

The counterterm tower has effective Taylor depth

`L_X~loglog X.`

The full RH provenance depth found previously is

`K_X~log X/(2loglog X).`

Therefore

`L_X=o(K_X).`

This separates two phenomena that had previously been conflated:

1. **product-budget boundary depth**: `O(loglog X)`, generated by the hyperbola shell and resumable by the continuum rough survival factor;
2. **RH-critical factor provenance depth**: `O(log X/loglog X)`, required to reach the Hildebrand/Alladi critical regime.

The deterministic budget tower occupies only a vanishing fraction of the full critical BRC depth.

Freeze:

`HYPERBOLA_COUNTERTERM_DEPTH << RH_PROVENANCE_DEPTH`.

This is encouraging but not a proof gain: after subtracting the counterterm tower, the remaining discrete prime-intensity and deep-provenance errors still require control.

---

## 8. Finite pilot

The task-local checker directly computes the first three coefficients of `C_X(t)` for the RH specialization.

| `X` | `c_1` | `c_2` | `c_3` |
|---:|---:|---:|---:|
| `10,000` | `-1.7925832710` | `1.4121399791` | `-0.5431992842` |
| `100,000` | `-1.9084352037` | `1.8383201790` | `-0.9045142857` |
| `1,000,000` | `-1.9225081573` | `2.2049799102` | `-1.2580639366` |

The corresponding fixed-order model values are approximately:

| `X` | model `c_1` | model `c_2` | model `c_3` |
|---:|---:|---:|---:|
| `10,000` | `-1.9901873372` | `1.4563053747` | `-0.5328205302` |
| `100,000` | `-1.9958654867` | `1.7119558927` | `-0.7342160577` |
| `1,000,000` | `-1.9954454371` | `1.9318522712` | `-0.9351428829` |

The logarithmic convergence is slow. The table is only a finite consistency check; it neither establishes the fixed-order asymptotic nor supplies growing-order uniformity.

---

## 9. Exact checker

Task-local checker:

`experiments/rh_hyperbola_counterterm_tower_check.py`.

It computes the first three covariance coefficients directly from all integers up to the selected finite bounds, checks the alternating signs, and compares them with the counterterm coefficients.

No finite computation is used as a proof of RH or of uniform resummation.

---

## 10. No-go and next target

The current result rules out another shortcut:

`REMOVE_ONLY_THE_FIRST_COVARIANCE_MODE -> INSUFFICIENT.`

The first defect belongs to an entire fixed-order tower. Removing finitely many derivatives leaves later terms whose scale grows with `L_X`.

At the same time, the formal exponential carrier suggests that handling each layer separately is the wrong operation. The next admissible target is a **uniform counterterm theorem** on a shrinking critical neighborhood, for example

`|t|<=c/L_X`

or a weighted Hardy disk adapted to that scale.

The first useful statement would be a bound of the form

`C_X(t)-B_X(t)=o(1/L_X)`

uniformly for `|t|<=c/L_X`, with explicit treatment of:

- the discrete one-point prime intensity source;
- suffix jets involving more than one small prime;
- floor-quotient errors;
- the high-arity repair;
- complex/signed observers without taking absolute branch mass.

Even such a local theorem would not prove RH. It would, however, rigorously remove the entire deterministic product-budget boundary layer and expose the genuinely arithmetic remainder before the full depth `K_X` is addressed.

No RH proof is claimed.
