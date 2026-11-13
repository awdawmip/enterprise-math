# Stage313-B — an exact algebraic preemption of the local eight-rate Pareto polynomial

**Scope and status:** Enterprise Math Researcher2, independent **portable author proof / exact rational and quadratic-field execution / UNREVIEWED / NOT_ADMITTED**. No claim of native owner, CLAIM, Result, Driver review, first global active-set transition, external physical universality, or native P000-X6 dynamical transfer.

**Frozen inputs of this run:** GLOBAL_KNOWLEDGE_V1 `awdawmip/chatgpt-global-knowledge main@ffc97b2fc5890fa54226ae4b464d5db401a87470`; Enterprise Math current control `main@673a838d7baa33e7427e98aa5b06381a2ada81d4`; Stage312-B immutable research head `2b33ac263fe327436da5a5bbf982deef89ba65ce`, `PROOF_STAGE312B.md`, blob `40c8335a5bd45ec8ff43c8f6ed9179970df1a955`. The date is 2026-10-31 Asia/Shanghai.

## Model and frozen observer pair

As Stage312-B, fair hidden `S in {0,1}` with `p0=1/4`, `p1=3/4`. Conditional on S, J has correctness 7/8, W has correctness 3/4, and Y ~ Bernoulli(p_S), mutually independent. The eight private histories `h=(J,W,Y)` have exact joint source masses `(a_h,b_h)/256`:

```
h        000    001    010    011    100    101    110    111
(a,b)   (63,1) (21,3) (21,3) (7,9)  (9,7) (3,21) (3,21) (1,63)
```

The compressed process uses a locked `t_h in [0,1]` for all three future F visits; H gives an independent fair bit. Public observation is `(G=(W,Y), future trace)`; tagged observation is `(S,J,G,future trace)`. The three F bits can be presampled and all other adaptive policies are a common stochastic postprocessing; hence all-F maximizes both public and tagged total variation. Define their worst risks `P(t)`, `T(t)`, and the eight-real-cube envelope `F_P(v)=min{T(t):P(t)<=v}`. At the unique tagged MAP vector `t^0_h=p0 if a_h>b_h else p1`, the exact baselines are `P0=11/256` and `T0=77/1024`.

We study **only** the one-fiber family `t_100=p0+u`, other seven rates MAP. The previous Stage312 theorem proves the *full-cube* frontier for `0<=epsilon<=18117/4000000`:

`F_P(P0-epsilon)=T0+g(q^{-1}(epsilon))`, where

```
q(u) = 9u/128 + 3u^2/32 - u^3/8,
g(u) = 117u/4096 - 123u^2/1024 + 23u^3/256.
```

Stage313 does **not** revise that earlier theorem. It proves that this polynomial branch **cannot remain the global frontier** on a later explicit interval.

## Theorem A — exact quadratic-field preemption and a first-break upper bound

Let

```
t_dag = (7-sqrt(13))/8,
u_dag = t_dag - 1/4 = (5-sqrt(13))/8,
P_dag = -1/32 + 9 sqrt(13)/512,
T_dag = (319-sqrt(13))/4096,
E_dag = P0-P_dag = 19/256 - 9 sqrt(13)/512.
```

These are **exact** values of `P,T` for the eight-rate vector with only `t_100=t_dag`. Numerically `u_dag≈0.17430609`, `E_dag≈0.010839919`, `T_dag≈0.077000598` (decimal indications, not proof inputs).

Let `u_c` be the unique root in the rational interval `(109/1000,11/100)` of

```
g(u_c) = T_dag-T0 = (11-sqrt(13))/4096,
```

and set `epsilon_c=q(u_c)`. Then

```
q(109/1000) < epsilon_c < q(11/100),
0.008616027625 < epsilon_c < 0.008702375.
```

For **every real** `epsilon` satisfying

```
           epsilon_c < epsilon <= q(3/25) = 0.0095715
```

the whole-cube Pareto value obeys the *strict* inequality

```
 F_P(P0-epsilon) <= T_dag < T0+g(q^{-1}(epsilon)).   (A)
```

Consequently, the Stage312 full-cube polynomial and two-minimizer formula has a genuine nonextendability obstruction by `epsilon_c`; the earliest failure of that specific formula, if defined, occurs **no later than** `epsilon_c`. This theorem does *not* identify the first change in the number or identity of active fibers, nor exclude an earlier competing eight-rate family.

### Proof of the exact algebraic witness

For an ordered three-bit word having `k` ones write `B_k(t)=t^k(1-t)^(3-k)`, with multiplicities `(1,3,3,1)`. Put `A(t)=B_0(t)+3B_1(t)=1-3t^2+2t^3`. The algebraic identity

```
B_1(t)-B_1(1/4) = (4t-1)(16t^2-28t+9)/64
```

has, after the root `t=1/4`, the first interior zero `t_dag=(7-sqrt(13))/8`. On `1/4<=t<=t_dag`, `B_1(t)>=B_1(1/4)`, while the ordered-word probabilities for k=2,3 increase and k=0 decreases. Thus

```
D_3(p0,t)=B_0(p0)-B_0(t).
```

At `t_dag`, the B1 difference vanishes, so also `D_3(p0,t_dag)=A(p0)-A(t_dag)=:d`. For `1/4<=t<=t_dag`, `D_3(p1,t)=A(t)-A(p1)`; hence its displacement from `t=p0` is `-d` at the dagger point. The 100 fiber carries source masses `(9,7)/256`, so

