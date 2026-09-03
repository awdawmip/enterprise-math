# Free Research #1161 — Gauss–Legendre AGM as rotation/chord renormalization

Status: `FREE_RESEARCH_RESULT / DERIVED_EXACT_RECONSTRUCTION + NATIVE-LIFT OBSTRUCTION / NOT WORKING_TRUTH / NOT FOUNDATION`
Date: `2026-09-03`
Researcher: `EM-FREE-G61R8`
Issue: `#1161`

## 0. Scope and strongest current verdict

The Gauss–Legendre update can be reconstructed exactly, without elliptic integrals or a prior value of pi, as a finite-per-step Pythagorean-cone renormalization with a provenance-preserving binary multiplicity channel.

The strongest current classification is deliberately split:

1. `EXACT_DERIVED_RECONSTRUCTION = YES`;
2. `FINITE_PER_STEP_INTEGER/ALGEBRAIC_CERTIFICATE = YES`;
3. `FIXED_FINITE_STATE_SPACE_REALIZATION = NO`;
4. `PURE_CURRENT_BOOLEAN/N/RATIONAL_PATH_CARRIER_REALIZATION = NO`;
5. `CURRENT_N0_SINGLE-CELL_OR_INTEGER-ENDPOINT_REALIZATION = NO`;
6. `FULL_NATIVE_LIFT = OPEN`, requiring an N0-definable positive algebraic root/Pythagorean-complement carrier or an equivalent exact relational construction.

The identification of the endogenous limit below with classical pi remains `ANALYTIC_COMPLETION`, not a native premise or native derivation.

## 1. Exact cone state

Start from the standard Gauss–Legendre state

\[
a_0=1,\qquad b_0=2^{-1/2},\qquad t_0=\frac14,\qquad p_0=1,
\]

with

\[
a_{n+1}=\frac{a_n+b_n}{2},\qquad
b_{n+1}=\sqrt{a_nb_n},
\]

\[
t_{n+1}=t_n-p_n(a_n-a_{n+1})^2,\qquad
p_{n+1}=2p_n.
\]

Define the derived finite state coordinates

\[
H_n=a_n+b_n,\qquad U_n=a_n-b_n,\qquad V_n=2\sqrt{a_nb_n},
\]

\[
A_n=4t_n,\qquad P_n=p_n.
\]

Then identically

\[
\boxed{H_n^2=U_n^2+V_n^2}.
\]

The pair is recovered from the cone state by

\[
a_n=\frac{H_n+U_n}{2},\qquad b_n=\frac{H_n-U_n}{2}.
\]

The exact update becomes

\[
\boxed{
H_{n+1}=\frac{H_n+V_n}{2},\quad
U_{n+1}=\frac{H_n-V_n}{2},\quad
V_{n+1}=\sqrt{H_nV_n}
}
\]

and

\[
\boxed{A_{n+1}=A_n-P_nU_n^2,\qquad P_{n+1}=2P_n.}
\]

Hence the arithmetic/geometric pair update has the compact geometric meaning

\[
\boxed{(a_{n+1},b_{n+1})=(H_n/2,V_n/2)}.
\]

The arithmetic mean is half the current cone hypotenuse coordinate; the geometric mean is half its complementary Pythagorean leg.

The cone constraint is preserved because

\[
H_{n+1}^2-U_{n+1}^2=H_nV_n=V_{n+1}^2.
\]

Thus the finite algebraic invariant of the dual mean channel is the null/cone relation

\[
\boxed{Q(H,U,V)=H^2-U^2-V^2=0.}
\]

This is a derived scalar/cone statement. It is not a claim that the displayed sum/difference transform is already an N0 carrier rotation.

## 2. Shape/scale factorization and chord-loss coordinate

Normalize

\[
r_n=V_n/H_n,\qquad s_n=U_n/H_n.
\]

Then

\[
r_n^2+s_n^2=1,
\]

and the shape evolution is autonomous:

\[
\boxed{
s_{n+1}=\frac{1-r_n}{1+r_n}
       =\frac{s_n^2}{(1+r_n)^2}
}.
\]

Consequently

