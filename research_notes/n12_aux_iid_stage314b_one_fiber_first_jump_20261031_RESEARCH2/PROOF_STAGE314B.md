# Stage314-B — exact first-order Pareto transition in the complete one-private-fiber parameter interval

**Scientific status:** `PORTABLE_AUTHOR_PROOF / EXACT_RATIONAL_AND_QUADRATIC_FIELD_EXECUTED / UNREVIEWED / NOT_ADMITTED`. This is an **exact global theorem inside a specified one-fiber family** (one free real parameter across its entire interval `[0,1]`), **not** an eight-parameter global-optimum or P000 native-X6 transfer theorem.

**Frozen source/read pins (2026-10-31 Asia/Shanghai):** `GLOBAL_KNOWLEDGE_V1 main@92d848163ce048addefac3d38c5a6cc77196c4e7`; Enterprise Math control `main@d23b2ca76ada54a5f8b38197a86e2ff45379f780`; research parent Stage313-B `1108f7eb1706d3f5daeef6bb3f78584d978a7657`, `research_notes/n12_aux_iid_stage313b_algebraic_branch_preemption_20261031_RESEARCH2/PROOF_STAGE313B.md`. Owner/claim authority is **not** inferred from GitHub publication. P000 remains `ACTIVE_LOCKED`; the exact source observer is an auxiliary finite positive-branch model.

## 1. Declared model and exact question

Let `S` be fair binary; conditional on `S`, let `J` correctly copy `S` with probability `7/8`, `W` correctly copy `S` with probability `3/4`, and `Y` be `Bernoulli(p_S)` with `p_0=1/4`, `p_1=3/4`, conditionally independent. Let private state `h=(J,W,Y)` have source masses `(a_h,b_h)/256`:

| `h` | 000 | 001 | 010 | 011 | 100 | 101 | 110 | 111 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `(a_h,b_h)` | (63,1) | (21,3) | (21,3) | (7,9) | (9,7) | (3,21) | (3,21) | (1,63) |

Future `F` uses the three-visit locked Bernoulli rate `t_h`, while `H` yields independent fair bits. Public observer is `(G=(W,Y), future trace)` and tagged observer is `(S,J,G,future trace)`; `P(t)` and `T(t)` are worst-case TV errors over adaptive `H/F` histories. Presampling all three future `F` bits and independent `H` coins shows every allowed adaptive transcript is a common stochastic postprocessing of all-`F` data; data processing gives the upper bound and all-`F` attains it.

At the unique source-tagged MAP vector `t_h^MAP=p_0` if `a_h>b_h` and `p_1` otherwise, exact 128-atom summation gives `P_0=11/256`, `T_0=77/1024`.

**Restricted family (`\mathcal C_{100}`):** all seven `h != 100` rates are fixed at MAP, and **the single rate** `t=t_100` varies over the **entire continuous interval `[0,1]`**. Define

```
V_100(epsilon) = min { T(t) : t in [0,1], P(t) <= P_0 - epsilon }.
q(u)= 9u/128 + 3u^2/32 - u^3/8,
g(u)= 117u/4096 - 123u^2/1024 + 23u^3/256.
```

This is an optimization over one parameter, **not** a finite grid. The full eight-rate frontier `F_P` satisfies `F_P(P_0-epsilon) <= V_100(epsilon)` but equality needs an independent eight-dimensional proof.

## 2. Theorem A — exact one-fiber envelope and discontinuous minimizer jump

Define the algebraic point and its exact risks

```
t_dagger = (7-sqrt(13))/8,
u_dagger = t_dagger - 1/4 = (5-sqrt(13))/8,
P_dagger = -1/32 + 9 sqrt(13)/512,
T_dagger = (319-sqrt(13))/4096,
E_dagger = P_0-P_dagger = 19/256 - 9 sqrt(13)/512.
```

Let `u_c` be the **unique** root in `(109/1000,11/100)` of

```
g(u_c) = T_dagger - T_0 = (11-sqrt(13))/4096,
```

and let `epsilon_c=q(u_c)`. Exact root bracketing gives

```
68928221/8000000000 < epsilon_c < 69619/8000000,
0.008616027625 < epsilon_c < 0.008702375,
E_dagger ≈ 0.0108399189859846  (decimal only).
```

**Then for every real `epsilon` in `[0,E_dagger]`:**

```
V_100(epsilon) = min { T_0+g(q^-1(epsilon)), T_dagger },         (1)
```

where `q^-1` denotes its increasing inverse on `[0,7/50]`. The complete set of optimal `t_100` values in this one-fiber family is

```
0 <= epsilon < epsilon_c : { 1/4 + q^-1(epsilon) }
epsilon = epsilon_c      : { 1/4 + u_c , t_dagger }
epsilon_c < epsilon <= E_dagger : { t_dagger }.
```

