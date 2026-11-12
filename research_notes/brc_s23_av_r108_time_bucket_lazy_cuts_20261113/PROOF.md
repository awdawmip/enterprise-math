# R108 — Exact time-bucket rank shielding and demand-driven rational phase cuts

Date: 2026-11-13 Asia/Shanghai. Auxiliary BRC S23 finite rational directed-circle model. Scientific input remains frozen at 43ec6098b1330ae86d0a7863be336c5d97f6ef34. This continues the R107 author-side proof at enterprise-math commit daec398e9161d853cea0dc25e91585dc47319384; it neither modifies P000 nor asserts a physical/native-X6 bridge.

## Definitions

A complete source is u=(t,b) in Z², ordered descending lexicographically by time t then branch b. Fix sigma=(j,x,a,c), where j,a,c are integers and x is rational. For theta real, M_t(theta) means that the fractional part of x+(t-j)theta lies in the half-open circular arc directed from {a theta} to {c theta}; equal endpoints yield the empty arc. The branch b determines identity and rank but not membership. Top_k(F,theta) is the descending list of up to k eligible complete identities from finite F, for integer k>=1.

Let C=F∩G and Delta=F△G. For every t appearing in Delta let d_t be the highest branch among discrepant identities at t; let c_s be the number of common complete identities at time s; let r_t be the number of common identities (t,b) with b>d_t. Define H_t(theta)=sum_{s>t} c_s*1[M_s(theta)].

## R108.1 — Time-bucket equality criterion (exact iff)

For every real theta and k>=1:

Top_k(F,theta)=Top_k(G,theta)  iff  for every discrepant time t,
M_t(theta) implies H_t(theta)+r_t>=k.

**Proof.** The R104 rank-shield lemma gives an exact pointwise iff: every currently eligible discrepant identity u must have at least k eligible common identities ranked strictly higher than u. For u=(t,b), higher common identities consist of all common eligible identities with time s>t, exactly H_t(theta), and those at the same time with branch strictly greater than b. All discrepant identities at time t have the same membership M_t(theta). Their same-time higher-common count is smallest at the largest discrepant branch d_t, where it is r_t. Consequently the single condition on that highest branch is necessary and sufficient for all discrepancies at t. Apply the pointwise rank-shield lemma. Every identity and its branch is preserved; time-bucketing only factors repeated eligibility evaluations. QED.

**Exact point-query algorithm.** Index distinct source times descending. Cache the common-identity count at each time and r_t for each discrepant time. Scan the times descending, evaluate eligibility once per distinct time and accumulate the number of higher eligible common identities. At eligible discrepancy times compare the accumulator+r_t with k. One point query uses O(m) membership evaluations and integer additions for m distinct times, after O(n log n) comparisons to build the reference sorted index for n complete identities. Rational bit-operation complexity is charged separately; the original complete identities remain available for exact output/witness recovery.

## R108.2 — Same-time zero-phase certificate

If r_t>=k for every discrepant time, Top_k(F,theta)=Top_k(G,theta) **for every real theta and every admissible observation sigma**. No phase evaluations, rational cutpoints or interval enumeration are needed for this certificate.

**Proof.** Whenever a discrepant (t,b) becomes eligible, its r_t higher-ranked common identities at that same time become eligible simultaneously because eligibility is independent of the branch. Therefore the R108.1 implication holds for all real theta. Ineligible discrepancies are harmless. QED.

**Asymptotic separation.** For any integer T>=4, take F_T={(T,0),(T,1)}, G_T={(T,1)}, k=1, sigma=(0,1/4,0,1) and I=[1/4,3/4]. The common (T,1) always shields the discrepant (T,0), so the two Top-1 functions are identical on all R. A zero-phase comparison certificate uses constant identity information of O(log T) bits. By the R107.3 construction, the one-source time-T eligibility function has Omega(T) transitions over I. Thus the explicit-function output lower bound and the compressed equality-certificate upper bound coexist. This is a precise comparison-specific benefit, not a claim that the oscillating individual source can be explicitly listed in sublinear output time.

The certificate survives adding an arbitrary identical source set to both versions by R107.2. A later asymmetric deletion or branch change must re-evaluate the affected common-rank counts or use the R106/R107 guarded update; the original identity arrays are not discarded.

## R108.3 — Exact successor of a rational affine phase boundary

For f(theta)=c theta+d, c a nonzero integer and d rational, and rational q, the first z>q satisfying f(z)∈Z equals

- (floor(cq+d)+1-d)/c if c>0;
- (ceil(cq+d)-1-d)/c if c<0.

**Proof.** If c>0 the first integer strictly above f(q) is floor(f(q))+1. If c<0 the first integer strictly below f(q) is ceil(f(q))-1. Since f is strictly monotone, solving the corresponding affine equation gives exactly the next crossing beyond q. Strict inequality also handles q itself being a crossing. QED.

R107's sufficient cut family is given by integer crossings of the six forms aθ, cθ, (t-j)θ+x, (t-j-a)θ+x, (t-j-c)θ+x and (a-c)θ. Duplicate forms for branches at a common time are needed only once. Given interval [L,U], taking the minimum of the R108.3 successors for all nonconstant distinct forms and U obtains the next exact phase cut from the current rational position without enumerating all cuts globally. Each singleton cut and midpoint of adjacent cuts is a valid exact atom representative. A demand-driven sweep can stop when the first failure of R108.1 is detected and return that representative as an exact rational inequality witness. The simple reference sweep performs O(pm) successor candidate computations for p visited cut advances and m distinct times, plus exact point checks and rational bit operations. Equality may require visiting every cut if no shorter certificate applies.

## Verification and evidence

The full standard-library Python checker is stored as check_r108.py.gz.b64; decode using base64 and gzip. It uses fractions.Fraction for mathematical arithmetic. Its direct oracle enumerates every eligible complete source and sorts identities; its independent finite-domain cut oracle enumerates integer crossings of all forms, while the streaming algorithm uses exact floor/ceil successors. Seed=108. Recorded execution: R108_PASS 420 54748 27164 180.

- 420 generated finite version pairs and all 54,748 rational singleton/gap representatives agree with the full-identity oracle; 47 pairs were equal and 373 produced an exact Fraction inequality witness.
- All 27,164 exact successor advances match an independent brute cut enumerator in their finite tested ranges.
- 180 constructed zero-phase time-bucket certificates were checked with 1,620 additional exact point comparisons.
- Tested large source times include 10003, 100000007 and 100000000000000000039, with zero phase cuts for the equality lease.
- Same-time branches are retained in Top-k output, including a k=2 versus k=3 rank distinction.

Finite tests validate the reference program in their declared domain; R108.1–R108.3 are established by the symbolic proofs above. The auxiliary parameter theta and source index t are not claimed to be Heartbeat World's physical time or a native spatial axis.

## Frontier

R108 improves R104–R107 by reducing repeated branch eligibility to exact time buckets, deriving a zero-phase rank certificate and generating phase cuts on demand. The immutable per-version index and sweep are implemented; a general persistent balanced interval-certificate DAG with lazy split/merge and memory/bit-cost accounting remains an open engineering/mathematical unit. R109 should couple time-bucket certificates with a persistent balanced map of only visited rational boundaries, measure changed-range invalidation under edits, historical memory and exact witness recovery, and compare against R103 net-edit overlays and R107 full refinement.

Original R107 frozen science: daec398e9161d853cea0dc25e91585dc47319384. Formal task RS-S23-AV currently returns NO_CURRENT_IMMUTABLE_PUBLICATION on native exact lookup; no formal CLAIM/review is asserted by this author-side result.
