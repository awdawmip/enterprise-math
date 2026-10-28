# EC49T: Sharp source-by-source stagewise-cost-neutral face

Status: AUTHOR_PROVED / EXACT_FRACTION_CHECK_PASS / UNREVIEWED / NOT_ADMITTED. This is auxiliary positive-branch BRC mathematics, not native signed BRC, X6 dynamics, a formal CLAIM or an admitted theorem.

Frozen input: GLOBAL_KNOWLEDGE_V1 main@83928001dae4f476462d19195555f336a9b361ee; Enterprise Math main@e87e611f35e068ba9a89e702cf81d292d23f8ac4; EC49S scientific parent research commit 613f00f7a013ce64286aabbdfa32a303726c9477, draft PR #1662. GLOBAL P000 projection's canonical blob 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc matched the actual P000 original blob. P000 and ACTIVE worldview unmodified.

## Model, question and new constraint

Let W=Z={0,1,2}, U={0,1}. Source Q has Q(w,z)=1/9. Source P has P(w,z)=1/6 when z=w and 1/12 otherwise. The first sensor produces U with conditional kernel t_w(u)=1/2+(2u-1) eta sigma_w, sigma=(1,0,-1), 0<=eta<1/2; it is the same under P and Q. Each source has 18 strictly positive joint atoms R(w,u,z)=R(w,z)t_w(u), and both have uniform W marginal. The joint P-Q branch difference is Delta(w,z)=(3 1_{w=z}-1)/36.

A full observer retains W; a compressed observer retains the chosen first action label A/B, one pre-erasure history memory bit D, U and later Z, but not W. The controller may stop/accept/reject, buy A (cost 1) or B (cost 2), then optionally buy S (cost 1) to see Z, and accept/reject. S is unavailable without a first purchase. All randomized decisions use source-independent fresh behavioral coins with no undeclared shared seed. Observable vector O=(alpha,beta,E_P T,E_Q T) records source acceptance probabilities and expected total resource bills. T is not heartbeat time.

Full reference strategy: always purchase A then S, and accept if and only if Z=W. It has four-vector O*=(1/2,1/3,2,2) and difference alpha-beta=1/6; in each of P and Q its expected stage-one and stage-two costs are separately 1.

Define the new constrained compressed policy class C_eta by demanding the SAME expected stage-one cost 1 and stage-two cost 1, separately in P and Q. Equality only of total expected bills would be a different problem.

## Theorem 1: exact all-real cost-neutral support

For every real 0<=eta<1/2,

  max_{pi in C_eta} (alpha-beta) = 1/9 + [6 eta-1]_+/36,

where [x]_+=max(0,x). This maximum is attained by a deterministic source-independent compressed policy.

Therefore the full vector O* cannot be realized by any source-by-source stagewise expected-cost-matched compressed policy. The exact, sharp discrimination gap relative to the full reference is

  g_cost(eta)=1/18                  for 0<=eta<=1/6;
  g_cost(eta)=(1-2 eta)/12          for 1/6<eta<1/2.

In particular, at eta=1/200 the compressed maximum is 1/9 and sharp gap 1/18. At eta=5/12 they are 11/72 and 1/72.

### Proof

**Cost rigidity on this specific face.** Every purchase of S has stage-two cost either zero or one. As the expected stage-two cost is one under P and Q, S is purchased almost surely under both. Thus A or B must be purchased before S on all supported paths. Its minimum stage-one cost is one; expectation one forces first action A almost surely. Positivity of every W,U,Z atom rules out concealing a positive-probability exceptional history. Consequently the cost constraints force pathwise costs (1,1); the compressed policy's only remaining information-bearing choice before U is a binary memory D chosen as a stochastic function of W. All terminal acceptance rules are still unrestricted.

For a single common source-independent encoding e(d|w) and terminal acceptance probability a(d,u,z), the difference is

  delta(e,a) = sum_{d,u,z} a(d,u,z) sum_w e(d|w)t_w(u)Delta(w,z).

The same e and a appear in P and Q. For fixed e the optimal terminal mask chooses a=1 precisely when its bracket is positive. Hence

  max_a delta(e,a)
    = sum_{d,u,z} [sum_w e(d|w)t_w(u)Delta(w,z)]_+.

As a function of e this is convex (a sum of positive parts of linear forms). On the product of three binary encoding simplices a maximum is achieved at a vertex, so evaluating eight deterministic maps W->D proves the bound for all real behavioral randomization; it does not extrapolate a numerical grid.

