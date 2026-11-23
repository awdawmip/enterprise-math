# R284FP — u=1 跨代漏写四代循环的全 q 强化下界

Date: 2026-11-23 (Asia/Shanghai)
Status: AUTHOR_PROVED (analytic q>=3, finite exact q=2, inherited sharp q=1); NOT_REVIEWED
Mode: informed TASK_RESEARCH, portable scientific source. No shared CLAIM or formal Result asserted.

## Theorem and exact scope

Keep the frozen R284CO four-phase observer-tag model inherited by R284FH, R284FM and R284FO: four distinct fixed binary words c0,c1,c2,c3 cycle; every changed bit is attempted once in fixed non-atomic order, at most q attempted writes are omitted on each edge, omissions can persist across arbitrarily many generations, and reads suffer at most u arbitrary bit flips. The stateless decoder must correctly identify all stable phases, never identify a third phase during publishing and never allow a successful new-phase read followed by an old-phase read at the same prefix.

**R284FP-1:** For every integer q>=1, with exactly one permissible read flip (u=1), every correct scheme, including arbitrary nonseparable codes and write orders, satisfies

    n_min(q,1) >= 4q+8.

At q=0 the already known sharp value is n_min(0,1)=7. At q=1 the earlier R284FH theorem gives n_min(1,1)=12. For q>=2 the two-block reset-free Gray construction of R284FC gives the upper bound n_min(q,1)<=4q+10. The remaining capacity gap is at most two bits.

## Analytic near-boundary classification

Normalize c0=0 by per-column complementation; remove all-constant columns. The seven nonzero types p=1,...,7 encode (c1,c2,c3) with the low bit belonging to c1. Write x_p for type multiplicity and b=x5 for the alternating type 0101.

Assume n=4q+7. With u=1 the existing four adjacent-prefix distance necessities are

    A=2q+5,     d(c_i,c_(i+1)) >= A,
    n+b >= 4q+10, hence b>=3.

R284FM's exact opposite-phase capacitated flow cuts are K2,2. The pair (0,2) uses types {2,3,6,7}, and (1,3) uses {1,3,4,6}. Their shared types 3 and 6 form disjoint edges. A separating witness for either graph must have either one type of size >=2q+3 (two-vertex cut), two adjacent types of total size >=3q+3 (three-vertex cut), or all four graph types of total size >=4q+3 (four-vertex cut).

**Two-vertex witnesses cannot occur:** their type is absent from at least one adjacent publication edge, which gives n >= (2q+3)+(2q+5)=4q+8.

**Two three-vertex witnesses cannot occur:** disjoint type supports would consume >=6q+6>n-b. Overlapping supports share a single type p in {3,6}. Let m=x_p. Inclusion-exclusion, an edge where p does not change, and the four-edge distance sum imply

    n-b+m >=6q+6;   n-m >=2q+5;   n+b >=4q+10.

At n=4q+7, all are equalities. Thus b=3, m=2q+2, and exactly two other supported types have q+1 coordinates apiece, one taken from each opposite graph. The two edges where p does not change receive together only 2(q+1) changes from these two types, whereas their distance bounds require 2(A-b)=4q+4 changes. Contradiction.

**A mixed four-vertex and three-vertex witness cannot occur when q>=1:** If the (0,2) graph uses four vertices, its complement obeys x1+x4<=4-b<=1. A three-vertex witness in the (1,3) graph would contain p in {3,6} plus one type in {1,4}, giving x_p>=3q+2. But a publication edge that leaves p fixed gives x_p<=n-A=2q+2, impossible for q>=1. The swapped case is symmetric.

Therefore BOTH opposite graphs require four-vertex witnesses, giving

    b+x1+x4<=4,    b+x2+x7<=4,    b>=3.

If b=4, the four exceptional types x1,x2,x4,x7 vanish and adjacent edge distances force x3,x6>=2q+1, with x3+x6=4q+3. If b=3, put s=x1+x2+x4+x7<=2. When s=1 the two alternating edge pairs require x3,x6>=2q+2 although their sum is only 4q+3. When s=2, one exceptional type must come from {1,4} and one from {2,7}; one of x3,x6 must be >=2q+2 and the other >=2q+1 although their sum is 4q+2. So s=0, x3=x6=2q+2. The only surviving necessary histograms are

    (x1,x2,x3,x4,x5,x6,x7)=
      (0,0,2q+1,0,4,2q+2,0)
      (0,0,2q+2,0,3,2q+2,0)
      (0,0,2q+2,0,4,2q+1,0).       (*)

