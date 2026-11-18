# S23/AV: the logarithmic factor is intrinsic to full-box reconstruction

Date: 2026-11-07. Status: author-side mathematical proof, independent review pending.
Frozen scientific input: awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34.
Predecessor: PR #1777 at b7552f25ec549eab04952b772d16a33947ee0a13 (five-fiber Hoeffding bound). This resolves the open order-of-convergence question in that note for the *complete lawful AV auxiliary box*. Mother-model transfer remains a distinct problem.

## Exact experiment and theorem

For a,c ∈ [1/2,7/8], set z=(1-a)c, b=1-a-z. Let P_(a,c)=(a,z,b) on ordered labels (1,3,4), and B_(a,c)=(z,1-z) on compressed letters (Y,N). Given one shared unknown (a,c), take n conditionally independent runs. Define

δ_n = inf_{L:{Y,N}^n → {1,3,4}^n parameter-independent stochastic} sup_{a,c} TV(P_(a,c)^{⊗n},B_(a,c)^{⊗n}L).

**Theorem.** For every integer n ≥ 20000,

1 - (28/3) sqrt(log n/n) - 2/n² ≤ δ_n ≤ 1 - [(1-exp(-n/128))/40] sqrt(log(n/2)/n).

Consequently, 1-δ_n = Θ(sqrt(log n/n)) as n→∞. The left bound is the predecessor's fixed-fiber packing theorem, used at its proved scope; the new right bound is established below by one universal stochastic decoder valid across the entire legal box. The full experiment keeps all 3^n ordered outputs, not only a coarse histogram.

## Universal count-uniform decoder

Given a binary input word y, put label 3 at exactly the positions where y=Y. Let M be the number of remaining positions. Draw K uniformly from {0,...,M}, choose uniformly one K-subset of the remaining sites, output label 1 there and label 4 on the rest. This is a single parameter-independent kernel L_n. It preserves all observed label-3 positions and the original ordering/multiplicities.

Let p=a/(1-z)=a/(1-c+ac). Direct monotonicity separately in a and c gives

1/16 ≤ z ≤ 7/16;     2/3 ≤ p ≤ 56/57.

The actual and decoded distributions agree on the probability of every configuration of label-3 positions. Given such a configuration with M=m other sites, the actual number K of label-1 entries is Bin(m,p), while decoder K is uniform on {0,...,m}. Conditional on K, both distribute the positions uniformly. Therefore the following is an **exact identity for full ordered outputs**:

1-TV(P_(a,c)^{⊗n}, B_(a,c)^{⊗n}L_n)
 = E_{M∼Bin(n,1-z)} [ Σ_{k=0}^M min{binom(M,k)p^k(1-p)^{M-k},1/(M+1)} ].  (1)

No approximation or false assumption of independent decoded coordinates is used in (1).

## Uniform overlap lemma, continuous p

For every integer m≥10000 and every p∈[2/3,56/57],

Σ_{k=0}^m min{binom(m,k)p^k(1-p)^{m-k},1/(m+1)}
 ≥ (1/40) sqrt(log(m)/m).  (2)

Proof. Put r=sqrt(m log(m)/400) and consider integers |k-mp|≤r. For m≥10000, r≥1 and r/m<1/100; in particular q=k/m∈(0,1) for every such k. By the standard two-sided Stirling factorial bounds (upper denominator factorials and lower numerator factorial), for 1≤k≤m-1,

binom(m,k)p^k(1-p)^{m-k}
 ≥ exp(-1/6)/sqrt(2π m q(1-q)) * exp(-m D(q||p))
 ≥ [1/(2 sqrt(m))] exp(-m D(q||p)),

where D(q||p)=q log(q/p)+(1-q)log((1-q)/(1-p)); the second inequality uses q(1-q)≤1/4 and exp(-1/6)sqrt(2/π)>1/2.

From log t≤t-1, D(q||p)≤(q-p)²/[p(1-p)]. Since p(1-p)≥56/3249 on the full legal range, at every selected k,

m D(q||p) ≤ (3249/22400) log m < (1/4) log m.

Thus each selected binomial probability is at least (1/2)m^(-3/4), which is ≥1/m≥1/(m+1) for m≥16. An interval of length 2r contains at least 2r-1≥r integers; all such integers lie between 0 and m. On these terms the minimum in (2) equals 1/(m+1). Hence the overlap is ≥r/(m+1)≥(1/40)sqrt(log(m)/m). This is a proof over **every real p in the stated interval**, not a grid calculation.

## Global box upper bound and sharp order

M~Bin(n,1-z) has mean n(1-z)≥9n/16. By the standard Bernoulli Hoeffding inequality,

Pr(M<n/2) ≤ exp[-2n(1/16)²] = exp(-n/128).

For n≥20000, on M≥n/2 the lemma applies, and sqrt(log M/M)≥sqrt(log(n/2)/n), because n/2≤M≤n. Taking expectations in (1) proves, simultaneously for all legal a,c,

1-TV(P_(a,c)^{⊗n}, B_(a,c)^{⊗n}L_n)
 ≥ [(1-exp(-n/128))/40] sqrt(log(n/2)/n).

This single kernel upper-bounds δ_n by the theorem's right side. The lower bound on δ_n is the already proved predecessor theorem, obtained by m indistinguishable z=1/4 sources and Hoeffding packing: for n≥1000, δ_n≥1-(28/3)sqrt(log n/n)-2/n². Combining gives the sharp Θ(log-enhanced square-root) convergence order on the **entire auxiliary AV box**. For instance 1-δ_n ≥(1/(80√2))sqrt(log n/n) for n≥20000.

## Tests, reused structure, and scope

The accompanying VERIFY.py independently enumerates all 3^n ordered words for n=2,...,5 at five legal (a,c) pairs and compares their exact Fraction overlap against (1). It also checks exact overlaps at n=12,24,48, parameter laws, probability normalization and rational constants; RUN_EVIDENCE.txt is its actual local output. These finite checks validate the decoder and count reduction. The all-real n≥20000 result rests on the displayed Stirling/KL/Hoeffding argument.

BRC reuse resolution: REUSE_APPLIED — positive rational observer-fiber and label-provenance discipline, with a constructive random repair of the missing 1-versus-4 split. This is a scoped statistical auxiliary theorem, not a native Heartbeat/BRC-Shor arithmetic run nor a six-source, ten-label S23 mother-model result.

Next questions: sharpen the leading constant from the exact overlap formula, and establish a lawful source/time/observer map for repeated ten-label mother experiments before transferring inequalities. Independent mathematical review and Source-native admission remain outstanding.

External analytic reference: W. Hoeffding, “Probability Inequalities for Sums of Bounded Random Variables,” JASA 58(301), 13–30 (1963), DOI 10.1080/01621459.1963.10500830. Standard Stirling factorial bounds and log t≤t−1 are classical mathematical inputs.
