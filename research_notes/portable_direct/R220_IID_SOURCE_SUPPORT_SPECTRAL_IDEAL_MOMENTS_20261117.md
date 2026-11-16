# R220 — Exact source-support stochastic spectrum of principal-ideal cardinality

Date: 2026-11-17 (Asia/Shanghai). Research status: AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED. Native physical EffectHistogram integration: NOT_EXECUTED.

## Scientific origin and model

Frozen science: awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34.
Direct antecedents: R209@27656bb342b9035c6e991f29e013ef9399ff7154, R215@71e9d86c4fea71a0ff1b2da66fe2b5656998a68b, R217@deda2c8c0eb5a128731fb061215a7d2955b37c4b and R219@eb35761dc71fa06f96361e6bbc9e6592b3bbc7a3.

Let m>=1, k>=0, L>=1. The finite paired-event observer monoid J_(m,k,L) uses alphabet A=[m] x ({0} union [k]), with neutral provenance label 0. A state records the order of last appearances of k selected provenance labels and the last min(L,word length) complete paired events. The neutral provenance label is not a native spatial axis.

Define exact full-tail fibre weights and principal ideal cardinalities (R209/R215):
  W_r = r! m^L sum_(j=0)^min(r,L) Stirling2(L+1,j+1)
  T_r = sum_(j=r)^k binom(k-r,j-r) W_j.
For any full-tail observer state x with selected-source support S(x), f(x)=|JxJ|=T_|S(x)|.

R219 studies x selected uniformly from the set J. Here the input is instead a sequence of iid paired events with source-label marginal nonnegative rational probabilities p_0,...,p_k summing to 1. Conditional directions may depend on source label; the theorem needs only the iid label marginal. This extra sampling assumption is an abstract observer experiment, not a physical Heartbeat World dynamics claim or native weighted BRC execution. P000 native signed-X6 directions, source provenance and distinct time remain unchanged.

Let S_n be the subset of selected provenance labels observed in the first n events, let q_U = p_0+sum_(i in U)p_i, and F_n = f(observation after n events). The full-tail readout statements apply to n>=L.

## Theorem A — exact support law and cardinality distribution

For every n>=0 and U subseteq [k],
  Pr(S_n subseteq U) = q_U^n,
  Pr(S_n=U) = sum_(V subseteq U) (-1)^(|U|-|V|) q_V^n.  (A1)
For n>=L,
  Pr(F_n=t)=sum_(U subseteq [k], T_|U|=t) sum_(V subseteq U) (-1)^(|U|-|V|) q_V^n. (A2)
Colliding numeric ideal cardinalities are aggregated in A2.

Proof: all n iid event labels lie in {0} union U with probability q_U^n, precisely the event S_n subseteq U. Invert this inclusion-zeta transform on the Boolean source-support lattice. For n>=L, the R215 full-tail ideal theorem gives F_n=T_|S_n|. Summation over exact supports establishes A2. QED.

## Theorem B — exact first and all higher moments

For n>=L,
  E[F_n] = sum_(U subseteq [k]) W_|U| q_U^n.  (B1)
For any integer p>=1,
  E[F_n^p] = sum_(U_1,...,U_p subseteq [k])
              (product_(j=1)^p W_|U_j|) q_(intersection_j U_j)^n.  (B2)
Variance follows as E[F_n^2] - E[F_n]^2.

Proof: the definition of T is a Boolean zeta transform:
  T_|S| = sum_(U superseteq S) W_|U|.
Hence F_n = sum_U W_|U| 1[S_n subseteq U]. Taking expectation proves B1. On expanding the p-th power, the conjunction of subset conditions is the single condition S_n subseteq intersection_j U_j, proving B2. No spurious independence of those indicator variables is used. QED.

For uniform labels p_i=1/(k+1), B1 groups into k+1 spectral modes:
  E[F_n] = sum_(r=0)^k binom(k,r) W_r ((r+1)/(k+1))^n.  (B3)
For p=2 an exact O(k^3) category grouping is:
  E[F_n^2] = sum_(r,s=0)^k sum_(t=max(0,r+s-k))^min(r,s)
              binom(k,t)binom(k-t,r-t)binom(k-r,s-t)
              W_r W_s ((t+1)/(k+1))^n.  (B4)
The triple binomial product counts ordered subset pairs of sizes r,s whose intersection has size t.

