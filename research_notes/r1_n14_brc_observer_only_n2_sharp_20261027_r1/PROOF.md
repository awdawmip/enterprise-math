# R1/N14 — Two-law BRC observer-only compression: sharp depth-two obstruction and exact seven-state minimum

Date: 2026-10-27. Classification: AUTHOR PROOF / EXACT RATIONAL CERTIFICATE, not a canonical Result, independent review, Lean theorem, or native Heartbeat/P000 bridge.

## Frozen source and role boundary

Verified account GLOBAL_KNOWLEDGE_V1 canonical main: c2658a2945f4decaf267d7f75f70eda63e6740ea (bootstrap, manual, project route, P000 V4, ACTIVE residual worldview). Enterprise Math research input: main 72bdcc67b5a8bc5178cf3a53fe8fe4ac5eaecc27. Current delivery: docs/PORTABLE_RESEARCH_PROTOCOL.md. Prior scientific frontier: research_notes/r1_n14_brc_minimal_two_law_repair_20261027_r1/PROOF.md and its exact LR/SL right-congruence theorem.

GitHub actor awdawmip has repository write permission, but the Source-native task lookup returned CONTROL_QUOTA and session_start returned STATIC_READONLY_SCOPE_DENIED (operation_sent=false). Accordingly this is independently scoped *unclaimed direct author research*, not use of another owner's Task, native CLAIM, Source Result, or Driver approval.

BRC carrier: ordered positive rational path masses (P(h),Q(h)) with branch labels and conditional transition kernels. Declared operations: common history-dependent randomized stopping and binary decisions; compressed implementation: deterministic time-typed state updates and only fresh, state-local randomization. Declared observer: (T,D), even coarser than the previous (T,x(H_T),D). This is an EXTERNAL finite probability model, not a native X6 Cell operation. Reuse resolution: REUSE_APPLIED, weighted BRC path-flow algebra and the prior finite two-law LR/SL theorem. No phase/sign cancellation is invoked.

## Exact strictly positive two-law instance

Let A={0,1,2}, horizon N=2. The first symbol I is uniform under both P and Q: P(I=i)=Q(I=i)=1/3.

The conditional distribution of second symbol J under P, in order J=0,1,2, is

- I=0: (1/4, 1/4, 1/2)
- I=1: (1/12, 3/4, 1/6)
- I=2: (1/6, 1/2, 1/3).

Define Q(J=j | I=i)=r_j P(J=j | I=i), where r=(2,1,1/2). Explicitly, Q's rows are

- I=0: (1/2, 1/4, 1/4)
- I=1: (1/6, 3/4, 1/12)
- I=2: (1/3, 1/2, 1/6).

All entries are positive and all rows sum to 1. The ordered cylinder likelihood ratios Q(h)/P(h) equal 1 at t=0,1 and r_j at t=2 for h=(i,j).

The candidate compression x has x_0=root, x_1=* (the first symbol is forgotten), and x_2=j (only the last symbol remains), with time tags. This is deterministically recursively updated. Likelihood ratio is constant on every x-fiber. The requested terminal observer o is constant, so the final readout is *only* (T,D).

## Theorem A — LR constancy is insufficient already at N=2

There is a common full-history policy with a joint law of (T,D) under P and Q that NO common x-state fresh-coin policy realizes.

**Full-history witness.** After seeing I, continue exactly when I=0; otherwise terminate at T=1 with D=0. At T=2 choose D=1 exactly when J=0. Then

P(T=2)=Q(T=2)=1/3,
P(T=2,D=1)=1/12,
Q(T=2,D=1)=1/6,
P(T=1,D=0)=Q(T=1,D=0)=2/3.

For any x-policy, since x_1 is constant, its continuation probability at t=1 has a single common value c. Matching P(T=2)=1/3 forces c=1/3. The unconditional second-letter marginals, averaging the three first-letter rows, are

bar P=(1/6,1/2,1/3),  bar Q=(1/3,1/2,1/6).

Write d_j in [0,1] for the x-policy's final probability of D=1 when x_2=j. Its terminal two-law contrast necessarily obeys

Q(T=2,D=1)-P(T=2,D=1)
 = c * sum_j (bar Q_j-bar P_j)d_j
 = (c/6)(d_0-d_2)
 <= c/6 = P(T=2)/6 = 1/18.                (1)

But the full-history witness has contrast 1/6-1/12=1/12. Its strict violation of (1) is

1/12-1/18 = 1/36 > 0.

This inequality eliminates ALL real randomized compressed policies of the stated fresh-coin class, not just a finite parameter grid. Earlier binary decisions cannot help: the target T=1,D=1 mass is zero. A policy stopping before the first observation cannot help because the target T=0 mass is zero.

