# R762BW — V17 directed-exchange ledger and S3 holonomy: sharp five-switch loss and six-switch zero-current memory

Date: 2026-11-16 (Asia/Shanghai). Task: RS-X6-TRIADIC-CLOSURE-DYNAMICS; immutable publication TP2-8B7E13C5904A2D6F1142.
Status: AUTHOR-PROVED / EXACT FINITE INTEGER CHECK THROUGH LENGTH SIX / NOT_REVIEWED.

## Frozen inputs and carefully typed conditional extension

Retain the task's scientific input pin awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389:p000_reality_foundation.json (P000 V5). The six signed native spatial axes, Cell relationships, separate native time and the three-force TRIADIC_CLOSURE_E primitive balance premise are unchanged. No Euclidean vector-sum-zero law is used.

V17 source: research_notes/X6_ACTIVE_TRIAD_HOLONOMY_CONTROL_V17_20260906.md, blob 42b810a8f82c504833027da17884cc4fb2943e5b. A conditional internal frame f=(a,b,c) consists of three distinct members of U={1,2,3,4,5,6}. Each switch chooses one of its three ordered slots and inserts one of the three absent labels, preserving the other two slots. There are 120 frames and nine outgoing switches at every frame. A *based return* starts at (1,2,3) and ends at any ordered frame containing the same unordered triad {1,2,3}. The resulting ordered frame is its S3 holonomy h, relative to the base frame.

Define an auxiliary **axis-context** nonnegative directed ledger H on the 30 ordered arcs (x,y), x≠y: each V17 replacement x→y increments H_xy by one. On each of the 15 unordered pairs x<y define j_xy=H_xy−H_yx. This is a V29-*style* counting transducer, not a claim that a native signed Cell/Port/Link event is literally an axis-label replacement.

V29: research_notes/X6_NETWORK_EVENT_LEDGER_AND_CONTRAST_TRANSDUCER_V29_20260906.md, blob 6849ebd3fc776fb7da3b46627376490aba3dad99; actual native PASS/TRANSFER are typed Cell and Port events. V39: research_notes/X6_CYCLE_CURRENT_S3_OPERATION_SAFE_PORT_V39_20260906.md, blob 8151d0b6a4b65225b93d858bbc8a5d7037bf9cef; (j,h) already forms the coarsest exact port for the stated based-loop current-plus-holonomy language. R762BV, Draft PR #2535@4d6f0d9d32c3b374d7f87ecd0269b300ad52d241, gave the exact *marginal* V17 return/holonomy spectrum. R762BW resolves newly the *joint* event-ledger/holonomy fibers and first possible information-loss lengths.

## Theorem 1: circulation and exact first loss of the directed event histogram

For any m≥0 and any m-step based V17 return:

(A) The nonnegative 30-vector H is balanced: for each x in U, sum_y H_xy = sum_y H_yx. Its antisymmetric current j is therefore a cycle (zero graph boundary).

(B) For each fixed m≤4, either H or the weaker j uniquely determines h among the based returns of length m.

(C) The first length where the complete **directed** histogram H fails to determine h is exactly m=5. There are 2,952 based five-switch paths, 684 distinct H-fibers and exactly 144 H-fibers containing two different holonomies; the other 540 have one. For the weaker j observer, 184 distinct current fibers occur, with 38 holonomy-mixed fibers.

**Proof of (A):** Let b_x(t) in {0,1} record whether label x occupies a frame slot at time t. A replacement x→y changes b_x by −1, b_y by +1, all other occupancies unchanged. Summing over the path gives b_x(m)−b_x(0)=sum_y H_yx−sum_y H_xy. Based return makes the left side zero. Antisymmetrization yields ∂j=0.

**Explicit shortest pair for (C):** The entries below are ordered frame slots, not signed native spatial Cell position vectors.

    A: 123 -> 423 -> 123 -> 143 -> 153 -> 123
    B: 123 -> 423 -> 523 -> 543 -> 243 -> 213

A has arc sequence 1→4, 4→1, 2→4, 4→5, 5→2. B has 1→4, 4→5, 2→4, 5→2, 4→1. Both have exactly one of each five listed arcs, with every other directed count zero, hence **identical full H**, not just the same j. Their net current is the directed 2→4→5→2 cycle. Yet A ends at the identity internal frame (1,2,3), whereas B ends at (2,1,3), a transposition.

