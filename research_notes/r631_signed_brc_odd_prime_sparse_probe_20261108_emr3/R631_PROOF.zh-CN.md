# R631｜任意安全奇素数的 signed BRC 双探针；模数选择与最短探针跨度

2026-11-08. Status: **AUTHOR_SIDE_EXACT_PROOF / UNREVIEWED / NOT_ADMITTED**.
Parent R630@256e0b45069acaa4b6e8eb7bc6c1a86bcfdd5310; frozen science R462@18783e01e3646c72b7aab3b16d3f565e83e6446f, original signed K generator blob 7fa7a762f758b30c6090468ac43487daa34abad8, theta=0. P000 defines six native X6 spatial axes and a separately typed time; the k index here is a deliberately selected **auxiliary probe index** and is not physical time or branch-grade.

## 1. Problem and frozen input

R629 recovered all 720 signed BRC directions using h+2 consecutive alternations under arbitrary independent integer Newton polynomial background of degree h. R630 exhibited a nonconsecutive two-reading pair using a 3-power index and coefficient reduction modulo 3. This unit studies how the modulus affects the required probe-index span.

For each native axis x, orientation `pi in S6`, j=pi^-1(x), frozen signed pairs `P_j=K_(2j-1)`, `M_j=K_(2j)`, `D_j=P_j-M_j`; unknown nonzero `A_x in Z[[t]]`, fixed across its two readings, and arbitrary `H_x(k)=sum_(l=0)^h B_(x,l)*binom(k,l)` with B_(x,l) in Z[[t]]. At indices 0 and L, read P_j at 0 and M_j at **odd** L, respectively. The observations are integer-coefficient formal series, or their d-jets, with explicit modular reduction to F_p[[t]] used only as a *direction observer*. All full signed/provenance/joint X6 state remains available for future operations.

Frozen branch-pair valuations over the integers are `nu_t(D_j)=(0,2,4,6,8,10)`, with nonzero leading coefficients
```
c=(2,-8,6,106,83,9).
```
The prime divisors of their product are exactly {2,3,53,83}. Every odd prime `p>=5` other than `p=53,83` makes **all six c_j units modulo p**; p=3 is separately useful because its observed modular valuations are `(0,2,7,6,8,11)`, also pairwise distinct.

## 2. Prime-power nuisance annihilation and integral repair lemma

Let p be an odd prime, h>=0, and `L=p^s` the **least p-power strictly larger than h** (s=0 and L=1 when h=0). Since p is odd, L is odd. The binomial identity
```
(1+X)^(p^s) = 1+X^(p^s) (mod p)
```
implies `binom(L,l)=0 (mod p)` for every `1<=l<=h<L`. Thus
```
Y_x(L)-Y_x(0) = - A_x D_(pi^-1(x)) (mod p).
```
This identity is coefficientwise exact in F_p[[t]] for *any* integer nuisance Newton coefficients.

When h>=1, one has s>=1, h>=L/p, and the gcd over `l=1,...,h` of the integer coefficients `binom(L,l)` is **exactly p**. They are all divisible by p. For l=L/p,
```
binom(L,l) = (L/l) binom(L-1,l-1) = p binom(L-1,l-1).
```
The second factor is not divisible by p: `binom(p^s-1,m)=(-1)^m mod p` for every `0<=m<p^s`, by expanding `(1+X)^(p^s-1)=(1+X^(p^s))/(1+X)` in F_p[X] through degree p^s-1. Hence gcd=p. By Bezout, every coefficient series in pZ[[t]] can be realized as the nuisance increment `H(L)-H(0)` with integral Newton coefficients. For h=0 the nuisance increment vanishes identically.

## 3. Theorem: safe-prime two-probe identifiability

**Theorem (all h, all admissible odd primes).** Let
```
P_safe = {3} union {odd primes p>=5 : p not in {53,83}}.
```
Fix h>=0, a>=0 and p in P_safe. For each axis x assume `nu_t(A_x)=a` and the coefficient at t^a in A_x is **not divisible by p**. Probe at indices (0,L) with L the least p-power >h, positive then negative branch. Then, uniformly over all pi in S6 and every declared independent integer Newton nuisance, **the six-axis orientation is recovered from d-jets if and only if d>=a+8** (as a uniform-guarantee threshold for this exact two-probe scheme).

