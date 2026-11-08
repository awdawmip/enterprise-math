# PREFIX-598-R6 — Native phase/branch-bit cancellation theorem and action-label boundary

Date: 2026-11-08 (Asia/Shanghai).
Status: AUTHOR_DERIVED / EXACT_INTEGER_27_CASE_CHECK / SOURCE_TRANSCRIPTION_CHECKED / UNREVIEWED / NOT_ADMITTED.
Researcher-ID: EM-DIRECT-B900FB / TASK_RESEARCH; Research-Activity-ID: RA-CC93244CAE5F854895CE2C8E.
Frozen scientific input: \`f42f2906d77f24085c123f3ccfe9667d41caa96d\`.
Source: \`research_notes/portable_direct/PREFIX565_positive_marginal_certificate.py\`, Git blob \`7d4ffaaa5f2e804bff01196f2c2c5cc8bcb79f41\`; exact definitions \`PHASES, NEXT, ACTIONS, ROOTS, TARGET, edge\`. Research derivation continues PREFIX-595/596/597; no modification of P000 or input pin.

## Question

PREFIX-595 discovered the raw-seven-reward and exact-next-original-port one-step equality between two pairs of start-mixtures and, for the pair \`(6,29) vs (7,28)\`, observed four surviving terms when action labels are retained. Derive these relations directly from the phase and branch-bit definition and determine all target predecessors and their action-label distinguishability.

## Exact native construction

For each phase \`p\` among 48 and native branch bit \`b∈{0,1}\`, the original port is \`i=2p+b\`. A primitive action is \`a=(s,b')\` with \`s∈{0,1,2}\`, \`b'∈{0,1}\`; destination phase is \`q=NEXT[p][s]\`, and next original port is \`j=2q+b'\`. Six-axis BRC rewards for this step depend on the signed source and destination phase components \`c(p),c(q)\`, on root \`r\`, and not on the source bit. The seventh (gate) reward is exactly

$$
g(p,b;s,b')=\mathbf 1\{b=b'=1,\ NEXT[p][s]=TARGET\}.
$$

All six primitive actions carry equal weight \`1/6\`. The nine allowed frozen roots are zero and the eight signed unit roots on axes 1–4.

Exact frozen source phase enumeration gives:

| phase p | PHASES[p] | NEXT[p] | target slot |
| --- | --- | --- | --- |
| 3 | (0,-6,+1) | (4,16,20) | 0 |
| 14 | (1,-4,+1) | (20,4,8) | 1 |
| 15 | (1,-5,+1) | (16,4,8) | 1 |

The unique gate target is \`TARGET=4\`, corresponding to original port \`2*TARGET+1=9\` when \`b'=1\`. These are **all** its incoming native phase predecessors, found by checking all 48 frozen \`NEXT\` tuples. All three have current signed component \`c=+1\`.

## Theorem A — all three unordered phase pairs have exactly vanishing raw one-step difference

For \`p∈{3,14,15}\` set \`d_p=δ_(2p)−δ_(2p+1)\`, a signed difference of start-port measures. For an allowed root \`r\` let \`L_r\` denote the exact one-step Markov operator retaining the entire original 7-component BRC reward \`w=(ΔR1,...,ΔR6,ΔK)\` and **exact original next port** \`j\`, but forgetting primitive action index.

Write \`w_0(r)\` for the original six-axis native BRC reward from current signed component \`+1\` to target signed component \`−3\`, with gate set to 0; write \`w_1(r)\` for the same native reward with gate 1. Both rewards are determined by the frozen \`edge\` definition and are independent of which of the three source phases was used. Then for each \`p∈{3,14,15}\` and every allowed root \`r\`,

$$
L_r(d_p)=\frac{1}{6}\bigl(\delta_{(9,w_0(r))}-\delta_{(9,w_1(r))}\bigr).
\tag{A1}
$$

In particular for every distinct \`p,q\` in this three-element set,

$$
L_r(d_p-d_q)=0. \tag{A2}
$$

Equivalently, the two **legal nonnegative** initial probability mixtures
\`(δ_(2p)+δ_(2q+1))/2\` and \`(δ_(2p+1)+δ_(2q))/2\`
have exactly identical one-step joint laws of the complete seven rewards and next original port. The three unordered pairs are \`(3,14), (3,15), (14,15)\`; the previously unrecorded explicit third pair is \`(6,31) vs (7,30)\`.

**Proof.** For a fixed phase and action with \`b'=0\`, or with \`NEXT[p][s]≠TARGET\`, the edge's output does not depend on the starting branch bit, so its contribution to \`L_r(d_p)\` cancels. The sole remaining action has \`b'=1\` and \`s=target_slot(p)\`: its next original port is 9 and the two source bits give the same six-axis rewards but gates 0 and 1. As all predecessor phases have the same signed component \`+1\` and reach the same target phase, the six-axis rewards coincide across phases at each root. Thus (A1) is independent of \`p\`, yielding (A2). QED.

The two differences \`d_3-d_14\` and \`d_14-d_15\` are linearly independent, so their span is a **two-dimensional explicit subspace** of the common kernel \`∩_r ker(L_r)\`. This is a lower bound on that kernel, not a claim about its full dimension.

## Theorem B — exact action-label information-loss boundary

Let \`L_r^{act}\` instead retain the primitive native action \`a=(s,b')\` in addition to the full seven rewards and original destination port. Then

$$
L_r^{act}(d_p)=\frac{1}{6}\left(
\delta_{((s_p,1),9,w_0(r))}-\delta_{((s_p,1),9,w_1(r))}
\right)
$$

where \`s_3=0\` and \`s_{14}=s_{15}=1\`. Therefore

$$
L_r^{act}(d_{14}-d_{15})=0
$$

for every allowed root. The special initial mixtures \`(δ_28+δ_31)/2\` and \`(δ_29+δ_30)/2\` retain **the entire primitive action label** in their equal one-step law. For the other two phase pairs (involving phase 3), the signed action-labeled difference has exactly four nonzero atoms, at destination original port 9, with actions \`(0,1)\` and \`(1,1)\`; it is not zero.

**Proof.** Repeat the single surviving target action argument but do not sum over primitive action indices. When target slots are equal the signed terms agree and cancel, whereas different slots produce two distinct gate0 and gate1 atoms for each slot, all with unit nonzero coefficients before dividing by 6. QED.

As a consequence, for each of the three mixture equalities from Theorem A, all prescribed root schedules produce identical distributions of the **ordered complete seven-reward history and terminal original port for every path length n≥1**. For the special pair \`(28,31) vs (29,30)\`, the entire ordered **action-plus-seven-reward** history and terminal port law also agree for every \`n≥1\`; this is an action-level equality (not an identity of the initial hidden port). Adaptive root schedules based only on the common observed history and independent exogenous randomness preserve the corresponding equality by the same one-step coupling and conditional Markov induction.

## Exact validation

Independent local Python transcription of the frozen PREFIX-565 \`edge\` formulas, using integer counters and exhaustive six-action enumeration, returned \`ALL_DIRECT_PHASE_SWAP_CHECKS_PASS\` across **nine roots × three unordered phase pairs = 27** equalities of full raw seven-reward and original destination-port counting measures, and 27 separate action-aware comparisons. Action-aware discrepancy atom counts are \`4,4,0\` per root, in phase-pair order \`(3,14),(3,15),(14,15)\`. The static predecessor enumeration checks exactly 48 phases. This is full finite exact coverage of the declared three-pair/nine-root domain; the all-depth results are proved by one-step equality and induction. A repository-native independent checker importing the exact PREFIX-565 module is supplied separately for rerun; **in this session the original GitHub module itself was not executed locally**. All claims are inside this frozen toy-native BRC model and retain user-defined X6 semantics.

Theorem and proof are author research, not independent review, formal Result, P000 change, or adopted Working Truth.

**Next unresolved unit**: describe a structural involution or group-action directly on the complete phase/action graph that realizes the signed two-dimensional kernel without the phase enumeration; determine its exact action-provenance quotient and test whether the two-dimensional relation extends to other native gate targets, signed c-values or larger BRC phase models.
