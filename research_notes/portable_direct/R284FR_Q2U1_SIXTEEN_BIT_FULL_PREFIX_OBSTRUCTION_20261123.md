# R284FR — 四代跨代漏写 q=2、读噪声 u=1：十六位全局排除

Date: 2026-11-23 (Asia/Shanghai)
Status: EXACT_FINITE_PROOF / AUTHOR_RECALCULATED / NOT_REVIEWED
Mode: informed TASK_RESEARCH, independent portable science. Frozen R284CO science inputs and P000 unchanged. No shared CLAIM or formal Result.

## Statement and inherited model

Four distinct fixed binary phase words c0,c1,c2,c3 cycle 0→1→2→3→0. Each publication attempts each nominally changed bit exactly once in a chosen non-atomic order, may omit at most q=2 of these writes, and does not clear residual omissions from prior cycles. Each stateless read may flip at most u=1 bit. All stable reads must identify the actual phase; at any publication prefix successes may name only its source and target phases, and a reader may not obtain new success followed by old success while the writer remains at the same prefix.

**Theorem R284FR-1.** No 16-bit protocol satisfies these requirements. With R284FQ's earlier exclusion of widths <=15 and R284FE's 18-bit Gray construction, the presently certified interval is

    17 <= n_min(q=2,u=1) <= 18.

This theorem is about an auxiliary discrete binary observer code, not a theorem or proposed change to native six-dimensional P000 geometry.

## Finite coverage of all codes

Normalize c0=0 by complementing individual columns. Any constant coordinate can be deleted while simulating its former fixed value at decode time; therefore a minimal-width candidate has only the seven nonzero column patterns p=(c1[k],c2[k],c3[k]) with multiplicities x1,...,x7. Permuting coordinates within or between equal patterns preserves omissions, Hamming read flips, and availability of arbitrary write orders. All width-16 candidates are exhausted by

    sum(p=1..7) xp = 16, xp >= 0,
    number of histograms = binomial(22,6) = 74613.

For each histogram impose the necessary adjacent code distances >=2q+4u+1=9, and opposite distances >=2(q+u)+1=7. Exactly 1270 histograms remain. For all six phase pairs apply R284FM's exact stable-phase separation criterion: the bipartite last-nominal-change multigraph G_ij must have a vertex subset V with its internal edge count >q*|V|+2u=2*|V|+2. The checker computes all subsets of the eight last-change vertices and applies the criterion. Exactly **36** histograms survive.

## Universal local-prefix obstruction

For phase i, let S_i be the complete stable physical-word set after arbitrary many omitted-write cycles. R284FM proves that a word s belongs to S_i iff, relative to c_i, the mismatching bits in each of the four groups classified by their last nominal change edge number at most q independently. The checker enumerates this exact finite product, with up to two mismatches per group.

Define the **forced-phase mask** for any physical word w:

    F(w) = { j : d_H(w,S_j) <= 2u }.

The equivalence is exact: if d_H(w,S_j)<=2, there is a readout y within u=1 of w and also within u=1 of a stable word in S_j. Stable correctness therefore forces the stateless decoder to return j on y.

At any reachable physical write prefix w of edge i→i+1, a correct protocol necessarily has

    F(w) subset {i,i+1}, and |F(w)| <= 1.

A forced third phase violates the no-third-phase rule. If F(w) contains both i and i+1, the writer may pause at that exact prefix while independent legal reads produce new success and then old success, violating no rollback. The condition is used ONLY as a necessary obstruction; passing does not certify a full protocol.

For a proposed attempted-prefix bit set A and an omission subset M subset A of size <=2, consider every source state s in S_i. Successful bits are A\M and the physical prefix is

    w = (s & ~(A\M)) | (c_(i+1) & (A\M)).

Coordinate permutation symmetry within each pattern allows the attempted prefix to be represented solely by the seven counts t_p of attempted bits of each column type. Every possible actual write order induces a monotone sequence of unit count increments from zero to the full target count vector. A count-vector prefix is deemed safe only if **every** legal omission set M and every s in S_i obey the necessary forced-phase condition above. A BFS of the finite prefix-count lattice determines whether even one path of safe prefixes exists. If no such path exists, no bit-order selection can be correct.

## Exact output

The standalone standard-library integer checker R284FR_q2u1_16bit_obstruction_checker.py was executed successfully:

    n=16: 74613 complete coordinate-pattern histograms
    n=16: 1270 pass all six necessary distance bounds
    n=16: 36 pass all six exact endpoint observer cuts
    n=16: 35 fail edge 0->1 local-prefix condition
    n=16: unique edge-0 survivor fails edge 1->2

The single histogram permitting a local-safe first edge is

    (x1,x2,x3,x4,x5,x6,x7) = (0,0,0,0,9,7,0)
    (c0,c1,c2,c3) = (0,511,65024,65535).

Its transition 1→2 has no safe prefix-count path. Thus all 36 endpoint survivors are eliminated, and every other histogram was already eliminated by necessary distance or exact stable-separation constraints. This is exhaustive for width16, independently of nominal code selection and write-bit order. Together with the earlier <=15 obstruction, the lower bound is 17. QED.

## Verification and provenance

Arithmetic is exact Python integers/bitmasks; no floating point, approximate metric, sampled search or external solver. The independent mathematical reviewer has not audited the new proof or checker. The model-specific reachability lemma, R284FM flow-cut theorem and R284FQ smaller-width proof are cited as earlier author-proved sources, not freshly re-proved here. The present exhaustive checker is the load-bearing finite certificate and checks its asserted survivor counts.

Immutable frozen scientific provenance:
- R284FQ: enterprise-math@5ee9ad22baf8ac68e942743960859abda863cb02, research_notes/portable_direct/R284FQ_Q2U1_FIFTEEN_BIT_FIRST_PREFIX_OBSTRUCTION_20261123.md
- R284FM: enterprise-math@1d1c5dd412719c7aaf016187b6493b77253cd9f9, research_notes/portable_direct/R284FM_NOISY_OBSERVER_FLOW_CUT_AND_ADDITIVE_LOWER_BOUND_20261123.md
- R284FE: enterprise-math@9974b3b5a1031bb5c841ab5a4950a9c55baed9e0, research_notes/portable_direct/R284FE_GRAY_EPOCH_SHARP_SEPARABLE_CAPACITY_20261123.md
- R284FO: enterprise-math@f6869ad1c8ad8896fb60fda9a41bd747375bab49, research_notes/portable_direct/R284FO_ALL_NOISE_GLOBAL_CYCLE_LOWER_BOUND_20261123.md

Next unresolved issue: search for a valid 17-bit protocol for (q,u)=(2,1), or derive a new finite prefix obstruction excluding all width17 candidates; either outcome settles whether n_min is 17 or 18. Reuse the exact last-change residual groups, six endpoint cuts and physical prefix constraints; avoid converting stable-only feasibility into completed protocol correctness.

Control: own registration request r1-20261123-1709-r284fr-own-register-v1 and owner inventory request r1-20261123-1703-owner-inventory-v1; registration identity/Activity and shared CLAIM are separate from publication.