At `epsilon=0` the unique optimizer is MAP `t=1/4`. Thus **the optimizer jumps discontinuously at `epsilon_c`**, from a rate below `0.36` to the algebraic rate approximately `0.424306`, while the optimal **value** remains continuous. The bit-complementary family in which only `h=011` moves has the same theorem under `t -> 1-t`.

### Proof of Theorem A (the entire real interval)

Put `B_k(t)=t^k(1-t)^(3-k)` for the probability of one ordered three-bit word containing `k` ones (multiplicities `m=(1,3,3,1)`) and `A(t)=B_0(t)+3B_1(t)=1-3t^2+2t^3`. `A'(t)=-6t(1-t)<0` for `t in (0,1)`.

**Lemma 1 (rates below MAP cannot meet a positive improvement).** The only changing public fiber is `G=00`. Its compressed-minus-target ordered-word residuals at MAP are `(13,3,-3,-13)/1024`, and the change at rate `t` is `[B_k(t)-B_k(1/4)]/16`. For `t<1/4`, the signed mass of the `G=00` subevent `k<=1` becomes

```
R_0(t)+3R_1(t)
  = (13+3*3)/1024 + [A(t)-A(1/4)]/16
  > (13+3*3)/1024.
```

Since total variation dominates the signed difference of any event and the other public fibers are unchanged, `P(t)>P_0`. Thus `t<1/4` is infeasible for `epsilon>=0`.

**Lemma 2 (the first public sign chamber).** The four `G=00` residual polynomials, each multiplied by `512`, are

```
512 R_0(t) = -32t^3 + 96t^2 - 96t +25,
512 R_1(t) =  32t^3 - 64t^2 + 32t -3,
512 R_2(t) = -32t^3 + 32t^2 -3,
512 R_3(t) =  32t^3 -7.
```

The first sign change on `t>1/4` is `R_2=0` at the unique `t_2` satisfying

```
32 t_2^2 (1-t_2) = 3,
392/1000 < t_2 < 393/1000.
```

Indeed the left side strictly increases for `t in [1/4, 1/2]`, and rational endpoint substitutions give opposite signs. `R_0` changes only later at `t_0=1-14^(1/3)/4` in `(397/1000,398/1000)`; `R_1>0` and `R_3<0` through `t_dagger` (their original Bernoulli polynomial ordering and root brackets suffice). Hence on `[1/4,t_2]` all signs remain `(+,+,-,-)` and exactly

```
P(t) = P_0 - q(t-1/4).
```

Moreover `q'(u)=-3(4u-3)(4u+1)/128>0` for the needed `0<=u<=u_dagger`.

**Lemma 3 (tagged-risk shape up to the algebraic kink).** Set `D(p,t)=TV(Bern(p)^{\otimes 3}, Bern(t)^{\otimes 3})`. Only `h=100` changes, so

```
T(t)-T_0=[9D(1/4,t)+7D(3/4,t)-7D(1/4,3/4)]/256.
```

For `1/4<=t<=t_dagger`, `B_1(t)>=B_1(1/4)` and `B_0(t)<B_0(1/4)`, while `B_2,B_3` move upward, hence `D(1/4,t)=B_0(1/4)-B_0(t)`. Relative to `3/4`, `k=0,1` remain positive, so `D(3/4,t)=A(t)-A(3/4)`. Algebra yields

```
T(t)=T_0+g(t-1/4),
g'(u)=3(4u-3)(92u-13)/4096.
```

Therefore `g` increases strictly on `(0,13/92)`, then decreases strictly on `(13/92,u_dagger)`. Exact rational brackets prove `13/92 < t_2-1/4 < u_dagger`. Thus for every `t in [t_2,t_dagger]`, `T(t)>T_dagger` except equality at `t=t_dagger`.

**Lemma 4 (every rate beyond the kink is at least as costly as the kink).** For `t in [t_dagger,3/4]`, the event `k<=1` and its complement yield the exact lower bounds

```
D(1/4,t) >= A(1/4)-A(t),
D(3/4,t) >= A(t)-A(3/4).
```

At `t_dagger` both are equalities, because `B_1(t_dagger)=B_1(1/4)` and the remaining signs have their stated order. Hence

```
9D(1/4,t)+7D(3/4,t)
  >= 9A(1/4)-7A(3/4)-2A(t)
  >= 9A(1/4)-7A(3/4)-2A(t_dagger),
```

with strict inequality for `t>t_dagger` as `A` strictly decreases. For `t>=3/4`, monotone Bernoulli coupling gives `D(1/4,t)>=D(1/4,3/4)=11/16`, while `D(3/4,t)>=0`. Consequently

```
T(t)-T_0 >= 2*(11/16)/256 = 11/2048
                        > (11-sqrt(13))/4096 = T_dagger-T_0.
```

So `T(t)>T_dagger` for every `t>t_dagger`. This establishes a **full-domain** lower bound, not just local optimality.