**Exact proof of the lower bound and census:** The executable companion R762BW_V17_EXCHANGE_LEDGER_VERIFY.py checks every switch path from the fixed base at lengths m=0,1,2,3,4,5,6. At each step the successor set is complete (exactly 3 occupied slot choices × 3 currently absent label choices). The dynamic program carries the full ordered frame, all 30 exact directed counts, and an exact nonnegative integer *path multiplicity*. It merges only identical (frame,H) keys, so no distinct holonomy can disappear through aggregation. For each m it groups all based-return keys by H and by antisymmetric j, checking how many distinct final ordered frames each fiber contains. This is a full finite exhaustive argument for the declared horizon, not sampling or extrapolation. For m≤4 every H and j fiber has exactly one terminal h; the explicit pair above attains five. At m=5 the H-fiber sizes by number of holonomies are 540×1 and 144×2.

| Switch length m | All 9^m paths | Based returns | Distinct H fibers | Mixed H fibers | Distinct j fibers | Mixed j fibers |
|---:|---:|---:|---:|---:|---:|---:|
| 0 | 1 | 1 | 1 | 0 | 1 | 0 |
| 1 | 9 | 0 | 0 | 0 | 0 | 0 |
| 2 | 81 | 9 | 9 | 0 | 1 | 0 |
| 3 | 729 | 36 | 36 | 0 | 36 | 0 |
| 4 | 6561 | 369 | 171 | 0 | 91 | 0 |
| 5 | 59049 | 2952 | 684 | 144 | 184 | 38 |
| 6 | 531441 | 26937 | 2571 | 1008 | 823 | 505 |

## Theorem 2: the first zero-net-current nontrivial holonomy has length six

For a based loop, j=0 means H_xy=H_yx for each unordered pair. Therefore m=sum_{x≠y}H_xy is even. Complete exact enumeration shows all zero-j based returns of lengths m=0,2,4 have identity terminal holonomy. A six-switch zero-current nontrivial holonomy is explicitly:

    123 -> 423 -> 523 -> 543 -> 513 -> 413 -> 213.

The arc multiset is 1→4, 4→5, 2→4, 4→1, 5→4, 4→2. Every directed edge has its reverse, so j=0. The endpoint ordered frame (2,1,3) is the slot transposition (12). Combining the even-length lower bound with the complete m≤4 check proves exact minimality: **six switches**.

At length six, the exact integer census finds **5,337** based paths with j=0: 5,265 with identity frame and 24 with each of the three possible transpositions (72 nonidentity total). This is a conditional BRC witness that zero net exchange current can preserve non-Abelian internal time/transport memory.

## Reproducible checker, observer semantics and actual boundary

The Python 3.9+ standard-library companion performs exact nonnegative-integer dynamic programming, iterates every permitted nine-way V17 switch at each length m≤6, checks both explicit witnesses, asserts the entire return census and holonomy-fiber distributions, and prints the JSON evidence with no floating point or random sampling. Its complete horizon is m≤6. The general circulation identity and even-length j=0 condition are algebraic proofs for all lengths. The checker is author-side evidence, awaiting independent review.

The raw branch population consists of distinct **ordered switch histories** and their nonnegative multiplicities. H, j and h are distinct typed observers. For a future language querying the complete H and h and appending compatible based loops, (H,h) updates under concatenation by (H+H', h'∘h); equality of this pair is the coarsest exact quotient because both components are directly queried. For the narrower net-current-plus-holonomy future language, use the existing V39 (j,h) theorem. A total path count or a current-only projection is not safe for exact h once the stated witnesses are admitted.

**Next native research problem:** Identify an actual legal signed TRIADIC_CLOSURE_E Cell/Link/Port event predicate under frozen P000 and an event-to-frame-replacement / event-to-ledger transducer that preserves source identity, axis signs, native 120° PERP_E typing, Port direction, event dependency order and conservation. Verify which of the nine V17 switches are realizable. If the native graph is a strict subset, recompute the first collision/zero-current holonomy in its induced state graph. The present proof establishes these results for the conditional V17 axis-context model, and makes no claim of native-event admission or independent mathematical acceptance.
