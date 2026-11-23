# R284FQ — 两次漏写、一次读取翻转的四代循环：十五位完全排除与首次写入见证

Date: 2026-11-23 (Asia/Shanghai)  
Status: EXACT_FINITE_PROOF / AUTHOR_CROSSCHECKED / NOT_REVIEWED  
Mode: informed TASK_RESEARCH; portable independent science. No shared CLAIM, formal Result, independent Review or P000 change.

## 1. Scope and statement

Continue the fixed R284CO scientific lineage and R284FO/R284FM, with four distinct fixed binary tags c0,c1,c2,c3 repeated cyclically. Each non-atomic publication attempts each changed bit once and may omit at most q=2 writes; residual omissions persist without a reset across arbitrarily many generations. Each stateless read may flip at most u=1 bits. All stable-phase observations must identify the correct phase; any write prefix may return only old/new success or RETRY, with no new-success-then-old-success rollback even if the writer pauses at that prefix. Write-bit order is arbitrary but fixed per edge. The claim is for this discrete auxiliary label/observer model; P000/ACTIVE six-axis ontology is untouched.

**Theorem R284FQ-1 (strict finite obstruction).** Every correct such protocol has

    n_min(q=2,u=1) >= 16.

The known two-group Gray majority construction of R284FE uses 18 bits, so the presently certified interval is

    16 <= n_min(2,1) <= 18.

Neither 16-bit nor 17-bit attainability is asserted. The previous universal R284FO bound gives n>=4q+5u+2=15 here, so it is enough to exclude n=15.

## 2. Exact exhaustive coordinate-orbit classification at width 15

Complement each coordinate as necessary to normalize c0=0. Constant columns can be removed: a putative code with a constant coordinate projects to a no-longer tag with the same target distinctions, and a reader can simulate the old decoder on the fixed constant-coordinate extension. Thus for a minimal width all columns are nonconstant. Permuting the remaining columns preserves the physical omission/read model and each phase's legal prefix-order choices. Every candidate is represented by one ordered multiplicity vector (x1,...,x7), sum 15, where p is the 3-bit column (c1,c2,c3), c1 least-significant.

There are exactly C(15+6,6)=54,264 weak compositions. Evaluate necessary R284FH/R284FO adjacent distance d(ci,c(i+1))>=2q+4u+1=9, the two opposite distances >=2(q+u)+1=7, and R284FM's *exact* stable-observation separation criterion on all six pairs:

    for each i<j there exists a vertex subset U in Gij with
           |E(U)| > q|U|+2u = 2|U|+2.

An eight-vertex subset scan is exact: each coordinate differing between two phases provides one edge from its last-nominal-update group on the left to its analogous group on the right, with multiplicity. For each nonempty subset U, its edge multiplicity is the sum of relevant x_p. The flow-cut theorem equates this condition to disjoint radius-one readout sets for stable phases, with arbitrary finite histories of omitted writes.

The independently executed standard-library checker gives

    54,264  total coordinate-permutation histograms;
       306 pass all six necessary distances;
         3 pass all six exact stable-observer cuts.

The three survivors, with x_p=0 unless p=3,5,6, are:

| Case | x3 | x5 | x6 | (c0,c1,c2,c3), decimals |
|---|---:|---:|---:|---|
| A | 5 | 4 | 6 | (0,511,32287,32736) |
| B | 6 | 3 | 6 | (0,511,32319,32704) |
| C | 6 | 4 | 5 | (0,1023,31807,32704) |

These three satisfy endpoint separation but must still satisfy the non-atomic publication-prefix conditions. There is no other 15-bit orbit to consider.

## 3. Six explicit first-write contradictions

In phase 0->1, exactly the pattern-3 and pattern-5 coordinates change. Any allowed order therefore starts with one of these two patterns. Within a pattern the coordinates are equivalent under bit permutation; test the representative first bit k in the following complete table.

For each row, s0 is a legal stable physical state in phase 0. Successfully writing bit k (no omission) produces physical prefix v. The table gives a legal observed readout y within one flip of v and a phase-j stable physical witness sj within one flip of y. Therefore the stateless decoder must label y as j. If j=1, a second observed readout v itself is at distance one from stable phase-0 word s0, so a reader at the **same physical prefix** may observe success phase 1 and then phase 0: forbidden rollback. If j is 2 or 3, the first observed success is already a forbidden third-phase success.