## Theorem C — exact complete monotonicity and spectral recurrence

Let E_n=E[F_n]. For every n>=L and integer j>=0,
  (-1)^j Delta^j E_n
    = sum_(U subseteq [k]) W_|U| q_U^n (1-q_U)^j >=0. (C1)
Here Delta E_n = E_(n+1)-E_n. Thus E_n is nonincreasing once the tail fills. For k>=1 with all selected-label masses positive it decreases strictly and tends to W_k=T_k.

Proof: the signed j-th forward difference of q_U^n is q_U^n(1-q_U)^j. Every W and probability factor is nonnegative. For positive selected-label masses only U=[k] has q_U=1; its term W_k persists and all others decay. QED.

For uniform labels define b_n=(k+1)^n E_n. Then
  b_n = sum_(r=0)^k binom(k,r) W_r (r+1)^n.
Writing E_shift b_n = b_(n+1), it follows that
  product_(j=1)^(k+1) (E_shift-j) b_n=0.  (C2)
This is the MINIMAL linear recurrence for the infinite full-tail sequence: the k+1 distinct exponential sequences have strictly positive coefficients binom(k,r)W_r, so a lower-degree annihilator would have to vanish at k+1 distinct points by Vandermonde independence. For uniform k>=1,
  E_n-W_k = k W_(k-1) (k/(k+1))^n
             + O(((k-1)/(k+1))^n).  (C3)
For k=1 the remainder vanishes for n>=1. More generally, with zero-probability selected labels the limit is T_|P| for P={i:p_i>0}, since exactly the supersets U of P have q_U=1. QED.

## Exact X6-compatible observer specialization

For 12 signed-native-direction labels, k=6 source labels and L=2:
  W=(144,576,1440,4320,17280,86400,518400);
  T=(1407600,1174176,986400,833760,708480,604800,518400).
For iid uniform provenance marginal p_i=1/7 and n>=2,
  E[F_n] = sum_(r=0)^6 binom(6,r) W_r ((r+1)/7)^n.
The integer b_n=7^n E[F_n] satisfies the exact minimal order-7 recurrence:
  P(X)=X^7-28X^6+322X^5-1960X^4+6769X^3-13132X^2+13068X-5040.
At n=2, E[F_2]=7447824/7 (~1063974.857);
at n=12, E[F_12]=8368509542724720/13841287201 (~604604.862),
  Pr(all six sources seen)=4115105280/13841287201 (~29.73%);
at n=24, E[F_24]=101787561082935860445091440/191581231380566414401 (~531302.364),
  Pr(all six seen)=164039387759075743200/191581231380566414401 (~85.62%).
The limit is exactly 518400. Uniform iid histories produce a different law from the uniform-J-state distribution and moments of R219.

For L=2, R217's 7-bit future-congruence scalar quotient supports the exact source-set process after tail fill. R210's 21-bit full paired-action code and the typed source, signed phase, port, exact rational weight, multiplicity and cross-moment BRC carriers remain separate; the scalar projection is used only for its certified query language.

## Computation, verification and continuation

Companion standard-library Python program R220_support_spectral_moments_check.py uses exact int/Fraction. It executed 48 parameter models (m in {1,2,3}, k in {0,1,2,3}, L in {1,2,3,4}), 216 model/horizon agreements comparing first and second moments by independent Boolean-subset paths, 4914 enumerated tagged histories, 56 exact spectral recurrence checks for k=0,...,6 and 224 alternating finite-difference inequalities; rational nonuniform probability (1/2,1/3,1/6) is also brute-checked. All performed checks PASS. R220_verification.json stores exact six-source outputs and verification scope. Symbolic proofs above support arbitrary admissible parameters; numeric tests substantiate implementation and selected cases.

Review=NOT_REVIEWED; formal Task CLAIM=None; native EffectHistogram integration=NOT_EXECUTED. This contribution is portable independent source research and has no Result/Review/Foundation admission assertion.

Next: implement a native typed EffectHistogram mapping preserving the full 21-bit action and exact positive rational weights, multiplicity, port/source signs, and R203 joint cross-moments, while separately indexing R217's 7-bit scalar state. Actually run composition and serialization benchmarks. An independent structural question is the least future-congruence for L>=3 cardinality readout, which must respect R216's border-only counterexample.
