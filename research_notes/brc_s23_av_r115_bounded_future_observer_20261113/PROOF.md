# R115 — Finite-horizon future observers and exact saturation for S23 ranked histories

Date: 2026-11-13. Author-side mathematical continuation of R114. Research scope: finite source-identity/rank/Boolean eligibility carrier, not a native Cell/Link/Port claim. Independent review pending.
Frozen scientific input: 43ec6098b1330ae86d0a7863be336c5d97f6ef34.
Parent verified R114: a5164fbc655dd09aa3fb681cca48d1f1003c5f78, research_notes/brc_s23_av_r114_future_stable_time_atoms_20261113/PROOF.md.

## 1. Typed setup

Let U be a finite universe of full identities u=(t,b), strictly ranked. The eligibility M_u(theta) depends only on time t. Let a history pair x=(F,G) have F,G subsets of U. For any parameter theta, define h_x(theta) as the number of eligible common identities above the highest-ranked eligible symmetric-difference identity. If there is no eligible difference, set h_x(theta)=infinity. From R112, for every integer k>=1:

Top_k(F,theta)=Top_k(G,theta) if and only if k<=h_x(theta).

For all-k equality observers, equality of capacity values, including infinity, is therefore exactly equality of all k comparison truth values.

An allowed primitive edit toggles membership of one complete identity in exactly one of F or G. For starting x=(F,G), let S_H(x) be all pairs reachable in at most H edits. Because edits toggle membership bits, this is exactly the Hamming ball:

S_H(x)={ (F',G') : |F triangle F'|+|G triangle G'|<=H }.

Define theta ~_H^x phi if and only if h_y(theta)=h_y(phi) for every y in S_H(x). Let sigma_U(theta)=(M_t(theta))_{t in T(U)}.

## 2. R115.1 — Coarsest bounded-future observer and refinement

For every nonnegative integer H, the vector

V_H^x(theta)=( h_y(theta) )_{y in S_H(x)}

is a coarsest sufficient observation for **all** Top-k equality questions following at most H permitted edits from x. Its image cardinality is the minimum possible number of deterministic abstract parameter states that answer all those questions without further access to theta or omitted eligibility information.

Proof: A matching vector answers each reachable equality question for every k by the capacity equivalence above. If two vectors differ at some y, their finite/infinite capacities differ; there is a positive integer k at which their equality answers differ. Any exact observer must separate that pair. The vector therefore has precisely the required observational kernel. As S_H subset S_(H+1), the relations ~_(H+1) refine ~_H, and the number of classes is nondecreasing. Because capacities are functions of sigma_U, no horizon distinguishes two parameters with equal sigma_U. This retains the exact distinction between a history-specific capacity observer and an unrestricted-future eligibility observer.

## 3. R115.2 — Constructive finite saturation bound

For a time t, define

rho_t(F,G) = min over u=(t,b) in U of
  min( |F triangle {u}|+|G|, |F|+|G triangle {u}| ).

Let H_star=max_{t in T(U)} rho_t(F,G), and let H_star=0 when U is empty.

Then for all theta,phi and all H>=H_star:

theta ~_H^x phi  if and only if sigma_U(theta)=sigma_U(phi).

Proof: For each t choose an identity u attaining rho_t. At cost rho_t we reach either ({u},empty) or (empty,{u}). There is exactly one possible difference and no common source. Its capacity is 0 when M_t(theta) holds and infinity otherwise. Thus the observer recovers that eligibility bit. Doing this for every t recovers sigma_U. Conversely identical sigma_U yields identical capacities in every history. In particular H_star <= 2|U| (the diameter of the complete pair-state hypercube). H_star is a constructive sufficient bound; earlier saturation is possible.

**One-edit collapse at equal histories.** If F=G and each identity may be toggled on either side, then H=1 already recovers sigma_U: toggle u in one history. The resulting symmetric difference is exactly {u}, so its capacity is finite if and only if M_t(theta) is true, irrespective of the other common identities. At H=0, capacity is infinity identically. If sigma_U has at least two realized values, one edit is both necessary and sufficient.

## 4. R115.3 — Sharp delayed-observation witness in the directed fractional-circle family

Use the exact S23 directed half-open arc observer on I=[0,1], with Y_t(theta)={1/4+t theta}, A(theta)=0, B(theta)={theta}, and M_t(theta): Y_t(theta) lies on the positive directed fractional arc [A,B), with equal endpoints interpreted as empty. Let U consist of t=-2,-1,0,1,2 and b=0,1, ranked descending by (t,b), and start with F={(2,1)}, G=empty.

Take theta=3/8 and phi=25/48. Direct exact fractional evaluation in time order (-2,-1,0,1,2) gives

sigma_U(3/8)=(0,0,1,0,1)
sigma_U(25/48)=(1,0,1,0,1).

The top source (2,1) is eligible at both parameters. With at most one primitive edit, that top difference either remains present, in which case the lower differing eligibility cannot affect the highest eligible difference, or the top difference is removed, leaving no differences. Therefore all reachable capacities match and theta ~_1^x phi. At two edits, remove (2,1) from F and add (-2,0) to F, reaching ({(-2,0)},empty), whose capacity is infinity at 3/8 and zero at 25/48. Thus theta is not ~_2^x phi. This is an exact counterexample to the proposition that a one-edit horizon always recovers full future eligibility from arbitrary unequal starting histories.

## 5. Exact verification and implementation

Executable standalone Python 3 script: check_r115.py. Uses fractions.Fraction only. Verification data: verification_r115.json. Deterministic exhaustive tests use:
- U with five time buckets {-2,-1,0,1,2} and two full identities each; exact I=[0,1] cut partition from all six affine integer-crossing forms, with endpoint singletons and rational open-gap midpoint representatives;
- 8 distinct interior critical cuts, 19 parameter atoms and 10 realized eligibility signatures;
- five initial history pairs with observed class counts by edit distance (until signature saturation):
  - empty histories: [1,10] (H=1 saturation);
  - equal full histories: [1,10] (H=1 saturation);
  - single top difference: [2,7,10] (H=2 saturation);
  - single lowest difference: [2,7,10] (H=2 saturation);
  - asymmetric split histories: [2,6,6,7,7,10] (H=5 saturation).
- all 64 starting history pairs over a smaller three-source identity universe; complete radius H=0,...,6;
- 4,864 independent direct Top-k tuple oracle comparisons;
- 23 pairs of distinct-signature exact parameter atoms indistinguishable at horizon <=1 in the single-top starting history, including the displayed witness.

The rational representatives use at most 5 numerator bits and 6 denominator bits in this test. These counts establish the precise finite test scope. General mathematical statements are proved in sections 2–4; this implementation enumerates reachable states, not an optimized persistent balanced tree. The program implements the all-k capacity observer and reports no native 6D event semantics or asymptotic performance gain.

## 6. Relation to source/authority and next unit

This is author-side auxiliary science. Source activity and official Task CLAIM, result freeze, and independent mathematical review are separate from GitHub research-note persistence. Respect the frozen source pin above. BRC/Heartbeat arithmetic restrictions retain their exact native scope; the fractional-circle Boolean/rank model here is the pre-existing explicitly auxiliary S23 carrier.

Next R116: design a persistent partition-refinement data structure that updates H-bounded observer signatures when the allowable edit alphabet/horizon changes, with exact rational cut insertion/deletion and cost accounting for bit operations, preprocessing, old roots, memory and witness restoration. Test whether S23 same-time coupling yields tighter constructive saturation bounds than the general rho_t witness bound.