| Case | First type | k | s0 | v | y | Forced j | sj | Defect |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| A | 3 | 0 | 102 | 103 | 111 | 1 | 127 | new then old |
| A | 5 | 5 | 195 | 227 | 231 | 1 | 239 | new then old |
| B | 3 | 0 | 198 | 199 | 207 | 1 | 223 | new then old |
| B | 5 | 6 | 387 | 451 | 455 | 1 | 463 | new then old |
| C | 3 | 0 | 3078 | 3079 | 3087 | 2 | 7183 | third phase |
| C | 5 | 6 | 1152 | 1216 | 3264 | 3 | 7360 | third phase |

Every number denotes an exact 15-bit integer physical word. All six rows were independently checked with Hamming XOR popcounts:

    d(v,y) <= 1, d(y,sj) <= 1,
    d(v,s0) <= 1 whenever j=1.

The latter relation is immediate: the first successful write changes exactly one bit of s0. Both s0 and sj obey the complete all-history stable-state criterion: for their respective phase, errors from the nominal codeword occupy at most two coordinates in each of the four last-nominal-change groups (R284FM's exact reachability lemma). The checker independently computes those groups and asserts this bound for each row. All witnesses use zero omissions during the current first-bit write, which is allowed under the budget.

By coordinate-permutation symmetry the two first-bit cases cover **every** possible first write choice, irrespective of all later update order and omission patterns. Thus no one of the three surviving histograms admits a legal phase-0->1 first step. Hence n=15 is impossible. Together with the already proved n>=15, we conclude n>=16. QED.

## 4. Reproducible artifact and verification strength

Source: R284FQ_q2u1_first_prefix_checker.py; Python 3 standard library only (itertools, math), no floating-point arithmetic or external solver. Execution completed:

    exact tuples 54264 pass six distances 306
    six-cut survivors 3 [(0,0,5,0,4,6,0),
                         (0,0,6,0,3,6,0),
                         (0,0,6,0,4,5,0)]
    first-prefix witnesses verified 6
    conclusion: no 15-bit protocol for q=2,u=1; with R284FO n>=15, n>=16

The finite exhaustiveness is justified by seven-class coordinate-permutation coverage plus all six exact observer cuts. Its symbolic witness check verifies the admitted stable states and the first-prefix read distances, rather than treating a stable-only code as a completed protocol. The existing R284FO all-parameter theorem supplies the smaller-width exclusion; R284FE supplies an 18-bit upper construction. Actual independent reviewer acceptance remains NOT_REVIEWED.

## 5. Immutable sources and open question

- R284FO universal lower bound: project @ f6869ad1c8ad8896fb60fda9a41bd747375bab49, research_notes/portable_direct/R284FO_ALL_NOISE_GLOBAL_CYCLE_LOWER_BOUND_20261123.md.
- R284FM exact residual observer flow cuts: project @ 1d1c5dd412719c7aaf016187b6493b77253cd9f9, research_notes/portable_direct/R284FM_NOISY_OBSERVER_FLOW_CUT_AND_ADDITIVE_LOWER_BOUND_20261123.md.
- R284FH adjacent-prefix distance: project @ 74b390d267ec130a2da8fb170e10214aeeb7351e, research_notes/portable_direct/R284FH_RESET_FREE_SHARP_TWELVE_BIT_CYCLE_20261123.md.
- R284FE 18-bit independent-group construction: project @ 9974b3b5a1031bb5c841ab5a4950a9c55baed9e0, research_notes/portable_direct/R284FE_GRAY_EPOCH_SHARP_SEPARABLE_CAPACITY_20261123.md.
- R284FP present-run all-parameter high-omission obstruction: project @ de49ae0239abee14619a730fe6ea60614a2cde5b, research_notes/portable_direct/R284FP_HIGH_OMISSION_NOISY_CYCLE_PLUS_ONE_BOUND_20261123.md.

Next: determine whether a 16- or 17-bit full protocol exists for (q,u)=(2,1), using exact endpoint flow cuts to reduce coordinate histograms, then observer-forced prefix cut arguments (or construct a legal update order). More generally extend the first-prefix obstruction into an all-q,u inequality beyond the R284FP high-omission region. Frozen R284CO science pins, P000, original authors and other live owner claims remain unchanged.
