# R1/N14 — Uniform two-law LR-fiber oscillation bound under P-strong lumpability

**Date:** 2026-10-27. **Status:** AUTHOR-LEVEL MATHEMATICAL DERIVATION + EXACT EXECUTED RATIONAL EXAMPLES. No native CLAIM, independent Driver approval, Lean proof or P000-X6 native transport is asserted.

## Immutable research input and authority

GLOBAL_KNOWLEDGE_V1: `main@bb0c0f4538fbc3ea90fc4118ecc8ce88f09f17bc` (same bootstrap/manual/P000/ACTIVE worldview snapshot for this research run). Enterprise Math initial research input: `main@8d749d17162ffa5da8886b9883cc97db695b1640`. Portable Research Protocol: `docs/PORTABLE_RESEARCH_PROTOCOL.md`. Predecessors: `research_notes/r1_n14_brc_two_law_strong_lumpability_iff_20261026_r1/PROOF.md` (exact LR+SL); `research_notes/r1_n14_brc_observer_only_n2_sharp_20261027_r1/PROOF.md` (non-IID LR-only failure, gap 1/36).

Native task read failed with `CONTROL_QUOTA`; native research session start returned `STATIC_READONLY_SCOPE_DENIED` / `operation_sent=false`. The connected GitHub actor `awdawmip` has repository push permission; this contribution is independent **unclaimed author research**, not execution of an existing owner's task or Source-native formal Result.

## Branch carrier, observer and future operations

Carrier: finite **positive** ordered path masses `P(h),Q(h)` (typed weighted BRC), with symbol-labelled branches, time and provenance retained before compression. Finite alphabet A; horizon N; strictly positive normalized path laws P and Q. The original policy may use the entire ordered history, law-independent behavioral fresh randomization, stopping and a final decision `D` in any fixed finite set, with terminal time `T<=N`. No intervention changes the path law beyond stopping. The compressed policy uses only `z_t(h)` and a fresh local randomization, never a persistent hidden selector.

The time-typed compression `z_t:A^t -> S_t` updates deterministically as `z_(t+1)(ha)=rho_t(z_t(h),a)`. **Assume P-strong lumpability**: for all `t<N`, states u,v and histories h with `z_t(h)=u`,

```
K_P(u,v) = sum_{a:rho_t(u,a)=v} P(a | h)
```

is independent of h. Q-strong lumpability and exact LR constancy are **not** assumed. Define the path likelihood ratio and its finite fiber range:

```
r_t(h) = Q(h) / P(h) > 0,
Delta_t(u) = max_{h:z_t(h)=u} r_t(h) - min_{h:z_t(h)=u} r_t(h).
```

This is an **external finite probability/decision model**. The Heartbeat native space remains X6 discrete Cell (six native spatial axes plus separately typed time); no X6 embedding, native-coordinate force law or phase/amplitude cancellation follows from this calculation. BRC reuse resolution: `REUSE_APPLIED` (positive rational path-flow carrier, prior exact LR/SL occupancy conservation). The new unit is an observer-scoped *quantitative residual error certificate*, not a new top-level BRC family.

## Theorem A — horizon-free-form quantitative two-law preservation bound

For **every** allowed common full-history policy pi, there exists **one common z-only fresh-coin policy** pi_bar such that

```
Law_P^pi(T,z_T,D) = Law_P^pi_bar(T,z_T,D),                                 (1)
TV(Law_Q^pi(T,z_T,D), Law_Q^pi_bar(T,z_T,D))
    <= (1/2) sum_{t=0}^N sum_{u in S_t} P_pi(T=t,z_T=u) Delta_t(u)        (2)
    <= (1/2) max_{t,u} Delta_t(u).                                        (3)
```

Here TV is half the sum of absolute mass differences. The effective upper bound can also be clipped at 1. The weighted bound depends on the actual P terminal occupancy and endpoint fiber LR ranges; it does not introduce a separate multiplicative N factor. `Delta_t` itself may grow with N, so this is **not** a horizon-uniform small-error claim without an additional range bound. Any deterministic coarser terminal observer `o_t(z)` has Q-TV no greater than (2), and its P law is exactly preserved.

### Proof

Write `s_pi(h)` for the law-independent probability that pi has not stopped before reaching ordered prefix h. For each time-state u define P-occupancy and P stop/decision/continue action masses:

```
m_pi(t,u) = sum_{h:z_t(h)=u} P(h) s_pi(h),
a_pi(t,u,d) = sum_{h:z_t(h)=u} P(h) s_pi(h) pi(d|h),
a_pi(t,u,c) = sum_{h:z_t(h)=u} P(h) s_pi(h) pi(c|h).
```

Set `pi_bar(a|t,u)=a_pi(t,u,a)/m_pi(t,u)` where the denominator is positive (arbitrary local action on unreachable states). These are nonnegative, sum to 1 and are **common across P,Q**. P-strong lumpability gives

```
m_pi(t+1,v) = sum_u K_P(u,v) a_pi(t,u,c).
```

The z-only policy obeys exactly the same recursion with the same initial mass, hence its P occupancy and each P terminal cell `C=(t,u,d)` agree. This proves (1).

For a fixed terminal cell C, define nonnegative P path-stop weights `w_pi(h,C)` and `w_bar(h,C)`; both are supported on `z_t(h)=u` and both sum to the **same** cell mass `p_C`. Since policy decisions do not alter the observation law, corresponding Q masses are `sum_h r_t(h) w_pi(h,C)` and `sum_h r_t(h) w_bar(h,C)`. Choosing `r_*(u)` as the midpoint of the minimum and maximum r in this fiber, cancel `r_* sum_h(w_pi-w_bar)=0` and apply the triangle inequality:

