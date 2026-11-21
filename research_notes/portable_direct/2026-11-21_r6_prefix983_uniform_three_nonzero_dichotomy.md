# PREFIX-983 — Universal three-phase nonzero-residual dichotomy (auxiliary signed-source observer)

**Date:** 2026-11-21 Asia/Shanghai. **Status:** AUTHOR_FINITE_EXHAUSTIVE_CERTIFICATE / EXACT_INTEGER_CHECKED / NOT_REVIEWED.  
**Continuation:** PREFIX-982, whose three-stage 13-step finite example was an explicit open candidate for a uniform upper bound.

## Precise statement

Fix any integer bit-width (p\ge3). For each nonzero residual (a) represented by
[
a=2^i-s2^j,\qquad 0\le i<p,quad 1\le j<p,quad s\in\{+1,-1\},
]
a named source ((i,j,s)) is legal for a current odd (p)-bit input (x) exactly when bit (j) of (x) equals ((1-s)/2). A legal move flips bit (j) and advances to the next of three phases. Let (w=(a,b,c)) be a fixed ordered **nonzero** residual word, repeated forever.

**Theorem 983.1 (sharp uniform dichotomy).** For every (p\ge3) and every such (w), exactly one of these alternatives applies:

1. There is an odd initial input, and a legal six-move path at phases (0,1,2,0,1,2), which returns to the same input and phase. Thus an infinite named-source path exists.
2. No infinite named-source path exists, and every legal path from any odd input in phase 0 terminates after at most **13 moves**.

The bound 13 is attained for all (p\ge5) by (w=(12,4,20)). In particular a longer closed cycle is never needed to witness *existence* of an infinite path in this three-stage nonzero-residual model.

This theorem is for the auxiliary bit-flip signed-source observer only. It makes no identification with the native X6 time/spatial model, Cell/Link/Port or `TRIADIC_CLOSURE_E`. The frozen P000 scientific input remains `enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d:p000_reality_foundation.json`.

## Lemma 983.2 — classification of source masks

Encode per-port legal input bits by mask 1 (bit 0), 2 (bit 1), or 3 (either). For any nonzero residual the multiset of its nonzero-port masks belongs to exactly one of
[
(1),\ (2),\ (1,2),\ (2,2),\ (2,3).
]
These types omit actual port indices; ports within any two-port type must be distinct. Furthermore, **every** type ((2,3)) has residual (3\cdot2^j) with mask 3 at port (j) and mask 2 at port (j+1), so its mask-3 port determines its mask-2 port uniquely.

*Proof.* A negative difference (2^i-2^j) ((i<j)) has a unique signed-source representation by its 2-adic valuation and the odd factor (2^{j-i}-1); it contributes a mask-1 port. For a positive difference (2^i-2^j) ((i>j)) the same uniqueness holds. Its odd factor (2^d-1) can also be the binary sum of at most two powers only when (d=1) or (d=2): these cases are (2^j) and (3\cdot2^j). Positive sums (2^i+2^j) with (i\ne j) have one or two mask-2 ports according to whether both exponents are in the legal port range; with (i=j), carrying gives the special pure power (2^{j+1}). When the difference and sum representations coincide, the pure-power case yields ((1,2)) (or the surviving one-port boundary type), and the (3\cdot2^j) case yields ((2,3)). No other collisions occur. For the latter, the two sum ports are (j,j+1), while the difference (2^{j+2}-2^j) adds mask 1 at (j). QED.

## Lemma 983.3 — exhaustive finite-state quotient

There are at most six relevant ports among three nonzero residuals. Relabel the distinct used ports by (0,1,\ldots,m-1) in order of their first appearance (this is only a *bit-coordinate renaming* in the auxiliary observer, not an X6 spatial map). Every equality pattern of the at most six port slots has one restricted-growth-string representative. Enumerating the five local mask types at all three phases, all canonical equality patterns, and excluding repeated indices inside one two-port phase gives exactly **4,207** canonical ordered-slot mask-overlap configurations. The enumeration is complete but not necessarily irredundant under graph isomorphism (identical-mask slots can generate equivalent graphs).

Each configuration has a complete state graph with ((phase,x)\in\{0,1,2\}\times\{0,1\}^m), at most (3\cdot2^6=192) vertices, and explicitly defined signed-source transitions. Kahn's exact topological algorithm detects acyclicity and computes the longest directed path in acyclic cases. For cyclic graphs, six exact successor expansions from every phase-zero state test the six-step return criterion.

The accompanying deterministic exhaustive checker gives:

| Canonical overlap configurations | Count |
|---|---:|
| All abstract mask classes | 4,207 |
| Classes satisfying mask-3 unique mask-2 successor | 4,071 |
| Admissible classes with a six-step closed path | 895 |
| Admissible acyclic classes | 3,176 |
| Admissible acyclic classes with longest path exactly 13 | 18 |
| Classes with a directed cycle but no six-step phase-aligned return | 0 |
| All abstract acyclic classes with path length 14 | 12 |

The **12** length-14 abstract overlap configurations all violate the source-specific uniqueness rule: two ((2,3)) phases share the same mask-3 port but have distinct mask-2 ports. Hence none is realizable by a true residual word. Among the 4,071 admissible configurations, no acyclic graph has a path longer than 13. The enumeration establishes the statement in every width because a larger width adds only input bits not touched by these six active ports. QED.

**Coverage argument:** the five masks exhaust Lemma 983.2; every six-or-fewer-port overlap pattern occurs in the restricted-growth enumeration; every possible input assignment and phase is checked in its graph; and the entire set of 4,207 canonical configurations is traversed by the supplied checker. This is a finite computer-assisted certificate with a small independently reproducible verifier, not a claim that 19-bit state graphs have all been explicitly built.

## Sharp real-residual witness

For (p=5) or any larger width, use (w=(12,4,20)) and odd initial input (x=31). The 13 legal ports are

`2,2,4,2,2,2,3,2,2,2,1,2,2`;

the successive integer states are

`31,27,31,15,11,15,11,3,7,3,7,5,1,5`.

Each move is checked against the actual residual's named source dictionary. The complete graph has no directed cycle and longest path 13; therefore this proves optimality of the uniform constant.

## Validation, provenance and next work

`PREFIX983_R6_TRIPLE_UNIFORM_13_CHECK.py` independently enumerates all 4,207 canonical configurations, verifies the 12 excluded 14-step cases, the absence of cyclic graphs without a six-step return, the maximum admissible length 13, the exact attaining path and the source-mask type list in real residual dictionaries for (3\le p\le19). All predicates use integers, bit operations and finite graph reachability, without floating-point tolerances.

The theorem extends PREFIX-982's exploratory (p=3..7) maximum-13 census to **every** bit-width for the actual three-stage nonzero-residual observer. No formal proof-assistant certificate or independent mathematical Review has yet been obtained. The (B_{\mathrm{fix,odd}}(32)\in\{19,20\}) mother question remains open.

**Next:** classify four-stage nonzero-residual words, where at most eight active ports exist, and seek a similarly small exact period/finite bound; separately identify typed native BRC/X6 operations that preserve the signed-source path relation before any native attribution.

**Research provenance:** prior Researcher `EM-DIRECT-FBEA5D`, session `MCP-45ad6d29cd534c1aad25595a72e3c532`, original Activity `RA-3FB2D033BE6048D8712FF056`. This publication is source evidence, not a CLAIM, PROGRESS, Result, Review, or P000 change.
