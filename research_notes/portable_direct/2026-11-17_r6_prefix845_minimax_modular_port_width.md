# PREFIX-845 — Minimax register width for stateless modular BRC provenance observers

**Status:** AUTHOR_PROVED / EXACT_FINITE_ENUMERATION / NOT_INDEPENDENTLY_REVIEWED / NOT_ADMITTED.
**Frozen scientific input:** `f42f2906d77f24085c123f3ccfe9667d41caa96d`, retained without changing its scientific assumptions.
**Dependencies:** PREFIX-840 tagged Q-only scalar, PREFIX-842 permanent coprime modulus, PREFIX-844 joint modular observer fiber theorem.
**Scope:** Only the explicitly declared positive-integer tagged Q-only observer. This is a modular interface and not a native X6 Cell/Link/Port event construction. No shared CLAIM/Result/Review is claimed.

## Problem

There are p>=1 named sources with weights 1<=w_i<=W (W>=2). There are N=W^p distinct named configurations U=0,...,N-1, with fixed offset S. At each t>=1, a fixed bank of k>=1 stateless raw modular channels reports
Y_j(t) = [c_t(S+U)] mod m_j,
c_t=a^floor(t/2)b^floor((t-1)/2), a,b>=1, C=ab.
Every channel must use at most B bits, meaning 1<=m_j<=2^B. Each time the current channels must independently distinguish all N configurations; the receiver is not permitted to retain an earlier full decode or add repair bits. Repeated moduli and modulus 1 are allowed (unused slots).

Let B_k(N,C) be the least possible maximum per-channel bit width for this infinite-time, stateless, fixed-bank objective.

## Theorem 845.1: exact finite minimax reduction

For any k,N,C as above,
B_k(N,C) = min { B>=0 : there exist 1<=m_1,...,m_k<=2^B, gcd(m_j,C)=1 for every j, and lcm(m_1,...,m_k)>=N }.
It is enough to test collections of at most k **distinct** C-coprime positive integers.

**Proof.** PREFIX-844 gives eventual joint information modulus M_perp(C), the largest C-coprime divisor of M=lcm(m_1,...,m_k). Its infinite-time injectivity criterion is M_perp(C)>=N. Put d_j=(m_j)_perp(C), the C-coprime part of m_j. Prime valuations show lcm(d_j)=M_perp(C). Replacing m_j by d_j cannot increase any channel's bit width, and duplicates and 1 add no information. Conversely, a C-coprime bank with lcm>=N remains injective at every t because all c_t consist only of primes dividing C. This proves the reduction. QED.

## Theorem 845.2: constructive k-port width bound, all N

Define D=rad(C*(k-1)!) (product of the distinct primes dividing C*(k-1)!), and X=ceil(N^(1/k)), both exactly as integers. Put q=ceil((X-1)/D) and choose
m_i=1+(q+i)D, i=0,...,k-1.
Then:
(i) gcd(m_i,C)=1;
(ii) gcd(m_i,m_j)=1 whenever i!=j;
(iii) product_i m_i>=N; and
(iv) max_i m_i<=X+kD.
Consequently,
  ceil((log_2 N)/k) <= B_k(N,C) <= ceil(log_2(X+kD)).
For every fixed k and C, the optimal minimax port width is
  B_k(N,C)=(log_2 N)/k + O_{k,C}(1)  as N tends to infinity.

**Proof.** Every m_i is 1 mod D, and rad(C) divides D, proving (i). If a prime ell divided both m_i and m_j, it would divide (j-i)D. It cannot divide D because m_i is 1 mod D. But every prime dividing j-i, with 1<=|j-i|<=k-1, divides (k-1)! and hence D: contradiction. This proves (ii). The definition of q gives m_0>=X; every subsequent m_i is at least X, so the product is >=X^k>=N. Since qD<X-1+D, the last m_i<X+kD, proving the quoted weak bound (iv). The construction is permanently injective by Theorem 845.1. Any k B-bit raw channels have product of moduli <=2^(kB), while their effective lcm is at most that product. Thus N<=2^(kB), giving the lower bound. For fixed k,C, D is constant and X=N^(1/k)+O(1), giving the asymptotic statement. QED.

**Interpretation.** Splitting a fixed readout across k ports asymptotically divides *maximum per-port* width by k. It does not beat PREFIX-844's lower bound on the *sum* of raw register widths. The arithmetic progression is an explicit construction, not a claim of exact finite optimum.

## Exact finite optimum experiment

The attached standalone JavaScript program exhaustively enumerates all subsets of at most k distinct integers m in [1,2^B] coprime to C for B increasing. It stops at the first B attaining lcm>=N. Because every smaller B and every admissible subset at those bounds is exhausted, these are certified finite optima under Theorem 845.1.

Domain: N in {4,16,64,256,1024}; C in {2,6,30}; k in {1,2,3} (45 exact minimax optima). All numbers in this enumeration and their lcm values fit exact IEEE-754 integer arithmetic; large arbitrary-precision construction tests use BigInt and exact integer kth-root binary search. No stochastic approximations.

Selected exact values:
| C | N | B_1 | B_2 | B_3 |
|---:|---:|---:|---:|---:|
| 2 | 16 | 5 | 3 | 3 |
| 2 | 256 | 9 | 5 | 4 |
| 2 | 1024 | 11 | 6 | 4 |
| 6 | 64 | 7 | 4 | 4 |
| 6 | 1024 | 11 | 6 | 5 |
| 30 | 16 | 5 | 4 | 4 |
| 30 | 256 | 9 | 5 | 4 |
| 30 | 1024 | 11 | 6 | 5 |

Example: C=2,N=1024,k=3 has optimal B=4 with a valid bank (7,11,15), whose lcm=1155. At B=3, the only positive odd choices are 1,3,5,7; even using three ports the maximal lcm is 3*5*7=105<1024, so B=4 is exact. A one-port infinite-time solution needs m>=1024 coprime to 2, minimally m=1025 and 11 bits.

## Verification boundary

The theorem is a direct proof for arbitrary positive integer parameters. The enumerated 45 parameter cases have an exhaustive finite checker; huge integer constructions only test the explicit formula, not the general theorem. Source identity in a modular tag is a **named weight coordinate**, not a complete signed native relation. No native X6 event mapping, dynamic source updates, network interaction or information-theoretic independence of actual native port observations is assumed.

## Next discriminating questions

1. Characterize the exact finite minimax width B_k(N,C) by a faster certificate than subset enumeration; identify when the arithmetic progression is width-optimal.
2. Extend to k ports with channel-specific time availability and permitted memory, explicitly separating stateless readout from stored residuals.
3. Establish or refute a lawful native X6 Cell/Link/Port observable that instantiates the tagged-source scalar while retaining signed path, source/port identity, and causal order.
4. Keep the existing q>=5 nonnegative-Q carrier problem independent of this scalar compression result.

Reproduce: `node PREFIX845_R6_MINIMAX_PORT_WIDTH_CHECK.js > PREFIX845_R6_MINIMAX_PORT_WIDTH_RESULTS.json`.
