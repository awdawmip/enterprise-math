# RH rough-divisor Duhamel expansion and quotient-cell BRC

Status: `RESEARCH FRONTIER / EXACT IDENTITIES + STATE-COMPLEXITY MATCH + NO-GO / NOT A PROOF OF RH`
Date: `2026-09-07`
Project: `Enterprise Math / 进取数论`
Scope: `RH / Möbius / Alladi polynomial / Kubilius coupling / rough-smooth factorization / BRC / quotient cells`
Parent frontier:

- `RH_KUBILIUS_SUFFIX_PREFIX_SHIFT_INTENSITY_BARRIER_20260907.md`
- `RH_ALLADI_PASCAL_FRAME_ORDERED_PRIME_EDGE_BRC_20260907.md`
- `RH_GREEN_ALLADI_CRITICAL_PRIMITIVE_SOURCE_PORT_20260906.md`

## 0. Typing and reuse guard

P000 remains unchanged. The arithmetic quotient `floor(X/a)`, rough-factor arity, prime label, and residual product budget are provenance/relation coordinates, not additional native X6 spatial axes.

BRC discipline is mandatory:

`PROVENANCE > MULTIPLICITY > BOOLEAN SUPPORT`.

Tool/interface resolution:

`COMPOSE_APPLIED`.

This note composes the existing collective Alladi polynomial, the rough-prefix monomial action, the critical Kubilius suffix model, and the BRC observer-preservation rule. No new top-level BRC family is asserted. No RH proof is claimed.

Throughout, `P^-(1)=infinity`, and every rough divisor `a` below is squarefree unless stated otherwise.

---

## 1. Exact rough-divisor expansion of the prefix phase

Fix `X>=1`, a cutoff `Y>=2`, and a prime test function `f` supported on `p<=Y`.

For every integer `n`, let

`h_Y(n)=#{p|n:p>Y}`

be the number of distinct rough-prefix primes. Put

`t=1+z`.

The parent frontier proved the global/suffix factorization

`A^glob_(n,f)(z)=(-z)^(h_Y(n)) A^suf_(n,f)(z)`.

Since `-z=1-t`, squarefree divisor expansion gives exactly

`(-z)^(h_Y(n))`
`= (1-t)^(h_Y(n))`
`= sum_{a|n, P^-(a)>Y} mu(a)t^(omega(a)).`

This is a genuine BRC branch expansion: each squarefree rough divisor records which rough-prefix prime labels were selected, and `mu(a)t^omega(a)` is applied only after the labeled branch exists.

Freeze:

`ROUGH_PREFIX_PHASE = SIGNED_SQUAREFREE_ROUGH_DIVISOR_BRC`.

---

## 2. Exact discrete Duhamel formula

Define the averaged global polynomial

`F_X(z)=(1/X)sum_(n<=X) A^glob_(n,f)(z)`

and the suffix average at population size `U` by

`G_U(z)=(1/U)sum_(m<=U) A^suf_(m,f)(z)`.

Insert the rough-divisor expansion and write `n=am`. Because every prime of `a` exceeds `Y`, the small-prime suffix of `am` equals the small-prime suffix of `m`. Therefore

`F_X(z)`
`= sum_(a<=X, P^-(a)>Y)`
`  mu(a)t^(omega(a)) floor(X/a)/X`
`  G_(floor(X/a))(z).`

Thus the exact branch weight is

`W_X(a,z)`
`= mu(a)(1+z)^(omega(a)) floor(X/a)/X.`

This closes the schematic weight left open in the parent note.

Interpretation:

- `a` is the rough-prefix provenance packet;
- `mu(a)(1+z)^omega(a)` is its signed observer amplitude;
- `floor(X/a)/X` is its exact surviving population fraction;
- `G_(floor(X/a))` is the suffix response at the residual population size.

This is a finite discrete Duhamel expansion: rough sources are injected at their exact product scale and propagated through the suffix response appropriate to the remaining integer budget.

---

## 3. Rough-prefix phase polynomial

Define

`R_X(z;Y)`
`= sum_(a<=X, P^-(a)>Y)`
`  mu(a)(1+z)^(omega(a)) floor(X/a)/X.`

The same divisor switch gives

`R_X(z;Y)=(1/X)sum_(n<=X)(-z)^(h_Y(n)).`

In the variable `w=-z`, this is the ordinary positive probability generating function of the rough-prefix depth `h_Y(N_X)` for uniform `N_X<=X`.

Exact observers are:

`R_X(-1;Y)=1,`

`R_X(0;Y)=Psi(X,Y)/X,`

`R_X(1;Y)=(1/X)sum_(n<=X)(-1)^(h_Y(n)).`