**Lemma 5 (assemble the constrained minimum).** Exact quadratic-field comparison gives `E_dagger<q(7/50)`, with `7/50<13/92<t_2-1/4`, so each `epsilon in [0,E_dagger]` has one `u_epsilon=q^-1(epsilon)` in `[0,7/50)`. The dagger is feasible for all these requirements since `P(t_dagger)=P_0-E_dagger`.

For feasible `t in [1/4,t_2]`, Lemma 2 forces `u=t-1/4>=u_epsilon`. Since `g` is strictly unimodal on `[u_epsilon,t_2-1/4]`, its minimum is at an endpoint. The upper endpoint has strictly larger cost than `g(u_dagger)=T_dagger-T_0` by Lemma 3; Lemmas 3–4 rule out every `t>t_2` as an improvement over the dagger. Lemma 1 rules out `t<1/4`. Therefore the global minimum **over all `t in [0,1]`** equals the minimum of exactly the two displayed candidates, proving (1) and excluding any missing third optimizer.

Finally `g` is strictly increasing on `[0,7/50]`. Direct exact arithmetic in `Q(sqrt(13))` gives

```
g(109/1000) < (11-sqrt(13))/4096 < g(11/100),
q(11/100) < E_dagger,
```

so exactly one `u_c` and thus one `epsilon_c` exist in the stated brackets. Cost ordering and the strict uniqueness analysis yield the three minimizer cases. At `epsilon=0`, the weighted TV triangle inequality gives `9D(1/4,t)+7D(3/4,t)>=7D(1/4,3/4)+2D(1/4,t)`, which is strict except at `t=1/4`. QED.

## 3. Theorem B — three distinct transition phenomena must not be conflated

Along the increasing small-`u` MAP branch, the **first public observation sign flip** occurs at `t_2` above, hence at `u_2=t_2-1/4 in (0.142,0.143)`. The **source-tagged cost maximum** occurs earlier, exactly at `u_m=13/92≈0.14130435`. The **full one-fiber Pareto optimizer jump**, however, occurs substantially earlier, at `u_c in (0.109,0.110)` and `epsilon_c in (0.008616,0.008703)`.

Therefore the optimizer jump happens while the departing small-`u` branch **still lies strictly in its original public sign chamber** and before the tagged-cost turning point. The mechanism is competition with a distant feasible algebraic rate at a different observation chamber, not the departing branch's first local sign flip. The three events have exact, different algebraic certificates.

This theorem is about the restricted complete one-fiber family. For the **full eight-rate cube**, Stage312-B independently proves the polynomial frontier through `18117/4000000`, and Stage313-B plus the present one-fiber theorem supplies the competing upper envelope and formula failure strictly after `epsilon_c`. Their combination **does not establish the first eight-rate transition at `epsilon_c`**; an earlier multi-fiber competitor is not excluded.

## 4. Evidence, source separation, and scope

- Reproduction: `REPRO_STAGE314B.py` executed with Python `Fraction`, an exact `Q(sqrt(13))` class, and SymPy exact polynomial identities. It literally enumerates `128` positive `(S,h,ordered three-bit)` atoms for `10` rational test rates, and the algebraic dagger rate; it checks MAP masses, closed forms, strict brackets, derivative polynomial identities and source/public TV values. Captured output: `REPRO_STAGE314B_EXECUTED_STDOUT.txt`, status `STAGE314B_ONE_FIBER_FIRST_ORDER_TRANSITION_EXACT_PASS`.
- Universal quantification and complete elimination of `t in [0,1]` use the five analytic lemmas, **not** the ten-sample computation. No floating-point search is cited as a proof and no Lean check or independent Driver review is claimed.
- Existing Stage313-B exact algebraic construction and Stage312-B full-eight local theorem are reused at their exact statements; no previously frozen Source result is overwritten.
- BRC reuse: `(S,h)` positive branch masses, explicit future F/H operations, `G` versus `(S,J,G)` observers, preserved source provenance, and *word-resolved signed residual* are kept distinct. This proves an observer-and-horizon-typed compression frontier; it does not erase the source joint relation or infer that signed TV residuals are positive masses.
- Native P000-X6 requires a separately proved typed embedding of paths, triadic closure, six-axis spatial Cell relations, time evolution and future-observer structure. The auxiliary Bernoulli parameter is not a new native axis, physical coordinate, physical theory, or Foundation claim.

**Next Stage315-B:** determine whether the **full eight-real-rate** frontier first leaves the local polynomial at `epsilon_c`, or construct a *rigorous earlier* two-/multi-fiber competitor in `(18117/4000000,epsilon_c)`. A certified interval/exact semialgebraic exclusion by observer sign chambers is needed; numerical SLSQP exploration is discovery only. Separately study the one-fiber frontier for `epsilon>E_dagger`, where the dagger rate becomes infeasible, without conflating this with the first full-cube transition.
