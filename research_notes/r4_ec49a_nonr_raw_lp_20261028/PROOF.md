# EC49A — Non-invariant reachable kernel with an exact RAW rational occupancy LP

Date: 2026-10-28 Asia/Shanghai. Researcher role TASK_RESEARCH; portable author-side mathematical work. Contribution tag R4-EC49A-20261028-1025-LOCAL (NOT a service-issued identity). Same-context successor to EC48Z Draft PR #1611, head 8d9009ba7eba43db42cc11ac4dbaccb94b584346; inherited EC48Y/EC48U/EC48Z exposure. AUTHOR_PROVED / EXACT_FINITE_CHECK_PASS / UNREVIEWED / NOT_ADMITTED. No native CLAIM, RA, Result or independent review.

Fixed account snapshot: GLOBAL_KNOWLEDGE_V1 main@8dd55dd8acb6de1f24688f4e70f492a36417775c. Distinct Enterprise Math reading snapshot: project main@ea46b5d29a7e35a921355413e4ea1b0a75888a97. Read project AGENTS, locked P000, native X6+time and joint-relation observer preservation contracts, autonomous and portable-research protocols. The following is a **typed auxiliary** strictly positive rational P/Q stopping-observer model, not native signed BRC, heartbeat physics or an embedding of the six-dimensional X6 Cell space. Time indices 1,2,3 are decision-order counters, not physical heartbeat durations or spatial axes. P000 and ACTIVE worldview remain unchanged.

## Complete eight-leaf model, readouts, actions

Let H,Z,W each take values 0 or 1. Initially P(H=h)=Q(H=h)=1/2. The source-neutral behavioral controller has **one** fixed causal memory state (H is erased before time 2), and no persistent private random seed.

At time 1 H is the readout, with legal actions {acc,rej,cont}. At time 2 the readout is the same constant y and the exact full fine-history likelihood ratio L=1 for BOTH hidden H; legal actions again {acc,rej,cont}. After continuation at time 2, terminal time-3 readout is (Z,W,L), with legal actions {acc,rej}; L is the exact full fine-history likelihood ratio.

Set Q(Z=0)=3/4, Q(Z=1)=1/4; P(Z=0)=1/4, P(Z=1)=3/4. Z is independent of H under both sources. Conditional on H (and independently of Z), draw source-neutral W with K(W=1|H=0)=1/4 and K(W=1|H=1)=3/4. Then for all h,z,w,

Q(h,z,w)=(1/2)q_z K(w|h),  P(h,z,w)=(1/2)p_z K(w|h).

All EIGHT terminal P and Q weights are strictly positive and sum to 1 under their respective sources; the exact fine-history LR is P/Q=p_z/q_z: L=1/3 at z=0 and L=3 at z=1. Source-neutral actions do not alter these ratios on surviving full histories.

## Theorem A1: reachable-kernel invariance (R) of EC48Z FAILS

Choose deterministic δ0: at time 1 continue only for H=0, reject for H=1; at time 2 always continue. Choose δ1 with the opposite time-1 choice: continue only for H=1. Both induce the SAME positive live mass x2(y)=1/2, the SAME time-2 readout y, and the SAME full fine-history LR 1. But their actual Q conditional next-readout probabilities are:

Qδ0(Z=1,W=1 | y,cont)= (1/4)(1/4)=1/16;
Qδ1(Z=1,W=1 | y,cont)= (1/4)(3/4)=3/16.

Thus EC48Z condition R cannot admit one policy-independent rational kernel Kbar to (Z=1,W=1). The conditional probability difference is exactly 1/8, despite all primitive source leaves being positive. The occupancy mixtures are actually reachable (not hypothetical hidden distributions).

## Theorem A2: the entire ORIGINAL four-coordinate region is EXACTLY a rational LP projection

Put nonnegative rational-LP variables u[h,a] for each time-1 H and a∈{acc,rej,cont}, subject to sum_a u[h,a]=1/2. Let x2=sum_h u[h,cont]. Put nonnegative v[a] for time 2 subject to sum_a v[a]=x2. Let x3=v[cont]. At terminal time 3 put nonnegative Q accepting masses b[z] with 0<=b[z]<=x3*q_z.

Define LP output vector O=(α,β,E_PT,E_QT) by

 β = sum_h u[h,acc] + v[acc] + b[0]+b[1],
 α = sum_h u[h,acc] + v[acc] + (1/3)b[0]+3b[1],
 E_PT = E_QT = 1+x2+x3.                                      (LP-A)

**Precise claim.** For ALL source-neutral real randomized behavioral controllers using the stated fixed one-state updater and only the specified available readouts/actions, the raw (not convexified) region S1 equals the image of (LP-A). Hence S1 is convex and rational-polyhedral, despite failure of EC48Z R for the finer time-3 readout. A rational feasible O has a rational behavioral witness, and a rational infeasible O admits a rational LP separation certificate.

