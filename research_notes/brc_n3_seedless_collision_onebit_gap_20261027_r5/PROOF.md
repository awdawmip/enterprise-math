# N=3 likelihood-ratio collision: exact signed-support gap and minimal transient one-bit repair

Date: 2026-10-27 (Asia/Shanghai). **AUTHOR-LEVEL derivation and rational test only**. Not Source-native TASK CLAIM, Result, independent Driver review or native P000/X6/Heartbeat dynamics.

## Sources, ontology and precise scope
Verified input snapshots: GLOBAL_KNOWLEDGE_V1 `main@2b9c24b59ef463dc978051b7aa31829371b0ae0e`; Enterprise Math `main@0a0ef2d97fde11967449a3fe33c14ee191ac1ac4`. Norms read: global bootstrap/operating manual and P000 startup (canonical blob `770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc` verified); ACTIVE residual worldview, native X6 plus separately typed time, joint-observer restrictions, BRC positive branch weights and `docs/PORTABLE_RESEARCH_PROTOCOL.md`. Exact predecessor: `research_notes/brc_n3_seedless_behavioral_nonconvexity_20261027_r5/PROOF.md`; contrast `research_notes/brc_n3_weak_markov_quotient_convexity_20261027_r5/PROOF.md`.

This is an EXTERNAL finite two-measure stopping tree, using ordered strictly positive rational Q/P branch masses as a typed BRC observational example. No native X6 embedding, plane, physical-time calibration or amplitude-cancellation result is asserted. Time is an observation-count index separate from six native spatial dimensions.

At each nonterminal history a behavioral policy chooses continue, decide P or decide Q, with real probabilities; at depth 3 only a final decision. Root stopping permitted. The **seedless quotient** observes only `(time, exact L=P(h)/Q(h))`; it has local randomized actions but no persistent randomized policy-choice seed. Four observables are `O=(e_P,e_Q,E_P tau,E_Q tau)`, where `e_P=P(decide Q)`, `e_Q=Q(decide P)`. A repaired policy has one extra transient branch bit **only at time 2 on the L=1 collision**.

## Entire eight-leaf strictly positive rational input

- Root: `Q(a,b)=(1/3,2/3)`, `P(a,b)=(2/3,1/3)`.
- From a: `Q(x,y)=(1/2,1/2)`, `P(x,y)=(1/4,3/4)`.
- From b: `Q(x,y)=(2/3,1/3)`, `P(x,y)=(1/3,2/3)`.
- From ax: `Q(u,v)=(16/21,5/21)`, `P(u,v)=(1/21,20/21)`.
- From ay, bx and by: both Q and P have final kernel `(1/2,1/2)`.

Thus `L(a)=2,L(b)=1/2,L(ax)=L(by)=1,L(ay)=3,L(bx)=1/4`; the terminal LR values below ax are `1/16,4`, and below ay, bx, by respectively `3,1/4,1`. P and Q are normalized at all histories. Ordered branch identities are retained before the LR quotient.

## Theorem A: exact support gap

Take the signed linear objective
```
J(O)=e_P+e_Q+(389/1344)*E_P(tau)-(347/1344)*E_Q(tau).
H(l)=min(l,1); c(l)=(389*l-347)/1344.
```
For each history h, Bellman continuation cost normalized by Q(h) is `c(L(h))+sum_child Q(child|h)*V(child)`, and stopping cost is `H(L(h))`. The exact full-history Bellman values:
```
V(ax)=71/224 (continue); V(ay)=1 (stop);
V(bx)=115/1792 (continue); V(by)=1 (stop);
V(a)=47/48 (continue); V(b)=353/1344 (continue);
V(root)=179/336 (continue).
```
For example, `V(ax)=1/32+(16/21)*(1/16)+(5/21)*1=71/224`; final likelihood ratios give the others by backward induction. Every randomized full-history policy is bounded by these Bellman minima; extreme actions attain them. Therefore `min_full J=179/336`.

For seedless policies, the predecessor provides a proven **all-real** envelope rather than an inference from deterministic enumeration. Conditional on root continuation, optimizing actions outside the LR=1 collision yields
```
J >= 67/96 + (431/4032)*x - (319/2016)*y
           + z*((-51/448)*x+(1/144)*y),
```
where `x=Pr(continue|a)`, `y=Pr(continue|b)`, `z=Pr(continue|time 2,L=1)`, each in `[0,1]`. The y slope is strictly negative; hence minimizing y=1 gives
```
J >= 34/63 + [431*x + z*(28-459*x)]/4032 >= 34/63.
```
For `x<=28/459`, minimum over z is at 0 and numerator is 431x; for `x>=28/459`, minimum is at z=1 and numerator equals 28(1-x). Root stop has cost 1. Both endpoint coarse strategies attain `34/63`. Thus **exactly**:
```
min_full J = 179/336,
min_seedless_LR J = 34/63,
strict gap = 1/144.
```
This improves the predecessor's one-sided bound to equality. All-real signed policy optimality is algebraic, not extrapolated from a grid.

