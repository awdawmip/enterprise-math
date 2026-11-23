# R284FP — 高漏写区的含噪四代循环容量再强化：一位普适严格增益

Date: 2026-11-23 (Asia/Shanghai)
Status: AUTHOR_PROVED / FINITE_CROSSCHECKED / NOT_REVIEWED
Research mode: informed TASK_RESEARCH; unshared portable scientific result, no formal CLAIM or Result.

## 1. Precise model and inherited science

This note continues R284FO on the unchanged frozen R284CO scientific lineage. Four distinct fixed n-bit tags c_0,c_1,c_2,c_3 repeat cyclically. A publication writes changed coordinates nonatomically, with at most q omitted writes per publication. Unwritten residual bits may survive arbitrarily many cycles. Each read may flip at most u coordinates. The stateless decoder must separate all stable phases, never succeed as a third phase in a prefix, and never allow later successful old-phase reading after a successful new-phase reading in the same publication trajectory. q,u are nonnegative integers. This is an auxiliary discrete observer/tag model; P000 and ACTIVE X6 worldview are not altered.

We reuse the *necessary* adjacent-prefix distance lemma from R284FH and R284FO,
`d(c_i,c_{i+1}) >= A=2q+4u+1`, and the *exact* stable-state observer-flow-cut lemma from R284FM: for phases i,j, the last-nominal-update bipartite multigraph must have a vertex subset U with `|E(U)|>q|U|+2u`. These conditions are necessary for the full protocol; no sufficiency is inferred from this note.

**Theorem R284FP-1 (high-omission noisy strict bound).** For every integer u>=1 and q>=2u+1, every correct four-phase protocol has

```
n_min(q,u) >= 4q + 5u + 3.
```

Thus the preceding R284FO universal bound `4q+5u+2` is strictly improvable throughout this unbounded two-parameter region. In particular, `n_min(q,1)>=4q+8` for all q>=3. For (q,u)=(5,2) the bound improves from 32 to 33 bits. The theorem is a necessary lower bound, not a construction or a claimed sharp formula.

## 2. Column patterns and rigid boundary geometry

Assume for contradiction a valid code with `n<=4q+5u+2`. By R284FO, the earlier necessary bound already forces `n=N:=4q+5u+2`. Discard constant coordinates and normalize `c_0=0`; constant coordinates never help the decoder and may be discarded without weakening correctness. Let `x_p` count bit patterns `p=(c_1[k],c_2[k],c_3[k])`, p=1,...,7, with c1 as least significant bit; write

```
a=x_3, b=x_5, c=x_6, r=x_1+x_2+x_4+x_7.
N=a+b+c+r.
K=2q+u+1, A=2q+4u+1,
B=3q+2u+1, C=4q+2u+1.
```

Pattern 5 alternates 0,1,0,1 and changes on all four publication edges; the other six nonconstant patterns change on exactly two edges. Summing the four adjacent distance necessities yields

```
N+b >= 4q+8u+2, so b>=3u.                 (1)
```

Every nonalternating pattern p belongs to an adjacent edge on which it does not change, giving

```
x_p <= N-A=K.                              (2)
```

The opposite-phase flow graphs are K_(2,2) on pattern sets G02={2,3,6,7} and G13={1,3,4,6}. Their shared edges 3 and 6 are nonadjacent in *both* graphs. By the strict flow cut, each opposite graph needs one of:

- a two-vertex witness: one x_p >= 2q+2u+1;
- a three-vertex witness: two adjacent edge types with total >=B;
- a four-vertex witness: all four edge types with total >=C.

There is no possible two-vertex witness: every relevant p changes on only two publication edges, so (2) gives x_p<=K<2q+2u+1 for u>=1.

**Neither opposite graph can be limited to a three-vertex witness.** If both use three-vertex witnesses with disjoint pattern supports, their total demands and (1) imply `2N>=2B+(4q+8u+2)=10q+12u+4`; hence `N>=5q+6u+2>N`, contradiction. If supports meet, they meet at exactly one p in {3,6}; inclusion-exclusion, (2), and (1) imply

```
3N >= 2B+A+(4q+8u+2)=12q+16u+5.          (3)
```

For u>=2 this exceeds `3N=12q+15u+6`. For u=1, equality is forced. Then b=3, x_p=2q+2, all nonalternating positive columns lie in the union of the two two-pattern witness supports, and `N-x_p=A`. Both publication edges on which p remains unchanged must therefore change *every* other active coordinate, to meet distance A. The only other nonalternating pattern changing on both those edges is pattern 6 when p=3, or pattern 3 when p=6. But that complementary pattern is absent from both witness supports (they intersect only at p). The remaining positive support types cannot meet the two edges simultaneously. Contradiction.

Therefore at least one opposite graph needs a four-vertex witness. Suppose it is G02. From (1), its mass >=C and N=b+sum(other nonalternating patterns), we get

```
3u<=b<=3u+1;   x_1+x_4<=1.               (4)
```