A deterministic D partitions the three W values into up to two nonempty fibers. If a fiber is a singleton {w}, its contribution is 1/18. If a fiber is a pair {i,j}, its possibly positive Z coefficients for each u are (2t_i(u)-t_j(u))/36 and (2t_j(u)-t_i(u))/36; the third is negative. Its exact positive sum, over both values of u, is

  1/18 + (sum_u ([t_i(u)-2t_j(u)]_+
                   + [t_j(u)-2t_i(u)]_+))/36.

For {0,2}, this extra numerator is [6 eta-1]_+. For {0,1} and {1,2}, it is [2 eta-1/2]_+. The first is at least the others for eta>=0. A partition of type singleton+pair thus contributes at most

  1/18+1/18+[6 eta-1]_+/36 = 1/9+[6 eta-1]_+/36.

If all three histories share D, direct summation yields eta/6. That is smaller than the preceding value for all 0<=eta<1/2. The eight deterministic maps are exhausted, proving the universal upper bound.

For eta<=1/6, take D=0 for W=0 and D=1 for W=1,2; after A+S accept Z=0 in D=0 and Z in {1,2} in D=1. This yields O=(2/3,5/9,2,2), hence delta=1/9. For eta>=1/6, take D=0 for W=0,2 and D=1 for W=1; accept Z=0 when D=0,U=1; accept Z=2 when D=0,U=0; accept Z=1 when D=1. This yields O=(5/12+eta/6,1/3,2,2), hence delta=1/12+eta/6. The two branches meet at eta=1/6, proving sharpness. The full reference delta=1/6 exceeds this for all eta<1/2. QED.

## Theorem 2: terminal event fiber criterion

Let F map finite fully supported terminal traces to compressed observations. A deterministic full-terminal event E is exactly reconstructible as a compressed deterministic event e(F(trace)) on every positive P/Q source trace if and only if E is constant on each nonempty fiber of F. The same fiber condition is necessary and sufficient for a stochastic compressed acceptance to equal E almost surely under both strictly positive source laws: an identical observable report cannot require acceptance with probability 1 and probability 0 at the same time.

Proof: define e by the common label on a fiber for sufficiency; two same-fiber traces with conflicting labels refute necessity, even with randomized e. QED.

Here any binary D encoding of three W histories merges two W values (or stochastic encodings have overlapping D support for two). Strict positivity of both U outcomes and all Z values means, on a shared (A,D,U,Z=i) report, the event E={Z=W} has opposite labels for W=i and another W=j in the same fiber. Pathwise cost neutrality does not make E measurable. More strongly, Theorem 1 proves that **even its two acceptance probabilities cannot both be matched** by any cost-neutral compressed policy. Eventwise obstruction and scalar separation are separate facts.

## Theorem 3: sufficient causal trace-simulation contract

Fix any finite-horizon pair of positive source laws on a common causal branch tree. Suppose every full-history policy admits an allowed source-independent compressed controller and a causal coupling such that: (a) the source-conditioned transition kernels for subsequent observations and actions are preserved at each step; (b) all required terminal observers are decoded from the compressed trace almost surely; and (c) each incremental resource bill agrees pathwise. Then, by induction over the finite stages, the joint terminal observer distributions under P and Q and the two source-specific expected resource totals agree exactly. Every full four-vector belongs to the compressed region; if full policies can simulate all compressed policies, the regions are equal.

This is only a sufficient criterion; no necessity for equality of *four scalars* is claimed. Matching source-expected costs alone supplies neither (a) nor (b). The event/trace contract is naturally stronger than equality of four aggregate numbers.

## Evidence and limits

VERIFY.py was actually executed using Python standard-library fractions.Fraction. Each test eta uses 18 positive P atoms, 18 positive Q atoms, eight binary deterministic encoders and exact optimization over the 12 (D,U,Z) report atoms. Seven eta values were checked: 0, 1/200, 1/6, 1/4, 1/3, 5/12 and 49/100. Every exact assertion passed, as recorded in EXACT_REPORT.json. All-real conclusions follow from the explicit analytic convexity/partition proof above, not finite tests. No Lean/formal checker or independent Driver review was run.

Typed BRC scope: P and Q are preserved as separate positive branch laws over ordered W->(action,U)->(S,Z) histories; the common encoding and terminal acceptance decision are source-coupled, with two source-specific resource readouts. P-Q is an external comparison of those positive measures, not a native signed/phase BRC primitive. No mapping to six-dimensional X6, its three-dimensional slice or heartbeat evolution is established.

The 18-atom counterexample is not claimed minimal. The stagewise-cost-matched face here is rigid; to study a genuinely non-pathwise expected-cost compensation one must relax the target costs to a nondegenerate interior budget, as stated in EC49U. No full semialgebraic region characterization or arbitrary multi-stage necessary-and-sufficient observer equivalence follows.