```
T(t_dag)-T0 = [9d-7d]/256=d/128.
```

Direct polynomial reduction in `Q[sqrt(13)]` gives `d=(11-sqrt(13))/32` and therefore `T(t_dag)=(319-sqrt(13))/4096`.

For the public risk, the MAP compressed-minus-target residuals of the outer public fiber `G=00`, one for each ordered word with k ones, are `(13,3,-3,-13)/1024`. Changing only `t_100` adds `[B_k(t_dag)-B_k(p0)]/16`. Substitution gives

```
k       0                     1           2                      3
R_k  (-9+2sqrt13)/1024      3/1024   (-21+6sqrt13)/1024  (63-20sqrt13)/1024
sign      -                    +           +                      -
```

The signs follow from comparing nonnegative rational squares with 13; no floating-point classification is needed. `G=11` keeps its untouched MAP residuals, and `G=01,10` retain zero residual. Summing one-half of weighted absolute residuals with word multiplicities gives

```
P(t_dag)=-1/32+9sqrt(13)/512.
```

That establishes both exact witness identities.

### Proof of interval preemption

For every `u in [0,3/25]`, the four MAP residual signs in the affected public fiber are unchanged (directly from `B_k(1/4+u)` and their monotonicity on `[1/4,37/100]`; the critical k=0,2 margins are positive at `u=3/25`). The source-tagged sign arrangement also stays as above. Therefore the one-fiber vector has **exactly**

```
P=P0-q(u),       T=T0+g(u)              (0<=u<=3/25).
```

Both `q` and `g` are strictly increasing on `[0,3/25]`: `q'(0)>0`, `q''>=39/400>0`; `g''<0` and `g'(3/25)>=9261/2560000>0`. Exact comparisons in `Q[sqrt(13)]` yield

```
g(109/1000) < (11-sqrt(13))/4096 < g(11/100),
E_dag > q(3/25)=95715/10000000.
```

The intermediate-value theorem supplies the unique `u_c` and the displayed rational epsilon bracket. For any epsilon in the theorem's interval, choose the unique `u=q^{-1}(epsilon) in (u_c,3/25]`. Its small-branch tagged cost is strictly above `T_dag`, while the dagger vector has public improvement `E_dag > epsilon` and is feasible. Hence the global minimum is at most its tagged cost. This proves (A). QED.

## Theorem B — completely rational strict dominance certificate

Set two eight-rate vectors with seven MAP entries:

```
t_small,100 = 1/4+11/100 = 9/25,
t_large,100 = 1/4+87/500 = 53/125.
```

Exact 128-atom enumeration gives

```
P_small=274131/8000000,   T_small=19712913/256000000,
P_large=256961/8000000,   T_large=2464069069/32000000000.
```

Both comparisons are strict and rational:

```
P_small-P_large = 1717/800000 > 0,
T_small-T_large = 11/7812500 > 0.
```

Thus a single-fiber parameter farther from MAP can **simultaneously improve both observation errors** compared with the small-u polynomial candidate. The small branch cannot be globally Pareto-optimal at the exact public requirement `epsilon=q(11/100)=69619/8000000`. The algebraic dagger witness strengthens this rational point to an interval and exact early upper bound.

## Evidence, limits, and reusable meaning

`REPRO_STAGE313B.py` executed on Python's standard-library `Fraction` and a minimal exact `Q(sqrt(13))` quadratic-field class. It directly enumerates **128 positive source/private-history/ordered-3-bit atoms**, recomputes both TV risks for MAP, two rational candidates and the algebraic dagger point, checks all stated strict inequalities, and asserts `B_1(t_dag)=B_1(1/4)`. Output is captured verbatim as `REPRO_STAGE313B_EXECUTED_STDOUT.txt` with `STAGE313B_ALGEBRAIC_BRANCH_PREEMPTION_EXACT_PASS`. Code checks exact finite identities, while the quantification over an interval in Theorem A uses the analytic monotonicity proof. No Lean/formal verification or independent Driver review was performed.

BRC reusable contribution: keep the positive rational `(S,h)` mass carrier, the distinct public versus `(S,J)`-tagged observers, and the **word-resolved sign chamber** of the total-variation projection. The kink is a concrete example of **observer-chamber rearrangement without a required change of active private fiber**. Conflating scalar output gains with joint-source preservation would miss the preemption mechanism. `BRC REUSE_APPLIED`, not novel foundation admission.

Native X6 note: the probability carrier is an auxiliary restricted observer, not a seven-dimensional native physical world or an alternate Cell address. A proof of P000 native six-axis path/triad/time/Cell-address embedding with future-observer preservation remains a separate obligation.

## Smallest next question — Stage314-B

Determine the **first global failure threshold** `epsilon_first` of the Stage312 formula over the complete eight-real-rate cube. The above certificate gives `18117/4000000 < epsilon_first <= epsilon_c` *only if the Stage312 theorem covers the left endpoint and the usual infimum is used* (it does); investigate whether a two-fiber or heavy-fiber competitor intervenes before the one-fiber dagger preemption. Classify active-set changes separately from the first change of algebraic sign chamber or optimizer parameter. Use exact piecewise TV polynomials with rational/Sturm or interval exclusion; numerical scans are discovery only. Preserve declared public/tagged observers, P000 transfer obligation and independent review boundaries.
