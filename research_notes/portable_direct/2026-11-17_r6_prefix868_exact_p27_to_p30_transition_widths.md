# PREFIX-868 — Exact peak widths for 27–30 named binary BRC sources

Date: 2026-11-17. Scope: auxiliary named-source BRC integer observer, NOT an admitted native X6 Cell/Link/Port event model.
Scientific input pin: `f42f2906d77f24085c123f3ccfe9667d41caa96d`, unchanged.
Scientific predecessor: PREFIX-867 (`2026-11-17_r6_prefix867_exact_p19_to_p26_fixed_odd_transition_widths.md`), with the shared-GCD/CRT proof of PREFIX-861 and the finite zero-fiber obstruction of PREFIX-866.
Evidence class: author proof + exact C++17 finite exhaustion; independently reviewed: NO; canonical mathematical admission: NO.

## Model and result

Let `p>=1` and `N=2^p`. Each `u in {0,...,N-1}` represents p named binary source bits. A legal ordered heartbeat is exactly `(u,u)` or `(u, u xor (1<<i))`, for one `0<=i<p`.
Two fixed odd moduli `q1,q2>=3` reveal `(u mod q1, v mod q2)`. Demand injective recovery of the entire ordered transition `(u,v)`, including the changed named bit and direction. Let `B_fix,odd(p)` be the least possible `max(bit_length(q1),bit_length(q2))`.

**Theorem PREFIX-868.**

| p | Counting lower bound L | Exact B_fix,odd(p) | Valid CRT moduli q1,q2 | Excluded width |
|--:|--:|--:|:--|--:|
| 27 | 16 | **17** | 88913, 89149 | 16 |
| 28 | 17 | **17** | 125847, 125965 | counting alone |
| 29 | 17 | **18** | 177885, 178121 | 17 |
| 30 | 18 | **18** | 255895, 256017 | counting alone |

Here `L=ceil(log2(N*(p+1))/2)`, equivalently the smallest integer B such that `2^(2B)>=N*(p+1)`. No numerical logarithm is used in proofs or checks.

## Upper-bound construction and proof

For each row choose `q1=g*a`, `q2=g*b` as follows:

| p | g | a | b | h(g) | lcm(q1,q2)=g*a*b | N |
|--:|--:|--:|--:|--:|--:|--:|
| 27 | 59 | 1507 | 1511 | 29 | 134347543 | 134217728 |
| 28 | 59 | 2133 | 2135 | 29 | 268683345 | 268435456 |
| 29 | 59 | 3015 | 3019 | 29 | 537034815 | 536870912 |
| 30 | 61 | 4195 | 4197 | 30 | 1073991315 | 1073741824 |

Here `gcd(a,b)=1`, and `h(g)` is the smallest positive d for which `2^d = +1 or -1 (mod g)`. Each row satisfies `h(g)>=p`. Hence the increments `E={0} union {+/-2^i : 0<=i<p}` are distinct modulo g.

Given two residues r1,r2, their difference modulo g uniquely determines the signed increment `delta=v-u`. The congruences `v=r1+delta (mod q1)` and `v=r2 (mod q2)` then determine v modulo `lcm(q1,q2)=gab >=N`, so at most one admissible v in `[0,N)` exists. Finally `u=v-delta`. This proves full-transition injectivity for all four witnesses, including named-source and direction preservation. Each witness has the claimed peak bit width. No exhaustive 2^p-state search is necessary for these upper bounds.

## Lower-bound proof for p=27 and p=29

Set `b=16` for p=27 and `b=17` for p=29, and `M=2^b-1`. Every candidate pair is an ordered pair of odd `q1,q2 in [3,M]`. The accompanying checker enumerates the complete finite candidate domain, using only exact integer operations.

For any valid observer the following are **necessary**:

1. `h(q1)>=p` and `h(q2)>=p`. When this fails, two p-bit states with Hamming distance 2 have equal residues modulo that observation modulus; they share a legal single-flip neighbor, causing two complete ordered trajectories to have the same transcript. The same argument applies in reverse to the second modulus.
2. `q1*q2 >= N*(p+1)` by counting all N(p+1) ordered transitions.
3. `lcm(q1,q2)>=N`, because no-op transitions must be distinguished.
4. The zero first-residue fiber contains `m=ceil(N/q1)` old states `u=k*q1<N`, each with exactly p+1 distinct legal updates. All `m*(p+1)` resulting terminal states must give distinct residues modulo q2, so `q2>=m*(p+1)`.

Every candidate pair surviving these four necessary tests is checked against the **entire** zero first-residue fiber: enumerate `u=k*q1` and `v=u`, plus `v=u xor 2^i` for all `0<=i<p`; reject the pair as soon as any terminal residue `v mod q2` repeats. Two distinct enumerated transitions would have the same first residue (zero) and the same second residue, proving a collision. For p=27 and p=29, **zero pairs survive**. Since all pruned pairs already fail a proven necessary condition, this exhausts every candidate fixed odd-modulus pair at the excluded width.

Exact C++17 calculation certificate:

| p, excluded b | odd candidate pairs | h-safe odd moduli | eligible first q1 | pairs after necessary filters | zero-fiber survivors |
|:--|--:|--:|--:|--:|--:|
| 27,16 | 1,073,676,289 | 32,535 | 4,084 | 8,583,704 | **0** |
| 29,17 | 4,294,836,225 | 65,262 | 4,080 | 8,417,211 | **0** |

For p=29, computations were divided into four disjoint first-modulus ranges `[0,126900]`, `[126901,129000]`, `[129001,130000]`, `[130001,131071]`. The shard eligible counts are 2,063,648; 2,680,074; 1,648,760; 2,024,729, respectively, with zero survivors in all four. Their exact sum is 8,417,211. The h-safe count is calculated over the full common modulus domain in each shard; it must not be summed across shards. The finite checker source and results JSON are stored alongside this note.

For p=28 and p=30, `2^(2(L-1)) < N*(p+1)` directly proves the counting lower bound; the upper witnesses attain it.

## Coverage, provenance, and open questions

The lower bounds for p=27 and p=29 are finite exhaustive proof conditional on the shown short C++17 integer checker's correct execution and its explicit necessary-condition proofs. The checker was compiled with g++ -O3 -std=c++17 and completed: p27 in 36.2 s, p29 four shards in 23.6, 21.1, 12.8, and 15.8 s. Mathematical proof of the CRT upper witnesses is independent of full-state enumeration. The full 27/29 finite exclusions have **one checker implementation**, not a completed independent full-range crosscheck. The p=19 predecessor was independently checked in Python and informs the algorithm, but is not a new p=27/29 second implementation.

The frozen scientific input, P000 six-native-space/one-independent-time ontology, branch and observer provenance, and prior sources stay unchanged. The auxiliary two-port arithmetic model has not been asserted to implement permitted native X6 triadic dynamics. Shared-task CLAIM, Result, Driver review, and formal Activity association are independent operations.

Next: find a compact symbolic zero-fiber collision criterion eliminating millions of candidate pairs without enumeration, and test the p=31 boundary; separately test adaptive second-port moduli as a different observer class.
