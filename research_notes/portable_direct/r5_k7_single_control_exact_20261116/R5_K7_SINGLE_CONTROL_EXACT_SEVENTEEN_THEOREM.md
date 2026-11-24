# R5: Exact 17-state source-labelled controller for a seven-cycle

Date: 2026-11-16 (Asia/Shanghai). Frozen scientific pin: `435e77af0d180eac32bd1f9c4c464bc4010b7551`. Evidence: **AUTHOR_PROVED / EXACT_FINITE_EXHAUSTIVE / NOT_REVIEWED**. Historical R5 attribution: `EM-DIRECT-B78E55`, Activity `RA-33C87C2B703418F0706695E9`. This file records independent science, not a new Task/CLAIM or Result/Review.

## Exact statement

Fix k=7 cyclic spine nodes. A raw unavailability mask u belongs to {0,1}^7 (integer 0..127). Let
`q(u)=sum_(i mod 7) u_i u_(i+1)`.
In the inherited *genuine source-labelled* radius-2 cycle-of-triangles repair model, the exact minimum single-a library has size `35+q(u)`. For any nonempty family B, the minimum common source library is `35+q(OR B)`. The canonical actual old-source library `L(r)` has size `35+q(r)` and serves every `u <= r`, with additive slack `q(r)-q(u)`. These statements are established upstream in `r5_shared_source_helly_20261116/SHARED_SOURCE_HELLY_AND_ROBUST_CONTROLLER_THEOREM.md`.

Fix additive slack s=2 and allow only named commands `Set_0(0)`, `Set_0(1)`, overwriting bit 0. A deterministic Moore controller may choose its initial state for each raw mask, outputs a single actual source-labelled library per internal state, and must remain feasible within slack after every finite command word. `M_stat` is the minimum number of static distinct source-library outputs; `N_dyn` is the minimum number of dynamic internal states.

**Theorem (exact).** `M_stat(7,2) = N_dyn(7,{0},2) = 17`.

## Upper certificate: a genuine 17-state transducer

Use exactly the 17 source centres
`R=(45,46,47,55,61,85,90,91,94,95,109,118,119,122,123,126,127)`.
State i emits the genuine labelled library `L(R[i])`. Its raw belief `B[i]` is encoded by the adjacent verifier's `BELIEF_HEX[i]`: the 128-bit integer has bit u set precisely when raw mask u belongs to B[i]. The complete transitions for input 0 and input 1, respectively, are:

```
i:      0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16
Set0:   0  1  1  3  4  5  6  6  8  8 10 11 11 13 13 15 15
Set1:   0  2  2  3  4  5  7  7  9  9 10 12 12 14 14 16 16
```

The standard-library verifier checks all 17 source labels against every belief member, the complete raw-mask union, and both named reset image inclusions `T_b(B[i]) ⊆ B[delta(i,b)]`. It executes **145 exact source membership checks, 290 exact reset image membership checks**, and verifies the union equals all 128 raw masks. An induction on word length extends the checked two single-command inclusions to all finite reset words. Thus `N_dyn <= 17`.

## Lower certificate: complete 16-output set-cover exclusion

For each of the 128 possible canonical source centres r define
`C(r)={u in [0,127]: u&~r=0 and q(r)-q(u)<=2}`.
By the inherited common-library lower bound, any single arbitrary source-labelled library serving B can be replaced, without increasing resource cost, by `L(OR B)`. Hence any hypothetical <=16-state controller induces a <=16-library static cover from the 128 sets C(r).

The verifier removes a candidate only when its coverage is included in another candidate's coverage (equal cover ties retain one). This leaves **57** undominated centres. An exact memoized recurrence `possible(rem,m)` chooses an uncovered raw mask u and branches on **every** remaining candidate C(r) containing u, continuing with `rem\C(r)` and m-1. The only pruning inequality is `|rem| > m * max_r |C(r)∩rem|`. Dominance and this inequality preserve all solutions, and every solution must cover the chosen u, so the recursion is complete.

The checker establishes `possible(all_128,16)=False`, traversing **299,008** memoized distinct states with **173,369** cache hits, using exact integer arithmetic. Thus `M_stat>=17`; the upper controller also exhibits a static 17-library cover, hence `M_stat=17`. Since every dynamic state emits at most one source library, `N_dyn>=M_stat`, yielding the theorem.

This removes the prior upper-bound gap `17 <= N_dyn <= 19` for k=7 with **proper nonmaximal beliefs**. The previous 19-state witness was optimized only in the maximal-belief subclass. The formerly reported 24-state inert solution is a distinct numerical-MILP claim with an exact upper witness, not part of this 17-state lower proof.

## Scope and recovery

This is a pinned auxiliary integer-indexed source observer, not P000's native six-axis Cell dynamics, a BRC physical operation, or a global observer quotient. P000, the ACTIVE Heartbeat World spatial foundation, joint-relation/source-identity constraint, and unmodelled provenance remain intact. No protected control-state mutation or formal acceptance follows from this publication.

**Next:** investigate whether `N_dyn(k,{0},2)=M_stat(k,2)` has a parametric source-labelled construction for infinitely many k, or find the first valid k counterexample. Separately derive an integer-verifiable certificate for the previously numerical k=7 inert 24-state lower bound.

Prerequisites: `r5_shared_source_helly_20261116/SHARED_SOURCE_HELLY_AND_ROBUST_CONTROLLER_THEOREM.md`; `r5_partial_set_future_safe_20261116/PARTIAL_NAMED_SET_FUTURE_SAFETY_THEOREM.md`; previous scoped k=7 MILP `r5_partial_single_control_20261116/R5_K7_SCOPED_MILP_AND_UPPER_WITNESSES.md` at `1da48c5497a18405d68b27e92c0ba7cf6426a051`.
