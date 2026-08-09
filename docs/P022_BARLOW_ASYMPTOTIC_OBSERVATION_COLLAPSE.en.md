# P022 — Barlow Asymptotic Observation Collapse

Status: `ACTIVE RESEARCH NOTE / EXACT CONSEQUENCE OF PROVED P022 FORMULAS / NOVELTY_UNVERIFIED`  
Owner: `program/p022-geometry-v2`  
Depends on: periodic geodesic-growth theorem BG03 and coordination theorem BC06  
Purpose: show that the information order between observables can change when the future language itself changes from finite-radius exact values to asymptotic leading invariants

## 1. Finite-radius observables are incomparable

The Barlow observation-lattice note gave explicit finite counterexamples proving

\[
S_n\not\Rightarrow T_n,
\qquad
T_n\not\Rightarrow S_n,
\]

where

- `S_n` is shell vertex cardinality;
- `T_n` is total number of shortest paths into the shell.

Thus at a fixed finite radius these two observables are genuinely incomparable.

This note shows that the relationship changes after replacing the finite future language by an asymptotic leading-order language.

## 2. Periodic stacking has one absolute drift density

Let the stacking have period length `L` and signed period drift `D`.

Both positive and negative directions have the same asymptotic absolute drift density

\[
\boxed{
\mu=\frac{|D|}{L}\in[0,1].}
\]

Literal period order and finite phase remain relevant to exact finite shells, but they disappear from the two leading asymptotic observables below.

## 3. Coordination leading coefficient

BC06 gives

\[
\boxed{
C_S
:=\lim_{n\to\infty}\frac{S_n}{n^2}
=rac{21}{2}-\frac{\mu^2}{2}.}
\]

The map

\[
\mu\mapsto C_S
\]

is one-to-one on `[0,1]`. Its inverse is

\[
\boxed{
\mu=\sqrt{21-2C_S}.}
\]

The exact periodic integer representation is

\[
C_S=\frac{21L^2-D^2}{2L^2}.
\]

## 4. Geodesic-multiplicity growth exponent

BG03 gives

\[
\boxed{
\Lambda
:=\lim_{n\to\infty}T_n^{1/n}
=2+2^{(1+\mu)/2}.}
\]

This map is strictly increasing on `[0,1]`, hence also one-to-one.

The real inverse is

\[
\boxed{
\mu=2\log_2(\Lambda-2)-1.}
\]

For integer-first periodic state, no logarithm need be stored: `Lambda` is the positive real root greater than `2` of

\[
\boxed{
(\Lambda-2)^{2L}=2^{L+|D|}.}
\]

## 5. P022-AO01 — asymptotic equivalence of the two leading observables

Because both `C_S` and `Lambda` are bijective functions of the same `mu`,

\[
\boxed{
C_S
\longleftrightarrow
\mu
\longleftrightarrow
\Lambda.}
\]

Therefore, within the class of periodic Barlow stackings and for the declared **leading asymptotic language**,

\[
\boxed{
C_S\text{ and }\Lambda\text{ are information-equivalent}.}
\]

This does not contradict their finite-radius incomparability. The asymptotic projection has deliberately erased finite phase information from both observables, causing the two previously different shadows to collapse onto one latent coordinate.

## 6. Explicit tradeoff curve

Eliminate `mu` using

\[
\mu=\sqrt{21-2C_S}.
\]

Then the two leading invariants satisfy

\[
\boxed{
\Lambda
=2+2^{\left(1+\sqrt{21-2C_S}\right)/2}.}
\]

The allowed ranges are

\[
10\le C_S\le\frac{21}{2},
\]

and

\[
2+\sqrt2\le\Lambda\le4.
\]

As `mu` increases:

- `C_S` strictly decreases from `21/2` to `10`;
- `Lambda` strictly increases from `2+sqrt(2)` to `4`.

So periodic stacking drift creates an exact asymptotic tradeoff:

\[
\boxed{
\text{fewer coordination-shell vertices per }n^2
\quad\Longleftrightarrow\quad
\text{larger exponential shortest-path redundancy}.}
\]

This is a combinatorial statement, not a physical efficiency or stability claim.

## 7. Extremes

### Zero drift

\[
\mu=0.
\]

Then

\[
C_S=21/2,
\qquad
\Lambda=2+\sqrt2.
\]

HCP is one periodic representative, but every zero-drift periodic Barlow word has the same leading pair.

### Constant drift

\[
\mu=1.
\]

Then

\[
C_S=10,
\qquad
\Lambda=4.
\]

FCC is the canonical constant-drift representative.

## 8. P022-AO02 — aperiodic asymmetric drift breaks the equivalence again

For an arbitrary two-sided stacking with one-sided absolute drift limits

\[
\mu_+,
\qquad
\mu_-,
\]

coordination reads

\[
\boxed{
C_S
=\frac{21}{2}
-rac{\mu_+^2+\mu_-^2}{4},}
\]

while geodesic multiplicity reads

\[
\boxed{
\Lambda
=2+2^{(1+\max(\mu_+,\mu_-))/2}.}
\]

Neither observable determines the other on the full two-dimensional drift domain.

However the pair `(C_S,Lambda)` reconstructs the unordered drift magnitudes:

1. `C_S` gives
   \[
   R_2=\mu_+^2+\mu_-^2=42-4C_S;
   \]
2. `Lambda` gives
   \[
   M=\max(\mu_+,\mu_-);
   \]
3. the other magnitude is
   \[
   \sqrt{R_2-M^2}.
   \]

Thus

\[
\boxed{
(C_S,\Lambda)
\longleftrightarrow
\{\mu_+,\mu_-\}
}
\]

up to exchanging the two sides.

A one-sided observable is required to restore the orientation label.

## 9. Horizon-induced change in the observation poset

The same two named observable families exhibit three different information relationships depending on the declared domain/horizon:

### Finite radius

\[
S_n\quad\text{and}\quad T_n
\]

are incomparable.

### Periodic asymptotic leading language

The hidden drift vector is restricted to the diagonal

\[
(\mu,\mu),
\]

so the two observables become equivalent through the single coordinate `mu`.

### Aperiodic two-sided asymptotic language

The hidden state regains two coordinates

\[
(\mu_+,\mu_-),
\]

and the observables become different norms of that vector: an `L^2`-square statistic and an `L^infinity` statistic. They become jointly sufficient but individually insufficient.

Therefore

\[
\boxed{
\text{the observation-factorization order can itself change when the future horizon/domain is changed}.}
\]

This is a concrete P022 realization of a broader precision-mathematics principle: quotient sufficiency is always relative not only to **what** is observed, but also to **which future domain** the observation is required to cover.

## 10. Upstream ownership boundary

The abstract statement about observation factorization and horizon-restricted equivalence belongs to A2/P023/P024 if promoted.

P022 owns the exact Barlow specialization:

- finite counterexamples;
- coordination and geodesic formulas;
- drift reconstruction;
- the periodic diagonal-collapse phenomenon.

No new generic quotient ontology is introduced here.