```
|Q_pi(C)-Q_bar(C)|
 = |sum_h (r_t(h)-r_*) (w_pi(h,C)-w_bar(h,C))|
 <= (Delta_t(u)/2) sum_h (w_pi(h,C)+w_bar(h,C))
 = Delta_t(u) p_C.
```

Summing over C and dividing by 2 gives (2), since `sum_d p_C=P_pi(T=t,z_T=u)`. Equation (3) follows because the terminal P masses sum to 1. Pushing both terminal distributions through a deterministic observer is TV-contracting. **QED.**

The proof applies to arbitrary finite positive real probabilities; `VERIFY.js` uses rational test instances only. It preserves the two-law **single-common-policy** quantifiers and has no conditional-expectation/martingale assumption.

### Exact LR special case

If `Delta_t(u)=0` for every fiber then the same construction preserves both laws exactly. This recovers the LR+P-SL sufficiency mechanism without having to postulate Q-SL separately. Conversely, the predecessor's non-IID `N=2` counterexample has exact LR constancy but lacks P-SL and demonstrably fails exact observer-only preservation; the strong-lumpability assumption cannot simply be erased.

## Theorem B — a sharp improvement at N=1, binary decisions

With a single initial root, observation horizon `N=1`, and binary D, the same P-Markovization obeys the **sharper** bound

```
TV_Q(T,z_T,D) <= (1/4) sum_{u in S_1} P_pi(T=1,z_1=u) Delta_1(u).
```

Root stopping is exactly duplicated and contributes zero. Conditional on reaching u at t=1, let `R=r_1(H_1)` and `A=pi(D=1|H_1)` under the P law conditional on that state. The final Q-probability difference for `D=1`, divided by `P_pi(T=1,z=u)`, is exactly `Cov_P(R,A)`: the compressed action uses the P mean of A, while the Q state mass is the P mean of R. Since R ranges over width Delta and A lies in [0,1], Cauchy–Schwarz and the elementary bounded-variable variance inequalities give

```
|Cov_P(R,A)| <= sqrt(Var_P(R) Var_P(A)) <= (Delta/2)(1/2) = Delta/4.
```

The two binary outcomes have opposite Q differences and fixed total Q mass at u, so their total-variation contribution is `P_pi(T=1,z=u)|Cov(R,A)|`. Sum over u. **QED.**

The coefficient 1/4 is attained: `A={0,1}`, `P=(1/2,1/2)`, `Q=(3/4,1/4)`, `z_1=*`, and full D=1 iff symbol 0. The LR values are 3/2,1/2 (Delta=1). Full Q gives `Q(D=1)=3/4`; the unique P-matching compressed decision gives `Q_bar(D=1)=1/2`. Thus TV=1/4=Delta/4. This is an exact **sharp constant for N=1**, not a claim of sharpness of the general N bound.

## Actual rational execution evidence

`VERIFY.js` is self-contained Node.js with exact BigInt reduced fractions and is also executed unchanged in a compatible JS evaluator for this author return. `RESULT.json` stores the actual JSON output. Assertions check law normalization, P terminal exactness, LR ranges, Q terminal TV and each stated bound.

The independent N=2 illustration has P IID (1/2,1/2), Q IID (3/4,1/4), and state `z_t=t` (all histories at each time merged). This state is trivially P-strong lumpable. Full policy: at t=1 continue iff first symbol=0, otherwise stop with D=0; at t=2 let D=1 iff second symbol=0. P-Markovized policy: continuation at t=1 equals 1/2, D=1 at t=2 equals 1/2. The exact terminal vectors in order `(T=1,D=0),(T=2,D=1),(T=2,D=0)` are

```
P_full = P_markov = (1/2, 1/4, 1/4)
Q_full = (1/4, 9/16, 3/16)
Q_markov = (1/2, 1/4, 1/4)
TV_Q = 5/16
Delta_1(*) = 1; Delta_2(*) = 2
(1/2)[P(T=1)*Delta_1 + P(T=2)*Delta_2] = 3/4 >= 5/16.
```

There are 3 prefixes in the N=1 example and 7 prefixes in N=2. This is a finite exact sanity check; the universal assertions are proven above, not inferred from two samples.

## Literature context, limits and non-novelty

Related work includes Gaoang Bian and Alessandro Abate (2017), *On the Relationship between Bisimulation and Trace Equivalence in an Approximate Probabilistic Context*, arXiv:1701.04547, https://arxiv.org/abs/1701.04547, which studies finite-horizon total-variation trace bounds from approximate bisimulation; and Fabian Michel and Markus Siegle (2024), *Formal Error Bounds for the State Space Reduction of Markov Chains*, arXiv:2403.07618, https://arxiv.org/abs/2403.07618, which studies aggregation error bounds. These are thematic prior-art context; the precise theorem above is author-derived, no independent literature novelty determination was made.

No conclusion is drawn about signed/complex phase cancellation, native six-dimensional Cell dynamics, infinite horizons, intervention-controlled kernels, or adversarial model misspecification. This quantitative theorem is **sufficient, not a necessary-and-sufficient criterion** for approximate universal compression. Independent Driver review, formal proof, and native bridge are outstanding.

**Next research unit:** combine nonzero P-transition lumpability defects with LR oscillation into one finite-horizon certified error inequality; independently continue the previously opened N>=3 uniqueness-vs-incomparable-minimal observer-only quotient problem, without treating this approximate side result as its solution.
