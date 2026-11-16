# R749SRZ — Joint numerator/denominator integer-error critical surface

Date: 2026-11-16 (Asia/Shanghai). Status: AUTHOR_EXACT_NOT_REVIEWED. Independent continuation of R749SRY, Draft PR #2543 at a8f396bbf316a3376b9ec7f337dbd2f1795bdfe9. Frozen scientific pin: a72226e2430ffa4786321ac86e7f0c599d5f0389. The study is an auxiliary positive labeled-source observer, not a native X6 spatial/temporal cell or signed BRC morphism. The earlier proof is retained at its immutable source.

## Fixed model and research question

Use weights w=(1,1,2,3,6), the first weight-one source marked, and shifts J=(0,1,5). For each integer r>=1, let C_r be the number of nonnegative integer vectors k satisfying sum(w_i*k_i)<=r-1, and T_r the sum of their marked coordinates k_1. Put

\[
H_4(r)=\frac16+\frac1{2r}-\frac{115}{36r^2}+\frac{115}{6r^3}-\frac{16315}{108r^4},\qquad
R(r)=\frac{r^3T_r}{C_r}-r^4H_4(r).
\]

The six-phase ideal P=(455,-295,-25,185,-25,-295)/36 is indexed by r mod 6. The ideal three-component phase signature is S_a=(P_a,P_{a+1},P_{a+5}). The R749SRY exact source proved for r>=516 that 0<R(r)-P_{r mod 6}<1600/r and for r>=1 that C_r>=r^5/4320.

In this unit permit *both* bounded signed integer errors e_i in marked counts, |e_i|<=M, and d_i in total counts, |d_i|<=K, independently for the three sampled cutoffs, with C_{r+h_i}+d_i>0. Actual observations are

\[
Y_i=\frac{(r+h_i)^3(T_{r+h_i}+e_i)}{C_{r+h_i}+d_i}-(r+h_i)^4H_4(r+h_i).
\]

Decode by the uniquely closest S_a in maximum norm; ties are failures. Define N(M,K) as the least integer N>=1 for which every integer r>=N and all admissible errors decode correctly.

## Theorem 1: global two-budget asymptotic critical surface

As nonnegative integers M+K tend to infinity along any path,

\[
\boxed{N(M,K)=96K+\sqrt{9216K^2+1152M}+O(1),}
\]

where the implied constant is absolute (independent of the growth path). Consequences:

\[
N(0,K)=192K+O(1),\qquad
N(M,0)=24\sqrt{2M}+O(1).
\]

For fixed lambda>=0 and M_K=lambda*K^2+O(K),

\[
\lim_{K\to\infty}N(M_K,K)/K=96+\sqrt{9216+1152\lambda}.
\]

**Proof.** Rational generating functions of the frozen model are

\[
\sum_{r\ge1}C_rz^r=\frac{z}{(1-z)^3(1-z^2)(1-z^3)(1-z^6)},\quad
\sum_{r\ge1}T_rz^r=\frac{z^2}{(1-z)^4(1-z^2)(1-z^3)(1-z^6)}.
\]

Consequently the six residue classes are exact quasipolynomials with uniform asymptotics

\[
C_q=q^5/4320+O(q^4),\qquad T_q/C_q=q/6+O(1).
\]

For a single coordinate the exact noisy-minus-clean difference is

\[
D_q(e,d)=q^3\frac{C_qe-T_qd}{C_q(C_q+d)}.
\]

Let L=K+sqrt(M); in the range q>=cL for any fixed c>0, we have K/C_q=O(L^{-4}), q^3/C_q=4320/q^2+O(q^{-3}), and T_q/C_q=q/6+O(1). Therefore, uniformly over all allowed integer errors,

\[
|D_q(e,d)|\le 4320M/q^2+720K/q+O(L^{-1}).
\tag{1}
\]

The exact predecessor bound gives R(q)-P_{q mod6}=O(1/q). Fixed shifts cause a further O(L^{-1}) difference. The six ideal signatures have minimum pairwise maximum-norm distance 15/2; every observed vector at distance strictly below 15/4 from its true signature is uniquely decoded.

Put F(r)=4320M/r^2+720K/r and define

\[
\rho=96K+\sqrt{9216K^2+1152M},
\]

so F(rho)=15/4. The positive root rho is comparable to L with absolute constants. Differentiating gives

