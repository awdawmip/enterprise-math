# BRC N=4 — lawful T4 continuation, a sharp two-law information-loss phase, and minimal stopped records

2026-10-30 (Asia/Shanghai). **AUTHOR_ANALYTIC_PROOF / EXACT_FRACTION_CHECKED / UNREVIEWED / NOT_ADMITTED**.

## Precise model, policy and lawful observation
This is the external strictly positive *16-leaf* dual-probability BRC N=4 model with original instantaneous behavioral S2/S23 information sets; the pinned source is PR #1735, `research_notes/brc_n4_bu_unrestricted_transfer_20261030_research1/PROOF.md`, Appendix I, at `6d9bc93c9d110418d22daf344ed83d883a4a1a23`. It does not claim native P000 X6/heartbeat physics, the three-dimensional slice, or a new target-relative `d_2,d_23` minimax.

The time-two sources `s=(AU,AV,BU,BV)` have Q masses `(1/6,1/3,1/4,1/4)`, respectively. At time three `j∈{0,1}`, likelihood-ratio pairs P/Q are `AU=(9/10,11/10)`, `AV=(1/4,1/4)`, `BU=(1/5,9/5)`, `BV=(2,2)`. At time four `k∈{0,1}` splits each child equally under both P and Q. Thus `Q(s,j,k)=q_s/4` and `P(s,j,k)=q_s*r_(s,j)/4`, with 16 strictly positive leaves and normalized P,Q.

For each real `u,v∈[0,1]` define the actual **causal** S23 policy G(u,v): at time one continue A and B with probability one; at time two continue AU and BU with the *same conditional kernel* (probability one), and stop AV/BV with Q; at time three stop AU with decision P, and on BU,j=0 (resp. BU,j=1) continue with probability u (resp. v), otherwise stop with Q; on any continued BU path at time four observe the real daughter k and stop with decision Q. Continuation coins are behavioral, source-law independent and independent of the future k. The time-three ratios `1/5,9/5,9/10,11/10` are distinct, so the stage-three action is current-likelihood-measurable; both time-four BU daughters use the identical action. This respects S23 and S2 at all reachable nodes.

The five-atom **lawful stopped** observer is `Y=(T,Decision,Z_BU,Z_AU,K_obs)`, where `K_obs=k` only when the strategy truly continued to T4 and otherwise equals ⊥. Its atoms are `E=(2,Q,0,0,⊥)`, `A=(3,P,0,1,⊥)`, `B3=(3,Q,1,0,⊥)`, and `B40=(4,Q,1,0,0)`, `B41=(4,Q,1,0,1)`. Define the previous K' compression extended to Y by fixing E,A and mapping B3,B40,B41 to the single B=(3,Q,1,0,⊥). Let C=K'(Y).

## Theorem 1 — exact continuous-parameter deficiency
For **every** real `(u,v)∈[0,1]^2` (including the boundaries), exact aggregation of all sixteen source leaves and their causal behavior kernels yields:

| Y atom | P mass | Q mass |
| --- | ---: | ---: |
| E | 7/12 | 7/12 |
| A | 1/6 | 1/6 |
| B3 | `1/4−(u+9v)/40` | `1/4−(u+v)/8` |
| B40 | `(u+9v)/80` | `(u+v)/16` |
| B41 | `(u+9v)/80` | `(u+v)/16` |

Proof of the table: Under Q, each BU time-three child has mass 1/8. Under P, BU,j0 has mass 1/40 and BU,j1 has mass 9/40. Continuing each child with its specified probability and then splitting its two time-four daughters equally gives the B40/B41 entries; the remaining BU mass gives B3. AU and the early AV/BV masses do not depend on u,v. Each row is nonnegative and the rows normalize under both laws for the entire real square.

Subtracting the Q from P vectors gives `(0,0,−(v−u)/10,(v−u)/20,(v−u)/20)`, and hence

**`TV(P_Y,Q_Y)=|v−u|/10`; whereas `P_C=Q_C=(7/12,1/6,1/4)`, so `TV(P_C,Q_C)=0`.**

Let D be **any** stochastic decoder of Y using C and optional private randomness, but not the identity of the source law. For L=P,Q let `e_L(D)=TV(L_Y,D_#L_C)`. Since P_C=Q_C, the decoded law R is the same under P,Q. The TV triangle inequality gives `|v−u|/10≤TV(P_Y,R)+TV(R,Q_Y)≤2max(e_P,e_Q)`. The bound is globally sharp: from C=E or A output the same atom, and from C=B output B3 with probability `1−(3u+7v)/10`, B40 and B41 each with probability `(3u+7v)/20`. The three B probabilities are nonnegative and sum to one on all of `[0,1]^2`. This **P/Q-common, C-preserving** decoder produces the midpoint law R=(P_Y+Q_Y)/2 and has `e_P=e_Q=|v−u|/20`. Therefore

