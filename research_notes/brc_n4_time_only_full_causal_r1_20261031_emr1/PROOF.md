# BRC N=4: sharp one-code time-only radius for the full causal S2/S23 grammar

Date: 2026-10-31. Status: **AUTHOR_ANALYTIC_PROOF / EXACT_INTEGER_EXECUTED / UNREVIEWED / NOT_ADMITTED**. This is a portable author-side mathematical continuation of Enterprise Math PR #1757 at immutable predecessor e30ebcffd8263842b1e6646e2fe16762a65935ce. It is a theorem about the stipulated positive-rational sixteen-leaf experiment, not about a native Heartbeat X6 physical evolution.

## Full causal model and quantifiers

The original P/Q source on (S,J,K), S in {AU,AV,BU,BV}, J,K in {0,1}, has per-K mass numerators over 240:
- Q: AU (10,10), AV (20,20), BU (15,15), BV (15,15).
- P: AU (9,11), AV (5,5), BU (3,27), BV (30,30).

The eight conditioned preparations i=(S,P/Q) have J rows AU_Q=(1/2,1/2), AU_P=(9/20,11/20), AV_Q=AV_P=(1/2,1/2), BU_Q=(1/2,1/2), BU_P=(1/10,9/10), BV_Q=BV_P=(1/2,1/2); K stays fair. The complete original *causal* timing grammar includes stopping at T=1,2,3,4. At time 1, A and B have separate continuation decisions. At time 2, AU/BU have the same conditional behavioral kernel, while AV and BV have their own. At time 3, S23 ties coincident likelihood-ratio histories and S2 allows the larger valid behavioral language. Decisions P/Q, K, and the BU sensor Z are discarded by the present observer Y=T. Every policy kernel is law-independent and its current information sets are preserved; no original S or P/Q label is newly revealed to the decoder.

For F equal to S23 or S2, define
  R_1^adapt(T;F) = inf_(one-symbol E) sup_(H in F) inf_(probability decoder d_H) max_(eight i) TV(P_i^H(T),d_H).
The encoder is necessarily constant, but d_H may depend on H. Define the stronger fixed-decoder order
  R_1^fixed(T;F) = inf_d sup_(H in F) max_(eight i) TV(P_i^H(T),d).
The decoders output distributions, not the actual hidden sample paths. Epsilon in [0,1/2] affects only the erased sensor.

## Theorem 1: exact unrestricted adaptive-decoder radius

For **every real epsilon in [0,1/2]** and both full original lawful causal families S23 and S2,
  **R_1^adapt(T;F) = 2/3.**

### Upper bound, including time-one stopping

First consider a deterministic complete policy table. Its first-stage A/B continuation decisions are binary.

Case I: both A and B continue. Every prepared time law is supported on {2,3,4}. The common decoder d=(delta_2+delta_3+delta_4)/3 has overlap at least 1/3 with every input law, so the total-variation error is at most 2/3.

Case II: both A and B stop. Every time law is delta_1, and the exact decoder delta_1 has zero error.

Case III: exactly one of A and B continues. All preparations under the other prefix produce delta_1. There are two surviving sibling source types: AU/AV when A continues, or BU/BV when B continues.

If both siblings stop at time 2, d=(delta_1+delta_2)/2 yields error at most 1/2. If both reach time 3, all surviving laws are supported on {3,4}; d=(delta_1+delta_3+delta_4)/3 yields error at most 2/3.

If exactly one sibling stops at time 2 and the other reaches time 3, use an equal three-way mixture
  d=(delta_1+delta_2+nu)/3,
where nu is a time-{3,4} probability law that is dominated after scaling by 1/3 by **each** preparation of the surviving source. If the continuing sibling is AV or BV, its P and Q conditioned J laws coincide, so choose nu to be their common pushed-forward time law. If it is AU, take the reference J law v_AU=(19/40,21/40); if it is BU, take v_BU=(1/5,4/5). In each case
  (1/3) v_S(j) <= min(L_(S,P)(j),L_(S,Q)(j)) for j=0,1.
