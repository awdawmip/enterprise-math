# R749N — Noisy C1 source retention: exact block likelihood, sufficient statistic, reversible memory, rational posterior

Date: 2026-11-12. Status: AUTHOR-PROVED / EXACT FINITE CHECK / UNREVIEWED / NOT ADMITTED. Independent author-side extension of R749, whose pure p=0 law is consumed, not recredited. Parent Task RS-X6-TRIADIC-CLOSURE-DYNAMICS has another active Source owner; this work makes no claim/open/Result or Driver assertion. Frozen mathematical input awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389; predecessor R749 PR #2165 and R748 PR #2163. The present finite candidate is not a native TRIADIC_CLOSURE_E, V29 PASS or V39 event law.

## Exact finite model

Let S={(i,±1):i=0,...,5} be 12 signed native Port labels and V the 60 unordered pairs of Ports with distinct axes. Adjacency u~v means one identical shared signed Port and a union of exactly three distinct axes. Every v has 16 neighbors; the directed-edge carrier D={(u,v):u~v} has 960 elements. For every directed edge, f(u,v)=u△v is its unique retained-source successor, and f(f(u,v),v)=u. For fixed v, f(·,v) permutes the 16 neighbors.

For a parameter p in [0,1], select initial (Z0,Z1) uniformly in D. Given (Z_(t-1),Z_t)=(u,v), with probability p select the retained successor f(u,v), otherwise draw uniformly from all 16 neighbors of v. Write q=(1+15p)/16 and r=(1−p)/16, so q+15r=1; the forced successor has probability q, and each of the 15 alternatives has probability r. Thus p=1 gives retained C1, while p=0 gives independent neighbor resampling. The interpolation is a typed candidate probabilistic law only.

## Theorem 1 — Stationary one- and two-point observations do not identify p

For every p, the uniform distribution on the 960 directed edges is stationary. For a target (v,w), the 16 incoming edges (u,v), u~v, include precisely one forced predecessor because f(·,v) is involutive; their total incoming transition probability is q+15r=1. Therefore the directed transition matrix is doubly stochastic. The stationary vertex law is uniform on 60 vertices and the consecutive ordered pair law is uniform on 960 directed edges. The one-step observed conditional P(Z_(t+1)=w | Z_t=v)=1/16 for w~v for every p, even when p>0 is not first-order Markov.

## Theorem 2 — All-horizon block likelihood and a one-integer sufficient statistic

For n≥2 put m=n−2. Let z=(z0,...,z_(n-1)) be any legal adjacent n-block and define

K(z)=sum_(t=2)^(n-1) 1{z_t = z_(t-2)△z_(t-1)}.

Exactly C(m,k)=960 binom(m,k) 15^(m-k) legal n-blocks have K=k. Each such path has probability P_p(z)=q^k r^(m-k)/960.

Proof: choose the initial directed edge (960 choices), the k time slots for forced completion, and one of 15 alternatives independently at every other slot; this is a bijective encoding. Multiplying transition probabilities gives the likelihood. At each time, the forced-completion indicator has conditional success probability q independent of all past states; the indicators are therefore iid Bernoulli(q). Hence K~Binomial(m,q).