Here `Psi(X,Y)` counts `Y`-smooth integers.

The factorial jets at `z=-1` are

`(1/m!) partial_z^m R_X(-1;Y)`
`= (-1)^m E C(h_Y(N_X),m).`

Thus one exact polynomial carries:

- smoothness probability;
- rough-prefix parity;
- every rough-depth factorial moment;
- full labeled-divisor provenance before averaging.

---

## 4. Arbitrary-reference split and conditional defect

For any reference suffix polynomial `G_*(z)`, add and subtract it inside the Duhamel sum:

`F_X(z)=G_*(z)R_X(z;Y)+C_*(X,Y;z),`

where

`C_*`
`= sum_a mu(a)t^(omega(a)) floor(X/a)/X`
`  [G_(floor(X/a))(z)-G_*(z)].`

Two choices are especially useful.

### Independent Kubilius reference

If `G_*` is the explicit independent Bernoulli suffix expectation from the parent frontier, `C_*` is the exact signed sum of conditional Kubilius defects over rough-prefix branches.

### Actual root-population reference

If `G_*=G_X`, then

`C_X=F_X-G_XR_X`

is exactly the covariance between the rough-prefix phase `(-z)^h` and the suffix polynomial under uniform integers `n<=X`.

Freeze:

`GLOBAL_FACTOR_STATE = MARGINAL_SUFFIX x ROUGH_PHASE + CONDITIONAL_COUPLING_DEFECT`.

The first product contains the one-point prime intensity. The second term is the remaining rough/suffix dependence. They must not be conflated.

---

## 5. Floor-quotient cells

For each positive quotient `U`, define the exact floor cell

`I_U(X)={a: X/(U+1)<a<=X/U}`

and its rough signed polynomial

`Q_(X,Y;U)(t)`
`= sum_(a in I_U(X), P^-(a)>Y)`
`  mu(a)t^(omega(a)).`

Every `a` in the same cell has the same residual population

`floor(X/a)=U`.

Therefore the Duhamel formula groups exactly as

`F_X(z)`
`= sum_(U in Q_X) (U/X)`
`  Q_(X,Y;U)(1+z) G_U(z),`

where

`Q_X={floor(X/a):1<=a<=X}`.

The classical floor-quotient count satisfies

`#Q_X <= 2 floor(sqrt(X)).`

Indeed:

- `a<=sqrt(X)` supplies at most `sqrt(X)` quotients;
- `a>sqrt(X)` has quotient below `sqrt(X)`.

The rough polynomial in each cell has degree at most

`K_Y(X)=floor(log X/log Y)`.

Even retaining every polynomial coefficient and every required suffix coefficient gives an exact carrier of size

`X^(1/2+o(1))`

at the critical cutoff `Y=(log X)^2`.

This matches the square-root identity budget found in the earlier collision-compression lower bound:

- a fixed 64-state endpoint is too small;
- an exact quotient-cell carrier naturally appears at square-root scale.

This is a representation-size statement, not a fast construction theorem.

---

## 6. Quotient-depth light cone

If the coefficient of rough arity `h>=1` in `Q_(X,Y;U)` is nonzero, some rough squarefree `a` satisfies

`floor(X/a)=U`, `omega(a)=h`, and `P^-(a)>Y`.

Then

`a>Y^h`

and

`Ua<=X`,

so necessarily

`U Y^h < X.`

Thus the rough quotient carrier has an exact triangular light cone.

At the critical choices

`Y=(log X)^2,`

`K=floor(log X/(2loglog X)),`

we have

`Y^K<=X<Y^(K+1).`

Consequently the deepest rough layers can occur only in the late, small-`U` boundary:

- arity `h` is confined to `U<X/Y^h`;
- arity `K` is confined to `U<X/Y^K<Y`.

This makes precise the earlier observation that growing provenance depth and shrinking residual population are conjugate coordinates.

---

## 7. Equivalent rough-partial-sum convolution

Define the rough polynomial partial sum

`M_rough(V;t)`
`= sum_(a<=V, P^-(a)>Y) mu(a)t^(omega(a)).`

Switch the Duhamel sum in the other order. Since

`G_U=(1/U)sum_(m<=U)A^suf_(m,f),`

we obtain exactly

`F_X(z)`
`= (1/X)sum_(m<=X)`
`  A^suf_(m,f)(z)`
`  M_rough(floor(X/m);1+z).`

This is the same carrier in convolution form:

`SUFFIX_INNOVATION x CUMULATIVE_ROUGH_PROVENANCE`.

No quotient or absolute value has been taken.

---

## 8. Exact Abel/innovation formula

The quotient-cell polynomial is the finite difference