The same subsequent law-independent time kernel pushes this pointwise domination to (1/3)nu <= P_(S,P)^H(T),P_(S,Q)^H(T). The stopped prefix has at least decoder mass 1/3 on T=1, the time-two-stopped sibling at least 1/3 on T=2, and either continuing preparation overlaps (1/3)nu. Their total-variation errors are therefore at most 2/3.

These cases exhaust all first- and second-stage deterministic stop/continue choices. Later S2/S23 decisions, including dependence on currently legal information, affect only the law on {3,4}; the common reference kernel argument does not constrain them beyond law independence.

Finally, an arbitrary lawful instantaneous behavioral randomized policy is a law-independent convex mixture of complete deterministic contingent policy tables: sample each node's behavioral action in advance, with the same plan-distribution for all eight inputs. For each pure table h select the decoder d_h constructed above. For its mixture H with plan weights lambda_h, choose d_H=sum_h lambda_h d_h. Then for every preparation i,
  TV(sum_h lambda_h P_i^h(T), sum_h lambda_h d_h)
     <= sum_h lambda_h TV(P_i^h(T),d_h) <= 2/3.
This handles all real behavioral randomization probabilities, zero-probability histories and all full S2/S23 actions, not only a finite deterministic S23 subfamily.

### Matching lawful lower witness

Use H_dagger: continue A and B at time 1; at time 2 stop AV, continue AU/BU and BV; at time 3 stop AU and BU and continue BV until time 4. All terminal Decisions can be fixed, and neither J nor future K is read illegally. AU/BU time-two actions agree; the time-three choices respect S23 likelihood-ratio classes, so H_dagger belongs to both families. Three legitimate preparations yield
  AV_Q -> delta_2; AU_Q -> delta_3; BV_Q -> delta_4.
For any common one-code decoder d, min(d(2),d(3),d(4)) <= 1/3, and the largest of the three true-versus-decoded TV distances is at least 2/3. This establishes the lower bound, completing Theorem 1.

## Theorem 2: a strict decoder-quantifier gap

When the decoder must be **fixed before the lawful policy is chosen**, both policy families and every epsilon satisfy
  **R_1^fixed(T;F) = 3/4.**

Each of the four deterministic all-source policies "stop everyone at time t", for t=1,2,3,4, is lawful: choose common first-stage, second-stage and third-stage stop/continue actions as necessary. These policies produce delta_t for every preparation. Any fixed decoder d must obey
  sup_(t=1..4) TV(delta_t,d)=1-min_t d(t)>=3/4.
Conversely uniform d=(delta_1+delta_2+delta_3+delta_4)/4 gives TV(P,d)<=3/4 for every probability law P on the four-time alphabet. Equality follows.

Thus the two infimum/supremum orderings are genuinely different:
  policy-dependent one-code decoder 2/3, policy-independent one-code decoder 3/4.
The prior all-policy k>=2 result for time-recoverable observers, at the same frozen source, remains R2=R3=1/2, R4=1/5, R5=1/40 and Rk>=6=0 (author-side predecessor, not independently admitted).

## Exact validation and boundaries

The actual executed VERIFY.js uses integers with denominator 120 for every scored time law and decoder. It rechecks the 16 strictly positive leaves under each law, then enumerates 4 first-stage A/B timing tables × 8 second-stage AU/BU-tied timing tables × 64 third-stage S23 likelihood-ratio-class stop/continue tables = **2048 deterministic timing policies**, for **16384 preparation-policy comparisons**. Each selected constructive decoder has exact TV<=2/3, and the fixed uniform decoder exact TV<=3/4; both sharp witnesses are checked. These finite tests cover the stated deterministic S23 timing projection. Universal randomized S2/S23 coverage and continuous epsilon are supplied by the analytic domination and behavioral-mixture proof, not an extrapolation from 2048 cases.

The experiment is a finite positive-weighted BRC provenance model. The observer Y=T is a lossy distributional readout; it need not preserve future-operation composition or samplewise source identity. Native P000 X6 six-axis Cell, triadic closure, separate physical time, and observer-future-operation-preserving correspondence remain distinct unproved bridge obligations. Mathematical independent review and Source admission are pending.
