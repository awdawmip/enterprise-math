# BRC Multiplier Basin — Round 2 Exact Laws

Status: `PROVED DERIVATIONS + EXECUTABLE GLOBAL_SUBTOOL / NO FOUNDATION PROMOTION`
Date: `2026-09-06`
Parent experiment: `research_notes/BRC_MULTIPLIER_BASIN_SCAN_20260906.md`
Parent evidence: `research_artifacts/brc_multiplier_scan_m1_100_k5_5000.csv`
Reuse resolution: `EXTEND_EXISTING_TOOL`
Tool classification: `GLOBAL_SUBTOOL` of `T0_BRC`

## 0. Scope and typing

This round closes the first proof targets from the multiplier scan. The canonical
square-root BRC collapse is unchanged:

`n -> floor(sqrt(n))^2`.

For multiplication by a positive integer `m`, retain the exact target state

`J_m(n) = floor(sqrt(mn))`,

`R_m(n) = mn - J_m(n)^2`.

The downward subtraction cost is `R_m(n)`. The counterfactual addition cost to
the next square is

`A_m(n) = (J_m(n)+1)^2 - mn`.

Boolean target support, unit-weight multiplicity, and source provenance remain
distinct observers. Positive Weighted-BRC is used only for multiplicity and is
not signed cancellation.

## 1. Point cost theorem

For every `m,n>=1`,

`R_m(n) + A_m(n) = 2 J_m(n) + 1`.

Thus the two edit costs are complementary coordinates in exactly one target BRC
basin. The total local edit budget is the target basin width.

This is exact and needs no asymptotics.

## 2. Square multiplier theorem — full range

Let the source basin be

`B_k={k^2,...,(k+1)^2-1}`

with size

`N=2k+1`.

Let the multiplier be `m=s^2`, `s>=1`.

### Theorem S1 — exact support cardinality

The number of occupied target BRC roots is

`H_{s^2}(k)=min(s,2k+1)`.

So the finite-window law from round 1 extends to all `k,s`.

### Dense regime: `s<=N`

Every target root

`sk, sk+1, ..., s(k+1)-1`

is occupied.

For `t=0,...,s`, define the exact source-offset threshold

`r_t = ceil((2 s k t + t^2)/s^2)`.

Then target root `sk+t` for `0<=t<s` receives exactly

`c_t = r_{t+1}-r_t`

source states.

Write

`N = q s + a`, `0<=a<s`.

Then

`c_t in {q,q+1}`

for every target, and exactly `a` targets have multiplicity `q+1`.

Equivalently, the square multiplier gives the most balanced possible partition
of the `N` source states into `s` nonempty target bins.

For unit branch weights the exact target CWM is

`CWM_t=(c_t,c_t,1)`.

#### Proof of balance

Since `2k=N-1=qs+a-1`,

`r_t = q t + ceil(B_t)`

with

`B_t = t(s(a-1)+t)/s^2`.

If `a=0`, then `B_t=t(t-s)/s^2` lies in `[-1/4,0]`, so every
`ceil(B_t)=0` and all counts equal `q`.

If `a>=1`, then

`0 < B_{t+1}-B_t = (s(a-1)+2t+1)/s^2 < 1`.

Therefore `ceil(B_{t+1})-ceil(B_t)` is always `0` or `1`. Also
`ceil(B_0)=0` and `ceil(B_s)=a`, hence exactly `a` of the `s` increments are
`1`. This proves the `{q,q+1}` law and the exact number of larger bins.

### Sparse regime: `s>N`

The `N` source states map injectively to `N` distinct target roots, so

`H_{s^2}(k)=N`.

Indeed, for two consecutive source integers in `B_k`,

`s(sqrt(n+1)-sqrt(n)) = s/(sqrt(n+1)+sqrt(n)) > 1`,

because `s>=2k+2` while the denominator is strictly below `2k+2`. Therefore
`floor(s sqrt(n))` strictly increases at every source step. Every occupied
Weighted-BRC target has multiplicity `1`; gaps are allowed.

### Structural interpretation

A square multiplier is a pure integer refinement. In the dense regime it
creates exactly `s` child roots and distributes source multiplicity as evenly as
integer arithmetic permits. Once the requested refinement `s` exceeds the
number `2k+1` of available source states, refinement saturates and becomes
injective.

