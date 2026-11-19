# PREFIX-925 — Complete named XOR collision mass at PREFIX-924's weakest positive capacity-bound pair

Date: 2026-11-19 (Asia/Shanghai); lane: 进取数论研究6. Scientific input pin: `f42f2906d77f24085c123f3ccfe9667d41caa96d`. Status: **AUTHOR_PROVED_BY_REUSED_EXACT_KERNEL / TWO_INDEPENDENT_PARAMETER_ENUMERATIONS / DIRECT_PORT_REVERSAL_CHECK / NOT_INDEPENDENTLY_REVIEWED / NOT_ADMITTED**.

References and dependencies: PREFIX-924's exact two-port marginal collision-mass theorem, PREFIX-918's named two-flip bit-window kernel and PREFIX-919's zero/flip exact-weight formula. This remains an auxiliary named XOR observer of a discrete system, not a full native X6 event/heartbeat dynamics theorem.

## Theorem: exact mass at the weakest capacity pair

At `p=32, N=2^32, a=464773, b=304985`, consider all `(p+1)*N` individually named zero-or-one-flip trajectories
`Z_x=(x,x)` and `F_x^i=(x,x xor 2^i)`, `0<=x<N, 0<=i<p`, observed at `(start mod a,end mod b)`.
Let `C(a,b)` be the number of **unordered pairs of different named trajectories** with identical two-port observations.

The complete, exactly disjoint collision classification is

| Disjoint pair class | Exact number |
|---|---:|
| Zero / zero | 0 |
| Zero / one flip | 515,898,112 |
| One flip / one flip, first source bit higher, positive final gap | 29,257,670,556 |
| One flip / one flip, first source bit higher, nonpositive final gap | 0 |
| One flip / one flip, first source bit lower | 29,257,670,556 |
| One flip / one flip, equal source indices | 197,492,246 |
| One flip / one flip, equal starting state | 0 |
| **All unordered named collision pairs** | **59,228,731,470** |

In particular,

```
C(464773,304985) = 59,228,731,470
B(464773,304985) = max(L,R) = 3
C/B = 19,742,910,490.
```

Here `B` is the proven compulsory collision-pair lower bound of PREFIX-924, *not* the actual collision mass. The ratio measures how much this combinatorial lower bound underestimates the real source-labeled XOR population at this observer; it makes no claim about all observers.

## Exact derivation and finite coverage

There is no zero/zero collision because `lcm(a,b)=a*b>2^32`. Equal-start two-flip pairs are counted by the PREFIX-917 source-bit order formula `(N/2)W_p(b)`, which vanishes at this `b`.

For mixed zero/flip pairs, PREFIX-919 gives the exact complete sum over `A=k*a<N`, source bit `i` and the two signs of `b | A±2^i`. Its only positive parameter fiber here is

```
(k,i,sign)=(8131,7,-1), A=3,779,069,263, 2^i=128,
N-A=515,898,033, tau_i(A)=79,
weight=N-A+tau_i(A)=515,898,112.
```

One explicit pair inside the fiber is `F_0^7=(0,128)` against `Z_A=(A,A)`. The start difference is `8131a), and the end difference is `12391b). Both endpoints lie in `[0,2^32)`.

For two-flip pairs with distinct starts `x<y`, `A=y-x=k*a` and signs `eps,eta in {-1,+1}`, the complete source label identity is

```
D = A+eta*2^j-eps*2^i, b|D,
K_p(A,i,j,eps,eta)
  = #{0<=x<N-A: bit_i(x)=1[eps<0], bit_j(x+A)=1[eta<0]}.
```

The PREFIX-918 verified exact periodic bit-window formulas evaluate `K_p` for each `i>j`, `i<j`, and `i=j` with ordinary integer arithmetic. The count in the table is the sum of `K_p` over **all** eligible `1<=k< N/a`, all `32^2` ordered source-index pairs and all four signs, with no restriction on the terminal-gap sign. For this pair there are `9,241` positive `k` candidates; precisely **113** distinct signed parameters have positive K. The enumeration and exact pair recovery are the disjointness argument from PREFIX-918, reused under its original hypotheses.

## Two distinct full calculations and port reversal

1. `PREFIX925_R6_KSWEEP_MASS.cpp` uses C++17 integer arithmetic, traverses every `k=1..9241` and every `(i,j,eps,eta)`, checks `D mod b=0`, then calls the exact integer bit kernel. It also computes zero/zero, mixed and same-start classes; its output is `PREFIX925_R6_KSWEEP_MASS_RESULTS.json`.
2. `PREFIX925_R6_CONGRUENCE_FIRST.py` instead enumerates signed `(i,j,eps,eta)` first and solves `k=(eps*2^i-eta*2^j)*a^{-1} mod b` using arbitrary-precision modular inverse. Every eligible positive `k<=9241` is then evaluated. Mixed pairs use a separate inverse-first loop. It reproduces all seven rows and 113 positive two-flip families.
3. **Exact reversal certificate.** The map `Z_x -> Z_x`, `F_x^i -> F_(x xor 2^i)^i` reverses every named trajectory while retaining its source label. Swapping observation ports sends the `(a,b)` collision problem bijectively to `(b,a)`; hence `C(p,a,b)=C(p,b,a)` for all positive integer moduli. Separate full computations at `(304985,464773)` give the same seven category totals and total `59,228,731,470`.

Both programs were actually executed against the indicated inputs; exact category counts, number of positive signed fibers, mixed mass and total agreed. The underlying mathematical kernel and its small-model exhaustive checks are imported at their **existing proved scope** from PREFIX-918/919, without disguising these two implementations as independent mathematical peer review. The PREFIX-924 proof also checked the marginal inequality directly on 485 complete small observer configurations.

No `2^32`-element trajectory array is materialized. All counts are exact integers, not floating estimates.

## Consequence and next discriminating question

The **unique weakest positive bucket obstruction** from PREFIX-924, up to swapping ports, corresponds to a highly nonuniform full named XOR collision mass: a minimum compulsory count of 3 versus an actual count of 59,228,731,470. Thus capacity overload is a valid Boolean certificate but a poor quantitative proxy for this observer's residual source multiplicity.

Next: study the conditional distributions of `C/B` for a reproducible band of near-threshold strict-19-bit pairs and identify which signed source-index families dominate the discrepancy. Separate the auxiliary Boolean existence of collisions, exact pair multiplicity, observer support and native X6 correspondence. The project's frozen mother question `B_fix,odd(32) in {19,20}` remains open, with no new formal Result/Review/CLAIM claimed.