If the other graph G13 uses a three-vertex witness, its two adjacent types consist of one of {3,6} and one of {1,4}; thus one common type x_p>=B-1=3q+2u. But (2) gives x_p<=K=2q+u+1, contradictory for q+u>=2. Since two-vertex witnesses were already excluded, **both opposite graphs must have four-vertex witnesses**.

Adding their four-vertex demands and using their shared edge classes {3,6} gives

```
(a+c)+(N-b) >= 2C
=> a+c >=4q-u+b.                         (5)
```

Now only three boundary histograms remain:

- If b=3u+1, (5) forces r=0 and a+c=2K-1. With a,c<=K, (a,c)=(K,K-1) or (K-1,K).
- If b=3u, then `a+c+r=2K`, (5) gives r<=2. Put alpha=K-a>=0 and beta=K-c>=0, so r=alpha+beta. Each residual type in {1,2,4,7} changes exactly one of edges (0,1),(2,3) and exactly one of edges (1,2),(3,0). The two former edges each need at least alpha residual changes, and the two latter each need at least beta, whence r>=2alpha and r>=2beta, forcing alpha=beta and r even. For r=2 the two residual columns must jointly cover all four edges exactly once. They can only be the pair {1,4} or the pair {2,7}. Yet (5) then gives a+c=2K-2=C-1, so both four-vertex witnesses separately require x_1+x_4>=1 and x_2+x_7>=1, which neither pair fulfills. Hence r=0 and a=c=K.

Thus, in all cases, x_p=0 outside {3,5,6} and the triple (a,b,c) belongs to

```
(K,3u,K),  (K,3u+1,K-1),  (K-1,3u+1,K).   (6)
```

This rigidity classification follows only from the necessary prefix distance and opposite-phase flow cuts; it does not assume a Gray architecture or a write ordering.

## 3. Adjacent-flow obstruction

With support confined to patterns {3,5,6}, the (0,1) comparison graph consists of an a-edge (pattern 3) and a b-edge (pattern 5), sharing exactly one last-update vertex; pattern 6 has identical phase values and contributes no edge. A separating cut must contain a single edge on two vertices or both edges on three vertices. The single-edge threshold is `2q+2u+1`; by (2) we have `a<=K<2q+2u+1`. Also `b<=3u+1<2q+2u+1` since q>=2u+1. Therefore the (0,1) separation cut forces

```
a+b>=B=3q+2u+1.                          (7)
```

Exactly analogously, (1,2) forces `c+b>=B`. Add them and use `a+c=N-b` from (6):

```
N+b>=2B
=> b>=2q-u>=3u+2.
```

This contradicts b<=3u+1 in (4). Hence the supposed N-bit protocol does not exist, proving `n_min(q,u)>=N+1=4q+5u+3`. QED.

## 4. Verification and precise boundary

Independent local exact-integer crosscheck used the full six-pair R284FO finite-cut model and the three histograms (6): for (q,u)=(1,1),(2,1) each of the three configurations passes the six *necessary* pair cuts; for (3,1),(4,1),(5,2), each configuration fails at least one adjacent flow cut. Separately, a SciPy/HiGHS mixed-integer feasibility search over all seven pattern counts returned infeasible for n=N at (3,1),(4,1),(5,2),(6,2), and feasible for (2,1),(4,2). These computations are secondary diagnostics, not the proof of the arbitrary-parameter statement; no claim of exhaustive full-protocol sufficiency is made for the feasible cases.

The existing R284FO standard-library integer checker previously enumerated all 177,100 seven-pattern histograms at (q,u,n)=(3,1,19) and excluded the boundary with six-pair cuts. This note extends the obstruction to every q>=2u+1, u>=1 by a written proof rather than redoing that complete search.

## 5. Source and next scientific question

- R284FO all-parameter baseline and near-boundary alternating-column bound: `awdawmip/enterprise-math@f6869ad1c8ad8896fb60fda9a41bd747375bab49:research_notes/portable_direct/R284FO_ALL_NOISE_GLOBAL_CYCLE_LOWER_BOUND_20261123.md` (also verified on current main).
- R284FM exact observer flow-cut theorem: `awdawmip/enterprise-math@1d1c5dd412719c7aaf016187b6493b77253cd9f9:research_notes/portable_direct/R284FM_NOISY_OBSERVER_FLOW_CUT_AND_ADDITIVE_LOWER_BOUND_20261123.md`.
- R284FH exact adjacent-prefix distance lemma and (1,1) sharp 12-bit result: `awdawmip/enterprise-math@74b390d267ec130a2da8fb170e10214aeeb7351e:research_notes/portable_direct/R284FH_RESET_FREE_SHARP_TWELVE_BIT_CYCLE_20261123.md`.

**Open:** Determine whether the new high-omission bound `4q+5u+3` is attainable on an infinite subfamily; at (q,u)=(2,1) classify the full prefix/no-rollback possibilities at width 15, where pair cuts alone allow three histograms but do not settle protocol legality; and extend the same typed residual observer to source-bank write omissions and H-lag reader aliasing. Author proof only; independent review and formal Result are pending. Preserve R284CO frozen inputs, P000 and existing source authors.