## 3. Non-square stable support theorem

Let `m` be non-square and let

`a=floor(sqrt(m))`, `alpha=sqrt(m)=a+beta`, `0<beta<1`.

Assume the sufficient no-skip condition

`m <= 4 k^2`.

This condition is eventually automatic for every fixed `m`.

The real increment between adjacent multiplied square roots is

`sqrt(m(n+1))-sqrt(mn)=sqrt(m)/(sqrt(n+1)+sqrt(n)) < 1`

throughout `B_k`; hence occupied target roots are consecutive.

Put `q=k+1` and define

`A=floor(k sqrt(m))`,

`T=floor(q sqrt(m))`,

`D_m(q)=m q^2-T^2`.

Because `m` is non-square, `D_m(q)>0`.

### Theorem N1 — exact endpoint correction

The final target root of the multiplied source basin is

`T-1` if `D_m(q)<m`,

and `T` if `D_m(q)>=m`.

Therefore, with

`epsilon_m(q)=1[D_m(q)<m]`,

`Delta_m(k)=floor((k+1)sqrt(m))-floor(k sqrt(m))`,

we have the exact stable support law

`H_m(k)=Delta_m(k)+1-epsilon_m(k+1)`.

The Beatty increment satisfies

`Delta_m(k) in {a,a+1}`,

so

`H_m(k) in {a,a+1,a+2}`.

The rare lowest value `a` can occur only through the endpoint correction.

### Proof of the endpoint rule

Since

`m(q^2-1)=T^2 + D_m(q)-m`,

the endpoint lies below `T^2` exactly when `D_m(q)<m`. Under the no-skip
hypothesis the endpoint cannot fall more than one root below `T`, giving the
claimed two cases.

## 4. Pell resonance theorem — zero density

The endpoint event is

`0 < D_m(q) < m`.

For every such event,

`T^2-mq^2=-D`

for one integer `D` in `{1,...,m-1}`. Hence the exceptional endpoint set is a
finite union of generalized Pell solution sets.

### Theorem N2 — logarithmic exceptional count

For each fixed positive non-square `m`, let

`R_m(K)=#{q<=K : 0<D_m(q)<m}`.

Then

`R_m(K)=O_m(log K)`.

Consequently the endpoint-resonance set has natural density zero.

### Proof sketch

For each fixed `D`, consider the integer solutions of

`x^2-m y^2=-D`.

Choose one nontrivial positive Pell unit

`epsilon=u+v sqrt(m)>1`, `u^2-mv^2=1`.

Multiplication by powers of `epsilon` preserves the norm `-D` and integer
coefficients. Every positive solution can be multiplied by a suitable inverse
power so that its positive real embedding lies in `[1,epsilon)`. In that
bounded strip the conjugate is `-D/z`, so both integer coefficients are bounded;
there are only finitely many reduced representatives. Thus all solutions form
finitely many unit orbits. Along each orbit the positive embedding, hence the
`y` coordinate up to fixed constants, grows exponentially in the orbit index.
Only `O(log K)` members can have `y<=K`. Summing over the finite set
`1<=D<m` proves the claim.

This uses only the classical Pell existence theorem as an external arithmetic
input; the BRC consequence is the zero-density endpoint correction.

## 5. Exact asymptotic support frequencies for non-squares

No equidistribution theorem is needed for the main frequency law.

Because

`Delta_m(k)=a + (0 or 1)`,

the number of `a+1` Beatty increments up to height `K` is obtained by telescoping

`sum Delta_m(k)=floor((K+1)alpha)-floor(k0 alpha)`.

Hence the high-increment count is

`beta K + O_m(1)`

and the low-increment count is

`(1-beta)K + O_m(1)`.

The Pell endpoint correction changes only `O_m(log K)` cases. Therefore, for
fixed non-square `m`, after ignoring the finite unstable prefix,

`#{k<=K : H_m(k)=a} = O_m(log K)`,

`#{k<=K : H_m(k)=a+1} = (1-beta)K + O_m(log K)`,

`#{k<=K : H_m(k)=a+2} = beta K + O_m(log K)`.

In particular,

`mean_{k<=K} H_m(k) = sqrt(m)+1 + O_m(log K / K)`.

For square `m=s^2`, Theorem S1 gives eventually

