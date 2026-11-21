# R284CZ — Exact 307-edge equality graph for frozen Port lower-matrix mutations

Date: 2026-11-21 (Asia/Shanghai)
Status: **AUTHOR_PROVED / EXACT_FINITE_CERTIFIED / NOT_REVIEWED**
Scope: independent finite 34-bit Port observer at immutable R284CO scientific input; no native X6 dynamical claim and no shared Task CLAIM.

## Research question and precise domain

R284CX gave two endpoint shifts yielding four genuinely unforced level-64 ties; R284CY exhausted *only those two shifts* and discovered three additional forced shadow ties. The next structural question is whether other source-level matrix mutations also yield exact farthest-arc equality, and whether any create another pair whose members are simultaneously unforced at its level-64 cutoff.

Retain the R284CO frozen source `awdawmip/enterprise-math@acba2d8667903434aaa2a10720f43637fcc2421b:research_notes/portable_direct/R284CO_spectral_witness_checker.py`, Git blob `b46e0f682b58e47c27094b4bea6fa4e55119a3ee`; frozen codeword SHA-256 `b6ce76b2c08b9ec6b79ec83173befd2589928ca7c636643c3eaecd40405f4ff4`.

Population: `16 * 4096 = 65,536` distinct codewords with 4 upper and 12 lower binary entries; 64 labeled arcs on modulus `P=17,179,869,143`. Let `D(x)=d_64(x)` be the largest exact integer circular distance to the arcs.

Build the undirected labeled source-mutation graph G whose vertices are the **original 65,536 matrix indices** (not collapsed Port values) and whose edges keep all upper entries fixed and change the lower entries by exactly one of:

- a flip at **one** of 12 zero-based lower positions; or
- a swap at one of the 66 lower-position pairs whose bit values differ, preserving their number of 1/2 entries.

Each edge is visited once in increasing original matrix index order. By binary combinatorics, G contains exactly `12*32768 + 66*16384 = 1,474,560` edges. The observer mapping is injective on these vertices as asserted by the frozen codeword hash/distinctness check.

## New finite theorem

**Theorem (complete source-neighbor equality census).** Among G's 1,474,560 undirected edges, precisely **307** satisfy `D(x)=D(y)`. They are partitioned by source mutation as follows.

| Lower mutation (zero-based) | Number of equal-distance edges |
|---|---:|
| Single-bit flip at position 0 | 3 |
| Single-bit flip at position 1 | 14 |
| Single-bit flip at position 2 | 228 |
| Single-bit flip at position 4 | 16 |
| Single-bit flip at position 6 | 45 |
| All other one-bit flip positions | 0 |
| Swap positions (0,1) | 1 |
| All other unequal-entry swaps | 0 |
| **Total** | **307** |

Every one of the 65,536 sites has a unique farthest maximizing arc label; equal **distance values between sites** do not require equal maximizing labels. Of these 307 equal-distance edges, the sizes of their *complete level-64 tied rank blocks* are: 290 edges in a 2-site block, 7 in a 3-site block, 10 in a 4-site block. The table counts edges; these need not be distinct tied blocks.

Define `tau(x)=min_{2<=k<=64} b_k(x)`, where `b_k(x)` is the final descending rank of the complete equal-value block of `d_k(x)`. For an equality edge with distance `v`, let `a=1+# {z: D(z)>v}` be the first descending rank of the corresponding level-64 tie block. Then **only four of the 307 edges** have both endpoint values `tau(x)>a` and `tau(y)>a`.

These four are precisely the previously classified exceptional pairs, at `a=779, 1263, 1563, 7587`: three single flips of lower position 6, and one swap of lower positions (0,1). All other 303 equal-distance source-neighbor edges have at least one endpoint already individually forced by some level at the cutoff, and hence are not a free binary choice at that cutoff.

This refines R284CW and R284CY by giving **complete coverage of every permitted single-flip/unequal-entry-swap source edge**, rather than assuming an endpoint shift was already known. The global uniqueness classification continues to be R284CW, which checked all levels and quotas independently.

## Exact verification

The reproducible standard-library checker `R284CZ_bit_neighbor_tie_checker.py` does the following on the unchanged R284CO generator:

1. Reproduces the original 65,536 site enumeration and asserts the frozen SHA-256 and unique-site count. Calculates all 65,536 x 64 exact integer arc distances and asserts one farthest arc per site.
2. Visits every one-bit source edge and every actual unequal-entry swap with `target_index>source_index`; asserts the combinatorial total `1,474,560`. Compares the two precomputed integer farthest-distance values; asserts the six nonzero mutation-class counts and total 307.
3. For all endpoints of those 307 edges, constructs the 63 descending integer order-statistic rows, retaining all repetitions, and evaluates `b_k` and `tau` by exact integer binary search. Counts 290/7/10 complete level-64 block sizes and identifies exactly four edges with both endpoints unforced at `a`.
4. Emits a summary certificate plus the SHA-256 digest of the complete **ordered 307-edge list**, serialized as compact JSON tuples `[edge_kind,lower_mutation,smaller_source_index,larger_source_index,d64,arc_at_smaller,arc_at_larger]`. The digest is `251a3ca8d2d72cf6f7ca19869f174eb9e370f330533e484faf13dcb2a68dab8b`.

The four unforced edges (orientation follows increasing original source index) are:

| Rank | Mutation | Original indices | Codewords in that order | Winning arc labels |
|---:|---|---|---|---|
| 779 | flip 6 | 9344, 9376 | 12724715924, 6055669926 | 18, 19 |
| 1263 | flip 6 | 1154, 1186 | 12720103016, 6051057018 | 18, 19 |
| 1563 | flip 6 | 9360, 9392 | 12717139434, 6048093436 | 18, 19 |
| 7587 | swap 0,1 | 62591, 63615 | 14547547380, 10044326029 | 21, 37 |

In each of these four edges the final tied rank is `a+1` and each endpoint has `tau=a+1`. The result is certified by exact finite enumeration and the ordinary finite cutoff-block lemma. It is `NOT_REVIEWED` by an independent mathematics reviewer.

## Information retained and next problem

This result preserves the original source-matrix identity, lower mutation, site residue, full labeled arc winner and coupled rank-forcing information. Collapsing each edge to only `D(x)=D(y)` would discard the structural difference between 303 absorbed and four unforced edges. This is the relevant Port/BRC observer-fidelity question; no BRC native dynamics is inferred from the auxiliary Port integer geometry.

A next constructive question is to derive all equal-distance edges from **arc-envelope branch equations and the determinant effect of each lower mutation**, without enumerating every 65,536 x 64 distance or all 1,474,560 graph edges. Candidate endpoint alignments could then be filtered through exact forced-rank incidence, reducing computation while retaining the entire source-label witness.

References: R284CW, R284CX, R284CY; companion executable checker and `R284CZ_bit_neighbor_tie_certificate.json` in this directory. This note is a new finite source-neighbor classification, not a modification of P000, accepted Foundation, Review or shared Task state. Historical line: `EM-DIRECT-20B766` and `RA-617F40704F37299B15489DCA`; original private Activity write authority not established in this research invocation.
