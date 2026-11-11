# R87 — Exact two-polarity champion certificates for all-real latest-source stability

Date: 2026-11-12. Evidence class: author-side theorem and exact finite checks. Predecessor R86: commit 5b4f6fa4f442358fe721e9c2c0eb3b238f588845; R85: f951a675d30d66ffeb72b0080f396f54dfbd66e4. Frozen S23/AV science: 43ec6098b1330ae86d0a7863be336c5d97f6ef34 (unchanged). This is an auxiliary rational circular-source model; no native X6/BRC theorem or authenticated shared Task CLAIM is asserted.

## 1. Domain and exact output

Fix a nonempty rational closed parameter interval I=[L,U], integer observer j, rational x, original integer labels a,b, and a finite set S of distinct source identities (t,branch), with both coordinates integral and ordered lexicographically. For each real theta in I, define source phase s_t(theta)={x+(t-j)theta} and arc endpoints A(theta)={a theta}, B(theta)={b theta}.

Membership M_t(theta) means s_t is in the directed half-open circular arc starting at A and ending at B: [A,B) if A<B, [A,1) union [0,B) if A>B, and empty when A=B. Identical times share the same membership predicate regardless of branch ID.

The latest qualifying source W_S(theta) is the lexicographic maximum present identity (t,branch) with M_t(theta), or NONE below every identity. The required complete all-real output is STABLE_NONE, STABLE(identity), or CHANGES with two exact rational parameters whose latest-source values differ.

For fixed query signature sigma=(I,j,x,a,b,arc convention), define two exact existential polarities for each distinct time t:

- P_t : exists theta in I with M_t(theta), and its rational IN witness when true.
- N_t : exists theta in I with NOT M_t(theta), and its rational OUT witness when true.

They are *existential certificates*, not samples.

## 2. Champion theorem R87.1

Choose the rational probe theta0=L. Let w0=W_S(theta0).

If w0=NONE, W is identically NONE on I iff P_t is false for every present distinct time t. If any P_t is true, its witness theta1 produces CHANGES between (theta0,NONE) and (theta1,W_S(theta1)).

If w0=(t0,b0), W is identically this identity on I iff both conditions hold:

(a) N_t0 is false; equivalently t0 qualifies at every theta in I.

(b) P_t is false for every present distinct time t>t0; equivalently no higher time qualifies anywhere in I.

If either condition fails, its polarity witness theta1 provides CHANGES between (theta0,w0) and (theta1,W_S(theta1)). The actual latest source at theta1 is calculated exactly.

**Proof.** At any theta, the winner is NONE iff no identity qualifies. This proves the first criterion. If w0 is present, then w0 wins at every theta iff it qualifies everywhere and every identity larger than w0 is absent from the qualifying set everywhere. Since w0 is the winner at theta0, any present branch greater than b0 at time t0 would qualify at theta0 too, contradicting maximality; hence no higher branch exists at t0. Every greater identity consequently has a strictly greater time. Those identities are precisely handled by condition (b). Failure of (a) removes w0 at a rational OUT witness, while failure of (b) inserts a greater qualifying identity at a rational IN witness. In either case W differs from w0. Conversely (a) and (b) guarantee no greater competitor and a permanently qualifying w0, regardless of all lower identities. QED.

**Corollary R87.2 (two-polarity cache).** For unchanged sigma, each P_t and N_t is independent of source-set version and of branch multiplicity. Caching their truth values and actual rational witnesses with key (sigma,t,polarity) supports arbitrarily many historical versions and requires at most two exact polarity-oracle calls for each distinct time ever queried. A query needs only P_t for times greater than its chosen champion and N_t for the champion (or P_t for present times when champion is NONE). This is a bound on oracle invocation count, not total CPU/bit/memory costs.

The cached negative universal conclusion (P_t false or N_t false) remains valid under interval restriction, while any positive witness must lie inside the new interval to be reused. Changes to j,x,a,b or the arc convention require the corresponding signature check.

## 3. Exact per-time polarity oracle

For a fixed t, use the R77 integer-crossing families:

1. a theta in Z;
2. b theta in Z;
3. (a-b) theta in Z;
4. x+(t-j)theta in Z;
5. x+(t-j-a)theta in Z;
6. x+(t-j-b)theta in Z.