`H_m(k)=s=sqrt(m)`.

So the multiplier-support observable has a genuine one-unit asymptotic split:

- square multiplier: mean support `sqrt(m)`;
- non-square multiplier: mean support `sqrt(m)+1`.

This is not a numerical artifact of the `m<=100` scan.

### Round-1 data versus the proved limits

The 4996-basin scan already shadows the theorem closely:

- `m=2`: predicted `(H=2,H=3)` frequencies about `(0.585786,0.414214)`; observed `(0.586469,0.413531)`;
- `m=3`: predicted `(0.267949,0.732051)`; observed `(0.269015,0.730985)`;
- `m=5`: predicted `(H=3,H=4)` about `(0.763932,0.236068)`; observed `(0.765813,0.234187)`;
- `m=26`: the proved zero-density `H=5` class appears once; the main `H=6,7` classes approach frequencies about `(0.900980,0.099020)`;
- `m=50`: the proved zero-density `H=7` class appears three times; the main `H=8,9` classes approach `(0.928932,0.071068)`.

## 6. Squarefree-kernel composition theorem

Write the multiplier canonically as

`m=a^2 d`

with squarefree `d`.

First apply only the squarefree core and retain its complete BRC state

`d n = y^2 + rho`, `0<=rho<=2y`.

Define the finite refinement phase

`u = floor(sqrt(a^2 d n)) - a y`.

Because

`y <= sqrt(dn) < y+1`,

we have

`0<=u<a`.

### Theorem C1 — exact composition law

The final multiplied BRC state is

`J_m(n)=a y+u`,

`R_m(n)=a^2 rho - 2 a y u - u^2`.

The addition cost is therefore

`A_m(n)=2(a y+u)+1-R_m(n)`.

Thus multiplication by `m=a^2 d` decomposes exactly into:

1. a squarefree-core BRC state `(y,rho)`;
2. a finite `a`-phase square refinement `u`.

The square factor contributes no new irrational direction; it refines the
squarefree-core state.

This turns the round-1 heuristic

`squarefree direction d + square refinement a`

into an exact composition statement.

### Observer-loss witness

The kernel root `y` alone does not determine `u`, because `u` depends on the
retained remainder `rho`. Therefore Boolean collapse to `y` is not sufficient
for exact later multiplication. The pair `(y,rho)` is sufficient.

This is a concrete instance of the BRC observer rule:

`ERASED_REMAINDER/PROVENANCE != RECOVERABLE_FROM_BOOLEAN_SUPPORT`.

## 7. Multiplicity/cost duality

Every source basin always contains `N=2k+1` source states, so for every exact
multiplier profile

`sum_j c_j=N`.

For square multipliers in the dense regime, support grows by exactly `s` while
mean target multiplicity is exactly `N/s`, up to the unavoidable integer
`q,q+1` split.

At the same time the target edit-budget width grows on the `s=sqrt(m)` scale.
Thus square multiplication exhibits an exact reciprocal pattern:

`support refinement scale ~ sqrt(m)`,

`mean multiplicity per occupied target ~ 1/sqrt(m)`,

`local add/sub budget scale ~ sqrt(m)`.

This is a BRC conservation statement about source branch count, not a physical
measure-preservation claim.

## 8. Toolization

This round promotes the surviving experiment into the executable subtool

`src/enterprise_math/brc_multiplier_basin.py`.

The tool exposes:

- exact point add/sub cost state;
- exact source-basin -> target multiplicity profile;
- full-range square multiplier law;
- stable non-square Beatty/Pell support law;
- endpoint-resonance defect;
- exact squarefree-kernel composition state.

Regression tests are in

`tests/test_brc_multiplier_basin.py`.

Method classification is persisted as `GLOBAL_SUBTOOL` under `T0_BRC`; this is
not a new top-level BRC family and does not mutate Foundation or theorem ledgers.

## 9. Next frontier

The strongest next question is no longer whether a pattern exists. It is whether
the exact phase data can be turned into useful arithmetic discrimination.

The next experimental unit should therefore compare, for composite/semiprime
inputs, the squarefree-core phase/remainder trajectory under candidate
multipliers against classical factor/valuation data. Required kill condition:
if the phase signature is completely determined by already-cheap classical
residue data and yields no compression or earlier witness, do not claim a
factorization speedup.