Explicit full-optimal policy: continue at root, a, b, ax, bx; stop and decide P at ay and by; at terminal decide Q iff LR<1. Its exact vector is
```
O_F=(5/42,3/7,41/18,47/18), J=179/336.
```
Coarse S1 must also continue at by when it continues at ax and has
```
O_S1=(5/42,3/7,5/2,17/6), J=34/63.
O_S1-O_F=(0,0,2/9,2/9).
```
The mass/decision errors agree; the invisible branch costs two extra equal sampling-time expectations. Since the coefficient L1 norm equals `1+1+389/1344+347/1344=107/42`, Hölder yields the **quantitative obstruction for every coarse policy**:
```
||O_seedless-O_F||_infinity >= (1/144)/(107/42) = 7/2568.
```
This is a lower bound in these four declared observer units, not a computed exact metric distance or a native physical error law.

## Theorem B: minimal transient collision tag repairs EVERY full behavioral policy

At t=0 there is one root history. At t=1, LR distinguishes a (2) and b (1/2). At t=2 it distinguishes ay (3) and bx (1/4), while ax and by have the **same LR=1**. Introduce a **binary tag only for the latter two time-2 histories**. The current time, LR and that one tag then distinguish all nonterminal histories; copy the complete history policy's exact local stop/continue/decision distributions there. This preserves all arrival probabilities and both expected sampling times.

At the terminal t=3 discard the tag. For each terminal leaf h put `A_h=Q(h)*prod_{g strict prefix h}pi_C(g)`, its Q arrival mass, and denote the full history policy's terminal decide-Q probability by `d_h`. For each nonzero-reach final exact-LR class ell, set a common terminal decision
```
d_ell=(sum_{h:L(h)=ell} A_h*d_h)/(sum_{h:L(h)=ell} A_h).
```
At a zero-reach final class choose anything. The Q-weighted terminal decision-Q sum is the same by construction. The P-weighted sum is also the same since `P(h)=ell*Q(h)` and the copied reach factors do not depend on the measure. Both complementary decision sums and earlier stop actions therefore agree. Terminal choices do not affect the time observers. Hence **every full-history real behavioral policy** is matched in all four observers by a seedless current-(time,LR) policy with **one transient time-2 collision bit**, with no persistent random seed. For rational inputs and rational full policy, recovered local probabilities are rational.

Necessity: with zero collision bit, every coarse policy obeys `J>=34/63` yet the full vector `O_F` gives `179/336`. Thus the L=1 collision must be split for universal four-observer fidelity, and two distinct symbols are sufficient. **Minimal refinement of this fiber is precisely two symbols, one bit.** This is a scoped statement for this fixed eight-leaf model; it is NOT a theorem that one bit always suffices for arbitrary N=3/4.

## Actual computation and evidence scope

`VERIFY.py` executes Python standard-library `fractions.Fraction` checks: strictly positive normalized P/Q mass, exact LR, all Bellman rows, full/coarse four-vectors and gap, 7/2568 obstruction, **23,328 complete deterministic time/LR policy tables**, exact two optimum time pairs, and **64 reproducible rational random full policies** reconstructed by terminal LR mass weighting under the one-bit repair. `EXACT_OUTPUT.txt` is actual execution output. The *all-real* sufficiency is the algebraic arrival-flow proof, not the 64 tests. The randomized coarse lower bound is the predecessor's all-real envelope, not just the 23,328 deterministic tables.

Method reuse: T0_BRC ordered positive-rational weighted branch mass and exact likelihood-ratio readout `REUSE_APPLIED`; existing exact Bellman support and full-history Q-occupancy arguments `COMPOSE_APPLIED`. This does not use the separately scoped affine-degree-two BRC transport interface for nonlinear stopping observers; no new BRC tool family claimed. Signed objective coefficients are algebraic observer weights, **not signed BRC branch probabilities**.

Native dispatch on this run: `CONTROL_QUOTA`; native source session create: `STATIC_READONLY_SCOPE_DENIED`, `operation_sent=false`. GitHub separately authenticated `awdawmip` with repository push rights. An author evidence file is not a Source-native winning Owner CLAIM, formal Result or independent Driver acceptance.

## Next exact question
See `NEXT_TASK.md`: equal all-signed-support hulls but unequal behavioral images remains unresolved. The present eight-leaf tree is a **negative candidate** (strict gap 1/144), not a solution of that stronger question.