**Depth sharpness.** For horizon N<=1 with a single root and positive laws, if Q(h)/P(h) is constant on each terminal x-fiber, any full-history binary decision kernel can be compressed using its P-weighted conditional mean per state. The same conditional mean works under Q because within-state Q mass is a fixed scalar multiple of P mass. Optional root stopping is duplicated before this operation. Therefore the analogous LR-only obstruction has minimal possible depth N=2. This does not assert minimal alphabet size or a result for unrestricted hidden-memory strategies.

## Theorem B — Even constant terminal observer requires seven time-typed states in this instance

Consider *all* deterministic time-typed quotients z_t of the ordered history with recursive labelled update z_{t+1}(ha)=rho_t(z_t(h),a). A z-policy is allowed a fresh random decision based only on (t,z_t), with no persistent hidden selector. Call z universally observer-sufficient if for every common full-history randomized stopping/decision policy, a single z-policy preserves both P and Q laws of (T,D).

**Claim:** the minimum total number of time-typed states |Z_0|+|Z_1|+|Z_2| is exactly 7, with profile (1,3,3).

*Three states at t=1 are necessary.* Put a_i=P(J=0|I=i); these values are a_0=1/4 > a_2=1/6 > a_1=1/12. For any admissible policy let c_i be the probability of continuing after I=i. Positivity of the path masses and q_ij-p_ij=(r_j-1)p_ij imply the universal support inequality

J_+(policy):=Q(T=2,D=1)-P(T=2,D=1)
 <= (1/3) sum_i c_i a_i.                   (2)

The total continuation mass m=P(T=2)=Q(T=2) is (1/3)sum_i c_i. For m=1/3 (sum c_i=1), the unique maximum of (2) is attained at (c_0,c_1,c_2)=(1,0,0), with J_+=1/12. For m=2/3 (sum c_i=2), the unique maximum is (1,0,1), with J_+=5/36. Both maxima are attained by full-history policies that continue on the indicated symbols and decide D=1 iff J=0.

If z_1 identifies I=0 with any other I, the unique optimizer for m=1/3 is unavailable because equal z_1 requires equal continuation probability. If it identifies I=1 with I=2, the unique optimizer for m=2/3 is unavailable. Thus no pair of different first symbols can share a state: |Z_1|>=3. This argument does not assume any terminal state structure: (2) is an upper bound even with arbitrary terminal history access.

*Three states at t=2 are necessary.* Take full-history policies that always continue, so P(T=2)=Q(T=2)=1. Positivity forces any matching quotient strategy also to continue on every first-letter state. Under this fixed arrival law, each nonempty terminal z-state has a ratio Q(B)/P(B) which is a positive weighted mean of {2,1,1/2}. The full policy that decides D=1 iff J=0 gives a nonzero event with exact ratio 2; a matching quotient therefore needs at least one terminal state consisting solely of histories with J=0. Likewise D=1 iff J=2 gives ratio 1/2 and needs a different terminal state supported only on J=2. If there were at most two terminal states, neither could contain the strictly positive J=1 histories. Contradiction. Thus |Z_2|>=3.

At t=0 there is one root, so every universally observer-sufficient quotient has at least 1+3+3=7 time-typed states.

*Attainment.* Define z_0=root, z_1=i, z_2=j. This seven-state recursive quotient has LR constant in every state and two-law strong lumpability: t=1 states are single ordered histories, and there are no outgoing transitions at t=2. The already established finite positive two-law LR/SL occupancy-flow theorem therefore produces a common z-policy matching (T,z(H_T),D) under both laws, hence (T,D). Directly: duplicate root and each first-symbol decision; for terminal state j set D=1 to the P-weighted mean of all surviving complete-history D=1 decisions at (i,j). Every such history has common ratio r_j, so the Q-weighted mean equals the P mean. This attains 7 and completes the minimum proof.

This is an instance-specific observer-only minimum, not a general uniqueness theorem for arbitrary coarse observers. It is strictly stronger in this instance than requiring that a repair retain the original x: the lower bound applies even when retaining x is not demanded.

## Exact check / reproducibility

Run node VERIFY.js in this directory. It uses native BigInt rational reduction (no floating approximation), validates all 13 ordered prefixes via positive normalized row laws and LR identities, the full-history law, the strict gap 1/36, and exact fractional-knapsack support bounds for all five partitions of three first-symbol histories. RESULT.json is the actual executed JSON output of the identical source. The universality, strict exclusion of all randomized parameters, and seven-state minimality rely on the proofs above; enumerating five first-letter partitions is only supplementary evidence. Independence, Lean, and P000/X6 transfer are pending.

## Existing knowledge and non-novelty boundary

This is a narrow finite two-law positive path-flow instance of classical sufficiency, occupancy flows, likelihood-ratio testing, and probabilistic quotient minimization; no claim of global priority or a new physics result. It extends the verified prior project's LR/SL repair theorem and specializes BRC's observer/provenance rule to a quantified information-loss witness.

Next executable question: identify necessary/sufficient observer-only quotient conditions beyond this N=2 special instance; determine uniqueness or exhibit incomparable minimally sufficient quotients at N>=3, while keeping common-policy quantifiers and no hidden persistent selector.