`Q_(X,Y;U)(t)`
`= M_rough(floor(X/U);t)`
` -M_rough(floor(X/(U+1));t).`

Let

`D_U(z)=G_U(z)-G_*(z)`

and

`H_U(z)=U D_U(z).`

Because

`U G_U-(U-1)G_(U-1)=A^suf_(U,f),`

we have

`H_U-H_(U-1)=A^suf_(U,f)-G_*.`

Discrete Abel summation in the quotient variable gives the exact identity

`C_*(X,Y;z)`
`= (1/X)sum_(U=1)^X`
`  M_rough(floor(X/U);1+z)`
`  [A^suf_(U,f)(z)-G_*(z)].`

This is the precise signed summation-by-parts formula requested by the parent frontier.

It converts the conditional average defect into a correlation between:

- a cumulative rough Möbius/BRC state;
- a centered one-Cell suffix innovation.

Nothing has been estimated yet, but the missing operation is now exact.

---

## 9. Covariance form removes the trivial late boundary exactly

Take `G_*=G_X`. Then

`sum_(U<=X)[A^suf_(U,f)-G_X]=0`.

Therefore the Abel formula may subtract the constant rough state `1`:

`C_X(z)`
`= (1/X)sum_(U<=X)`
`  [M_rough(floor(X/U);1+z)-1]`
`  [A^suf_(U,f)(z)-G_X(z)].`

If

`floor(X/U)<=Y`,

there is no nontrivial integer `a` in the rough sum, so

`M_rough(floor(X/U);t)=1`.

Hence the covariance is supported exactly inside

`U<=floor(X/(Y+1)).`

The late region with residual rough budget below one cancels from the dependence channel. It remains present only through the separate marginal/intensity term `G_XR_X`.

This corrects a possible overstatement of the late-source obstruction:

- late branches are a genuine obstacle in an arbitrary-reference absolute estimate;
- after exact covariance centering, their constant rough state disappears;
- the unresolved dependence begins where at least one rough prime can occur.

Freeze:

`COVARIANCE_CENTERING_REMOVES_TRIVIAL_LATE_ROUGH_STATE, NOT PRIME_INTENSITY`.

---

## 10. Exact rough-arity layer expansion

Let

`R_h(V;Y)`
`=#{a<=V: a squarefree, P^-(a)>Y, omega(a)=h}.`

Then

`M_rough(V;t)-1=sum_(h>=1)(-t)^h R_h(V;Y).`

Substitution into the covariance formula gives

`C_X(z)`
`= (1/X)sum_(h>=1)(-(1+z))^h`
`  sum_(U<=X)`
`  R_h(floor(X/U);Y)`
`  [A^suf_(U,f)(z)-G_X(z)].`

The light cone makes the inner sum vanish unless

`U Y^h<X`.

At the critical cutoff, the hierarchy terminates at depth `K` up to the already declared high-arity repair layer.

This is an exact fixed-width/growing-depth propagation table. The sign comes from rough arity; the suffix innovation retains prime labels and local ordered-factor provenance.

Positive counts `R_h` alone are not cancellation. The alternating arity observer must remain attached until the final sum.

---

## 11. First dependence mode

At the full-support endpoint `z=-1`, `t=0`, so

`C_X(-1)=0`

for the actual-marginal reference `G_X`.

Differentiate with respect to `t=1+z` at `t=0`. Only the one-rough-prime layer survives:

`partial_t C_X |_(t=0)`
`= -(1/X)sum_(Y<p<=X) floor(X/p)`
`  [G_(floor(X/p))(-1)-G_X(-1)].`

Since

`G_U(-1)`
`= -sum_(q<=Y) f(q) floor(U/q)/U,`

this is equivalently the exact covariance

`partial_t C_X |_(t=0)`
`= (1/X)sum_(p>Y,q<=Y)`
`  f(q) floor(X/(pq))`
` - [(1/X)sum_(p>Y)floor(X/p)]`
`   [(1/X)sum_(q<=Y)f(q)floor(X/q)].`

Thus the first nontrivial rough/suffix coupling is not an abstract high-dimensional effect. It is the finite product-budget covariance between:

- one rough prime incidence;
- the weighted small-prime incidence source.

This is compatible with the independently obtained `critical rank = 1`, but it is not yet an estimate of that mode.

---

## 12. Endpoint certificates and their limit

Use

`f_Y(p)=sqrt(p)1_(p<=Y)`

and the critical cutoff `Y=(log X)^2`.

### `z=-1`

Only `a=1` survives in the Duhamel expansion. Hence

`F_X(-1)=G_X(-1)`

exactly. Relative to the independent Bernoulli suffix reference, the residual is only the elementary floor error

`O(Y^(3/2)/X)=X^(-1+o(1)).`