**`inf_{all law-independent stochastic D} max(e_P(D),e_Q(D)) = |v−u|/20`.**

In particular, C is exactly sufficient for the *single-read distribution* of Y for both laws iff `u=v`. The iff statement concerns this observer and two fixed P/Q laws, not all future operations or pathwise reproduction.

## Theorem 2 — maximal rational G4 witness and separating event
Choose `G4=G(0,1)`. This is a deterministic legal policy continuing BU,j=1 to the fourth stage with positive mass under both laws; it stops BU,j=0 at time three. Its Y distributions, in atom order (E,A,B3,B40,B41), are:

`P_Y=(7/12,1/6,1/40,9/80,9/80)` and
`Q_Y=(7/12,1/6,1/8,1/16,1/16)`.

The legitimate stopping-time event H4={T=4} has `P(H4)=9/40`, `Q(H4)=1/8`, with signed difference **1/10**. Thus `TV(P_Y,Q_Y)=1/10`, while the old K'-collapsed C laws are identical. The sharp common C-decoder radius is **1/20**; its B-output probabilities are exactly `(3/10,7/20,7/20)`.

This is a precise obstruction to treating K' as *lossless for a genuine time-four-dependent downstream observer*. The preceding K' **data-processing contraction toward the old target** remains valid for its own terminal-observer objective. The present theorem does not change the old target-relative minimax.

## Theorem 3 — seven actual stopped atoms and two types of sufficiency
For deterministic G4 the source filtration is F2=σ(s), F3=σ(s,j), F4=σ(s,j,k). The actual stopping times are 2 on AV/BV; 3 on AU,j=0/1 and BU,j=0; and 4 on BU,j=1,k=0/1. By the definition `F_T={D: D∩{T≤t}∈F_t for every t}`, its **exact seven** atoms are `AV, BV, AU0, AU1, BU0, BU10, BU11`. At time two AV/BV are distinct source events; at time three AU0/AU1 and BU0 are available but their future k is not; at time four BU10/BU11 become distinguishable. Every stopped-measurable set is a union of these seven, and every such union is admissible. Their P/Q TV is 43/120; splitting BU,j1 by fair k preserves the predecessor G0 stopped-TV value.

For the **single-read two-law distribution of Y**, adding the **actually recorded BU branch bit j** to C is enough for every G(u,v): from BU,j0, continue with u and on time-four arrival emit a fair k; from BU,j1 do the same with v. Conditional on each BU,j, k is fair under **both** laws, so this *same* kernel reconstructs the full Y distribution under P and Q. With `u≠v` no additional recorded information (C alone) is insufficient by Theorem 1's strict radius. With `u=v` no bit is needed for this distributional objective. Newly sampled k is not necessarily the *actual* k, and cannot be reused as fresh independent randomness for repeated reads of the same leaf while claiming pathwise fidelity.

For **universal pathwise F_T reconstruction under G4**, C's BU fiber contains three distinct positive stopped atoms (BU0,BU10,BU11), so **one** extra binary recorded bit is impossible; **two** are necessary and sufficient. Let `(b1,b2)` be (BV-indicator,0) on the E fiber, `(j,0)` on the A fiber and `(j,k)` on BU,j1 versus `(0,0)` on BU,j0. Then `(C,b1,b2)` uniquely identifies all seven actual stopped atoms. This is a sharp worst-case conditional bit count, not an entropy bound.

## Verification and source boundaries
`VERIFY.py` has been executed under standard-library Python `Fraction`: all 16 raw leaves, positive masses and both normalizations; exact distributions, total variation and midpoint radius for G4; 16 additional rational (u,v) pairs; the sharp midpoint formulas; and the seven-atom G4 stopped partition. `VERIFY_EVIDENCE.txt` preserves actual stdout. The continuous-domain conclusion rests on the displayed algebra and universal TV inequality, **not** an extrapolation from 16 finite test pairs.

Predecessor G0 stopped filtration: PR #1738, `research_notes/brc_n4_g0_stopped_sigma_sixatom_20261030_r11/PROOF.md` at `f8eff8bfaad1ff2e338d81361adcafd01f7a47b1`. Original causal information-set specification: PR #1735 Appendix I at `6d9bc93c9d110418d22daf344ed83d883a4a1a23`. Frozen GLOBAL_KNOWLEDGE_V1 main input `f4599a2002221a170cb3b64a241885aa045be3cd`; Enterprise Math main input `f58a70fd8a216e3da2e15800e6b1d7d0f09a97dc`.

Formal independent review is needed for the S23 rule, stopping-time partition and common-decoder quantifiers. Native P000 X6, the three-dimensional slice, independent time dynamics and original physical BRC operations are separate open correspondence obligations; ordinary finite-probability Fraction computation here cannot verify native heartbeat residuals. This is author-side portable research only: no native CLAIM, Result, Driver admission or current active Owner is inferred from GitHub publication.