\[
\rho[-F'(\rho)]=8640M/\rho^2+720K/\rho\in[15/4,15/2].
\tag{2}
\]

For any sufficiently large absolute integer B, (1), monotonicity and (2) imply strict correctness for all r>=rho+B. In particular the O(1/L) error is dominated by the reduction of F over B units.

To prove sharpness of the leading surface, choose an integer r divisible by 6 inside [rho-B-6,rho-B]. The true phase zero and rival phase three obey

\[
S_3-S_0=(-15/2,+15/2,+15/2).
\]

Take the exact integer error witness e=(-M,+M,+M), d=(+K,-K,-K). Then the exact D_q expression, uniform quasipolynomial asymptotics and fixed shifts yield

\[
Y-S_0=(-F(r),+F(r),+F(r))+O(L^{-1}).
\tag{3}
\]

For B large enough, (2) and (3) make F(r)>15/4 by more than the uniform remainder; F(r)<15/2 for all sufficiently large budgets. Thus the rival phase three is *strictly closer* than the true phase zero. All three perturbed denominators are positive, since C_q grows on the order of L^5 while K=O(L). Such a failure exists within a fixed additive distance below rho. Upper and lower bounds yield N(M,K)=rho+O(1), with one absolute constant. QED.

The two error channels have distinct asymptotic powers: numerator errors contribute 4320M/r^2 and denominator errors 720K/r to the same residual phase observer.

## Theorem 2: exact global denominator-only thresholds K=0,...,4

When M=0, with integer d_i and positive total counts,

| Denominator budget K | 0 | 1 | 2 | 3 | 4 |
|---|---:|---:|---:|---:|---:|
| Exact N(0,K) | 35 | 261 | 507 | 759 | 1005 |
| Last failing cutoff r | 34 | 260 | 506 | 758 | 1004 |

**Exact finite-feasibility lemma.** For a rival b at a fixed cutoff, failure is the existence of a vector Y such that max_i|Y_i-S_{b,i}|<=max_i|Y_i-S_{a,i}|=:t. Pick a coordinate j attaining the right-hand maximum. Since T_q>=0, the value q^3*T_q/(C_q+d_j)-q^4*H_4(q) is monotone nonincreasing as the allowed integer d_j increases. Moving d_j to one endpoint of the allowed interval in the direction of the current deviation increases t and preserves the rival inequality at j; all other coordinates retain deviations no larger than the old t. Conversely, if such an endpoint j satisfies the rival inequality and each of the other coordinates has some permitted integer d_i meeting *both* |Y_i-S_a,i|<=t and |Y_i-S_b,i|<=t, the rival ties or beats truth. Therefore examining 2*3 endpoint candidates and independent integer feasibility in the other two coordinates exactly replaces a full cubic error search.

The paired Python Fraction certificate checks this criterion at every r=1,...,1349 for each K=0,...,4. It additionally checks 144 independent full-cube enumerations for 1<=r<=48 and K<=2. The last finite failures are as tabled.

**Infinite-tail certificate.** At r>=1350 the predecessor bound and max P_a=455/36 imply

\[
T_r/C_r=rH_4(r)+R(r)/r^3<r/6+1.
\]

Using C_r>=r^5/4320 gives, uniformly for r>=1350 and K<=4,

\[
|D_r(0,d)|\le\frac{r^3K(T_r/C_r)}{C_r-K}
 <\frac{4320K(r/6+1)}{r^2(1-4320K/r^5)}.
\]

Since the right-hand bound decreases with r, the total true-signature deviation is strictly bounded by

\[
\frac{1600}{1350}+
\frac{4320\cdot4(1350/6+1)}{1350^2(1-4320\cdot4/1350^5)}
=\frac{93267895499872}{28025208984267}
<\frac{15}{4}.
\]

Hence every r>=1350 decodes correctly, and the finite scan plus the infinite-tail certificate prove all five numbers *globally*. QED.

## Evidence, verification range and continuation

Reproducibility consists of the paired standalone standard-library Python script and its exact JSON output. The run returned PASS: 6745 cutoff/budget tests, 144 independently enumerated full error cubes, the precise rational tail bound, and five explicit joint-channel adversarial witnesses at or near the continuous critical surface. Finite tests verify these finite instances. The global asymptotic is based on the analytic proof above; the global denominator-only thresholds use the exact finite-and-tail proof.

This is AUTHOR_EXACT_NOT_REVIEWED. It does not change the frozen source pin, P000, ACTIVE Heartbeat worldview, task publications, CLAIM ownership or independent review status. The observer preserves its declared scalar phase future operation; no typed signed BRC port morphism is inferred.

Next questions: determine the eventual residue-dependent additive offset of N(M,K) from its critical surface; develop an exact integer-lattice feasibility procedure when both error channels vary (the ratio introduces coupled numerator and denominator); test which labeled/joint provenance observations can be preserved under a signed BRC source-port interface.
