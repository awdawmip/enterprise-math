# PREFIX-864 — Exact odd two-read full-transition peak widths at p=10..16 and p=18

Date: 2026-11-17. Role: auxiliary TASK_RESEARCH / named-source BRC observer.
Frozen scientific input: `f42f2906d77f24085c123f3ccfe9667d41caa96d` (unchanged).
Predecessors: PREFIX-861 common-GCD CRT, PREFIX-862 lower bound, PREFIX-863 universal two-bit upper gap.
Status: AUTHOR_PROVED + EXACT_FINITE_EXHAUSTION; NOT_INDEPENDENTLY_REVIEWED; NOT_ADMITTED.

## The exact problem

The complete state is `u in {0,...,2^p-1}`, with its p binary positions denoting p named sources. One legal heartbeat maps u to v=u (no-op) or v=u xor 2^i for exactly one i in [0,p-1]. Both endpoints are unknown. Read the ordered transcript `(u mod q1, v mod q2)` with fixed, preselected ODD moduli `q1,q2>=3`; demand injectivity on all `2^p(p+1)` legal ordered transitions.

A modulus q uses exactly `ceil(log2(q+1))` bits in the inclusive-maximum-residue convention, which equals the binary bit length of q for odd q. Peak width is the larger of the two widths. Write `B_fix,odd(p)` for the minimum.

This is a complete-transition observer, not an initially-synchronized terminal-state-only observer and not a native X6 event/Cell/Link/Port equivalence.

## Theorem 864-A: exact fiber/divisibility criterion (any positive moduli)

For fixed q1, and each old-residue class r=0,...,q1-1, define the MULTISET

`V_r = [v : (u,v) is a legal ordered transition and u mod q1 = r]`.

The ordered map `(u,v) -> (u mod q1, v mod q2)` is injective if and only if BOTH hold:

1. No `V_r` contains repeated integer v.
2. For every r and every pair of DISTINCT values v,w in `V_r`, the positive difference `|v-w|` is not divisible by q2.

Proof: Two distinct legal transitions collide exactly when their old endpoint residues modulo q1 agree AND their new endpoint residues modulo q2 agree. Grouping by the first residue gives the specified multisets. A repeated v collides under all q2; different v,w collide exactly when q2 divides their difference. Both directions follow, without a probabilistic assumption. QED.

**Certificate algorithm**: For all odd q1 from 3 through 2^B-1, build `V_r` exactly by iterating `u=r,r+q1,...<2^p` and emitting `u, u xor 1, ..., u xor 2^(p-1)`. If `2^p(p+1)>q1(2^B-1)`, pigeonhole excludes this q1. Otherwise sort each multiset, detect duplicates, and mark forbidden odd q2<=2^B-1 dividing every nonzero pair difference. Every unmarked q2 is an injective witness. Precompute odd divisors of all possible differences 1..2^p-1. This enumerates EVERY admissible ordered odd pair; no sampling or heuristic pruning is used.

## Theorem 864-B: new exact optimal widths

The certified values are:

| p | Counting lower L(p) | B_fix,odd(p) | Constructive (q1,q2) | Proof of lower width |
|---:|---:|---:|---|---|
| 10 | 7 | **8** | (115,207) | all 3,969 odd pairs at B=7 fail |
| 11 | 8 | **8** | (207,253) | counting bound (attained) |
| 12 | 8 | **9** | (261,493) | all 16,129 odd pairs at B=8 fail |
| 13 | 9 | **10** | (261,1015) | all 65,025 odd pairs at B=9 fail |
| 14 | 9 | **10** | (493,1015) | all 65,025 odd pairs at B=9 fail |
| 15 | 10 | **11** | (629,1961) | all 261,121 odd pairs at B=10 fail |
| 16 | 11 | **11** | (1295,1887) | counting bound (attained) |
| 18 | 12 | **12** | (2405,4033) | counting bound (attained) |