Each nonconstant rational-affine equation produces finitely many rational cuts in bounded rational I; a zero coefficient contributes no isolated cut. At every cut evaluate M_t exactly, and on each open gap evaluate it at its rational midpoint. Between successive cuts all relevant floor/ordering/sign predicates remain unchanged, and thus M_t is constant throughout the gap. This proves that the finite atom scan returns an IN or OUT witness iff that polarity exists for *some real theta in I*. At A=B, M_t is false by definition and is evaluated accordingly, including singleton intervals.

Combining the complete per-time witness oracle with Theorem R87.1 gives exact STABLE/CHANGES classification over the entire real parameter interval without ever constructing the union of all source-time cuts or an entire merged winner Profile. R71/R84 class-envelope exclusions and R85's memoized source certificates can replace exact calls when their hypotheses apply.

## 4. Work bounds and one discriminating family

Suppose w0=(t0,b0) and h distinct present source times exceed t0. Then R87 needs at most h+1 exact polarity-oracle calls, plus a point-winner computation at theta0 and, on a change, a second point-winner computation at its witness. If w0=NONE, the number of calls is at most the number of present distinct times, with early exit upon a positive witness. The per-time scan can still enumerate many rational integer crossings when input coefficients or the interval are large; no logarithmic end-to-end or bit-complexity bound is claimed.

Consider I=[1/4,1/4+10^-8], j=x=0, a=1, b=2, and present times 1,...,n together with top time 4n+1 (branch 1). At theta0=1/4 the top phase equals 1/4, so the included lower arc boundary is attained. For all theta in I and n<=512, its phase increases by at most (4n+1)*10^-8 while the upper boundary is near 1/2, so the top always qualifies. Theorem R87.1 needs one exact N_(4n+1) oracle and no lower-time oracle, whether n=16,64,256 or 512. The R86-style reference fully constructs n+1 source-time profiles on each such input; the union atomization itself contains only 3 atom representatives because the interval is very short. The avoided work is the construction of lower-time source profiles, not a smaller final union atom count in this family.

## 5. Actual executed reproducibility

Source: check_r87.py (Python standard library Fraction, Random and Counter). Seed 8720261112. The executable independently computes a complete R86-style global critical-cut union profile for each checked version and compares it against the witness-driven champion classification. It verifies actual rational CHANGES witnesses with direct winner evaluation, persistent historical-version snapshots as immutable source sets, negative coefficients and source times, branch ties, equality A=B, and singleton parameter intervals. No floating-point tolerances.

Actual local output: R87_PASS 1280 904 256 1674.

The deterministic run performed 640 identity update steps and 1,280 version/reference classifications: 376 STABLE or STABLE_NONE, 904 CHANGES with checked distinct witnesses, 256 new exact polarity oracle calls and 1,674 cache hits. The independent reference evaluated 36,336 global atom representatives; the champion path evaluated 691 source-specific oracle atoms, plus point-winner evaluations. For the four top-stable families, the champion used one exact polarity oracle and one point test per input; the reference constructed respectively 17,65,257,513 per-time profiles. All assertions passed. Source verifier returns aggregate metrics in verification.json.

The proof of the all-real theorem is the maximality argument of Section 2 together with the finite-cut polarity-oracle completeness in Section 3; executed checks demonstrate implementation agreement on the specified finite workloads and are author-side evidence.

## 6. R88 continuation and control note

Next: combine R82 persistent maximum/time/phase indices with the R87 champion logic, R71/R84 group exclusions and R85 immutable polarity/witness cache. Compare exact STABLE/CHANGES against the R86 baseline on the *same* update histories, measure wall-clock, integer-bit arithmetic, copied nodes, retained historical memory and witness reconstruction; extend to changing intervals with explicit subset transfer rules.

The native session_start attempt returned SESSION_ISSUANCE_QUOTA for this run. The canonical dispatch read selected a separate X6 triadic-closure task; no claimed execution authority on that task is inferred. Therefore R87 is saved as GitHub author-side material on its isolated research branch without a new Researcher-ID/RA/CLAIM/Result/Review. Restore source-native bookkeeping through an actually issued session when the service allows it, without binding the contribution to an old activity.