This is an exact symbolic classification at n=4q+7, q>=1, using only existing necessary conditions.

## Analytic exclusion for q>=3

In every candidate (*) an adjacent phase pair differs on exactly two types, p=5 and p=3 or p=6. The two edges in its capacitated residual graph share the newly updated vertex: a 3-vertex star. For q>=3, no two-vertex cut can separate this pair, because x3,x6<=2q+2 and b<=4<2q+3. Its three-vertex cut therefore requires BOTH

    x3+b>=3q+3,    x6+b>=3q+3.

But (*) gives x3+x6+b=n=4q+7 and b<=4. Hence

    6q+6 <= x3+x6+2b =4q+7+b <=4q+11,

which is impossible for every q>=3. So n>=4q+8 for the entire infinite range q>=3, with no enumeration.

## Exact finite exclusion at q=2

For q=2,u=1,n=15, (*) gives only three histograms, with triples (x3,x5,x6)=(5,4,6), (6,3,6), (6,4,5). The companion Python checker independently enumerates all C(21,6)=54,264 seven-type histograms and all six exact flow cuts; precisely these three survive. It constructs all stable words from the last nominal update of each coordinate, with up to two missed writes in each last-update group, and determines the labels forced by any observation within one bit of a stable word.

For each of the four publication edges, for every possible FIRST written bit, the checker finds a reachable stable source state such that the physical word after this first successfully attempted write admits either (i) a forced third-phase label, or (ii) both forced old and new labels, so two reads may legally return new then old without another write. The no-omission case of this first attempt is legal. Therefore no fixed order can work.

Actually executed, with Python standard-library exact integers:

| (x3,x5,x6) | Stable state counts, phases 0,1,2,3 | First-bit choices excluded |
| --- | --- | ---: |
| (5,4,6) | 896,1012,896,1012 | 38 |
| (6,3,6) | 1012,1012,1012,1012 | 36 |
| (6,4,5) | 1012,896,1012,896 | 38 |

All **112/112** first-bit choices are excluded. Examples (phase 0, first bit 0; stable physical source, physical prefix, forced phase bitmask) are (102,103,3), (198,199,3), (3078,3079,5). Mask 3 forces labels 0 and 1; mask 5 forces 0 and 2. Every stable read ball is checked for interphase collision. The checker emits every witness, not only these examples.

For q=1 reuse the already proved sharp R284FH value 12. These cases complete R284FP-1.

## Provenance, limits, and next research question

The scientific input is the frozen R284CO lineage, carried unchanged through R284FH/R284FM/R284FO. Relevant source pins:
- R284FH theorem and executable proof: enterprise-math@74b390d267ec130a2da8fb170e10214aeeb7351e, research_notes/portable_direct/R284FH_RESET_FREE_SHARP_TWELVE_BIT_CYCLE_20261123.md
- R284FM observer-flow theorem: enterprise-math@1d1c5dd412719c7aaf016187b6493b77253cd9f9, research_notes/portable_direct/R284FM_NOISY_OBSERVER_FLOW_CUT_AND_ADDITIVE_LOWER_BOUND_20261123.md
- R284FO previous all-u lower bound: enterprise-math@f6869ad1c8ad8896fb60fda9a41bd747375bab49, research_notes/portable_direct/R284FO_ALL_NOISE_GLOBAL_CYCLE_LOWER_BOUND_20261123.md

P000, the ACTIVE worldview, the six-axis geometry and BRC source semantics are unchanged. These auxiliary binary observer codes are not a native six-axis geometry or BRC numerical computation. No independent mathematical Review or formal Result is asserted.

**Next:** Decide whether a q=2,u=1 complete 16-bit or 17-bit nonseparable code exists, with every prefix and persistent omission checked. For q>=3, check full six-pair cuts at n=4q+8 and 4q+9; look for a universal second obstruction or a tight construction.