The universal counting bound is `L(p) = ceil((p+log2(p+1))/2)`, as there are exactly `2^p(p+1)` ordered legal transitions and no more than `2^(2B)` distinct pairs of B-bit messages. The finite complete lower-width exclusions and the constructive upper witnesses yield the exact widths. Monotonicity in allowed peak width rules out all smaller widths. The companion C++17 program outputs exact counts and checks the witnesses' arithmetic. All output is deterministic integer arithmetic.

At B=8, p=11 has EXACTLY TWO injective ordered odd pairs in the whole search domain: (207,253) and its reversal (253,207). At p=10, B=8 has 56 pairs; at p=12, B=9 has 54 pairs. Reversal is not assumed valid in general; both pairs here were enumerated and checked.

## Theorem 864-C: compact CRT witnesses and reproducible decoding

The eight constructions share the same sufficient invariant. Let `q1=g a, q2=g b` with g odd >1, a and b coprime, `g a b >= 2^p`, and `h(g)>=p`, where `h(g)=min {d>=1 : 2^d == +1 or -1 (mod g)}`.

The legal difference `delta=v-u` belongs to `{0} union {+/-2^i : 0<=i<p}`. This set has pairwise distinct residues modulo g when h(g)>=p. Consequently `(v mod q2)-(u mod q1) (mod g)` uniquely determines delta. From `v == (u mod q1)+delta (mod q1)` and `v == v mod q2 (mod q2)`, generalized CRT uniquely recovers `0<=v<2^p` because `lcm(q1,q2)=g a b>=2^p`. Then `u=v-delta` and the named source/direction are recovered. QED.

The small shared factors are `h(23)=11, h(29)=14, h(37)=18`, each checked by modular powering. Witness multipliers (g,a,b) by p are:
`10:(23,5,9); 11:(23,9,11); 12:(29,9,17); 13:(29,9,35); 14:(29,17,35); 15:(37,17,53); 16:(37,35,51); 18:(37,65,109)`.
For p=18, CRT's combined modulus is exactly `37*65*109=262145=2^18+1`. The p=11, p=16 and p=18 constructions attain the counting bound, hence are optimal among ALL two-read B-bit transcript schemes, including adaptive choice of the second read, for the same complete-transition objective.

## Evidence and limitations

- `PREFIX864_R6_EXACT_ODD_TRANSITION_OPTIMIZER.cpp` is a self-contained C++17 exact exhaustive checker and CRT verifier; build with `g++ -O3 -std=c++17`.
- `PREFIX864_R6_EXACT_ODD_TRANSITION_RESULTS.json` is the exact stdout. The local execution returned `ALL_EXACT_ASSERTIONS_PASSED`.
- The program exhausts the lower-width candidate pairs for p=10,12,13,14,15; verifies all candidate pairs at p=11,B=8 and two additional upper-width domains p=10,B=8 and p=12,B=9; directly enumerates complete transitions for p=10,11,12 witnesses. The p=13,14,15,16,18 upper witnesses are established by the proven CRT sufficient conditions, so no unrun full-state enumeration is claimed.
- This is an auxiliary discrete named-source observer; BRC residual type, actual port semantics and native X6 event authorization are unchanged.

## Next unresolved scientific unit

Find a symbolic necessary condition stronger than counting, capable of deciding p=17 at B=11 without large enumeration. Test whether the exact fiber-divisor criterion can be compressed to a small signed-difference invariant and locate further counting-optimal infinite or unbounded parameter families without changing the observation target. The current p=17 CRT witness gives B<=12 and counting gives B>=11.

## Exact source anchors

Frozen pin above; `awdawmip/enterprise-math` PREFIX-863 at `2a142a74731baf17f97d8f0e2240e4ed14a6da86`, PREFIX-861 at `727d6ca2dee6f707e3dd3cabba600d2c21b12bc8`, PREFIX-862 at `77cb8fcf7c4583af5325bcfc229941b321b25612`. Current P000 V5 and ACTIVE Heartbeat World are project premises; this note does not alter those files or the shared X6 task.