\[
\frac{s_n^2}{4}\le s_{n+1}\le s_n^2,
\]

with strict inequalities away from the fixed axis. The RG exponent is therefore exactly quadratic, with asymptotic coefficient `1/4`.

For the standard initialization,

\[
\boxed{s_0=3-2\sqrt2=(\sqrt2-1)^2},
\]

so a fully explicit no-pi contraction bound is

\[
\boxed{s_n\le (3-2\sqrt2)^{2^n}}.
\]

Define the algebraic chord-square readout

\[
\chi_n^2=2(1-r_n).
\]

No classical circle is required for this definition. If a classical unit-circle completion is later chosen, this equals the usual squared chord associated with the normalized angle.

The same quantity controls both scale loss and the next shape defect:

\[
\boxed{
H_{n+1}=H_n\left(1-\frac{\chi_n^2}{4}\right),
\qquad
s_{n+1}=\frac{\chi_n^2}{4-\chi_n^2}.
}
\]

Equivalently, with

\[
\ell_n=\chi_n^2/4=(H_n-V_n)/(2H_n),
\]

one has the especially simple projective form

\[
\boxed{H_{n+1}=H_n(1-\ell_n),\qquad s_{n+1}=\ell_n/(1-\ell_n).}
\]

This is the current strongest exact sense in which the algorithm is a chord-loss renormalization.

## 3. Defect mass, exact scaling, and budget conservation

Define the retired defect mass

\[
\delta_n=P_nU_n^2.
\]

The budget channel is

\[
A_{n+1}=A_n-\delta_n.
\]

Using the cone update,

\[
\boxed{
\frac{\delta_{n+1}}{\delta_n}=\frac{s_{n+1}}2.
}
\]

Hence the apparent exponential growth `P_n=2^n` is dominated by the quadratic collapse of the local shape defect.

If

\[
\Sigma_n=\sum_{k=0}^{n-1}\delta_k,
\]

then the full GL budget has the exact finite conservation law

\[
\boxed{A_n+\Sigma_n=1.}
\]

Thus there are two distinct invariants:

- dual mean/cone invariant: `H^2-U^2-V^2=0`;
- full budget invariant after adding retired defect provenance: `A+Sigma=1`.

Because `0<s_{n+1}<1`,

\[
\delta_{n+1}<\frac12\delta_n.
\]

Therefore

\[
\boxed{0<A_n-A_\infty<2\delta_n.}
\]

A sharper local finite certificate follows because subsequent `s_k` decrease:

\[
\boxed{
A_n-A_\infty
\le
\widehat E_n
:=\frac{\delta_n}{1-s_{n+1}/2}.
}
\]

At initialization

\[
\delta_0=(1-2^{-1/2})^2=\frac{3-2\sqrt2}{2},
\]

so

\[
A_\infty>1-2\delta_0=2\sqrt2-2>0.
\]

No target constant is needed to prove positivity of the limiting denominator.

## 4. Endogenous precision-pi readout

The standard AGM inequalities give

\[
b_n<b_{n+1}<a_{n+1}<a_n
\]

for every finite `n`, so both sequences converge to a common positive limit `M`.

Set

\[
H_\infty=2M,
\qquad
\boxed{\Pi_*:=H_\infty^2/A_\infty}.
\]

`Pi_*` is defined only from the finite recursion and its monotone limits. No circumference, elliptic integral, or prior numerical value of pi is used in this definition.

The standard Gauss–Legendre readout is

\[
R_n=H_n^2/A_n.
\]

For this initialization it is strictly increasing. Indeed, writing `r=r_n`,

\[
A_nH_{n+1}^2-A_{n+1}H_n^2
=
H_n^2(1-r)
\left[
P_nH_n^2(1+r)-\frac{A_n(3+r)}4
\right].
\]

Here `P_n>=1`, `H_n^2>=2`, and `0<A_n<=1`, so the bracket is positive. Therefore

\[
\boxed{R_n<R_{n+1}<\Pi_*}.
\]

For a certificate not even requiring this monotonicity theorem in its lower endpoint, observe

\[
V_n=2b_{n+1}\le H_\infty\le H_n,
\]

and

