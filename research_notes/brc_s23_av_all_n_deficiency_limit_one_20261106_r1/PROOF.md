# S23 shared-parameter AV observer: all-n deficiency tends to one

Date: 2026-11-06. Author-side analytic proof and exact rational verification.
Frozen scientific input: awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34.
Previous frontier: PR #1777, commit 72dc5831521b97979cf76ef45255f25c099c83f6 (all-n Blackwell fiber extremality).

## Experiment and quantifiers

For a,c in [1/2,7/8], let z=(1-a)c, P_(a,c)=(a,z,1-a-z) on labeled stops (1,3,4), and B_(a,c)=(z,1-z). The same unknown pair governs n conditionally IID trials. Define

δ_n = inf_{L:{Y,N}^n -> {1,3,4}^n stochastic} sup_{a,c in [1/2,7/8]} TV(P_(a,c)^⊗n, B_(a,c)^⊗n L).

L may correlate reconstruction coordinates but cannot depend on a,c.

## Theorem (all positive integers n, any integer m>=2)

δ_n >= max{0, 1 - 1/m - 196(m-1)^2/(9n)}.

Consequently lim_(n->infinity) δ_n = 1. In particular, δ_1000 >= 652/1125 and δ_10000 >= 1809/2500.

### Proof

Choose m legal parameters sharing z=1/4:

a_j = 1/2 + 3j/[14(m-1)], c_j = (1/4)/(1-a_j), j=0,...,m-1.

All a_j lie in [1/2,5/7], all c_j in [1/2,7/8], and each compressed observation has the same distribution B=(1/4,3/4). Thus for every parameter-independent kernel L, Q=B^⊗n L is the same reconstructed distribution under all m hypotheses.

Let X be the number of complete stop-1 events. Under hypothesis j, X is Bin(n,a_j). Let Δ=3/[14(m-1)] and let E_j be the decision event obtained by classifying X/n to its nearest a_j, resolving ties deterministically. The events E_j form a disjoint partition. By Chebyshev and a_j(1-a_j)<=1/4,

P_j^⊗n(E_j^c) <= P_j(|X/n-a_j|>=Δ/2)
                 <= 4 a_j(1-a_j)/(n Δ²) <= 1/(n Δ²).

For any laws R,Q and event E, TV(R,Q)>=R(E)-Q(E). Hence

m max_j TV(P_j^⊗n,Q)
 >= sum_j [P_j^⊗n(E_j)-Q(E_j)]
 >= m - m/(n Δ²) - 1

since sum_j Q(E_j)=1. Divide by m, then take the supremum over all legal parameters and infimum over L. Substituting Δ yields the asserted bound.

For fixed m, liminf_(n->∞) δ_n >= 1-1/m. Let m grow without bound. TV always <=1, so δ_n tends to one. QED.

## Stronger exact finite-n rational certificate

For n=1000 use m=3 with first-stop masses a_0=1/2, a_1=17/28, a_2=5/7. The legal (a,c) pairs are (1/2,1/2), (17/28,7/11), (5/7,7/8); their complete laws are respectively (1/2,1/4,1/4), (17/28,1/4,1/7), (5/7,1/4,1/28), and the binary law for each is (1/4,3/4).

Partition complete sequences by first-stop count X:
E_0={X<=553}, E_1={554<=X<=660}, E_2={X>=661}.
Define the exact rational binomial sums

S_0 = sum_{k=0}^{553} binom(1000,k) (1/2)^1000;
S_1 = sum_{k=554}^{660} binom(1000,k) (17/28)^k (11/28)^(1000-k);
S_2 = sum_{k=661}^{1000} binom(1000,k) (5/7)^k (2/7)^(1000-k).

The partition argument, with no approximation, proves

δ_1000 >= (S_0+S_1+S_2-1)/3 > 13/20.

VERIFY.py uses Fraction to evaluate those three sums exactly and asserts the strict rational bound; the exact rational right-hand side has decimal approximation 0.666338327539439... .

## Information interpretation and limitations relevant to the mother goal

Prior all-n fiber extremality fixed the worst two hypotheses and proved δ_n>=D_n/2, which tends to 1/2. The new theorem uses arbitrarily many increasingly distinguishable complete distributions inside a single compressed-observer fiber, proving the stronger asymptotic δ_n->1. The two statements concern different bounds: pairwise diameter versus many-hypothesis reconstruction radius.

This is the scoped three-stop auxiliary AV statistical experiment, not the frozen original ten-label S23 encoding/decoding game. The binary observer deliberately collapses the first/fourth-stop split; P000, native X6/Heartbeat assumptions and the provenance of observer data are preserved. The ten-label lawful bridge to R_beh(k,10) remains a separate open mathematical problem.

## Evidence and next work

The general theorem is proved by the displayed partition/Chebyshev argument. VERIFY.py is Python 3 standard-library Fraction exact arithmetic, executed locally; RUN_EVIDENCE.txt contains its stdout. Author proof; independent mathematical review pending; no formal CLAIM/Result/Review or canonical admission asserted.

Next: optimize finite-n multi-point decision regions and convergence rate of 1-δ_n; separately improve the n=4 16x81 joint kernel and inspect frozen ten-label S23 source/encoder/decoder quantifiers for a lawful bridge.