For any p,p' in (0,1), the full-path likelihood ratio is (q/q')^K (r/r')^(m-K). Conditional on K=k, all full legal blocks have the same distribution independent of p, so K is sufficient for testing/estimating p. Including boundary p=0,1, the exact total variation is the total variation of two binomials:

TV(P_p^(n),P_p'^(n)) =
  (1/2) sum_(k=0)^m | binom(m,k) q^k (1-q)^(m-k)
                       − binom(m,k) q'^k (1-q')^(m-k) |.

For interior p,p', base-two relative entropy equals

D2(P_p^(n)||P_p'^(n)) = m[q log2(q/q')+(1-q)log2((1-q)/(1-q'))].

In particular for retained p=1 versus p∈[0,1]:

TV(P_1^(n),P_p^(n))=1−q^(n-2),
equal-prior optimal Bayes error=q^(n-2)/2,
D2(P_1^(n)||P_p^(n))=(n-2)log2(1/q).

At p=0 this reduces precisely to R749: TV=1−16^(−(n−2)) and D2=4(n−2) bits. Sufficient K for parameter inference is not a sufficient state for general future path/Port/BRC queries.

## Theorem 3 — Exact predictive memory threshold and conditional information

Set h(p)=−q log2(q)−15r log2(r), with 0 log 0=0. Then

H(Z0,...,Z_(n−1))=log2(960)+(n−2)h(p),
H(Z_(t+1)|Z_t)=4 bits,
I(Z_(t+1);Z_(t−1)|Z_t)=4−h(p).

The conditional mutual information varies continuously from 0 to 4 bits as p increases from 0 to 1. Nevertheless, for every p>0 and fixed current v, each of the 16 possible previous neighbors u gives a **different exact next-step distribution**: its unique preferred neighbor f(u,v) has mass q>r. Thus exactly 16 distinct conditional predictive classes exist given v, so four additional fixed-length bits are necessary and sufficient for lossless next-state prediction. When p=0, all 16 distributions coincide and the process is genuinely first-order Markov.

Proof: the stationary initial edge entropy is log2(960), each later transition has the same conditional entropy h(p), and the current-only next neighbor is uniform by Theorem 1. The Markov law and injectivity of f(·,v) establish sufficiency and the sharp class lower bound.

## Theorem 4 — All finite stationary blocks are time-reversal invariant

The probability of a legal block is q^K r^(m-K)/960. In every legal triple (u,v,w), f(u,v)=w iff f(w,v)=u, by cancellation of symmetric difference. Therefore K(z) is invariant under reversing z; hence for every p,n, P_p(z0,...,z_(n−1))=P_p(z_(n−1),...,z0). The result concerns a stationary finite observer candidate, not a physical native time-arrow law.

## Theorem 5 — Exact rational online post-allocation for unknown retention p

Give p a uniform prior on [0,1]; equivalently q is uniform on [a,1] where a=1/16. After m observed transitions, k of which were retained, the posterior density of q is proportional to q^k(1-q)^(m-k) on [a,1]. Let for integers A,B≥0

J(A,B)=sum_(j=0)^B (-1)^j binom(B,j) [1-a^(A+j+1)]/(A+j+1).

This is the exact rational integral of q^A(1-q)^B from a to 1. The posterior mean preferred-neighbor probability is J(k+1,m-k)/J(k,m-k); each other neighbor has posterior mean probability [1-E(q)]/15. At (m,k)=(0,0), (1,0), (1,1) the means are 17/32, 3/8 and 91/136 respectively. Thus (k,m) exactly records the parameter-learning residual while (u,v) records the source-location predictive residual. The combined state (u,v,k,m) is sufficient for exact one-step Bayesian prediction. The calculation uses finite binomial expansion and rational arithmetic, no numerical approximation.

## Finite verification and next genuinely new question

Companion Python checker R749N_NOISY_C1_EXACT_CHECK.py rebuilds the 60 states and 960 edges; checks unique completion, all incoming transition positions, exhaustive legal n=2,3,4 blocks (960, 15360, 245760), exact match-count histograms, reversal invariance on every block, rational probability normalization for p∈{0,1/4,1/2,1}, and rational posterior for m≤3. Exact output: R749N_NOISY_C1_EXACT_RESULTS.json. Universal all-n and all-p statements follow from the displayed proofs.

For n=4 the number of paths with K=(0,1,2) is (216000,28800,960). At p=1/2, q=17/32 and K probabilities are (225/1024,510/1024,289/1024); TV relative to pure C1 is 735/1024.

The next mathematical discrimination concerns genuinely permitted native Cell/Link/Port interactions: find one frozen-input TRIADIC_CLOSURE_E plus V29 PASS/V39 transition witness, compute whether its source observer factors through this 16-neighbor completion and whether K-only statistics remain safe under branch/provenance-sensitive future operations. No existing source owner is displaced.