*Proof (sufficiency).* Reduce the difference in Section2 modulo p. The gain reduction has first nonzero t-coefficient at degree a, so `nu_p(Y_L-Y_0)=a+nu_p(D_j)`, where `nu_p` is first nonzero t-degree after coefficient reduction mod p. For p>=5 safe, the six values `nu_p(D_j)=(0,2,4,6,8,10)`; for p=3, the values are `(0,2,7,6,8,11)`. In either case five labelled axes are visible at d=a+8 and the remaining unknown axis label is forced by the permutation. The signed gain coefficients need not be equal across axes.

*Proof (sharp depth).* For d<=a+7 exchange branch labels j=5 and j=6 on two axes with gain `t^a`. Both modular differences are zero modulo t^(d+1): their integer D valuations are 8 and 10. If h>=1, the nuisance increments span pZ[[t]], so one can choose integral Newton nuisance coefficients whose two-probe jets exactly correct the (p-divisible) signal differences; first match Y(0) with the arbitrary constant nuisance, then match Y(L). If h=0, both raw D jets vanish through d and a constant nuisance adjustment suffices. Thus the observed d-jets can coincide for two different orientations.

*Proof (one-reading lower bound).* With an arbitrary nuisance constant `B_(x,0)`, any single sign readout at any index can be cancelled identically to zero on all six axes for every permutation. Hence **two readings are sample-minimal** in this declared model. The optimal-jet statement above is **specific to the stated (0,L) protocol**; other observation languages may require an independent lower-bound analysis.

## 4. Index-span minimization within prime-power modular protocols

For fixed h and a particular allowed p with calibrated p-unit gains, the least eligible index is `L_p(h)=min{p^s>h : s>=0}`. Among the listed safe-modulus protocols, choose
```
L_*(h)=min_(p in P_safe) L_p(h);
```
ties can be resolved by the smaller p. All h have a finite choice by existence of arbitrarily large safe primes. This is a **minimum within the declared prime-power modular cancellation family**, not a proof of globally smallest sampling interval across all integer indices, arbitrary nuisance constraints or operation programs. The selected p must have the required p-unit leading gain coefficient on each axis; when the actual gain is not p-unit, one must use another certified modulus or add a calibration/repair observation.

Exact examples:

| h | smallest selected p | L_* | p=3-only L_3 |
|---:|---:|---:|---:|
| 1 | 3 | 3 | 3 |
| 2 | 3 | 3 | 3 |
| 3 | 5 | 5 | 9 |
| 4 | 5 | 5 | 9 |
| 5 | 7 | 7 | 9 |
| 8 | 3 | 9 | 9 |
| 9 | 11 | 11 | 27 |
| 24 | 5 | 25 | 27 |
| 26 | 3 | 27 | 27 |
| 52 | 59 | 59 | 81 |
| 82 | 89 | 89 | 243 |
| 100 | 101 | 101 | 243 |

For h>=1, each fixed p protocol has `h<L_p(h)<=p h`. One may trade modular arithmetic and the requirement on the gain's leading coefficient against the interval over which the gain must remain stable. No physical-time duration is implied by L without a Source-defined operation-to-time bridge.

## 5. Executable evidence, reuse and next

The `R631_VERIFY.js` verifier uses JS BigInt on the frozen signed K generator, enumerates safe odd primes <=219 (44 candidates), validates all six modular signatures, evaluates min-index choices for h=0..100, checks 1,010 prime-binomial gcd cases for h=0..100 and the first ten admissible primes, and performs 51,840 full-permutation reading recoveries for p in {3,5,7,11}, h in {0,1,2,3,4,8,9,24,26}, gain valuations a in {0,2}. It also checks 4,320 one-probe nuisance fibers. Total **57,315** checks, marker `R631_ODD_PRIME_SPARSE_BRC_EXACT_PASS`. All universal mathematical claims follow the integer/modular proof; finite evidence exercises exact stated instances. The h<=100 schedule minima were enumerated within safe primes <=219, which suffices for that window because every h<=100 has an eligible prime <=101.

Reuse: `T0_BRC=REUSE_APPLIED` with original frozen signed K, R630 exact modular probe law; `T6_OPERATION_SAFE_QUOTIENT=REUSE_APPLIED` as readout-only compression discipline. No new general-purpose tool or native operator acceptance is requested.

**Next unit:** Find a Source-defined native X6 internal field readout that supports independently chosen positive/negative K source probes with fixed gain through an index span L; prove its nuisance bound and future-operation descent, or show an explicit legal operator violating them and quantify the minimal carried source/field coordinate. A fixed heartbeat evolution program has not been registered (`fixed_heartbeat_program=null`), and this theorem does not instantiate one.
