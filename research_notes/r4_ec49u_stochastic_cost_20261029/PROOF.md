# EC49U — Exact separation under genuinely stochastic, non-rigid cost compensation

Status: **AUTHOR_PROVED / EXACT_FRACTION_CHECK_PASS / UNREVIEWED / NOT_ADMITTED**.
Date: 2026-10-29. Author route: portable research, **not** a native CLAIM/Result/Driver review.

## Frozen scientific scope and type boundary

Continuing EC49T (Draft PR #1666, research commit `dd5711b0c27d1886918c8bd69b2660978fde4593`), preserve the source distribution and first/second sensor semantics. Scientific reference snapshot: `GLOBAL_KNOWLEDGE_V1 main@75c30a747792c0e33c7116eb01db2f77d00868da`; Enterprise Math `main@4dab5fcd7d61f67f721f21b2f6251b4eede4750c` (read before this research unit). This is a *finite positive-rational labeled-branch BRC auxiliary observer*: the labels and positive source weights are retained until the P/Q signed **difference of readout probabilities** is formed. That difference is **not** native signed BRC amplitude. No X6/heartbeat transfer theorem is asserted. P000 and ACTIVE worldview are unchanged.

Population: `W=Z={0,1,2}`, `U={0,1}`, two sources P/Q, each with 18 strictly positive leaves `(w,u,z)` when `0 <= eta < 1/2`. Define

\[
 Q(w,z)=1/9,\qquad P(w,z)=\begin{cases}1/6&z=w,\\1/12&z\ne w,\end{cases}
 \quad t_w(u)=\tfrac12+(2u-1)\eta\sigma_w,\quad \sigma=(1,0,-1),
\]

with `R(w,u,z)=R(w,z)*t_w(u)` for `R=P,Q`. Thus `P(W,U)=Q(W,U)=t_w(u)/3` and

\[
 \Delta(w,u,z)=P(w,u,z)-Q(w,u,z)=t_w(u)\frac{3\mathbf{1}_{z=w}-1}{36}.
\]

Before any observation U, the full observer knows W. The compressed observer may use W to select STOP or one of actions A/B and set a one-bit pre-erasure memory D, then forgets W. It remembers its own first action and D. Buying A costs 1; B costs 2. Either purchase returns a U distributed by t_w (same kernel for A and B). Following U it may STOP or buy S for cost 1, observe Z, and accept/reject using only `(A/B,D,U,Z)`. It may also accept/reject without S. The full observer retains W for terminal decisions. The protocol allows arbitrary source-independent real behavioral randomization at every available information set, independent fresh coins; all terminal decisions and stop rules are free. Cost T is *sensor resource*, not heartbeat time.

Observation vector: `O=(alpha,beta,E_P T,E_Q T)`, with alpha=P(accept), beta=Q(accept). Both source/stage costs are equal for *every* legal controller because the entire pre-Z `(W,U)` distribution agrees: `C1_P=C1_Q`, `C2_P=C2_Q`. Hence the four source/stage expectations collapse to **two independent constraints** in this model; we do not count four independent cost equations.

## Theorem A — a strict four-vector separator with non-rigid costs

For `eta=1/200`, **every** real behavioral compressed policy satisfies

\[
 H(O):=\alpha-\beta-\frac{E_PT+E_QT}{36}\leq \frac1{27}.
\]

For `eta=5/12`, **every** real behavioral compressed policy satisfies

\[
 H(O)\leq \frac1{24}.
\]

Both support bounds are **attained by deterministic compressed policies**, so they are exact global extrema for the stated linear functional (not merely sample bounds). In fact the first bound holds for every real `0 <= eta <= 1/6`.

The full observer has the following rational policy, with probabilities independent of W: STOP `1/8`; buy A then S `41/48`; buy B then S `1/48`. On either S path accept precisely when `Z=W`; on STOP reject. It produces

\[
 \boxed{O^*=(7/16,\;7/24,\;85/48,\;85/48)},
 \quad C_{1,P}=C_{1,Q}=43/48,\quad C_{2,P}=C_{2,Q}=7/8.
\]

The stage costs are strictly nonextremal, and the resource bill varies between paths. Directly,

\[
 H(O^*)=7/16-7/24-\frac{(85/48)+(85/48)}{36}=\frac{41}{864}.
\]

Therefore the full four-vector is **outside even the convex hull** of the compressed region. The exact linear-separator gaps are

\[
 \boxed{1/96\quad(\eta=1/200),\qquad 5/864\quad(\eta=5/12).}
\]

These are exact *support gaps for H at the selected full witness*, not claimed sharp deficits for the constrained acceptance problem at the witness's exact budget.

### Explicit expected-cost compensation is possible but does not recover acceptance

A different rational **compressed** policy sets D=0 and rejects always: STOP with probability `11/96`; buy A then S with probability `84/96=7/8`; buy B and stop before S with probability `1/96`. For both sources its first-stage cost is `84/96+2/96=43/48`, and its second-stage cost is `84/96=7/8`, exactly equal to the full witness in *each source and each stage*. However its acceptance pair is `(0,0)` rather than `(7/16,7/24)`. Its total bill takes values only 0 or 2, whereas the full policy puts probability `1/48` on bill 3. Thus equal source/stage expectations can coexist with different pathwise cost laws. The support inequality proves **no** compressed acceptance rule or randomized reallocation—not merely this example—can recover the full four-vector.

## Proof of the global extrema (all-real, not a random grid)

Let `lambda=1/18`. Since P/Q agree on `(W,U)`, acceptance before S contributes **zero** to `alpha-beta`, while first-stage and S costs remain nonnegative. Thus, when maximizing `H = alpha-beta-lambda*C` with `C=E_PT=E_QT`, STOP/early-reject can replace any branch that never buys S without lowering H. With finite acyclic information sets and source-independent behavioral coins, H is separately affine in each action/acceptance kernel; maximize one kernel at a time to reach a **deterministic** vertex. Consequently a compressed maximizing prefix is a map

`W -> {STOP, A0, A1, B0, B1}`,

where the numeral is D. There are exactly `5^3=125` such assignments; all possible post-U S/accept actions are optimized analytically, not sampled.

For an action-memory code c with assigned fiber F_c (a subset of W), define

\[
 \begin{aligned}
 D_{F,u,z}&=\sum_{w\in F}\Delta(w,u,z),\\
 M_{F,u}&=\sum_{w\in F} Q(W=w,U=u)=\frac13\sum_{w\in F}t_w(u),\\
 G_\eta(F)&=\sum_{u=0}^1\Big[\sum_{z=0}^2[D_{F,u,z}]_+-\lambda M_{F,u}\Big]_+,\\
 V_a(F)&=G_\eta(F)-\lambda |F|c(a)/3,\quad c(A)=1,\ c(B)=2.
 \end{aligned}
\]

The inner positive parts optimize the terminal accept mask *separately for each Z* after S, and the outer positive part optimizes whether to buy S after observing U. Stage one cost is deterministic on each W in that fiber. Distinct code fibers are disjoint, and the total maximum H of any chosen prefix is the sum of its four V values; STOP contributes zero. This formula is exact for all real randomized policies by the vertex argument.

**Case `0 <= eta <= 1/6`.** All `t_w(u)` are between 1/3 and 2/3. For any singleton F, `G(F)=1/27`; for any pair F, both pair-indexed Z coefficients are nonnegative and `G(F)=1/54`. For the triple, the terminal positive difference per u is `eta/12`, strictly below the S penalty `1/36`, hence `G({0,1,2})=0`. Therefore

- a singleton A fiber contributes `1/54`, a singleton B fiber contributes zero;
- a pair A fiber contributes `-1/54` (a pair B fiber is worse);
- any triple fiber contributes a negative amount.

There are only **two** distinct A memory codes. Hence at most two positive singleton A fibers can be used, proving `H <= 2/54=1/27`. Equality: choose two different histories to buy A with different D, always S then accept `Z=W` for those histories; STOP on the third. This settles `eta=1/200` and the entire interval analytically.

**Case `eta=5/12`.** Direct substitution into the displayed exact formula gives the following complete nonempty fiber table (the first and second columns are `V_A` and `V_B`):

| F | A | B |
|---|---:|---:|
| any singleton | `1/54` | `0` |
| `{0,1}` or `{1,2}` | `-1/108` | `-5/108` |
| `{0,2}` | `5/216` | `-1/72` |
| `{0,1,2}` | `-1/24` | `-7/72` |

All B fibers are nonpositive. Since there are only two A codes and the three histories must be assigned to disjoint fibers or STOP, the largest total is obtained by A-fiber `{0,2}` and A-fiber `{1}`: `5/216+1/54=9/216=1/24`. A pair of A singletons yields only `8/216`; all other partitions are no better. Exact terminal choices are recovered by the two positive-part operations. This proves the second bound and its attainment.

For either eta, the full witness has stage costs `43/48,7/8` and acceptance pair `7/16,7/24` because `P(Z=W)=1/2` and `Q(Z=W)=1/3`. Its H value is `41/864`. Compare with `1/27=32/864` and `1/24=36/864` to conclude the strict support gaps. QED.

## Verification, provenance and boundaries

The `VERIFY.py` checker uses only Python `fractions.Fraction` and the standard library. It checks all 18 source atoms for positivity/normalization for each eta, independent 8-mask terminal enumeration for each `(F,U)`, all 125 deterministic prefix assignments per eta, direct full-witness source acceptance and stage-cost expectations, and the distinct compensated compressed policy. It writes `EXACT_REPORT.json`; all assertions passed for `eta=1/200` and `eta=5/12`. The all-real coverage comes from the preceding deterministic-extreme-point argument. It does **not** imply that finite checking alone proves an infinite-dimensional statement, nor that this observer model admits native signed BRC, original X6 coordinate dynamics, or formal Lean proof.

External background: Zaccaria et al., *Finite-Time Guarantees for Constrained Reinforcement Learning under Partial Observability*, 2026-10-15, arXiv:2610.21548, studies constraints and finite-window approximations under filter stability. Anderson and Montufar, *The Value Function Semi-Algebraic Set in Partially Observable Markov Decision Processes*, ICML/PMLR 2026, studies infinite-horizon feasible value-function geometry under memoryless policies. Those are model-context references, not proofs of EC49U, and no originality or peer review is asserted.

Next bounded research question: EC49V in `NEXT_TASK.md`. Maintain the exact source pins, explicit randomness assumptions and `UNREVIEWED / NOT_ADMITTED` boundary. Only actual service-issued Source/Driver review can change native status.