\[
A_n-2\delta_n\le A_\infty\le A_n.
\]

Thus the entirely finite bracket

\[
\boxed{
\frac{V_n^2}{A_n}
\le
\Pi_*
\le
\frac{H_n^2}{A_n-2\delta_n}
}
\]

is valid whenever the quantities are represented exactly or by outward rational intervals.

The sharper upper endpoint may replace `2 delta_n` by `widehat E_n`.

## 5. Integer/dyadic certificate experiment

Committed checker:

`scripts/check_free_research_1161_agm_dyadic_certificate.py`

Initial checker commit:

`1b9d16f8446f573611b604c3350c23c38a5aa91f`

The checker uses only Python standard-library `Fraction` and integer `isqrt`.
For a positive rational `q` and dyadic precision `m`, it encloses `sqrt(q)` by computing the integer floor square root of the rational radicand scaled by `2^(2m)`. All subsequent arithmetic is outward rational interval arithmetic.

It never evaluates pi and never invokes floating-point square root.

At 300 dyadic bits, the exact rational certificate produces these common decimal cells for the endogenous `Pi_*` bracket:

| AGM step `n` | certified decimal places | common cell prefix |
|---:|---:|---|
| 1 | 2 | `3.14` |
| 2 | 7 | `3.1415926` |
| 3 | 18 | `3.141592653589793238` |
| 4 | 39 | `3.141592653589793238462643383279502884197` |

These are certificates for `Pi_*` as defined above, not an assumption that `Pi_*` equals classical pi.

The precision readout can be typed without logarithms. For a rational/algebraic bracket `[L,U]` and radix `B`, define

\[
\operatorname{Prec}_B([L,U])
=
\max\{m\in\mathbb N_0:\lfloor B^mL\rfloor=\lfloor B^mU\rfloor\}.
\]

Carrying the running intersection of successive valid brackets makes this a monotone integer precision state.

## 6. Fixed-finite-state no-go

If `finite state` means a fixed finite set `S` of possible exact states with a deterministic update `F:S->S`, exact infinite AGM reproduction is impossible.

Every deterministic orbit in a finite set is eventually periodic. But for `a_n>b_n>0`, strict AM–GM gives

\[
b_n<b_{n+1}<a_{n+1}<a_n,
\]

and equality cannot occur at any finite step unless it already held one step earlier. Starting from `1 != 1/sqrt(2)`, every exact pair `(a_n,b_n)` is therefore distinct.

Hence

\[
\boxed{FIXED_FINITE_CARDINALITY_EXACT_AGM_STATE=IMPOSSIBLE.}
\]

The viable interpretation of `finite native state` must be `finite encoding at each finite precision/time`, not a fixed finite automaton.

## 7. Pure rational path-carrier obstruction

On the currently frozen path side, Boolean support, natural path multiplicity, positive rational branch weights/histograms, rational arithmetic, and operation-safe quotienting do not by themselves create an irrational scalar.

An operation-safe quotient can descend an already-defined operation/observation; it cannot synthesize a missing positive-square-root operation from a carrier that has no such datum.

Already at initialization,

\[
b_0=1/\sqrt2\notin\mathbb Q.
\]

Therefore any construction whose scalar readout is restricted to rational expressions of the current Boolean/N/rational path data cannot exactly reproduce the AGM orbit.

The existing path-valued square-root operator does not close this gap: its frozen completeness scope is square native norms `r^2` with integer component-root fibers, not arbitrary positive algebraic products `a_nb_n`.

This yields the restricted no-go:

\[
\boxed{
CURRENT\_BOOLEAN/N/RATIONAL\_PATH\_CARRIER
\;\not\Rightarrow\;
EXACT\_AGM\_MEAN\_CHANNEL.
}
\]

This is not a ban on roots. It identifies the exact missing capability.

## 8. Finite exact algebraic tower

Although a pure rational carrier fails, every finite AGM stage has a finite exact algebraic presentation.

Let

\[
K_0=\mathbb Q(\sqrt2),
\qquad a_0=1,\quad b_0=1/\sqrt2,\quad A_0=1.
\]