The discrete-versus-continuous prime intensity discrepancy remains in the common marginal.

### `z=0`

The global largest-prime observer is nonzero only on `Y`-smooth integers. Therefore

`|F_X(0)|<=sqrt(Y) Psi(X,Y)/X.`

At `Y=(log X)^2`, the Rankin bound from the parent frontier gives

`F_X(0)=X^(-1/2+o(1)).`

Also

`R_X(0)=Psi(X,Y)/X=X^(-1/2+o(1)).`

These endpoint controls are useful consistency checks.

But two small endpoints do not control the whole polynomial or its critical jets. A polynomial may vanish at selected points while remaining large elsewhere. No interpolation conclusion is permitted without a uniform norm and enough observer data.

Freeze:

`ENDPOINT_SMALLNESS != UNIFORM_CRITICAL_TRANSPORT`.

---

## 13. Triangular coefficient carrier

Expand around `t=1+z`:

`G_U(t-1)=sum_(j>=0) g_j(U)t^j,`

`Q_(X,Y;U)(t)=sum_(h>=0)q_(U,h)t^h.`

Here

`q_(U,h)`
`= (-1)^h #{a in I_U(X):P^-(a)>Y,omega(a)=h}.`

Then

`[t^m]F_X(t-1)`
`= sum_U (U/X)sum_(h=0)^m q_(U,h)g_(m-h)(U).`

Thus the exact machine-facing state is triangular:

`ROUGH_ARITY h`
` x RESIDUAL_QUOTIENT U`
` x SUFFIX_JET (m-h)`
` x PRIME_LABEL_PROVENANCE`.

This is the operation-safe repair of both lossy summaries identified previously:

- `h` alone loses residual product scale;
- `U` alone loses signed rough arity and branch provenance.

---

## 14. New no-go boundaries

The exact identities prove the following scope limits.

1. `ROUGH_ARITY_ONLY` is non-operation-safe because `G_(floor(X/a))` depends on the product scale of `a`, not only on `omega(a)`.
2. `QUOTIENT_ONLY` is non-operation-safe because the signed polynomial `Q_U(t)` is needed to recover parity and higher rough-depth observers.
3. Taking `sum_h |q_(U,h)|` replaces Möbius orientation by positive capacity and destroys the desired cancellation.
4. Replacing every suffix response by its independent mean solves internal small-prime dependence but leaves the one-point prime intensity discrepancy unchanged.
5. Endpoint identities do not bound intermediate coefficients or jets.
6. A fixed finite recurrence cannot retain the exact quotient carrier uniformly in `X`; the number of relevant floor cells grows on the square-root scale.
7. A generic Cauchy bound on the Abel form is too coarse: the trivial rough state `1` fills the late region. It must first be removed by covariance centering, as in Section 9.

---

## 15. Exact checker

Task-local checker:

`experiments/rh_rough_divisor_duhamel_check.py`.

It verifies with exact rational arithmetic:

- the global average/Duhamel identity;
- the rough-divisor/rough-phase polynomial identity;
- the `z=-1` and `z=0` endpoint laws;
- exact quotient-cell grouping;
- the rough-partial-sum convolution;
- the arbitrary-reference split;
- the Abel/innovation formula;
- the quotient-depth light cone.

The checker is a finite regression certificate, not asymptotic evidence and not an RH proof.

---

## 16. New smallest research unit

The previously schematic conditional defect now has two exact equivalent forms:

`C_*`
`= sum_U (U/X)Q_U(1+z)[G_U-G_*]`

and

`C_*`
`= (1/X)sum_(U<=X)`
`  M_rough(floor(X/U);1+z)`
`  [A^suf_U-G_*].`

For the actual-marginal reference, it further becomes

`C_X`
`= (1/X)sum_(U<=X/(Y+1))`
`  [M_rough(floor(X/U);1+z)-1]`
`  [A^suf_U-G_X].`

The representation and state-budget problems are now closed at the power scale. The remaining task is a signed correlation estimate.

The first admissible target is weaker than RH:

prove any fixed power saving for a smoothed or restricted version of the centered innovation pairing, uniformly over a nontrivial observer neighborhood, without:

- taking absolute values over rough arity;
- dropping the quotient variable `U`;
- replacing prime labels by an arity histogram;
- assuming square-root control of `theta(x)-x`;
- treating positive rough capacity as signed cancellation.

A plausible next route is to compare the discrete cumulative rough state with its Dickman/Buchstab carrier inside the Abel formula, leaving the exact difference as a source term, and then test whether the centered suffix innovation annihilates the rank-one Green charge. That annihilation must be proved, not inferred from mean zero.

No RH proof is claimed.
