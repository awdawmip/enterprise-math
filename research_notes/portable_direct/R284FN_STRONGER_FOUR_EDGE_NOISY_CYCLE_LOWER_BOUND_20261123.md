# R284FN — 四代跨代漏写与全局读取噪声：四边距离强化下界

Date: 2026-11-23 (Asia/Shanghai) · Scientific status: AUTHOR_PROVED / FINITE_CROSSCHECKED / NOT_REVIEWED.

## The improvement

Directly continuing R284FM's exact global-noise flow-cut criterion, the prior bound

    n ≥ 4q + 2u + 2

is sharpened **for all nonnegative integers q,u** to

    **n ≥ 4q + 3u + 2.**                               (R284FN)

This is a **necessary bound for arbitrary four fixed binary epoch tags and legal non-atomic write orders**, with per-publication at most q omitted nominal changes, omissions carried arbitrarily many cycles, up to u independent read-bit flips, stateless stable decoding, and no wrong/rollback success during writes. Only stable endpoint correctness is used for the lower bound. It is sharp when u=0 by the R284FL construction. The existing separate R284FH general bound n≥3q+5u+2 remains complementary:

    n ≥ max(4q+3u+2, 3q+5u+2).

The new branch improves the second branch when q>2u. No universal constructive sharpness for u>0 is asserted.

## Complete symbolic proof

Use R284FM's precise model and all-u capacitated Hall criterion: for a phase-pair last-update bipartite multigraph G_ij, their noisy stable readout sets are disjoint iff there is a vertex subset U such that |E(U)|>q|U|+2u, where E(U) counts **internal multiedges**. Normalize c0 to zero and classify each coordinate by one of the seven nonzero bit patterns p=(c1,c2,c3), multiplicities x1,…,x7. Removing all-constant coordinates can only reduce n.

Assume for contradiction n≤4q+3u+1. Because any two phases' noisy stable balls must be disjoint, their Hamming distance is ≥2(q+u)+1: every total ≤q+u bit error is realizable by at most q omissions at its latest-transition buckets and at most u read flips. Every nonconstant four-phase pattern p takes the same value on at least one phase pair, so its multiplicity obeys

    x_p ≤ n−[2(q+u)+1] ≤ 2q+u.                      (1)

Consider the two opposite-phase graphs G_02 and G_13. Each is a four-edge-type K_(2,2). Their type sets are A0={2,3,6,7} and B0={1,3,4,6}; the common types {3,6} are **nonadjacent** edges in *each* graph. By R284FM, a separating witness with 2, 3 or 4 vertices must collect respectively ≥2q+2u+1, ≥3q+2u+1, or ≥4q+2u+1 internal coordinate edges. Equation (1) rules out all two-vertex witnesses.

There are now only the following cases.

**Both use 3-vertex witnesses.** Each witness contains two adjacent types. Let A⊆A0 and B⊆B0 be their two-type supports. Because common types 3 and 6 are nonadjacent, A∩B contains at most one type, with mass ≤2q+u by (1). Thus

    n ≥ Σ_(p∈A)x_p+Σ_(p∈B)x_p−Σ_(p∈A∩B)x_p
      ≥ 2(3q+2u+1)−(2q+u)
      = 4q+3u+2,

contradiction.

**One uses a 4-vertex witness and the other a 3-vertex witness.** Without loss of generality G_02's four types contain at least 4q+2u+1 positions, hence at most u positions lie outside A0. In G_13, a two-type adjacent witness can contain at most **one** of the shared nonadjacent types {3,6}, of mass at most 2q+u, and at most u positions from outside A0. Its total is ≤2q+2u, below the necessary 3q+2u+1. Contradiction. The reversed orientation is identical.

**Both use 4-vertex witnesses.** G_02 consumes all but at most u positions in A0. In particular x5≤u. Four pairwise distances d01,d12,d23,d30 are each ≥2(q+u)+1. Every nonconstant pattern except p5 contributes exactly twice to their sum, while p5 contributes four times; hence

    d01+d12+d23+d30 = 2n+2x5 ≥4[2(q+u)+1],

so n+x5≥4q+4u+2. But n≤4q+3u+1 and x5≤u imply n+x5≤4q+4u+1. Contradiction.

All possible witness combinations are exhausted, proving n≥4q+3u+2 for every q,u≥0. The proof is independent of the write-bit order, because it already rules out the stable-phase necessary conditions.

## Recalculation and scope

The standard-library checker R284FN_four_edge_noise_bound_checker.py, saved beside this note, exhaustively enumerates every 7-pattern multiplicity vector at n=4q+3u+1 for q∈{0,1,2,3}, u∈{0,1}. It checks all six pair-distance necessities and both exact K_(2,2) diagonal noise cuts; 128,996 vectors were checked, no candidates. These finite cases crosscheck the algebra but the theorem is the complete symbolic case proof above.

No new P000 axiom, classical continuum reinterpretation, formal CLAIM, author-independent Review or shared Result is introduced. The four-phase label is an auxiliary discrete state encoding; its relationship to heart-world/native geometric transport has not been promoted.

## Immutable provenance and next open question

- R284FL proof: enterprise-math@66cd6dcb564dc0d95c5a9536bd61aa2f62d3895e / research_notes/portable_direct/R284FL_ALL_Q_RESET_FREE_OMISSION_SHARP_CAPACITY_20261123.md.
- R284FM flow-cut theorem: enterprise-math@1d1c5dd412719c7aaf016187b6493b77253cd9f9 / research_notes/portable_direct/R284FM_NOISY_OBSERVER_FLOW_CUT_AND_ADDITIVE_LOWER_BOUND_20261123.md.
- Task-frozen R284CO scientific inputs retained as inherited by R284FL; no rebase of those sources.

**Next:** strengthen the combined lower bound in the positive-u transition regime 0<q≤2u using full six-pair flow cuts plus write-prefix monotonicity, or construct a complete code with n below the known two-block Gray upper bound 4q+8u+2. In particular the (q,u)=(1,1) sharp twelve-bit case should serve as a control witness. Afterwards extend to source-bank omissions and H-lag readers.