Given `K_n` containing `a_n,b_n,A_n`, adjoin one distinguished positive root

\[
\beta_{n+1}^2=a_nb_n,
\qquad \beta_{n+1}>0,
\]

and set

\[
K_{n+1}=K_n(\beta_{n+1}),
\]

\[
a_{n+1}=(a_n+b_n)/2,
\qquad b_{n+1}=\beta_{n+1},
\]

\[
A_{n+1}=A_n-2^n(a_n-b_n)^2.
\]

Each extension has degree at most two, hence

\[
\boxed{[K_n:\mathbb Q]\le 2^{n+1}.}
\]

A stage can therefore be encoded by a finite tower of integer polynomial relations plus rational isolating data selecting the positive real root. This is an exact, finite, discrete/computable presentation at every finite stage.

The tower is a derived algebraic implementation, not yet an N0-native promotion. It does, however, prove that elliptic integrals and classical circumference are unnecessary for the exact recursion itself.

## 9. Native binary multiplicity source for `P_n=2^n`

The frozen native line/multipath theory already contains the local `(1,1)` commuting diamond with exactly two distinct typed path witnesses

`X_i X_j` and `X_j X_i`.

If each RG time step appends one independently provenance-tagged diamond block and block boundaries are retained, then the Path-formal/N-BRC product has exactly

\[
\boxed{2^n=P_n}
\]

path histories after `n` blocks.

This is not true after premature flattening. If the `n` block boundaries are erased and the whole word is replaced by the complete trace fiber `T_{n,n}`, the multiplicity is

\[
\binom{2n}{n},
\]

not `2^n` for `n>=2`.

Therefore

\[
\boxed{P_n\text{ requires temporal/block provenance before recoalescence}.}
\]

This is a genuine native/discrete contribution to the Gauss–Legendre state rather than a manually inserted doubling counter.

## 10. Current hybrid exact state

The strongest presently justified state is a typed product

\[
\mathfrak S_n
=
(\mathcal D^{\otimes n}_{\rm tagged},\;K_n;\;a_n,b_n,A_n),
\]

where

- `D_tagged^tensor n` is the native provenance-preserving sequence of commuting diamond blocks;
- its N-BRC multiplicity readout is `P_n=2^n`;
- `K_n` is the finite positive algebraic tower carrying the exact mean state;
- `A_n` is the conserved-budget remainder.

One update performs exactly two typed refinements:

1. append one binary diamond, giving `P -> 2P`;
2. append one positive quadratic relation `beta^2=ab`, giving the geometric channel, while the arithmetic channel uses only rational linear combination.

The coupling subtracts the total defect mass `P U^2` from `A`.

This reproduces the full Gauss–Legendre recursion exactly without importing the target pi value.

Its semantic status is `CONDITIONAL_DERIVED / EXACT_ALGEBRAIC_IMPLEMENTATION`, not `NATIVE_ADMISSIBLE` under the current N0 substrate.

## 11. Native-lift frontier

The remaining hard question is now sharply localized.

A full native lift would need to show that the positive quadratic-complement relation used above is definable from the current N0 cell/path substrate, choice-independent, and equivariant under the relevant native relabelings.

Current quotient machinery cannot solve that by itself because quotienting only forgets/descends existing information.

The current fork is therefore:

- `LIFT`: derive the algebraic positive-root/Pythagorean-complement witness from a richer finite native multipath relation;
- `NO-GO`: prove two N0 states with the same current path/branch observables but incompatible required algebraic-root readouts, forcing an extra primitive/decoration.

Either outcome would close the remaining native-status ambiguity of #1161.

## 12. Prior-art calibration

The standard AGM recursion and its quadratic convergence are classical and are not claimed as historical novelty here. DLMF §19.8 records the arithmetic/geometric iteration, the quadratic defect relation, and then connects AGM to complete elliptic integrals.

Accordingly, this research claims only the Enterprise-Math-specific decomposition/type result:

`Pythagorean cone + algebraic chord-loss RG + provenance-derived 2^n multiplicity + finite rational certificate + native-lift obstruction`.

The later identity `Pi_*=classical pi` remains outside the native derivation until an admissible bridge is supplied.