**Proof, actual policy -> LP (without convexification).** Given an arbitrary policy, set u[h,a]=(1/2)π1(a|h) and v[a]=x2 π2(a|y). Denote terminal acceptance probabilities π3(acc|z,w). Let c_h=π1(cont|h), c2=π2(cont|y). For each z define

 b[z]=c2*q_z * Σ_h (c_h/2) * Σ_w K(w|h)π3(acc|z,w).

This is between 0 and c2*q_z*Σ_h c_h/2=x3*q_z. Since under every live fine history P/Q=p_z/q_z independently of W and H at time 3, its P accepting mass is (p_z/q_z)b[z] for the SAME policy, so the LP α and β match. Prior to drawing Z, the two sources have the same live H mixture and the same time-1/time-2 action probabilities, hence both survival masses at times 2 and 3 are x2 and x3. The discrete stopping-time tail identity yields E_PT=E_QT=1+x2+x3. Every actual raw O therefore satisfies this LP.

**Proof, LP -> ONE actual behavioral controller.** Given any feasible LP point, set π1(a|h)=2u[h,a]. If x2>0, set π2(a|y)=v[a]/x2; otherwise use any legal distribution. At terminal time choose π3(acc|z,w)=b[z]/(x3 q_z), independently of w, when x3q_z>0; otherwise use any legal terminal action. This is valid source-neutral randomization on the current readout; it never sees erased H. Terminal Q accepted mass is b[z], P accepted mass is (p_z/q_z)b[z], and both stopping times follow the displayed tail relation. All four coordinates match **exactly**, yielding a genuine single policy, not a mixture of different P- and Q-controllers. Thus equality of the raw region and LP image holds. QED.

Interpretation: after H-dependent survival, W is a **policy-dependent** random nuisance signal, so the fine next-readout kernel is not invariant. Yet because W is terminal and its LR given Z is constant, its effect on P/Q acceptance can be replaced by private randomness using the same conditional average. The coarser Z-only successor kernel is fixed; LP-A is an exact quotient for the declared four outputs. This is a scoped application of earlier EC48U terminal-nuisance reasoning; no priority claim over Blackwell sufficiency, weak lumpability or occupancy-LP classics.

## Concrete witness, precision and limits

With δ0, time-2 continue, and terminal accept iff Z=1, the vector is exactly O=(3/8,1/8,2,2). The strict kernel gap 1/8 is a difference in CONDITIONAL next-readout probability, not an objective-function value gap. For δ0 versus δ1, Q(W=1,T=3) differs, 1/8 versus 3/8, even though Z-only terminal decisions can give identical four-vectors. Therefore the result does NOT preserve H/W joint relations, arbitrary future W-conditioned operations, full path laws, signed amplitudes or native X6 dynamics.

The accompanying actually executed Python Fraction verifier checks source weights, full LR, A1, 432 exhaustive deterministic policies (3^2 * 3 * 2^4), 1,200 seeded rational policies and reverse W-ignoring realizations: 1,632 exact policy pairs PASS. Analytical A2, not finite extrapolation, gives the all-real-policy claim. A universal irrational-only feasibility result is NOT obtained.

## Prior art and provenance

Predecessor: https://github.com/awdawmip/enterprise-math/pull/1611; source immutable commit 8d9009ba7eba43db42cc11ac4dbaccb94b584346, particularly EC48Z Theorem Z1 (R) and NEXT_TASK EC49A. Verified broad-context literature: Peter Buchholz, "Exact and ordinary lumpability in finite Markov chains", *Journal of Applied Probability* 31(1), 59–75, March 1994, DOI 10.2307/3215235; Khan, Yu and Zhang, "A simple proof of Blackwell's theorem on the comparison of experiments for a general state space", *Economics Letters* 247, February 2025, article 112146, DOI 10.1016/j.econlet.2024.112146. Only bibliographic abstracts, not their full proofs, were consulted. These are not cited as direct proofs of A1/A2.

## Proposed next research: EC49B (not native-published Task)

Introduce a fourth decision stage after W, and a genuinely informative next signal V. Determine whether ancillary W still permits an exact raw-region LP when (i) V is conditionally H-independent given Z, (ii) its full future P/Q output law is independent of W, or (iii) weaker fixed-mixture conditions hold. Produce an exact source-positive counterexample with strict support separation if any proposed condition fails. Separately retain EC48Z unit B: seek an all-positive rational stopping model, outside R, with a rational feasible O realizable only by irrational behavioral probabilities; do not confuse a restricted two-knob polynomial with the full legal policy class.

### Authority and handoff status

Original P000/ACTIVE Heartbeat X6 stay unchanged. Native EM service v0.6.11 reported research_authority_granted=false; active Owner list responded CONTROL_QUOTA, thus current formal Owner, CLAIM and Activity remain unverified. A previous platform-denied RA write was not retried by another channel. This is GitHub-persisted author research for independent review, **not an admitted Result**. GitHub archive does not grant role-bound formal execution, and no platform approval was bypassed.
