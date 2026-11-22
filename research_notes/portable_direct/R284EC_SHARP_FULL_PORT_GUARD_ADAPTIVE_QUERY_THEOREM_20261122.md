# R284EC — Sharp global decision-tree complexity of the 16-bit frozen Port quotient-exception guard

Date: 2026-11-22 (Asia/Shanghai). Scientific status: `AUTHOR_PROVED / EXACT_FINITE_CERTIFIED / NOT_REVIEWED`.

## Scope and exact inputs

This theorem sharpens R284EB, which constructed but did not prove optimal the full 16-bit short-circuit guard. The original frozen source remains `awdawmip/enterprise-math@acba2d8667903434aaa2a10720f43637fcc2421b:research_notes/portable_direct/R284CO_spectral_witness_checker.py`, Git blob `b46e0f682b58e47c27094b4bea6fa4e55119a3ee`, source codeword SHA256 `b6ce76b2c08b9ec6b79ec83173befd2589928ca7c636643c3eaecd40405f4ff4`. Predecessors: R284EA exact threshold (`bc66d7bdd3210f426dc38497e6c0368ab11ab292`), R284EB full guard and nine-bit subproblem (`528efede65bb1c5b097f4fd0fa5861535c1e7925`).

Define the Boolean correction on the original 16 source bits: `F(c,b,B3) = (AND_{i=1}^6 c_i) AND 1[13Y+6Z+28U+25G+11H+12R+26B0+17B1+6B2 >= 77]`. Here each `c_i` marks whether one of `(u1,a,x,u2,w,b)` is 2, `b=(Y,Z,U,G,H,R,B0,B1,B2)` are the other nine relevant bits, and upper bit `B3` does not enter the function. These are precisely the R284EA conditions on the frozen state cube, with no state-coordinate deletion or change to the underlying determinants.

The **bit-probe cost model** charges one unit each time an adaptive deterministic algorithm reads one original input bit, uses exact noiseless answers, and makes all 65,536 original source states equiprobable. All other arithmetic and branch processing is uncharged. This is query complexity, not measured runtime or memory/bit-packing performance.

## Sharp theorem

**The globally minimal expected number of bit probes for F over the original uniformly distributed 16-bit cube is**

\[\boxed{\mathbb E_{\min}Q=\frac{33623}{16384}=2.05218505859375.}\]

The minimal sum of bit queries over all 65,536 original states is **134,492**, and the minimum possible worst-case number of queries is **15**. Both sharp bounds are attained by the explicit R284EB procedure: inspect the six core bits in fixed order until a zero is found; on the all-one core, query nine threshold bits in order `U,B0,G,B1,Y,R,H,Z,B2`, stopping when the remaining weight bounds decide the threshold. No query of B3 is needed.

Exact query histogram for the optimal procedure:

| Queries | 1 | 2 | 3 | 4 | 5 | 6 | 9 | 10 | 11 | 12 | 13 | 14 | 15 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| State count | 32768 | 16384 | 8192 | 4096 | 2048 | 1024 | 256 | 192 | 96 | 160 | 152 | 84 | 84 |

The Boolean exception has exactly 446 true states and 65,090 false states, consistent with R284EA.

## Exhaustive lower-bound proof over every adaptive query order

B3 is an independent **irrelevant bit**. Any decision tree querying it can replace that node by whichever of the two B3-conditional subtrees has smaller expected cost on the identical remaining problem. This cannot increase the expected cost; the same reduction applies to worst-case depth. Thus it suffices to consider the remaining 15 bits.

Suppose all previously observed core bits were one, with `k` still unobserved (`0<=k<=6`); a seen core zero makes F known to be false. On the threshold bits, let `Z,O` be disjoint sets known to be zero and one, and `A` be the free coordinates. Define `L=sum_{j in O} w_j`, `M=sum_{j in A} w_j`, `n=k+|A|`. If `L+M<77`, the function is already false; if `k=0` and `L>=77`, it is already true. Both conditions have future query cost zero.

Let `C(k,Z,O)` be the **minimum sum of queries over the 2^n equiprobable completions**. Every nonterminal algorithm first queries either a core bit (when k>0) or a free threshold bit. Its optimal recurrence is

\[\begin{aligned}C(k,Z,O)=2^n+\min\big(&C(k-1,Z,O)\quad(k>0),\\ &C(k,Z\cup\{j\},O)+C(k,Z,O\cup\{j\})\quad(j\in A)\big).\end{aligned}\]

After querying a core bit, the zero branch immediately terminates with F=0 and the one branch has the same residual problem with k-1. For a threshold query, the zero/one branches split the remaining assignments. Induction on `n` proves the recurrence minimizes across **all deterministic adaptive decision trees**. The companion checker evaluates exactly `7·3^9=137,781` typed partial states using integers, obtaining

`C(k,empty,empty) for k=0..6 = (2734,3758,5806,9902,18094,34478,67246)`.

Thus the total for 15 relevant bits is `C(6,empty,empty)=67246`. Each relevant assignment occurs twice as B3 varies, proving `2·67246=134492` and the displayed exact mean. A separate minimax recurrence replacing the total cost by `1 + min_action max(child depths)` yields sharp depth 15. Root-optimal first action is a core bit; after observing it equal one, the same conclusion recurs for k=5,...,1, so the explicit core-first strategy attains the global optimum. Its downstream nine-bit fixed order attains R284EB's exact 2734 total.

Every DP state and its two optimum values and chosen actions are serialized in deterministic order for an independently recomputable SHA256 digest, and the 65,536-input witness is checked exhaustively. The theorem is exact for this declared query model and uniformly distributed frozen source cube.

## Evidence, limitations and next question

Run `python R284EC_full_guard_optimality_checker.py` (Python standard library); it regenerates `R284EC_full_guard_optimality_certificate.json`. Test coverage: 137,781 DP states, two recurrences, exact 65,536-input direct circuit simulation. `AUTHOR_PROVED / EXACT_FINITE_CERTIFIED`; independent mathematical review `NOT_REVIEWED`.

**Next scientific question:** whether R284EA's threshold and R284DZ's seven-bit quotient arithmetic combine to reduce actual end-to-end machine cost when all source bits are already packed, including branch prediction, precomputed masks, determinant evaluation, R284DS arc envelope and recovery. The native P000/X6 and joint-observer/future-operation semantics are preserved; an auxiliary query-cost theorem does not substitute for an X6 observer bridge.
